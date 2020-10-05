alex = turtle.Turtle()     
alex.speed(100)
def rajz(szogek_szama,hossz,szin):
    alex.color(szin)
    for i in range(szogek_szama):
        alex.forward(hossz)           
        alex.left(360/szogek_szama)
    
rajz(6, 100, 'black')
rajz(6, 80, 'crimson')
rajz(6, 60, 'red')
rajz(6, 40, 'orange')
rajz(6, 20, 'yellow')
