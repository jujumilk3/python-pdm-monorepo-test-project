import requests  # it must be imported from common pdm project


def hello_world():
    return "Hello, World!"


def test_requests():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
    return response


if __name__ == "__main__":
    print(hello_world())
    print(test_requests())
