import bs4


def process_page(page_number) :
    file_name = 'pages/' + str(page_number) + '.html'
    html_file = open(file_name, 'r', encoding='utf-8')
    html_doc = html_file.read()
    html_file.close()

    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    for item in soup.find_all('div','post'):
        hd_tag = item.find('div', 'title').a
        title=hd_tag['href']

        print(title)
        

        

for i in range(10) :
    process_page(i)
