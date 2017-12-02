#03. Program that prints Happy Birthday Song for a Friend

def greeting(style):
    wish= "Happy Birthday to You\n"
    print(wish*2)
    print("Happy Birthday, Dear " + name)
    print(wish)

name = input("What is your name?:")
greeting(name)


