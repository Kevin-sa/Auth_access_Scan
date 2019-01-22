from Auth_request import Auth_request
from Auth_scan import Auth_scan


def scan(url_example,url_scan):
    request = Auth_request()
    auth_scan = Auth_scan()
    status_example, resp_example, Content_type_example = request.method_get(url_example)
    status_scan, resp_scan, Content_type_scan = request.method_get(url_scan)

    if ((status_example != 200) or (status_scan != 200)):
        print("[-] target status is wrong")
        exit(0)

    diff_string = auth_scan.SequenceMatcherDiff(resp_example.text, resp_scan.text)
    diff_param = auth_scan.json_data(resp_example.text,resp_scan.text)
    diff = (diff_param+diff_string)/2

    if diff < 0.8:
        print("[-]the url is unauthorized access")


if __name__ == "__main__":
    url = "http://127.0.0.1:8080/wiki/index.php/vultest/unauthtest/Jsonone"
    scan(url,url)
