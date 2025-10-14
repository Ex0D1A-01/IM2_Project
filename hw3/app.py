from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('reg.html')


@app.route('/submit', methods=['POST'])
def submit():
  
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    sex = request.form['sex']
    institution = request.form['institution']
    email = request.form['email']


    return render_template(
        'result.html',
        lastname=lastname,
        firstname=firstname,
        sex=sex,
        institution=institution,
        email=email
    )


if __name__ == '__main__':
    app.run(debug=True)
