class Tuna:
    def __init__(self):
        print('Tuna')

    def swim(self):
        print('I am swimming')


#flipper = Tuna()
#flipper.swim()

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(80)
charles = Enemy(60)

jason.get_energy()
charles.get_energy()

#print jason.energy
#print charles.energy


