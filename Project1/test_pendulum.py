import numpy as np
from pendulum import Pendulum

def test_call():
    tol = 1E-6
    L = 2.7; theta = np.pi/6; omega = 0.15
    y = (theta, omega)
    InitialValues = Pendulum(L)
    expected = (0.15, -1.8166666667)
    computed = InitialValues(0,y)
    success = (abs(expected[0] - computed[0]) < tol) and (abs(expected[1] - computed[1]) < tol)
    print(computed)
    assert success, "Call method not correctly implemented!"

    theta = 0; omega = 0
    y = (theta, omega)
    InitialValues = Pendulum(L)
    expected = (0, 0)
    computed = InitialValues(0,y)
    success = (abs(expected[0] - computed[0]) < tol) and (abs(expected[1] - computed[1]) < tol)
    print(computed)
    assert success, "Call method does not return only zeros!"

def test_solve_has_not_been_called():
    InitialValues = Pendulum()
    success = (InitialValues.has_been_called != True)
    assert success, "Solve-method has been called!"

def test_solve_has_been_called():
    InitialValues = Pendulum()
    y0 = (np.pi, np.pi/4); T = 20; dt = np.linspace(0, T, 100)
    InitialValues.solve(y0, T, dt)
    success = (InitialValues.has_been_called == True)
    assert success, "Solve-method has not been called!"

def test_theta_omega():
    InitialValues = Pendulum()
    y0 = (0, 0); T = 20; dt = np.linspace(0, T, 100)
    InitialValues.solve(y0, T, dt)
    theta = InitialValues._theta
    nonzeros_theta = np.count_nonzero(theta)
    omega = InitialValues._omega
    nonzeros_omega = np.count_nonzero(omega)
    success = ((nonzeros_theta and nonzeros_omega) == 0)
    assert success, "Solve does not return only zeros!"

def test_time_points():
    InitialValues = Pendulum()
    y0 = (0, 0); T = 20; dt = np.linspace(0, T, 100)
    InitialValues.solve(y0, T, dt)
    success = np.array_equal(InitialValues._t, dt)
    assert success, "The timepoints are not equal!"

def test_radius():
    L = 1; tol = 1E-2
    InitialValues = Pendulum()
    y0 = (np.pi, np.pi/4); T = 20; dt = np.linspace(0, T, 100)
    InitialValues.solve(y0, T, dt)
    x = InitialValues.x
    y = InitialValues.y
    r_squared = np.zeros(len(dt))
    for i in range(len(dt)):
        r_squared[i] = x[i]**2 + y[i]**2
    success = (abs(r_squared[i] - L**2) < tol for i in range(len(dt)))
    assert success, "The radius is not constant!"
