import requests

class Auth_request(object):
    def __init__(self):
        self.headers_payload = {'User-Agent':"unauthorized access (parameter traversal vulnerablitiy) scan"}

    #return status,resp.Content-Type = Auth_request.mdthod_get(url)

    def method_get(self,url,params="",headers="",timeout=5):
        if self.target_alive(url):
            return
        self.headers_payload.update(headers)
        #headers_payload.update()  Consider whether to join special http headers,for example Autherusername:admin
        resp = requests.get(url,params=params,headers=self.headers_payload,timeout=timeout)
        return (resp.status_code,resp,resp.headers.get('Content-Type',''))

    def method_post(self,url,data="",params="",headers="",timeout=5):
        if self.target_alive(url):
            return
        self.headers_payload.update(headers)
        resp = requests.post(url,data=data,params=params,headers=self.headers_payload,timeout=timeout)

        return (resp.status_code,resp,resp.headers.get('Content-Type',''))


    def target_alive(self,url):
        if requests.get(url,headers=self.headers_payload).status_code == 404:
            print("[-] the target is 404")
            return True




if __name__ == "__main__":
    request = Auth_request()
    url = "http://127.0.0.1:8080/wiki/index.php/vultest/unauthtest/JsonTwo"
    status, resp, Content_type = request.method_get(url)
    print(status,resp,Content_type)
