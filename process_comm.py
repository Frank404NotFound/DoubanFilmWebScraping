import sqlite3
import jieba
import filter

def process_comm(movie_id) :
    conn = sqlite3.connect('db/data.db')
    cur = conn.execute('select content from comments where movie_id = ' + str(movie_id) + ' limit 50')
    voca = {}
    for idx,row in enumerate(cur) :
        words = jieba.lcut(row[0])
        for word in words:
            if word in voca :
                voca[word] += 1
            else :
                voca[word] = 1
        print('processing ' + str(idx) + ' row...')
    
    temp = list(voca.items())
    voca = []
    for t in temp :
        if t[0] not in filter.filter :
            voca.append(t)
    voca.sort(key=lambda x : x[1], reverse=True)
    pass

process_comm(1292052)
