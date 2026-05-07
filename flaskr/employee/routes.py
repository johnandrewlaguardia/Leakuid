from flask import render_template, request, redirect, url_for
from . import employee_bp
from .models import db, Employee


# READ
@employee_bp.route('/')
def index():
    employees = Employee.query.all()
    return render_template('employee/index.html', employees=employees)


# CREATE
@employee_bp.route('/create', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        lastname = request.form['last_name']
        firstname = request.form['first_name']
        middlename = request.form['middle_name']

        new_employee = Employee(
            lastname=lastname,
            firstname=firstname,
            middlename=middlename
        )

        db.session.add(new_employee)
        db.session.commit()

        return redirect(url_for('employee.index'))

    return render_template('employee/create.html')


# UPDATE
@employee_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)

    if request.method == 'POST':
        employee.lastname = request.form['last_name']
        employee.firstname = request.form['first_name']
        employee.middlename = request.form['middle_name']

        db.session.commit()

        return redirect(url_for('employee.index'))

    return render_template('employee/update.html', employee=employee)


# DELETE
@employee_bp.route('/delete/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for('employee.index'))