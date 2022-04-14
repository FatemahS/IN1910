import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class DoublePendulum:
    """
    Class for calculating the motions of a double pendulum, calculating the
    energy and animating it's motions.
    """
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
        """
        Constructor that takes in the parameters M1, L1, M2 and L2.
        These are default set to 1.
        """
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2
        self.g = 9.81
        self.has_been_called = False

    def __call__(self, t, y):
        """
        Returns a tuple of the right hand sides of the system of equations.
        """
        theta1, omega1, theta2, omega2 = y
        dth = theta2 - theta1
        domega1 = (
            self.M2*self.L1*omega1**2*np.sin(dth)*np.cos(dth)
            + self.M2*self.g*np.sin(theta2)*np.cos(dth)
            + self.M2*self.L2*omega2**2*np.sin(dth)
            - (self.M1+self.M2)*self.g*np.sin(theta1)) / ((self.M1+self.M2)*self.L1-self.M2*self.L1*(np.cos(dth))**2
        )

        domega2 = (
            - self.M2*self.L2*omega2**2*np.sin(dth)*np.cos(dth)
            + (self.M1+self.M2)*self.g*np.sin(theta1)*np.cos(dth)
            - (self.M1+self.M2)*self.L1*omega1**2*np.sin(dth)
            - (self.M1+self.M2)*self.g*np.sin(theta2)) / ((self.M1+self.M2)*self.L2-self.M2*self.L2*(np.cos(dth))**2
        )

        dtheta1 = omega1
        dtheta2 = omega2
        y = (dtheta1, domega1, dtheta2, domega2)
        return y

    def solve(self, y0, T, dt, angles="rad", method="Radau"):
        """
        Solves the system of equations from the call method, given the initial
        condition "y0", a time "T" and a "dt".
        If the angles of the initial condition are given in degrees, this
        should be specified by implementing the parameter angles="deg".
        Saves the solutions as private variables.
        """
        if angles == "deg":
            for i in range(len(y0)):
                y0[i] = y0[i] * (np.pi/180)

        self.dt = dt
        dt_ = np.linspace(0, T, T/dt)
        sol = solve_ivp(self, (0, T), y0, t_eval=dt_)
        self._t = sol.t
        self._theta1 = sol.y[0]
        self._omega1 = sol.y[1]
        self._theta2 = sol.y[2]
        self._omega2 = sol.y[3]
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
    def theta1(self):
        """
        Property that returns theta1 and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._theta1
        else:
            raise ValueError("Solve-method not called.")

    @property
    def omega1(self):
        """
        Property that returns omega1 and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._omega1
        else:
            raise ValueError("Solve-method not called.")

    @property
    def theta2(self):
        """
        Property that returns theta2 and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._theta2
        else:
            raise ValueError("Solve-method not called.")

    @property
    def omega2(self):
        """
        Property that returns omega2 and checks if the solve-method
        has been called.
        """
        if self.has_been_called == True:
            return self._omega2
        else:
            raise ValueError("Solve-method not called.")

    @property
    def x1(self):
        """
        Property that returns x1.
        """
        return self.L1*np.sin(self._theta1)

    @property
    def y1(self):
        """
        Property that returns y1.
        """
        return -self.L1*np.cos(self._theta1)

    @property
    def x2(self):
        """
        Property that returns x2.
        """
        return self.x1+self.L2*np.sin(self._theta2)

    @property
    def y2(self):
        """
        Property that returns y2.
        """
        return self.y1-self.L2*np.cos(self._theta2)

    @property
    def potential(self):
        """
        Property that returns potential energy.
        """
        P1 = self.M1*self.g*(self.y1 + self.L1)
        P2 = self.M2*self.g*(self.y2 + self.L1 + self.L2)
        return P1 + P2

    @property
    def vx1(self):
        """
        Property that returns vx1.
        """
        return np.gradient(self.x1, self.t)

    @property
    def vy1(self):
        """
        Property that returns vy1.
        """
        return np.gradient(self.y1, self.t)

    @property
    def vx2(self):
        """
        Property that returns vx2.
        """
        return np.gradient(self.x2, self.t)

    @property
    def vy2(self):
        """
        Property that returns vy2.
        """
        return np.gradient(self.y2, self.t)

    @property
    def kinetic(self):
        """
        Property that returns kinetic energy.
        """
        K1 = 0.5*self.M1*(self.vx1**2 + self.vy1**2)
        K2 = 0.5*self.M2*(self.vx2**2 + self.vy2**2)
        return K1 + K2

    def create_animation(self):
        """
        Creates animation.
        """
        fig = plt.figure()

        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))

        self.pendulums, = plt.plot([], [], 'rH-', lw=2)

        self.animation = animation.FuncAnimation(fig,
                                                self._next_frame,
                                                frames=range(0, len(self.x1)),
                                                repeat=None,
                                                interval=1000*self.dt,
                                                blit=True)

    def _next_frame(self, i):
        """
        Calculates the next frame for the create animation method.
        """
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        """
        Shows the animation.
        """
        plt.show()


    def save_animation(self, filename):
        """
        Takes a filename and saves the animation as that name.
        Must be called before the show animation method.
        """
        self.animation.save(filename, fps=60)

if __name__ == "__main__":

    InitialValues = DoublePendulum()
    y0 = (np.pi/6, 0.5, np.pi/2, 0.5); T=15; dt=0.01
    InitialValues.solve(y0, T, dt)
    t = InitialValues.t
    kinetic = InitialValues.kinetic
    potential = InitialValues.potential
    total = kinetic + potential
    plt.plot(t, kinetic, label="Kinetic")
    plt.plot(t, potential, label="Potential")
    plt.plot(t, total, label="Total")
    plt.legend()
    plt.show()

    InitialValues = DoublePendulum()
    y0 = (np.pi, np.pi, -np.pi, -np.pi); T=10; dt=1/60
    InitialValues.solve(y0, T, dt)
    InitialValues.create_animation()
    InitialValues.save_animation("example_simulation.mp4")
    InitialValues.show_animation()

    """Task 5: Plotting the trajectories of three double pendulums with slight change in intial conditions"""

    fig, axs = plt.subplots(3, sharex=True, sharey=True)
    fig.suptitle("Three double pendulum trajectories: Chaotic system")

    y0 = (np.pi/2, 1, np.pi, 1)
    InitialValues.solve(y0, T, dt)
    x1 = InitialValues.x1
    y1 = InitialValues.y1
    x2 = InitialValues.x2
    y2 = InitialValues.y2
    axs[0].plot(x1, y1, "y")
    axs[0].plot(x2, y2, "g")

    y0 = (np.pi/3, 1, 2*np.pi/3, 1)
    InitialValues.solve(y0, T, dt)
    x1 = InitialValues.x1
    y1 = InitialValues.y1
    x2 = InitialValues.x2
    y2 = InitialValues.y2
    axs[1].plot(x1, y1, "y")
    axs[1].plot(x2, y2, "g")

    y0 = (3*np.pi/4, 1, 3*np.pi/4, 1)
    InitialValues.solve(y0, T, dt)
    x1 = InitialValues.x1
    y1 = InitialValues.y1
    x2 = InitialValues.x2
    y2 = InitialValues.y2
    axs[2].plot(x1, y1, "y", label="First pendulum")
    axs[2].plot(x2, y2, "g", label="Second pendulum")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("chaotic_pendulum.png")
    plt.show()


    """Comments on the plot: With only slight changes in the initial conditions, the three systems of double pendulums
    are showing completely different outcomes with different moving patterns,
    illustrating the major difference a slight change in intitial conition does in a chaotic system and
    the chaotic nature of the double pendulum over time."""
