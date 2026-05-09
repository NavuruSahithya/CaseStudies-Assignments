from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from datetime import datetime
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

app = Flask(__name__)

DATA_FILE = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(DATA_FILE, index=False)


# Home Route
@app.route('/')
def home():
    df = pd.read_csv(DATA_FILE)

    total_expense = df["Amount"].sum() if not df.empty else 0

    category_expense = (
        df.groupby("Category")["Amount"].sum().to_dict()
        if not df.empty else {}
    )

    highest_category = (
        max(category_expense, key=category_expense.get)
        if category_expense else "None"
    )

    monthly_expense = (
        df[df["Date"].str.contains(datetime.now().strftime("%Y-%m"))]["Amount"].sum()
        if not df.empty else 0
    )

    generate_chart(category_expense)

    return render_template(
        "dashboard.html",
        total=total_expense,
        monthly=monthly_expense,
        highest=highest_category,
        expenses=df.to_dict(orient='records')
    )


# Add Expense Route
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']

        try:
            amount = float(amount)

            new_data = pd.DataFrame([{
                "Date": date,
                "Category": category,
                "Amount": amount,
                "Description": description
            }])

            new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)

            return redirect(url_for('home'))

        except ValueError:
            return "Invalid Amount Entered"

    return render_template("add_expense.html")


# Generate Pie Chart
def generate_chart(category_expense):
    if not category_expense:
        return

    categories = list(category_expense.keys())
    amounts = list(category_expense.values())

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/chart.png")
    plt.close()


if __name__ == '__main__':
    app.run(debug=True)