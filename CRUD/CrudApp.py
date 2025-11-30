from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret-key"


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/studentdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        sex = request.form.get('sex')
        department = request.form.get('department')

      
        if not name or not sex or not department:
            flash('Please fill all fields.', 'error')
            return redirect(url_for('add_student'))

        new_stud = Student(name=name, sex=sex, department=department)
        db.session.add(new_stud)
        db.session.commit()

        flash('Student Added Successfully!', 'add')
        return redirect(url_for('index'))

    return render_template('add_edit.html', action="Add", student=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    stud = Student.query.get_or_404(id)

    if request.method == 'POST':
        stud.name = request.form.get('name')
        stud.sex = request.form.get('sex')
        stud.department = request.form.get('department')

        if not stud.name or not stud.sex or not stud.department:
            flash('Please fill all fields.', 'error')
            return redirect(url_for('edit_student', id=id))

        db.session.commit()
        flash('Student Updated Successfully!', 'edit')
        return redirect(url_for('index'))

    return render_template('add_edit.html', action="Edit", student=stud)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    stud = Student.query.get_or_404(id)
    db.session.delete(stud)
    db.session.commit()
    flash('Student Deleted Successfully!', 'delete')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
