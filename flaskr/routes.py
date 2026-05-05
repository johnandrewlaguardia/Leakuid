from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Employee

bp = Blueprint('employees', __name__, url_prefix='/employees')

# 📖 READ (employee list)
@bp.route('/')
def index():
    employees = Employee.query.all()
    return render_template('employee/index.html', employees=employees)


# ➕ CREATE
@bp.route('/create', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        emp = Employee(
            employee_id=request.form['employee_id'],
            last_name=request.form['last_name'],
            first_name=request.form['first_name'],
            middle_name=request.form['middle_name']
        )
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('employees.index'))

    return render_template('employee/create.html')


# ✏️ UPDATE
@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    emp = Employee.query.get_or_404(id)

    if request.method == 'POST':
        emp.employee_id = request.form['employee_id']
        emp.last_name = request.form['last_name']
        emp.first_name = request.form['first_name']
        emp.middle_name = request.form['middle_name']

        db.session.commit()
        return redirect(url_for('employees.index'))

    return render_template('employee/update.html', emp=emp)


# ❌ DELETE
@bp.route('/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('employees.index'))