import pytest 

import math

def test_get_heatmap(app):
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
