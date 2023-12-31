import random
import string

from flask import json
from src.app import app


def generate_random_letters(num=50):
    word = string.ascii_letters
    words = "".join(random.choice(word) for i in range(num))
    return words

def generate_random_domain():
    list = [".com", ".net", ".org", ".edu", ".info"]
    return random.choice(list)

def generate_random_url():
    s1 = generate_random_letters(10)
    s2 = generate_random_domain()
    s3 = "http://" + s1 + s2
    return s3


# TEST index page for 404
@app.route("/", methods=["GET"])
def test_index_page_gives_404():
    res = app.test_client().get("/")
    assert res.status_code == 500


# Test if one can create bookmark in the database
def test_create_bookmark():
    my_data = {
        "title": generate_random_letters(),
        "description": generate_random_letters(100),
        "url": generate_random_url(),
    }
    res = app.test_client().post(
        "/bookmark/",
        data=json.dumps(my_data),
        content_type="application/json",
    )
    print(res.data.decode('utf-8'), 'res')
    assert res.status_code == 201


# Test if all bookmarks are returned
def test_get_all_bookmarks_route():
    res = app.test_client().get("/bookmarks/")
    assert res.headers["Content-Type"] == "application/json"
    assert res.status_code == 200

# Test if a single bookmark is returned
def test_get_one_bookmark_route():
    res = app.test_client().get("/bookmark/1/")
    assert res.headers["Content-Type"] == "application/json"
    assert res.status_code == 200


# Test json data format is  are returned
def test_get_json_data_format_returns():
    res = app.test_client().get("/bookmarks/")
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
