from flask import Flask, render_template, request, redirect
import sqlite3
from helpers import init_db
app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return "The app is running!"

@app.route("/input")
def input_form():
    return render_template("income_expense.html")

@app.route("/add_income", methods=["POST"])
def add_income():
    income = request.form["income"]
    date = request.form["income_date"]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (amount, date) VALUES (?, ?)", (income, date))
    conn.commit()
    conn.close()
    return redirect("/input")

@app.route("/add_expense", methods=["POST"])
def add_expense():
    category = request.form["category"]
    expense = request.form["expense"]
    date = request.form["expense_date"]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", (category, expense, date))
    conn.commit()
    conn.close()
    return redirect("/input")

if __name__ == '__main__':
    print("starting app")
    app.run(debug=True)
