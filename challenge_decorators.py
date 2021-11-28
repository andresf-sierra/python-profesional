def general_grievous(func):
    def wrapper ():
        func()
        print("Grievous: General Kenobi")
    return wrapper

@general_grievous
def general_kenobi():
    print("Kenobi: Hello There!")

general_kenobi()
print("*Sound lightsabers*")            
