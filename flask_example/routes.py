# Here, we import the forms, since they are used for routing.
# We also add routing to the registration and the login pages.

from flask import render_template, url_for, flash, redirect
from flask_example import app
from flask_example.forms import MatrixForm
import numpy as np


@app.route('/')
def myhome():
    return render_template('home.html')
myhome.username = "Anonymous"
myhome.homepage = None

def password_is_valid(username,password):
    return password=="123"

@app.route("/matrix", methods=['GET', 'POST'])
def matrixpage():
    form = MatrixForm()
    if not form.validate_on_submit():
        form.matrix.data = matrixpage.matrix_string
        return render_template('matrix.html', title='Data', form=form)
    else:
        matrixpage.matrix_string = form.matrix.data
        try:
            matrix = np.matrix(matrixpage.matrix_string)
        except Exception  as error:
            return render_template('matrix.html', title='Error', form=form,  error=error)

        try:
            inverse_matrix = np.linalg.inv(matrix)
        except Exception  as error:
            return render_template('matrix.html', title='Error', form=form, matrix=matrix, error=error)

        return render_template('matrix.html', title='Data', form=form, matrix=matrix, inverse_matrix=inverse_matrix)
matrixpage.matrix_string = "[1 2];\n[3 4]\n"



@app.route("/leximin", methods=['GET', 'POST'])
def leximinpage():
    form = MatrixForm()
    if not form.validate_on_submit():
        form.matrix.data = leximinpage.matrix_string
        return render_template('leximin.html', title='Data', form=form)
    else:
        matrixpage.matrix_string = form.matrix.data
        try:
            valuation_matrix = np.asarray(np.matrix(matrixpage.matrix_string))
        except Exception  as error:
            return render_template('leximin.html', title='Error', form=form,  error=error)

        import fairpy
        try:
            # allocation = fairpy.divide(algorithm=fairpy.items.leximin_optimal_allocation, input=[[1,2],[3,4]])
            print("valuation_matrix.shape: ", valuation_matrix.shape)
            valuation_matrix = fairpy.ValuationMatrix(valuation_matrix)
            print("valuation_matrix: ", valuation_matrix)
            print("num_of_agents: ", valuation_matrix.num_of_agents)
            print("num_of_objects: ", valuation_matrix.num_of_objects)
            allocation = fairpy.divide(algorithm=fairpy.items.leximin_optimal_allocation, input=valuation_matrix)
            # allocation = fairpy.items.leximin_optimal_allocation(fairpy.ValuationMatrix(valuation_matrix))
        except Exception  as error:
            return render_template('leximin.html', title='Error', form=form, valuation_matrix=valuation_matrix, error=error)

        return render_template('leximin.html', title='Data', form=form, valuation_matrix=valuation_matrix, allocation=allocation)
leximinpage.matrix_string = "[1 2];\n[3 4]\n"
