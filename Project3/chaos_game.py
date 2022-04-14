import numpy as np
import matplotlib.pyplot as plt
from math import pi, cos, sin

class ChaosGame:
    def __init__(self, n, r=1/2):
        if type(n) != int:
            raise TypeError()
        if type(r) != float:
            raise TypeError()
        if n < 3:
            raise ValueError()
        if 1 <= r <= 0:
            raise ValueError()

        self.n = n
        self.r = r
        self._generate_ngon()

    def _generate_ngon(self):
        thetai= np.linspace(0, 2*pi, self.n+1)
        corners = []
        for i in thetai:
            corners.append((sin(i), cos(i)))
        return np.array(corners)
    
        self.corners = corners

    def plot_ngon(self):
        plt.figure()
        plt.title('{}-gon'.format(self.n))
        plt.scatter(*zip(*self._generate_ngon()), c="black")
        plt.axis('equal')


    def _starting_point(self):
        x0 = 0
        weight = []
        
        for i in range(self.n):
            rand_weight = np.random.random()
            weight.append(rand_weight)
            
        weight = np.array(weight)
        w = np.array(weight/sum(weight))
          
        for i in range(self.n):
            x0 += w[i]*self._generate_ngon()[i]        
        return x0
     
          
    def iterate(self, steps, discard=5):
        del_list = []
        for i in range(1000):
            points = self._starting_point()
            del_list.append(points)        

        X = []
        X_indices = []
        rang = steps +discard

        
        for i in range(rang):
            if i <= (discard-1):
                index= np.random.randint(self.n)
                points =  self.r*del_list[index] + (1-self.r)*self._generate_ngon()[index]
                del_list.append(points)
                
            elif i == discard:
                index= np.random.randint(self.n)
                X_indices.append(index)
                first_x=  self.r*del_list[index] + (1-self.r)*self._generate_ngon()[index]
                X.append(first_x)
                
            else:
                index= np.random.randint(self.n)
                X_indices.append(index)
                x = self.r*X[i-(discard+1)] + (1-self.r)*self._generate_ngon()[index]
                X.append(x)
                
        self.X = X
        self.X_indices = X_indices
        return self.X
                                
        
    def plot(self, color=False, cmap="jet"): 
        if color == True:
            #colors = self.iterate(steps=len(self.X))
            colors = self.gradient_color()
        else:
            colors = "black"
        
        plt.scatter(*zip(*self.iterate(steps=1000)), c=colors, cmap=cmap)
        plt.title("Plot of generated points")
        plt.axis('equal')
        
    def show(self, color=False, cmap="jet"): 
        self.plot(color=color, cmap=cmap) #Calling plot method
        plt.show()
        
    @property 
    def gradient_color(self):
        color_list = []         
        color_list.append(self.X_indices(0))
        
        N = len(self.X)
        
        for i in range(N-1):
            c = (color_list[i] + self.X_indices[i])/2
            color_list.append(c)
        
        self.color_list = np.array(color_list)
        return self.color_list
           
       
    def savepng(self, outfile, color=False, cmap="jet"):     
        name = list(outfile)
        N = len(name)
        ending = False
        
        for i in range(N): 
            if name[i] == '.':
                ending = True
                end = ''.join(name[i:])
                break

        if ending == True:
            if end == '.png':
                name = outfile
                self.plot(color=color)
                plt.savefig(fname=name,dpi=300, transparent=True)
            else:
                print(end)

        else:
            end = '.png'
            name= ''.join(outfile+end)
            self.plot(color=color)
            plt.savefig(fname=name,dpi=300, transparent=True)
        
            

if __name__ == "__main__":     
    #2b - Tester plot_ngon n=3,4,5,6,7,8 for å bekrefte at hjørnene i n-gonet ser ut som forventet
    plot_n3 = ChaosGame(n=3)
    plot_n3.plot_ngon()

    plot_n4 = ChaosGame(n=4)
    plot_n4.plot_ngon()

    plot_n5 = ChaosGame(n=5)
    plot_n5.plot_ngon()

    plot_n6 = ChaosGame(n=6)
    plot_n6.plot_ngon()

    plot_n7 = ChaosGame(n=7)
    plot_n7.plot_ngon()

    plot_n8 = ChaosGame(n=8)
    plot_n8.plot_ngon()

    #Oppave 2c
    plot_1000 = ChaosGame(n=5)
    N = 1000
    p = []
    for i in range(N):
        points = plot_1000._starting_point()
        p.append(points)

    plot_1000.plot_ngon()
    plt.scatter(*zip(*p))
    plt.show()

    #Oppgave 2f - Sjekker gradient_color
    plot_gradient_color = ChaosGame(n=3)
    plot_gradient_color.plot()    
  
    
    #Oppgave 2h -Lager de fem figurene
    chaos1 = ChaosGame(n=3)
    chaos1.iterate(10000)
    chaos1.savepng("chaos1.png")
    plt.clf() #Clears figure after each figure

    chaos2 = ChaosGame(n=4, r=1/3)
    chaos2.iterate(10000)
    chaos2.savepng("chaos2.png", color=False)
    plt.clf()

    chaos3 = ChaosGame(n=5, r=1/3)
    chaos3.iterate(10000)
    chaos3.savepng("chaos3.png")
    plt.clf()

    chaos4 = ChaosGame(n=5, r=3/8)
    chaos4.iterate(10000)
    chaos4.savepng("chaos4.png")
    plt.clf()

    chaos5 = ChaosGame(n=6, r=1/3)
    chaos5.iterate(10000)
    chaos5.savepng("chaos5.png")
    plt.clf()
