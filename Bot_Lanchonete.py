# lanchonete bot!

bebidas=['coca','guaraná','guaravita','agua']

def find(text):
    i=0
    while i<4:
        if text.index(bebidas[i])>0:
            if   i==0:    print "a coca lata é 1,50"
            elif i==1:    print " teste guarana"
            elif i==2:    print "teste guaravita"
            elif i==3:    print "teste agua"
        else: print "posso ajudar?"
        i=i+1
        

