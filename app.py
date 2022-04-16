from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DXA.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastnaem = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.firstname} - {self.lastnaem} - {self.email} - {self.phone}"
    

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        firstname = request.form['firstname']
        lastnaem = request.form['lastnaem']
        email = request.form['email']
        phone = request.form['phone']
        todo = Todo(firstname=firstname,lastnaem=lastnaem,email=email, phone=phone)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

if __name__ == "__main__":
    app.run(debug=True, port=8000)