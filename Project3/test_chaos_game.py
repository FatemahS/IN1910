#Oppgave 2h - Skriver noen unit tester

from chaos_game import ChaosGame

#Tester konstruktøren __init__ med de fire unit testene under
def test_init1():
    try:
        print("Setter n=1.")
        n_1 = ChaosGame(n=1)
        print("n er gyldig")
    except ValueError:
        print("Feilmelding: n er lavere enn 3, og derfor ugyldig")
test_init1()
        
def test_init2():        
    try:
        print("Setter n=3.")
        n_3 = ChaosGame(n=3)
        print("n er gydlig")
    except ValueError:
        print("n er ugyldig")
test_init2()
 
def test_init3():  
    try:
        print("Setter n=8")
        n_3_float =ChaosGame(n=float(3))
        print("n er gyldig")
    except TypeError:
        print("n er en float, og derfor ugyldig")
test_init3()
    
def test_init4():        
    try:
        print("Setter r=1")
        r_neg1 = ChaosGame(n=3, r=float(1/2))
        print("r er gyldig")
    except TypeError:
        print("r er en ikke en float og derfor ugyldig") 
test_init4()

#Tester at lengden til X og X_indices i iterate-metoden er lik steps med de fire funksjonene under
def test_iterate1():
    test_iterate1= ChaosGame(n=3)
    test_iterate1.iterate(steps=100)
    assert 100 == len(test_iterate1.X), "Failed."
    print("Success. The length of X is 100 when steps=100.")
    
test_iterate1()

def test_iterate2():
    test_iterate2= ChaosGame(n=3)
    test_iterate2.iterate(steps=100)
    assert 100 == len(test_iterate2.X_indices), "Failed."
    print("Success. The length of X is 100 when steps=100.")
    
test_iterate2()
  
def test_iterate3():
    test_iterate3= ChaosGame(n=3)
    test_iterate3.iterate(steps=100)
    assert 100 == len(test_iterate3.X), "Failed. The length of X is not 10 when steps=150. "
    print("Success. The length of X is 10 when steps=150.")

test_iterate3()

def test_iterate4():
    test_iterate4= ChaosGame(n=3)
    test_iterate4.iterate(steps=150)    
    assert 10 == len(test_iterate4.X_indices), "Failed. The length of X_indices is not 10 when steps=150. "
    print("Success. The length of X is 10 when steps=150.")
    
test_iterate4()

def test_generatengon():
    test_ngon = ChaosGame(n=3)
    length_corners = len(test_ngon._generate_ngon())
    assert test_ngon.n == length_corners, "n is not the same as the lenght of the list of corners."
    print("Success, the lenght of the list of corners is the same as n. n=3 gives a list with length {}".format(length_corners))

test_generatengon()
        
