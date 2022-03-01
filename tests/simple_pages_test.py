"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about!">About</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python_flask">Python and Flask</a>' in response.data
    assert b'<a class="nav-link" href="/contid">Continuous Integration and Deployment</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about!")
    assert response.status_code == 200
    assert b"About Page" in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_python_flask(client):
    """This makes the index page"""
    response = client.get("/python_flask")
    assert response.status_code == 200
    assert b"Python and Flask" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/contid")
    assert response.status_code == 200
    assert b"Continuous Integration and Development" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
