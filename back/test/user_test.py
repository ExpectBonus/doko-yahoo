import pytest 

# ユーザの登録・取得・削除
def test_user_basic(app):
    client = app.test_client()

    response = client.get('/api/user/googleid')
    assert response.status_code == 404

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

    assert response.status_code == 201
    user_id = response.json["id"]

    # GET
    response = client.get("/api/user/googleid")

    assert response.status_code == 200
    assert response.json["id"] == user_id 
    assert response.json["username"] == "ほげほげ"
    assert response.json["job"] == "designer"
    assert response.json["born_pref"] == 46
    assert response.json["first_pref"] == 1
    assert response.json["second_pref"] == 2
    assert response.json["third_pref"] == 3
    assert len(response.json["hobbies"]) == 2
    assert set(response.json["hobbies"]) == {"バイク","温泉"}


    # DELETE
    response = client.delete("/api/user/{}".format(user_id))
    assert response.status_code == 200


    # GET
    response = client.get("/api/user/googleid")
    assert response.status_code == 404

# ユーザ情報の更新
def test_user_update(app):
    client = app.test_client()

    response = client.get("/api/user/googleid")

    assert response.status_code == 404

    # POST (新規作成)
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

    assert response.status_code == 201
    id1 = response.json["id"]

    # POST (更新)
    response = client.post("/api/user/", json={
        "provider_id": "googleid",
        "username": "ほげほげ２",
        "job": "engineer",
        "born_pref": 44,
        "first_pref": 4,
        "second_pref": 5,
        "third_pref": 6,
        "hobbies": [
            "温泉",
            "サッカー"
        ]
    })

    assert response.status_code == 201
    id2 = response.json["id"]
    assert id1 == id2


    response = client.get("/api/user/googleid")

    assert response.status_code == 200
    assert response.json["id"] == id2
    assert response.json["username"] == "ほげほげ２"
    assert response.json["job"] == "engineer"
    assert response.json["born_pref"] == 44
    assert response.json["first_pref"] == 4
    assert response.json["second_pref"] == 5
    assert response.json["third_pref"] == 6
    assert len(response.json["hobbies"]) == 2
    assert set(response.json["hobbies"]) == {"サッカー","温泉"}