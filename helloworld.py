def hello(to):
    return f"hello{to}!"

def goodbye(to):
    return f"goodbye{to}"

def main():
    user = input("Name: ")
    print(hello(user))
    print(goodbye(user))
    
if __name__ == '__main__':
    main()
