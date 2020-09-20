import requests

def test_example(base_url):
    assert requests.get(base_url+"/xadmin/").status_code == 200