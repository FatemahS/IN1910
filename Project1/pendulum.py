import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class Pendulum:
    """
    Class for calculating the motions of a double pendulum and calculating the
    energy.
    """
    def __init__(self, L=1, M=1):
        """
        Constructor that takes in the parameters L and M.
        These are by default, set to 1.
        """
        self.L = L
        self.M = M
        self.g = 9.81
        self.has_been_called = False

    def __call__(self, t, y):
        """
        Returns a tuple of the right hand sides of the system of equations.
        """
        theta, omega = y
        dtheta = omega
        domega = (-self.g*np.sin(theta))/self.L
        y = (dtheta, domega)
        return y

    def solve(self, y0, T, dt, angles="rad"):
        """
        Solves the system of equations from the call method, given the initial
        condition "y0", a time "T" and a "dt".
        If the angles of the initial condition are given in degrees, this
        should be specified by implementing the parameter angles="deg".
        Saves the solutions as private variables.
        """
        if angles == "deg":
            y0[0] = y0[0] * (np.pi/180)
            y0[1] = y0[1] * (np.pi/180)

        sol = solve_ivp(self, (0, T), y0, t_eval=dt)
        self._t = sol.t
        self._theta = sol.y[0]
        self._omega = sol.y[1]
        self.has_been_called = True

    @property
    def t(self):
        """
        Property that returns t and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._t
        else:
            raise ValueError("Solve-method not called.")

    @property
    def theta(self):
        """
        Property that returns theta and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._theta
        else:
            raise ValueError("Solve-method not called.")

    @property
    def omega(self):
        """
        Property that returns omega and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._omega
        else:
            raise ValueError("Solve-method not called.")

    @property
    def x(self):
        """
        Property that returns x.
        """
        return self.L*np.sin(self._theta)

    @property
    def y(self):
        """
        Property that returns y.
        """
        return -self.L*np.cos(self._theta)

    @property
    def potential(self):
        """
        Property that returns potential energy.
        """
        return self.M*self.g*(self.y + self.L)

    @property
    def vx(self):
        """
        Property that returns vx.
        """
        return np.gradient(self.x, self.t)

    @property
    def vy(self):
        """
        Property that returns vy.
        """
        return np.gradient(self.y, self.t)

    @property
    def kinetic(self):
        """
        Property that returns kinetic energy.
        """
        return 0.5*self.M*(self.vx**2 + self.vy**2)

class DampenedPendulum(Pendulum):
    """
    Subclass of Pendulum.
    Calculates a new right hand side of the equation for the pendulum, based
    on a dampening parameter B.
    """
    def __init__(self, B):
        """
        Constructor that takes in the dampening parameter B.
        """
        self.B = B
        Pendulum.__init__(self)


    def __call__(self, t, y):
        """
        Returns a tuple of the right hand sides of the system of equations.
        """
        theta, omega = y
        dtheta = omega
        domega = (-self.g*np.sin(theta))/self.L - (self.B/self.M)*omega
        y = (dtheta, domega)
        return y



if __name__ == "__main__":

    InitialValues = Pendulum()
    y0 = (np.pi/6, np.pi/8); T = 20; dt = np.linspace(0, T, 1000)
    InitialValues.solve(y0, T, dt)
    theta = InitialValues.theta
    t = InitialValues.t
    plt.plot(t, theta)
    plt.show()

    kinetic = InitialValues.kinetic
    potential = InitialValues.potential
    total = kinetic + potential
    plt.plot(t, kinetic)
    plt.plot(t, potential)
    plt.plot(t, total)
    plt.show()

    B = 0.2
    InitialValues = DampenedPendulum(B)
    y0 = (np.pi/6, np.pi/8); T = 20; dt = np.linspace(0, T, 1000)
    InitialValues.solve(y0, T, dt)
    t = InitialValues.t
    kinetic = InitialValues.kinetic
    potential = InitialValues.potential
    total = kinetic + potential
    plt.plot(t, total)
    plt.show()
