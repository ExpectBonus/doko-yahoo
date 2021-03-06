import pytest 

import math

def test_get_heatmap_basic(app):
    PREFECTURES = ["北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県",
    "茨城県","栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県",
    "新潟県","富山県","石川県","福井県","山梨県","長野県","岐阜県",
    "静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県",
    "奈良県","和歌山県","鳥取県","島根県","岡山県","広島県","山口県",
    "徳島県","香川県","愛媛県","高知県","福岡県","佐賀県","長崎県",
    "熊本県","大分県","宮崎県","鹿児島県","沖縄県"]

    client = app.test_client()

    # POST
    response = client.post("/api/user/", json={
        "provider_id": "googleid",
        "username": "ほげほげ",
        "job": "designer",
        "born_pref": 46,
        "first_pref": 1,
        "second_pref": 2,
        "third_pref": 3,
        "hobbies": [
            "バイク",
            "温泉"
        ]
    })

    response = client.get("/api/heatmap/designer?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"]["北海道"],1.0)
    assert math.isclose(response.json["data"]["青森県"],2.0/3)
    assert math.isclose(response.json["data"]["岩手県"],1.0/3)
    for i in range(3,47):
        assert response.json["data"][PREFECTURES[i]] == 0

    response = client.get("/api/heatmap/all?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"]["北海道"],1.0)
    assert math.isclose(response.json["data"]["青森県"],2.0/3)
    assert math.isclose(response.json["data"]["岩手県"],1.0/3)
    for i in range(3,47):
        assert response.json["data"][PREFECTURES[i]] == 0
    
    response = client.get("/api/heatmap/designer")
    assert math.isclose(response.json["data"]["北海道"],1.0)
    assert math.isclose(response.json["data"]["青森県"],2.0/3)
    assert math.isclose(response.json["data"]["岩手県"],1.0/3)
    for i in range(3,47):
        assert response.json["data"][PREFECTURES[i]] == 0
    
    response = client.get("/api/heatmap/all")
    assert math.isclose(response.json["data"]["北海道"],1.0)
    assert math.isclose(response.json["data"]["青森県"],2.0/3)
    assert math.isclose(response.json["data"]["岩手県"],1.0/3)
    for i in range(3,47):
        assert response.json["data"][PREFECTURES[i]] == 0

    
    response = client.get("/api/heatmap/wrongname")
    assert response.status_code == 400
    

    response = client.get("/api/heatmap/engineer")
    for i in range(0,47):
        assert response.json["data"][PREFECTURES[i]] == 0
    response = client.get("/api/heatmap/business")
    for i in range(0,47):
        assert response.json["data"][PREFECTURES[i]] == 0
    response = client.get("/api/heatmap/all?hobbies=バイク&hobbies=おんせん")
    for i in range(0,47):
        assert response.json["data"][PREFECTURES[i]] == 0



    # 複数のユーザを追加したケース

    response = client.post("/api/user/", json={
        "provider_id": "googleid2",
        "username": "ほげ",
        "job": "business",
        "born_pref": 46,
        "first_pref": 4,
        "second_pref": None,
        "third_pref": None,
        "hobbies": [
            "バイク",
            "温泉"
        ]
    })


    response = client.get("/api/heatmap/all?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"]["北海道"],0.5)
    assert math.isclose(response.json["data"]["青森県"],1.0/3)
    assert math.isclose(response.json["data"]["岩手県"],1.0/6)
    assert math.isclose(response.json["data"]["宮城県"],1.0)
    for i in range(4,47):
        assert response.json["data"][PREFECTURES[i]] == 0
    response = client.get("/api/heatmap/designer?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"]["北海道"],1.0)
    assert math.isclose(response.json["data"]["青森県"],2.0/3)
    assert math.isclose(response.json["data"]["岩手県"],1.0/3)
    for i in range(3,47):
        assert response.json["data"][PREFECTURES[i]] == 0
    response = client.get("/api/heatmap/business?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"]["北海道"],0)
    assert math.isclose(response.json["data"]["青森県"],0)
    assert math.isclose(response.json["data"]["岩手県"],0)
    assert math.isclose(response.json["data"]["宮城県"],1.0)
    for i in range(4,47):
        assert response.json["data"][PREFECTURES[i]] == 0
