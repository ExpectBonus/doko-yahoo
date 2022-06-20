import pytest 


def test_get_comment(app):
    client = app.test_client()

    response = client.get("/api/comments/0")
    assert response.status_code == 400
    response = client.get("/api/comments/48")
    assert response.status_code == 400

    response = client.post("/api/comments/1", json={
        "id": 10,
        "comment": "この県こそ至高。異論は認めない。"
    })
    assert response.status_code == 400



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
    id1 = response.json["id"]

    response = client.post("/api/comments/1", json={
        "id": id1,
        "comment": "この県こそ至高。異論は認めない。"
    })
    assert response.status_code == 201


    response = client.get("/api/comments/1")
    assert len(response.json["comments"]) == 1
    assert response.json["comments"][0]["comment"] == "この県こそ至高。異論は認めない。"
    assert response.json["comments"][0]["born_pref"] == 46
    assert response.json["comments"][0]["job"] == "designer"


    response = client.post("/api/comments/1", json={
        "id": id1,
        "comment": "ここに住みたい。"
    })
    assert response.status_code == 201


    response = client.get("/api/comments/1")
    assert len(response.json["comments"]) == 2


    response = client.post("/api/user/", json={
        "provider_id": "googleid2",
        "username": "ほげ",
        "job": "engineer",
        "born_pref": 25,
        "first_pref": 10,
        "second_pref": 11,
        "third_pref": 12,
        "hobbies": [
            "自転車"
        ]
    })
    id2 = response.json["id"]
    response = client.post("/api/comments/1", json={
        "id": id2,
        "comment": "賛成。"
    })
    assert response.status_code == 201


    response = client.get("/api/comments/1")
    assert len(response.json["comments"]) == 3

    for comment in response.json["comments"]:
        assert comment in {
            {
                "comment": "この県こそ至高。異論は認めない。",
                "born_pref": 46,
                "job": "designer"
            },
            {
                "comment": "ここに住みたい。",
                "born_pref": 46,
                "job": "designer"
            },
            {
                "comment": "賛成。",
                "born_pref": 25,
                "job": "engineer"
            }
        }