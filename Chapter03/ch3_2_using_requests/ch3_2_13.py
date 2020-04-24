import requests

headers = {
    'Cookie': (
    '_zap=981830c7-f913-4bbc-ac8b-c62a044f08c4; d_c0="AFAUfkBsKRGPTptJjpMIrsl'
    'n4OubLc5ncoY=|1587617617"; _ga=GA1.2.1245074251.1587617624; _gid=GA1.2.2'
    '138336649.1587617624; _xsrf=927rz2X6plNeT0lpcMUwGG2w1NoA9rgB; Hm_lvt_98b'
    'eee57fd2ef70ccdd5ca52b9740c49=1587617624,1587703504; _gat_gtag_UA_149949'
    '619_1=1; SESSIONID=HhMkkPLb4Zp9iThgaLCEP2LbVC5JfECb3p4R3TBRSiQ; JOID=W1E'
    'XBkP52f24VpKZQvW44jeALbJYsbq33jzC3ifMg4aGMsfxLju7VepXm''ZVI1_DeR5pK8nFtz'
    'dgr7IABMfxpBXg=; osd=Vl4QBkv01vq4Xp-WRfWw7ziHLbpVvr231jHN2SfEjomBMs_8ITy'
    '7XedYnpVA2v_ZR5JH_XZtxdUk64AJPPNuBXA=; capsion_ticket="2|1:0|10:15877035'
    '02|14:capsion_ticket|44:NzQyZTVmOGMyMzgzNGE0MGFkNTMyZTEzMDVjMTIyYzk=|a00'
    '965b6270115cebdf8ec61859f1a54cd9f82f4abd64c1586b114ada6a220fb"; z_c0="2|'
    '1:0|10:1587703514|4:z_c0|92:Mi4xYUdtNEdnQUFBQUFBVUJSLVFHd3BFU1lBQUFCZ0Fs'
    'Vk4ycnlQWHdBSW1WS0RkbFE1My1sVEtLSUpCVmF1b1JOSzFB|73e31052ca58fca513f928c'
    '40c4126632e1f197f59737df364ca3857458df71d"; tst=r; Hm_lpvt_98beee57fd2ef'
    '70ccdd5ca52b9740c49=1587703523; KLBRSID=81978cf28cf03c58e07f705c156aa833'
    '|1587703517|1587703495'
    ),
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
    '537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
