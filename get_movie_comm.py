import requests
import bs4
import random
import time
import sqlite3

def get_movie_comm(movie_id) :

    cookies = {
        'bid': '4pnrfSEl3iw',
        'douban-fav-remind': '1',
        '__gads': 'ID=b141e5b018452fe4-22e84b23e9c70063:T=1620470827:RT=1620470827:S=ALNI_MasrCBU9tOMDy_PUCUIYEfjsXreoQ',
        'll': '118282',
        '_vwo_uuid_v2': 'D5A3531FB17E774B66FCBF4E95F24A184|50d0fec6769f9adba0bcfd315f763a49',
        '__utmz': '223695111.1623567810.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
        'dbcl2': '138469848:xiJ3P3P3KR4',
        'push_noty_num': '0',
        'push_doumail_num': '0',
        '__utmv': '30149280.13846',
        '__utmc': '30149280',
        'ck': 'aXdZ',
        '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1625751755%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DcAE4jgAwnv_4TvMPSEwnAibh5X8lEc6rxyxQkGJRfR0QzAtwvjk37uT3wZu7iMNKAE2Ic8NJVhVU_vwS1Uw1ma%26wd%3D%26eqid%3Df4ab3d850000093f0000000660c5ad7d%22%5D',
        '__utma': '30149280.1256448335.1620470829.1625402632.1625751761.14',
        '_pk_id.100001.4cf6': '5f71818eded18252.1623549145.13.1625751875.1625402632.',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://movie.douban.com/subject/1292052/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    }

    conn = sqlite3.connect('db/data.db')

    url = 'https://movie.douban.com/subject/' + str(movie_id) + '/comments'
    for i in range(0, 500, 20) :
        params = (
            ('start', str(i)),
            ('limit', '20'),
            ('status', 'P'),
            ('sort', 'new_score'),
        )
        response = requests.get(url, headers=headers, params=params, cookies=cookies)

        soup = bs4.BeautifulSoup(response.text)

        items = soup.find_all('div', 'comment-item')
        for item in items :
            content = str(item.find('span', 'short').string)
            user_id = item.find('span', 'comment-info').a['href']
            user_id = user_id[30:-1]
            sql_str = "insert into comments (movie_id, content, user_id) values (" + str(movie_id) + ",'" + content.replace("'", "''") + "','" + user_id + "')"

            conn.execute(sql_str)
        
        time.sleep(random.randint(1,5))
        print('处理完成第' + str(i//20) + '页')

    conn.commit()
    conn.close()


get_movie_comm(1292052)
