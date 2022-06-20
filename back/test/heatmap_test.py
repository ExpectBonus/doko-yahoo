import pytest 

import math

def test_get_heatmap_basic(app):
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
    assert math.isclose(response.json["data"][0],1.0)
    assert math.isclose(response.json["data"][1],2.0/3)
    assert math.isclose(response.json["data"][2],1.0/3)
    for i in range(3,47):
        assert response.json["data"][i] == 0

    response = client.get("/api/heatmap/all?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"][0],1.0)
    assert math.isclose(response.json["data"][1],2.0/3)
    assert math.isclose(response.json["data"][2],1.0/3)
    for i in range(3,47):
        assert response.json["data"][i] == 0
    
    response = client.get("/api/heatmap/designer")
    assert math.isclose(response.json["data"][0],1.0)
    assert math.isclose(response.json["data"][1],2.0/3)
    assert math.isclose(response.json["data"][2],1.0/3)
    for i in range(3,47):
        assert response.json["data"][i] == 0
    
    response = client.get("/api/heatmap/all")
    assert math.isclose(response.json["data"][0],1.0)
    assert math.isclose(response.json["data"][1],2.0/3)
    assert math.isclose(response.json["data"][2],1.0/3)
    for i in range(3,47):
        assert response.json["data"][i] == 0

    
    response = client.get("/api/heatmap/wrongname")
    assert response.status_code == 400
    

    response = client.get("/api/heatmap/engineer")
    for i in range(0,47):
        assert response.json["data"][i] == 0
    response = client.get("/api/heatmap/business")
    for i in range(0,47):
        assert response.json["data"][i] == 0
    response = client.get("/api/heatmap/all?hobbies=バイク&hobbies=おんせん")
    for i in range(0,47):
        assert response.json["data"][i] == 0



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
    assert math.isclose(response.json["data"][0],0.5)
    assert math.isclose(response.json["data"][1],1.0/3)
    assert math.isclose(response.json["data"][2],1.0/6)
    assert math.isclose(response.json["data"][3],1.0)
    for i in range(4,47):
        assert response.json["data"][i] == 0
    response = client.get("/api/heatmap/designer?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"][0],1.0)
    assert math.isclose(response.json["data"][1],2.0/3)
    assert math.isclose(response.json["data"][2],1.0/3)
    for i in range(3,47):
        assert response.json["data"][i] == 0
    response = client.get("/api/heatmap/business?hobbies=バイク&hobbies=温泉")
    assert math.isclose(response.json["data"][0],0)
    assert math.isclose(response.json["data"][1],0)
    assert math.isclose(response.json["data"][2],0)
    assert math.isclose(response.json["data"][3],1.0)
    for i in range(4,47):
        assert response.json["data"][i] == 0
