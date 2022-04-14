import numpy as np
import matplotlib.pyplot as plt


class AffineTransform():
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
	    self.a = a
	    self.b = b
	    self.c = c
	    self.d = d
	    self.e = e
	    self.f = f
    
    def __call__(self, x, y):
        x = self.a*x + self.b*y + self.e
        y = self.c*x + self.d*y + self.f
        return [x, y]

if __name__ == "__main__":
    functions = []
    functions += [AffineTransform(0, 0, 0, 0.16, 0, 0)]
    functions += [AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)]
    functions += [AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)]
    functions += [AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)]

    def non_uniform(x, y):
        p = [0.01, 0.85, 0.07, 0.07]
        p_cumulative = [0.01, 0.85+0.01, 0.85+0.07+0.01, sum(p)]

        r = np.random.random()
        for j, p in enumerate(p_cumulative):
            if r < p:
                return functions[j](x, y)

    def iterate(n):
        x = []
        x += [[0, 0]]
        for i in range(n):
            X = non_uniform(x[i][0], (x[i][1]))
            x.append(X)
        return x

    points = iterate(5000)

    def save(outfile):
        plt.scatter(*zip(*points), s=0.1, color="forestgreen")
        plt.axis('equal')
        marker = '.'
        if ".png" in outfile:
            plt.savefig(outfile)
        elif "." in outfile and "png" not in outfile:
            raise SyntaxError("Please save file as PNG file")
        else:
            plt.savefig(outfile + ".png")
    save("barnsley_fern.png")
