from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Total"])

def get_last_total():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = list(csv.reader(file))
            if len(reader) > 1:
                total = float(reader[-1][2])
    except:
        pass
    return total

@app.route("/", methods=["GET", "POST"])
def index():
    initialize_file()

    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]

        new_total = get_last_total() + amount

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, new_total])

        return redirect("/")

    expenses = []
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(row)

    total = get_last_total()

    return render_template("index.html", expenses=expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)