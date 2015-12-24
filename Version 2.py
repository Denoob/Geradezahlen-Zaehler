__author__="Denoob"
__version__="2.0"
__name__="Gearadezahlen-Zaehler"

print(__name__ + "von" + __author__ + __version__)
print("Dieses Programm wird bei der eingegeben Zahl alle Zahlen von 0 bis zu Ihrer Zahl, alle gerade Zahlen angeben (durch 2 teilbar)")

#Programmstart
from time import *

#Zählt in zweier-Schritten
#x = x+2
def counter(x):
    for i in range (0, x, 2):
        print(i)
        x+=2
    print("\nDas sind alle gerade Zahlen.")

numberIn = int(input("Bitte geben Sie die Zahl ein: "))

t1 = clock()
counter(numberIn)
t2 = clock()
t = t2-t1
print("%.2fs" % (t))

#Ende
exit = input("\nBitte drücken Sie Enter um das Programm zu beenden.")
