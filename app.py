from flask import Flask
from src.factorial import factorial

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! '

@app.route('/factorial/<int:n>')
def factorial_route(n):
    try:
        result = factorial(n)
        return f'The factorial of {n} is {result}.'
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
