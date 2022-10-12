import sqlite3 as sq

output_file = open('guess.html', 'w')

temp = '''
<html>

    <script type="text/javascript">
    function flip(id) {
        elem = document.getElementById(id)
        if (elem.style.display == "block") {
            elem.style.display = "none"
        } else {
            elem.style.display = "block"
        }
    }
    </script>
    <body>
        <table width="900" align="center">
'''
output_file.write(temp)

conn = sq.connect('db/data.db')
cur = conn.execute('select id, img_url from movies')
for row in cur : 
    temp = '<tr> <td width="300">< img id="' + str(row[0]) + '" src="' + row[1] + '" style="display:none"/>'
    temp += '</td><td>< img src="wordcloud/' + str(row[0]) + '.png" onclick="flip(\'' + str(row[0]) + '\');"/></td></tr>'
    output_file.write(temp)



output_file.write(" </table> </body> </html> ")
output_file.close()