import json
from Auth_request import Auth_request
from difflib import SequenceMatcher,Differ

class Auth_scan(object):

    def json_data(self,data_example,data_test):
        dict_example = json.loads(data_example)
        dict_test = json.loads(data_test)
        data_key = "data"


        diff = float(0)
        data_example = dict_example[data_key]
        data_test = dict_test[data_key]
        if data_test:
            if isinstance(data_test,str):
                diff = self.Levenshtein(data_example,data_test)
                print(diff)

            if isinstance(data_test,dict):
                for key,value in data_test.items():
                    diff += self.Levenshtein(data_example.get(key,""),value)
                diff /= len(data_test)

            if isinstance(data_test,list):
                for i in range(len(data_test)):

                    for key,value in data_test[i].items():
                        diff += self.Levenshtein(data_example[i].get(key,""), value)

        return diff



    def Levenshtein(self,str_example,str_test):
        if str_example == str_test:
            return 1.0
        if str_test == 0:
            print("[-]","str_test data is null")
            return False

        cost = 0
        for i in range(len(str_test)):
            if i > len(str_example)-1:
                break
            if str_example[i] == str_test[i]:
                cost += 1

        diff = cost/len(str_example)
        return diff

    def SequenceMatcherDiff(self,str_example,str_test):
        diff = SequenceMatcher(None,str_example,str_test).ratio()

        if diff > 0.5:
            diff_str = Differ().compare(str_example.splitlines(),str_test.splitlines())
            print("\n".join(list(diff_str)))
        return diff


class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, obj(b) if isinstance(b, dict) else b)

d = {'a':1, 'b':{'c':2}, 'd':[{'e':1}]}
d = {'a':1, 'b':{'c':2}, 'd':[{'e':1}]}

if __name__ == "__main__":
    data_sample = '{"errMsg": "sucess", "data": {"id": "1789", "username": "QvDhQiAiPImrFJVE", "password": "HuDuPLulrQmuLXfRROJQUfRiJcoSYBmH", "hash": "653824e331aaf7c910919104720b672c"}}'
    request = Auth_request()
    url = "http://127.0.0.1:8080/wiki/index.php/vultest/unauthtest/Jsonone"
    status, resp, Content_type = request.method_get(url)
    print(resp.text)
    auth_scan = Auth_scan()
    #auth_scan.SequenceMatcherDiff(data_sample,resp.text)
    auth_scan.json_data(data_sample,resp.text)
