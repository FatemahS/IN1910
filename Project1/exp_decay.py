from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay:
    """
    Solves the exponential decay ODE.
    """
    def __init__(self, a):
        """
        Constructor that a decay constant "a" as a parameter.
        """
        self.a = a

    def __call__(self, t, u):
        """
        Returns the derivative of u.
        """
        return -self.a * u

    def solve(self, u0, T, dt):
        """
        Solves and returns the ODE.
        """
        sol = solve_ivp(self.__call__, (0, T), u0, t_eval=dt)
        t = sol.t; u = sol.y[0]
        return t, u

if __name__ == "__main__":
    a = 0.4; u0 = (50,); T = 20; dt = np.linspace(0, T, 100)
    decay_model = ExponentialDecay(a)
    t, u = decay_model.solve(u0, T, dt)

    plt.plot(t, u, label="Exponential decay")
    plt.xlabel("Time")
    plt.ylabel("u")
    plt.legend()
    plt.show()
