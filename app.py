from flask import Flask,request,redirect
import sqlite3

app = Flask(__name__)



def url_sec(address):

    db = sqlite3.connect('godb.db')

    cursor = db.cursor()

    cursor.execute('create table if not exists godb(address text, url text)')
    cursor.execute('insert into godb(address,url) values("amazon", "https://www.amazon.com"),("myntra", "https://www.myntra.com"),("flipkart", "https://www.flipkart.com"),("github", "https://www.github.com"),("movies", "https://web.netmovies.to/home/"),("localmovies", "https://www.5movierulz.ink/"),("info", "https://www.wikipedia.com/")')

    cursor.execute('select url from godb where address=?', (address,))

    goresul = cursor.fetchone()

    db.commit()

    db.close()

    return goresul[0]


#print(url_sec('flipkart'))

@app.route('/')
def zero():
    return "Welcome to redirect'Ls Program"

@app.route('/', methods=['GET'])
def home():
    address = request.args.get('address')
    goresul = url_sec(address)
    return redirect(goresul, code=302)

@app.route('/<address>')
def index(address):
    goresul = url_sec(address)
    return redirect(goresul, code=302)

    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

