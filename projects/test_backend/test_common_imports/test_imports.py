from utils.test_utils import hello_world, test_requests

# utils 안에 __init__.py 파일이 있어야만 사용이 된다.

if __name__ == "__main__":
    print(hello_world())
    print(test_requests())
