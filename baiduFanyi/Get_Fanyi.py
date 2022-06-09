import re
import execjs 
import requests

## execjs ==> pip install PyExecJs


## 准备参数， 发起请求，
session = requests.session();
##token gtk
## sign = execjs.compile(.js).call('方法名', 参数，参数)

index_url = "https://fanyi.baidu.com/"
fanyiApi = "https://fanyi.baidu.com/v2transapi"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        }


def get_params():
    session.get(url=index_url, headers=headers)
    response = session.get(url=index_url,headers=headers).text
    
    token = re.findall("token: '([a-z0-9]*)'",response)[0]
    
    gtk = re.findall("window.gtk = '([\d\.]*)'", response)[0]

    return [token,gtk]


def ctr_params(v,sign, token):
    data={
        "from":"zh",
        "to":"en",
        "query":v,
        "transtype":"translang",
        "simple_means_flag":"3",
        "sign":sign,
        "token":token,
        "domain":"common"
    }
    response = session.post(fanyiApi, headers=headers, data=data).json()
    
    return response["trans_result"]["data"][0]["dst"]
    

if __name__ == "__main__":
    v = input("请输入需要翻译的文字: ")
    
    token,gtk = get_params()
    
    with open("fanyi.js", mode="r") as f:
        content = f.read()
    sign = execjs.compile(content).call('e', v, str(gtk))
    
    print("结果是: ",ctr_params(v, sign, token))

























