import requests
import random
import time

c = {
    '_vwo_uuid_v2':'D26C268C463E881D8B3F19F931E72BBEE|423b984a681d0c1fb1d4de808225e994',
    'douban-fav-remind':'1',
    'douban-profile-remind':'1',
    'gr_user_id':'929bbc95-9f28-4f21-b928-34cb80780b6f',
    '_ga':'GA1.2.1735148410.1591167822',
    'UM_distinctid':'173cb8f7645d0-0631536196c836-f7d1d38-144000-173cb8f7646517',
    "ll":"118282",
    "__gads=ID=ba864bcdc76acc31:T=1609114485":"S=ALNI_Mab-ccezfbjCDYjXFlrr2thPy8qxQ", 
    "push_doumail_num":"0",
    "_vwo_uuid_v2":"D26C268C463E881D8B3F19F931E72BBEE|423b984a681d0c1fb1d4de808225e994",
    "cn_d6168da03fa1ahcc4e86_dplus":'{"distinct_id": "173cb8f7645d0-0631536196c836-f7d1d38-144000-173cb8f7646517","$id": "101475087","$_sessionid": 0,"$_sessionTime": 1618209628,"initial_view_time": "1596848043","initial_referrer": "https://www.douban.com/","initial_referrer_domain": "www.douban.com","$dp": 0,"$_sessionPVTime": 1618209628}',
    "bid":"FAtBEJaNPfA",
    "dbcl2":"101475087:et2YAuu8NDM",
    "ct":"y",
    "__utmz":"30149280.1626340578.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", 
    "__utmv":"30149280.1014",
    "push_noty_num":"0",
    "__utma":"30149280.1735148410.1591167822.1626782555.1626785888.33",
    "ck":"ufgF",
    "ap_v":"0,6.0",
    "__utmc":"30149280",
    "__utmb":"30149280.32.6.1626787327335",
    "_pk_ref.100001.8cb4":'["","",1626789537,"https://cn.bing.com/"]',
    "_pk_id.100001.8cb4":"8c9c8ceacd5f7b2a.1591167818.2614.1626789537.1626787388.",
    "_pk_ses.100001.8cb4":"*"
    
   


}

h = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/doulist/135371163/?start=25&sort=time&playable=0&sub_type=',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for i in range(40) :
    url1 = "https://www.douban.com/doulist/135371163/?start="
    url2 = "&sort=time&playable=0&sub_type="
    url = url1 + str(i*25) + url2

    response = requests.get(url, cookies=c, headers=h)

    print(response.status_code)

    file_name = 'pages/' + str(i) + '.html'

    html_file = open(file_name, 'w', encoding='utf-8')
    html_file.write(response.text)
    html_file.close()

    time.sleep(random.randint(3,9))