from flask import Flask, render_template
from flask import request

import pymysql

db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'test',
    charset = 'utf8'
)

print(db_conn)

cursor = db_conn.cursor()

query = 'select * from player'

cursor.execute(query)

for i in cursor:
    print(i)

app = Flask(__name__)

@app.route('/')
def index():
    temp = request.args.get('uid')
    temp1 = request.args.get('cld')

    print(temp, temp1)

    return render_template('index.html')

@app.route('/test')
def testget():
    return render_template('posttest.html')

@app.route('/test', methods=['POST'])
def testpost():
    value = request.form['input']

    print(value)

    return render_template('posttest.html')

@app.route('/sqltest')
def sqltest():
    cursor = db_conn.cursor()

    query = 'select * from player'

    cursor.execute(query)

    result = []

    for i in cursor:
        temp = {'player_id':i[0], 'player_name':i[1]}
        result.append(temp)

    return render_template('sqltest.html', result_table = result)

if __name__ == "__main__":
    app.run(debug=True)