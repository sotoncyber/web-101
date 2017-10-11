import flask
from challenge import app
import challenge.forms as forms
import base64
import datetime

@app.route('/')
def index():
    return flask.render_template('index.html')

# Challenge 1
@app.route('/1', methods=['GET', 'POST'])
def ch_1():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data.lower() == 'admin' and form.password.data == 'my5up3rs3cr3tp4ssw0rd':
            return flask.render_template('success.html', current=1, next=2, flag='flag1')
        else:
            return flask.render_template('ch1.html', lvl=1, form=form, invalid=True)
    return flask.render_template('ch1.html', lvl=1, form=form)

# Challenge 2
@app.route('/2', methods=['GET', 'POST'])
def ch_2():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data.lower() == 'webmaster' and form.password.data == 'd0ntgu355m3!':
            return flask.render_template('success.html', current=2, next=3, flag='flag2')
        else:
            return flask.render_template('ch2.html', lvl=2, form=form, invalid=True)
    return flask.render_template('ch2.html', lvl=2, form=form)

# Challenge 3
@app.route('/3', methods=['GET', 'POST'])
def ch_3():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data.lower() == 'test' and form.password.data == 'password123!':
            return flask.render_template('success.html', current=3, next=4, flag='flag3')
        else:
            return flask.render_template('ch3.html', lvl=3, form=form, invalid=True)
    return flask.render_template('ch3.html', lvl=3, form=form)

# Challenge 4
@app.route('/4', methods=['GET', 'POST'])
def ch_4():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data.lower() == 'test' and form.password.data == '#n0tp455w0rd':
            return flask.render_template('success.html', current=4, next=5, flag='flag4')
        else:
            return flask.render_template('ch4.html', lvl=4, form=form, invalid=True)
    return flask.render_template('ch4.html', lvl=4, form=form)

# Challenge 5
@app.route('/5', methods=['GET', 'POST'])
def ch_5():
    flag = 'flag5'
    form = forms.LoginForm()
    invalid = False
    if flask.request.method == 'POST':
        invalid = True
    r = flask.make_response(flask.render_template('login.html', lvl=5, form=form, invalid=invalid))
    r.headers.set('Flag', flag)
    return r

# Challenge 6
@app.route('/6', methods=['GET', 'POST'])
def ch_6():
    form = forms.LoginForm()
    invalid = False
    if flask.request.method == 'POST':
        if flask.request.cookies.get('access-level') == 'admin':
            r = flask.make_response(flask.render_template('success.html', current=6, next=7, flag='flag6'))
            r.set_cookie('access-level', expires=0)
            return r
        invalid = True
    r = flask.make_response(flask.render_template('login.html', lvl=6, form=form, invalid=invalid))
    r.set_cookie('access-level', 'user')
    return r

# Challenge 7
@app.route('/7', methods=['GET', 'POST'])
def ch_7():
    form = forms.LoginForm()
    invalid = False
    if flask.request.method == 'POST':
        if form.username.data.lower() == 'bank-manager' and form.password.data == 'ilovemoney!':
            r = flask.make_response(flask.render_template('success.html', current=7, next=8, flag='flag7'))
            r.set_cookie('super-secret-cookie', expires=0)
            return r
        else:
            invalid = True
    r = flask.make_response(flask.render_template('login.html', lvl=7, form=form, invalid=invalid))
    r.set_cookie('super-secret-cookie', 'VXNlcjogYmFuay1tYW5hZ2VyIHwgUGFzc3dvcmQ6IGlsb3ZlbW9uZXkhCg==')
    return r

# Challenge 8
@app.route('/8', methods=['GET', 'POST'])
def ch_8():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data.lower() == 'user' and form.password.data == 'password':
            r = flask.make_response(flask.render_template('ch8.html', user='user'))
            r.set_cookie('session-cookie', base64.b64encode((str(datetime.datetime.now()).replace(' ', '') + '-username:user').encode('ascii')).decode('ascii'))
            return r
        else:
            return flask.render_template('ch8-login.html', lvl=8, form=form, invalid=True)
    if flask.request.cookies.get('session-cookie') and base64.b64decode(flask.request.cookies.get('session-cookie')).decode('ascii').endswith('-username:admin'):
        r = flask.make_response(flask.render_template('ch8.html', user='admin', flag='flag8'))
        r.set_cookie('session-cookie', expires=0)
        return r
    elif flask.request.cookies.get('session-cookie') and base64.b64decode(flask.request.cookies.get('session-cookie')).decode('ascii').endswith('-username:user'):
        return flask.render_template('ch8.html', user='user')
    else:
        return flask.render_template('ch8-login.html', lvl=8, form=form, invalid=False)

@app.route('/8/logout')
def ch_8_logout():
    r = flask.make_response(flask.redirect('/8', code=302))
    r.set_cookie('session-cookie', expires=0)
    return r

# Challenge 9
@app.route('/9', methods=['GET', 'POST'])
def ch_9():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data == 'rob':
            if form.password.data == 'unicorns123':
                return flask.render_template('success.html', current=9, next=10, flag='flag9')
            else:
                return flask.render_template('ch9.html', lvl=9, form=form, badpass=True)
        else:
            return flask.render_template('ch9.html', lvl=9, form=form, baduser=True)
    return flask.render_template('ch9.html', lvl=9, form=form)

# Challenge 10
@app.route('/10', methods=['GET', 'POST'])
def ch_10():
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        return flask.render_template('login.html', lvl=10, form=form, invalid=True)
    return flask.render_template('login.html', lvl=10, form=form)

@app.route('/10/panel')
def ch_10_panel():
    return flask.render_template('ch10-part1.html', current=10, next=11, flag='flag10')

@app.route('/10/panel/details.pdf')
def ch_10_pdf():
    return flask.send_file('files/details.pdf')

# Challenge 11
@app.route('/11')
def ch_11():
    return flask.render_template('ch11.html')

@app.route("/11/<page>")
def ch_11_serve_page(page):
    f=open('challenge/files/ch11/'+page+'.txt','r')
    content = """
        <html>
            <head>
                <title>%s</title>
                <link rel="stylesheet" href="/static/style.css" />
            </head>
            <body>
                <h1>Welcome to Secure Services Ltd</h1>
                <div class="container">
                    <h3>Hello and welcome to <i>%s</i></h3>
                    <br /><br />
                    <p>%s</p>
                </div>
            </body>
        </html>"""%(page, page, f.read())
    f.close()
    return content
