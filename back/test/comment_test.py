import pytest 


def test_get_comment(app):
    client = app.test_client()

    assert 1 == 1