from flask import Flask, render_template

dsa = Flask(__name__)

@dsa.route('/')
def  index():
    return render_template('web.html')

if __name__ == "__main__":
    dsa.run(debug=True)