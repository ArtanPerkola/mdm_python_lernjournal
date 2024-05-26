from flask import Flask, request, render_template

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form.get('operation')
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))

    if operation == 'add':
        result = add(num1, num2)
        operation_str = "addition"
    elif operation == 'subtract':
        result = subtract(num1, num2)
        operation_str = "subtraction"
    elif operation == 'multiply':
        result = multiply(num1, num2)
        operation_str = "multiplication"
    elif operation == 'divide':
        result = divide(num1, num2)
        operation_str = "division"
    else:
        result = "Invalid operation"
        operation_str = "unknown operation"

    return render_template('result.html', result=result, num1=num1, num2=num2, operation=operation_str)

if __name__ == '__main__':
    app.run(debug=True)
