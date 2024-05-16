class Vogel:

    def __init__(self, schnabelform, kann_fliegen):
        self.schnabelform = schnabelform
        self.kann_fliegen = kann_fliegen

    def abheben(self):
        if self.kann_fliegen:
            print("Ich hebe ab")
        else:
            print("Ich kann leider nicht fliegen :(")

    def print_info(self):
        print(f"Ich bin ein Vogel, mein Schnabel ist {self.schnabelform}.")

    def __add__(self, other):
        if self.kann_fliegen and other.kann_fliegen:
            return Küken(self.schnabelform, True)
        else:
            return Küken(self.schnabelform, False)


class Küken(Vogel):

    def __init__(self, schnabelform, kann_fliegen, ist_süss=True):
        super().__init__(schnabelform, kann_fliegen)
        self.ist_süss = ist_süss

    def print_info(self):
        print(f"Ich bin ein Küken und ich bin süss: {self.ist_süss}")

    # def __str__(self):
    #     return f"Küken Object mit Eigenschaft süss: {self.ist_süss}"
    

v1 = Vogel("ründlich", True)
v2 = Vogel("ründlich", False)

x = "Teo"
y = "Detlef"
# print(v1 + v2)
v1.print_info()

mein_küken = v1 + v2
print(mein_küken)


# class FibCounter:

#     def __init__(self, ende):
#         self.ende = ende

#     def __iter__(self):
#         self.aktuell = 1
#         self.vorgänger = 0
#         return self

#     def __next__(self):
#         if self.aktuell < self.ende:
#             x = self.aktuell + self.vorgänger
#             self.vorgänger = self.aktuell
#             self.aktuell = x
#             return x
#         else:
#             raise StopIteration
        

# for i in FibCounter(50):
#     print(i)
