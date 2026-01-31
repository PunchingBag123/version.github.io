from flask import Flask, render_template
import datetime

app = Flask(__name__)
date= datetime.datetime.now()

blogs = [
    {'AI': 'bot fr', 'date': 'IDK'},
    {'ML': 'pretend bot', 'date': 'I DONT KNOW'}
]
table_data = [
    {'Gender': 'Male', 'Name':'John'},
    {'Gender': 'Female', 'Name': 'Sam'}
]
fruits = ['apple','banana', 'peach','orange']

@app.route("/")
def hello_world():
    return render_template('normalpage.html')
@app.route('/Home')
def first():
    return render_template('home.html', good_thing=fruits)
@app.route('/About')
def about():
    return render_template('templete.html', blogs=blogs, title = 'About')
@app.route('/Table')
def table_chart():
    return render_template('table.html', table_datas = table_data, title= 'chart')
@app.route('/Time')
def world():
    return render_template('worldtime.html', time=date)

if __name__ == "__main__":
    app.run(debug=True)