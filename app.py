from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route('/produit')
def produit():
    return render_template('produit.html') 

@app.route('/appli')
def appli():
    return render_template('appli.html') 

if __name__ == "__main__":
   app.run(debug=True)
