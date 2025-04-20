from flask import Flask, render_template

app = Flask(__name__)

app_name = "Aplikasi Flask"

@app.route("/")
def hello_world():
    return f"<p>Hello World!</p>"

@app.route("/aplikasi")
def aplikasi():
    return "<p>Selamat datang di aplikasi</p>"

#App Route dengan HTML 
@app.route("/about/")
def about():
    return render_template('about.html')

#4 App Route HTML dengan bostrapp
@app.route("/bootstrap/")
def about_bostrapp():
    return render_template('bootstrap.html')

#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
    return "nama kamu : {}".format(nama_mahasiswa)

#6 App Route ID
@app.route('/NIM/<int:NIM>')  
def NIM(NIM):
    return f"NIM: {NIM}"

#7 App Route Variabel Global
@app.route('/var/')
def variabel_global():
    return f"Wellcome to {app_name}"

#8 App Route Dictionary Variabel
@app.route('/data')
def data():
    user = {"nama": "Ariel", "Umur": 20, "Prodi": "Bisnis Digital"}
    return render_template('data.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)