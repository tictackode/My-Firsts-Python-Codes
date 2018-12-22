
# exemplo de classe inimigo
from random import randint
class Enemy:
        nome="none"
        life=0
        ataque=0
        def __init__(self,nome,life,ataque):
                self.nome=nome
                self.life=life
                self.ataque=ataque
        def showStats(self):
                print self.nome,"Life: ",self.life,"Ataque: ",self.ataque
        def genStats(self):
                self.life=randint(1,50)
                self.ataque=randint(1,20)

# funcao que checa qual dos 2 tem mais life

def strongest(enemy1,enemy2):
        if enemy1.life>enemy2.life: print enemy1.nome," é o mais forte!"
        else:   print enemy2.nome," é o mais forte!"
