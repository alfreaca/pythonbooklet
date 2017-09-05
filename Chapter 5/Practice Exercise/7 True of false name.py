name = input("What is your name: ")

def long_name(name):
    if len(name) > 14:
        return True
    else:
        return False

print(long_name(name))
