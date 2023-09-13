def function_circle():
    radius=float(input("\nType the radius of the circle:"))
    if radius <0:
        print("\nThis doesn\'t seem to be the radius of a NORMAL circle.\n")
        return -1, -1
    else:
        return 3.14*(radius**2), 6.28*radius
    
def function_rectangle():
    side_one=float(input("\nType one side of the rectangle:"))
    side_two=float(input("Alright, now type the other side of the rectangle:"))
    if side_one<0 or side_two<0:
        print("\nThese don\'t seem to be the sides of a NORMAL rectangle.\n")
        return -1, -1
    else:
        return side_one*side_two, 2*(side_one+side_two)
    
def function_triangle():
    import math
    side_one=float(input("\nType one side of the triangle:"))
    side_two=float(input("And, type another side of the triangle:"))
    side_three=float(input("Alright, now type the other side of the triangle:"))
    if (side_one+side_two<side_three) or (side_one+side_three<side_two) or (side_three+side_two<side_one): #有任兩邊長和小於第三邊
        print("\nThese don\'t seem to be the three sides of a NORMAL triangle.\n")
        return -1, -1
    else:
        average=(side_one+side_two+side_three)/2
        return math.sqrt(average*(average-side_one)*(average-side_two)*(average-side_three)), side_one+side_two+side_three

def main():
    while True:
        area=-1
        quest=input("Hi there, choose a geometric shape: \n Type \"1\" for a circle.\n Type \"2\" for a rectangle.\n Type \"3\" for a triangle.\n Type \"4\" if you don\'t need this program anymore.\n")
        if quest=="4":
            print("\nThanks for using. Have a nice day. :D\n")
            break
        elif quest=="1":
            shape="circle"
            area, perimeter=function_circle() 
        elif quest=="2":
            shape="rectangle"
            area, perimeter=function_rectangle()
        elif quest=="3":
            shape="triangle"
            area, perimeter=function_triangle()
        else:
            print("Oops, something went wrong. Try again. :(\n")
        if area!=-1:
            print(f"\nThe area of the {shape} is {area:.2f}.\nAnd the perimeter of it is {perimeter:.2f}.\n")             
    return
        
if __name__ == "__main__":
    main()