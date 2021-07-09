# conftest.py

from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--baseUrl",
        action="store"
    )

    parser.addoption(
        "--consoleUrl",
        action="store"
    )   

    parser.addoption(
        "--iUser",
        action="store"
    )  

    parser.addoption(
        "--iPass",
        action="store"
    )  

    parser.addoption(
        "--cUser",
        action="store"
    )  

    parser.addoption(
        "--cPass",
        action="store"
    )                   

@fixture()
def baseUrl(request):
    return request.config.getoption("--baseUrl")

@fixture()
def consoleUrl(request):
    return request.config.getoption("--consoleUrl")

@fixture()
def iUser(request):
    return request.config.getoption("--iUser")

@fixture()
def iPass(request):
    return request.config.getoption("--iPass")

@fixture()
def cUser(request):
    return request.config.getoption("--cUser")

@fixture()
def cPass(request):
    return request.config.getoption("--cPass")        