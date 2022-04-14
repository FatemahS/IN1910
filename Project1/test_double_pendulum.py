import numpy as np
import pytest
from double_pendulum import DoublePendulum

g = 9.81
M1 = 1
M2 = 1
L1 = 1
L2 = 1
omega1 = 0.15
omega2 = 0.15


def delta(theta1, theta2):
    return theta2 - theta1


def domega1_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2):
    dth = theta2 - theta1
    return (
        M2*L1*omega1**2*np.sin(dth)*np.cos(dth)+
        M2*g*np.sin(theta2)*np.cos(dth)+M2*L2*omega2**2*np.sin(dth)-
        (M1+M2)*g*np.sin(theta1))/((M1+M2)*L1-M2*L1*(np.cos(dth))**2
    )


def domega2_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2):
    dth = theta2 - theta1
    return (
        -M2*L2*omega2**2*np.sin(dth)*np.cos(dth)+
        (M1+M2)*g*np.sin(theta1)*np.cos(dth)-
        (M1+M2)*L1*omega1**2*np.sin(dth)-
        (M1+M2)*g*np.sin(theta2))/((M1+M2)*L2-M2*L2*(np.cos(dth))**2
    )




@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0),
        (0, 0.5235987755982988, 0.5235987755982988),
        (0.5235987755982988, 0, -0.5235987755982988),
        (0.5235987755982988, 0.5235987755982988, 0.0),
    ],
)
def test_delta(theta1, theta2, expected):
    assert abs(delta(theta1, theta2) - expected) < 1e-10


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5235987755982988, 3.4150779130841977),
        (0.5235987755982988, 0, -7.864794228634059),
        (0.5235987755982988, 0.5235987755982988, -4.904999999999999),
    ],
)
def test_domega1_dt(theta1, theta2, expected):
    assert (
        abs(domega1_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2) - expected)
        < 1e-10
    )


@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (0, 0, 0.0),
        (0, 0.5235987755982988, -7.8737942286340585),
        (0.5235987755982988, 0, 6.822361597534335),
        (0.5235987755982988, 0.5235987755982988, 0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    assert (
        abs(domega2_dt(M1, M2, L1, L2, theta1, theta2, omega1, omega2) - expected)
        < 1e-10
    )

def test_theta_omega():
    InitialValues = DoublePendulum()
    y0 = (0, 0, 0, 0); T = 20; dt = 1/60
    InitialValues.solve(y0, T, dt)
    theta1 = InitialValues._theta1
    nonzeros_theta1 = np.count_nonzero(theta1)
    omega1 = InitialValues._omega1
    nonzeros_omega1 = np.count_nonzero(omega1)
    theta2 = InitialValues._theta2
    nonzeros_theta2 = np.count_nonzero(theta2)
    omega2 = InitialValues._omega2
    nonzeros_omega2 = np.count_nonzero(omega2)

    success = ((nonzeros_theta1
                and nonzeros_omega1
                and nonzeros_theta2
                and nonzeros_omega2) == 0)
    assert success, "Solve does not return only zeros!"

def test_time_points():
    InitialValues = DoublePendulum()
    y0 = (0, 0, 0, 0); T = 10; dt = 0.05
    InitialValues.solve(y0, T, dt)
    success = np.array_equal(InitialValues._t, np.linspace(0, T, T/dt))
    assert success, "The timepoints are not equal!"

def test_call():
    tol = 1E-6
    theta1 = 0; omega1 = 0; theta2 = 0; omega2 = 0
    y = (theta1, omega1, theta2, omega2)
    InitialValues = DoublePendulum()
    expected = (0, 0, 0, 0)
    computed = InitialValues(0,y)
    success = ((abs(expected[0] - computed[0]) < tol)
        and (abs(expected[1] - computed[1]) < tol)
        and (abs(expected[2] - computed[2]) < tol)
        and (abs(expected[3] - computed[3]) < tol)
    )
    assert success, "Call method not correctly implemented!"
