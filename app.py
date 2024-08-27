from flask import*

app=Flask(__name__) 

@app.route('/wlogin')
def home():
    return render_template('home.html')

@app.route('/tlogin')
def tlogin():
    return render_template('tlogin.html')

@app.route('/wlogin')
def wlogin():
    return render_template('wlogin.html')


@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/upload.html')
def tupload():
    return render_template('tupload.html')

@app.route('/wupload')
def wupload():
    return render_template('wupload.html')

if(__name__=='__main__'):
    app.run(debug=True)

