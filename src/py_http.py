import http.client
import json
import urllib.request
import requests


# 原生http发起get请求
class NativeHttpGetRequest:
    url = 'http://localhost:8989/file/data?type=json'

    @staticmethod
    def call_url_by_witch(url):
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                print(json.loads(data))
            else:
                print('接口调用失败')

    @staticmethod
    def call_url_by_catch_e(url):
        response = None
        try:
            response = urllib.request.urlopen(url)
            if response.status == 200:
                data = response.read()
                print(json.loads(data))
            else:
                print('接口调用失败')
        except IOError:
            print('http链接异常')
        finally:
            if response is not None:
                response.close()


# 原生http发起post请求
class NativeHttpPostRequest:
    @staticmethod
    def call_url():
        conn = http.client.HTTPConnection('127.0.0.1', 8989)

        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({'requestId': 10086})

        conn.request('POST', '/index/post', payload, headers)

        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            print(json.loads(data))
        else:
            print('post request error')

        conn.close()


#  使用requests库发起Get、Post请求
class RequestsSdkReqeust:

    def __init__(self):
        print('RequestsSdkReqeust create......')

    @staticmethod
    def http_get():
        params = {'type': 'json'}
        response = requests.get('http://localhost:8989/file/data', params)
        print(response.json())

    @staticmethod
    def http_post():
        params = {'requestId': 10086}
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://localhost:8989/index/post', headers=headers, data=json.dumps(params))
        print(response.json())


# 使用requests库进行文件上传
class FileUpload:
    @staticmethod
    def upload_file():
        files = {'file': open('../index.xlsx', 'rb')}

        response = requests.post('http://localhost:8989/file/upload', files=files)

        if response.status_code == 200:
            print('文件上传成功')
        else:
            print('文件上传失败')

