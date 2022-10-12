import bs4
import sqlite3 as sq

def process_page(page_number) :
    file_name = 'pages/' + str(page_number) + '.html'
    html_file = open(file_name, 'r',encoding='utf-8')
    html_doc = html_file.read()
    html_file.close()

    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    items = soup.find_all('div', 'item')

    for idx, item in enumerate(items) :
        # image url
        img_url = item.find('img')['src']

        hd_tag = item.find('div', 'hd').a
        # movie url
        movie_url = hd_tag['href']
        # movie names
        names = ''
        for span in hd_tag.find_all('span', 'title') :
            n = str(span.string)
            if n[0] == '\xa0':
                n = n[3:]
            names = names + ' ' + n
        names = names.strip()
        name = names.split(' ')[0]

        bd_tag = item.find('div', 'bd').div
        # rate
        rate = str(bd_tag.find('span', 'rating_num').string)
        # number of comments
        num = str(bd_tag.find_all('span')[-1].string)
        num = num[:-3]

        rp = movie_url.rindex('/')
        lp = movie_url.rindex('/', 0, rp)
        movie_id = movie_url[lp+1:rp]

        output = str(page_number*25+idx) + ' ' + movie_id + ' ' + img_url + ' ' + movie_url + ' ' + names + ' ' + rate + ' ' + num
        print(output)

        sql_str = "INSERT INTO movies (id, img_url, name, rate, num_comm) VALUES ("
        sql_str += movie_id + ",'" + img_url + "','" + name + "'," + rate + "," + num + ")"

        conn.execute(sql_str)
    

conn = sq.connect('db/data.db')

for i in range(40) :
    process_page(i)

conn.commit()
conn.close()