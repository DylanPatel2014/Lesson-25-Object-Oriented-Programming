class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("Blu",7)
greeny=parrot("Greeny",4)
print("Blu is a {}".format(blu.species))
print("Greeny is also a {}".format(greeny.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(greeny.name,greeny.age))

