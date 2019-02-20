from django.shortcuts import render,HttpResponse
import sys,io,requests,base64,json

# Create your views here.

def index(request,account,password,hycard):


    def get_hymingxi(account,password,hycard):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
        url = 'https://qian.sicent.com/member/Detail.do?'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5733.400 QQBrowser/10.2.2019.400',
            'X-Requested-With': 'XMLHttpRequest', 'Referer': 'https://qian.sicent.com/member/page.do',
            'Content-Type': 'application/json; charset=utf-8', 'Host': 'qian.sicent.com'}
        url1 = 'https://qian.sicent.com/Login/Login.do'
        header1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5733.400 QQBrowser/10.2.2019.400',
            'X-Requested-With': 'XMLHttpRequest', 'Referer': 'Referer: https://qian.sicent.com/Login/toLogin.do',
            'Content-Type': 'application/json; charset=utf-8', 'Host': 'qian.sicent.com'}
        # base64
        pwd = password.encode()
        pwd = base64.b64encode(pwd)

        parm1 = {
            'txtLoginName': account,
            'txtPassword': pwd,
            'showCode': 'false',
            'txtVerify': ''
        }


        parm = {
            'sNbid': account,
            'dtTime': '',
            'dtBegTime': '',
            'dtEndTime': '',
            'sCardID': hycard,
            'sIDCard': '',
            'sName': '',
            'sDis': '',
            # 'sCardId': '',
            'i': '0.40228503393768444',
            '_search': 'false',
            'nd': '1550545851336',
            'rows': '30',
            'page': '1',
            'sidx': 'dtTime',
            'sord': 'desc',
        }
        s = requests.Session()
        #登录
        s1 = s.post(url1, params=parm1, headers=header1, verify=False)
        print(s1.status_code)
        print('---------------------')
        # if s1.status_code != 303:
        #     login_res = {
        #         'success': {
        #             'code': '-1',
        #         },
        #     }
        #     return json.dumps(login_res)
        # print(card)
        #获取会员详情.
        result = s.get(url, params=parm, headers=header, verify=False)
        print('=================')
        if result.status_code == 200:
            try:
                dic = json.loads(result.text)
            except Exception as e:
                login_res = {
                        'success': {
                            'code': '-1',
                            'msg':'login error',
                        },
                    }
                return json.dumps(login_res)

            # dicts = json.loads(result.text.replace(u'\xa9', u''))
            if dic['dataObj']['mRemain'] != '':
                print(dic['rows'][0]['sName'])
                print(dic['rows'][0]['sIDCard'])
                print(dic['rows'][0]['sDis'])
                print(dic['dataObj']['mRemain'])

                print(dic['rows'][0]['iHeapCanUse'])
                dict_user = {
                    'success':{
                        'code':'1',
                        'msg':'login ok',
                    },
                    'data':{
                        'name': dic['rows'][0]['sName'],
                        'hycard': hycard,
                        'return_hycard': dic['rows'][0]['sIDCard'],
                        'dengji': dic['rows'][0]['sDis'],
                        'sfzno':dic['rows'][0]['sCardID'],
                        'benjin': dic['dataObj']['cMnyNoJ'],
                        'jiangli': dic['dataObj']['cEncourage'],
                        'mRemain': dic['dataObj']['mRemain'],
                        'zongjifen':dic['rows'][0]['iHeap'],
                        'keyongjifen': dic['rows'][0]['iHeapCanUse'],
                    }
                }
                filename = 'd:/wxhy/%s.txt' % (account)
                with open(filename, 'a') as f:
                    f.write('account: %s\t password %s \n'%(account,password))
                    f.write(dic['rows'][0]['sName'] + '\t')
                    f.write(hycard + '\t')
                    f.write(dic['rows'][0]['sDis'] + '\t')
                    f.write(dic['rows'][0]['sCardID'] + '\t')
                    f.write(str(dic['dataObj']['cMnyNoJ']) + '\t')
                    f.write(str(dic['dataObj']['cEncourage']) + '\t')
                    f.write(str(dic['dataObj']['mRemain']) + '\t')
                    f.write(str(dic['rows'][0]['iHeap']) + '\t')
                    f.write(str(dic['rows'][0]['iHeapCanUse']) + '\n')
                # time.sleep(1)
                json_user = json.dumps(dict_user)
                return json_user
            else:
                dict_user = {
                    'success': {
                        'code': '-2',
                        'msg':'hy not found',
                    },
                }
                json_user = json.dumps(dict_user)
                return json_user
        else:
            return False

    hy_mx = get_hymingxi(account,password,hycard)

    return HttpResponse(hy_mx)

