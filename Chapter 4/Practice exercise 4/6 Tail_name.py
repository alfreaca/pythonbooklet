name = input("What is your name: ")

def tail_name(name):
    name = name.replace(name[0], "")
    return name