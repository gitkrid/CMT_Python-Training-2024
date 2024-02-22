"""
Iterators (oder auf Deutsch: Iteratoren) sind Klassen, welche zwei besondere
Methoden implementiert haben:
__iter__
__next__

Wir haben bei den Generatoren bereits gesehen, dass man die next() Methode
(der manuelle Aufruf der __next__ Methode) nutzen kann.
Effizienter können wir das innerhalb von for loops bspw. nutzen, die automatisch
die __next__ Methode aufruft, wenn vorher ein iterator object mit Hilfe der
__iter__ Methode zurückgegeben wurde.
"""
class MeinZähler:

    def __init__(self):
        self.stop = 10

    def __iter__(self):
        self.x = 0
        return self
    
    def __next__(self):
        x = self.x
        if x >= self.stop:
            raise StopIteration
        
        self.x = x + 1
        return x
    

for i in MeinZähler():
    print(i)
