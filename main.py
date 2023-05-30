from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('caculate_total_amount.html')


@app.route('/', methods=['POST'])
def submit():
    choice = request.form['choice']
    try:
        if choice == 'caculate_total_amount':
            interest_rate = float(request.form['interest_rate']) / 100
            starting_capital = float(request.form['starting_capital'])
            deposit_term = int(request.form['deposit_term'])
            calculated = starting_capital * (1 + interest_rate) ** deposit_term
            calculated = round(calculated, 10)
        elif choice == 'calculate_interest_rate':
            your_goal = float(request.form['your_goal'])
            starting_capital = float(request.form['starting_capital'])
            deposit_term = int(request.form['deposit_term'])
            calculated = ((your_goal/starting_capital)**(1/deposit_term) - 1) * 100
            calculated = round(calculated, 10)
        elif choice == 'calculate_starting_capital':
            your_goal = float(request.form['your_goal'])
            deposit_term = int(request.form['deposit_term'])
            interest_rate = float(request.form['interest_rate']) / 100
            calculated = your_goal/((1 + interest_rate)**deposit_term)
            calculated = round(calculated, 10)
        else:
            your_goal = float(request.form['your_goal'])
            starting_capital = float(request.form['starting_capital'])
            interest_rate = float(request.form['interest_rate']) / 100
            calculated = (math.log(your_goal/starting_capital)/math.log(1+interest_rate))
    except:
        return render_template(f"{choice}.html", selected_option=choice)
    return render_template(f"{choice}.html", calculated=calculated, selected_option=choice )


def interest_rate(var):
    interest_rate = 1.5
    return interest_rate


def starting_capital(var):
    starting_capital = 1.5
    return starting_capital


def deposit_term(var):
    deposit_term = 1.5
    return deposit_term



if __name__ == '__main__':
    app.run(debug=True)