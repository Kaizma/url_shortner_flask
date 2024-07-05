from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import hashlib


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///url.db"  
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)


class Urls(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     hashed_value = db.Column(db.String(10))
     db_url_long =db.Column(db.String(150))
     db_url_short= db.Column(db.String(30)) 

     def __repr__(self) -> str:
          return f"Long URL: {self.db_url_longurl_long} | Short URL: {self.db_url_short}"

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method=="POST":
            url_long = request.form['url']
            encoded_url = url_long.encode('utf-8')
            hashed = hashlib.sha256(encoded_url).hexdigest()[:8]

            url_short = "http://127.0.0.1:5000/"+hashed

            new_record = Urls(db_url_long = url_long, db_url_short = url_short)

            db.session.add(new_record)
            db.session.commit()

            return render_template("index.html", url_short=url_short )
    
    else:
        return render_template ("index.html")
    




            




if __name__ == "__main__":

    app.run(debug=True)