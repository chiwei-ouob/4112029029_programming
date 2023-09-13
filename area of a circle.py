# import sys
# x=3
# print(x)
# print(type(x)) #輸出x的資料類型
# print(id(x)) #輸出x在記憶體中的絕對位置
# print(sys.getsizeof(x)) #輸出x所使用的記憶體空間

# y=str("3")
# print("The y is " + y)
# print((y+" ")*10)

# while x<=5:
#     print(x)
#     x=x+1
    #條件和程式區塊都不需要括號，但是條件後方需要冒號，且程式區塊一定要縮排

# while x<=6:
#     if x<5:
#         print (f"{x} is smaller than 5.")
#         x=x+1
#     elif x==5: #像是 else if
#         print (f"{x} is equal to 5.")
#         break

def greet(name):
    return f"Hello, {name}"

def function_area (radius):
    return 3.14*(radius**2)

def main():
    name=input("Type your name: ")
    print(greet(name))
    for i in range(3): #i從0到2
        while True: #True要大寫
            radius_str=input(f"Type the radius of the circle or \"exit\" ({3-i} chance left):")
            if radius_str.lower()=="exit":
                print(f"Thank, {name}. See you next time.")
                return
            radius=float(radius_str)
            if radius>0:
                area=function_area(radius)
                print(f"The area of the circle is {area}.")
                break
            else:
                print("Oops, something went wrone. Try again.")
    print(f"Thank, {name}. See you next time.")
    return

if __name__ == "__main__": #底線有兩個
    main()