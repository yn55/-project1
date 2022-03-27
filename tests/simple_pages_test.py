"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/">Home</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python_flask">Python and Flask</a>' in response.data
    assert b'<a class="nav-link" href="/contid">Continuous Integration and Deployment</a>' \
           in response.data
    assert b'<a class="nav-link" href="/glossaryoop">OOP Glossary</a>' in response.data
    assert b'<a class="nav-link" href="/aaa">AAA Testing</a>' in response.data
    assert b'<a class="nav-link" href="/oopfundamentals">OOP Fundamentals</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data


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


def test_request_contid(client):
    """This makes the index page"""
    response = client.get("/contid")
    assert response.status_code == 200
    assert b"Continuous Integration and Deployment" in response.data


def test_request_glossaryoop(client):
    """This makes the index page"""
    response = client.get("/glossaryoop")
    assert response.status_code == 200
    assert b"Object Oriented Programming Glossary" in response.data


def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/AAA")
    assert response.status_code == 200
    assert b"Arrange-Act-Assert" in response.data


def test_request_oopfundamentals(client):
    """This makes the index page"""
    response = client.get("/oopfundamentals")
    assert response.status_code == 200
    assert b"Object Oriented Programming Fundamentals" in response.data


def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"5 Principles of Object-Oriented Programming" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
