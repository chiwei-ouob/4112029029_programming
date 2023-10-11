cat=[]
class Cat:
    what = "animal"
    def __init__(self, name):
        self.name = name
        
class Owner:
    def __init__(self):
        self.title = f"{cat[0].name}\'s owner"
        # self.title = "Kitty\'s owner"

def do_nothing():
    mycat = cat[0]
    return mycat

cat.append(Cat("Kitty"))
Owen = Owner()
print(Owen.title)
print(cat[0].what)