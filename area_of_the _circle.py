#2. program which accepts the radius of a circle from the user and compute the area.

def f(num):
    appx_pi=22/7
    area= appx_pi*num**2
    print("{} * {}^2 = ".format(appx_pi,num),end="")
    print("{0:.3f}".format(area))
    
radius=int(input("Enter the radius: "))

f(radius)

