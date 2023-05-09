from flask import Flask, render_template, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from  wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


#creating Calculator with FLaskForm library
class Calculator(FlaskForm):
    num1 = FloatField('Enter first number', validators=[DataRequired()])
    num2 = FloatField('Enter second number', validators=[DataRequired()])
    ope = SelectField('Enter the name of operation to be performed', choices=[('add', 'addition'),
                                                                               ('sub', 'subtract'),
                                                                               ('mult', 'multiply'),
                                                                               ('div', 'divide')])
    submit = SubmitField('Submit')



##this is our main page for calculator
@app.route('/', methods = ['GET', 'POST'])
def index():
    form = Calculator()

    #after clicking submit button it will redirect to result page
    if form.validate_on_submit():
        session['num1'] = form['num1'].data
        session['num2'] = form['num2'].data
        session['ope'] = form['ope'].data
        return redirect('result')
    
    #else it will return to home page
    return render_template('home.html', form = form)



#this is our final page for displaying result
@app.route('/result', methods = ['GET', 'POST'])
def result():
    if session['ope'] == 'add':
        operation = 'Addition'
        res = session['num1'] + session['num2']
        return render_template('answer.html', operation = operation, res = res)
    
    if session['ope'] == 'sub':
        operation = 'Subtraction'
        res = session['num1'] - session['num2']
        return render_template('answer.html', operation = operation, res = res)
    
    if session['ope'] == 'mult':
        operation = 'Multiplication'
        res = session['num1'] * session['num2']
        return render_template('answer.html', operation = operation, res = res)
    
    if session['ope'] == 'div':
        operation = 'Division'
        res = session['num1'] / session['num2']
        return render_template('answer.html', operation = operation, res = res)
        
            
        





if __name__ == '__main__':
    app.run()