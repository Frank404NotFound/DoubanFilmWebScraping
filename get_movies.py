import requests
import random
import time

c = {
    'bid': '4pnrfSEl3iw',
    'douban-fav-remind': '1',
    '__yadk_uid': 'YdG8t4Xjs3gDmxfsLpi3rxG436dsXxDK',
    '__gads': 'ID=b141e5b018452fe4-22e84b23e9c70063:T=1620470827:RT=1620470827:S=ALNI_MasrCBU9tOMDy_PUCUIYEfjsXreoQ',
    '__utmc': '30149280',
    'll': '118282',
    '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1623549135%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoS15wv0B6JnawJp-gw5xiCnMGW6blcQ9Hssjo3sRzoOGx_N3MSHNW59Q2lzFasL5jhBF3itq8-vOfPgMQhBpe_%26wd%3D%26eqid%3De71087460008216b0000000660966c0f%22%5D',
    '_pk_id.100001.8cb4': 'e9e8e075510d7b63.1620470825.3.1623549143.1620478378.',
    '__utma': '30149280.1256448335.1620470829.1623553014.1623567810.5',
    '__utmz': '30149280.1623567810.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    
}

h = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    
}

for i in range(10) :
    url1 = "https://movie.douban.com/top250?start="
    url2 = "&filter="
    url = url1 + str(i*25) + url2

    response = requests.get(url, cookies=c, headers=h)

    print(response.status_code)

    file_name = 'pages/' + str(i) + '.html'

    html_file = open(file_name, 'w', encoding='utf-8')
    html_file.write(response.text)
    html_file.close()

    time.sleep(random.randint(3,9))