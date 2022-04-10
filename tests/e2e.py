import requests
import json

url = "http://0.0.0.0:6700/api"


def test_get_list(id):
    r = requests.get(f"{url}/lists/{id}")
    print('[read]', r.status_code, r.json())

def test_create_list():
    r = requests.post(
        f"{url}/lists",
        json.dumps({"name": "sample_test"})
    )
    print('[create]', r.status_code, r.json())
    return r.json()['id']

def test_update_list(id):
    r = requests.put(
        f"{url}/lists/{id}",
        json.dumps({"name": "new_sample_test"})
    )
    print('[update]', r.status_code, r.json())

def test_delete_list(id):
    r = requests.delete(f"{url}/lists/{id}")
    print('[update]', r.status_code, r.json())

def test_get_all_list():
    r = requests.get(f"{url}/lists")
    print('[read all]', r.status_code, r.json())


def test():
    id = test_create_list()
    test_get_list(id)
    test_get_all_list()
    test_update_list(id)
    test_delete_list(id)
    test_get_all_list()


if __name__ == '__main__':
    test()