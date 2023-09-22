books =[
    {"name":"book1","quantity":1,"price":100},
    {"name":"book2","quantity":2,"price":200},
    {"name":"book3","quantity":3,"price":300},
    {"name":"book4","quantity":4,"price":400}
    ] #列表中含有字典
nmuber_of_book=4
while True:
  function=int(input("1 for adding. \n2 for removing. \n3 for updating. \n4 for displaying all. \n5 for exiting the program."))
  if (function==1):
    temp_name=str(input("Tell me the name of the book you wanna add: "))
    books.append({"name":temp_name,"quantity":0,"price":0})
    nmuber_of_book+=1
    print(f"The book \"{temp_name}\" has been added to the list successfully.")
  elif (function==2):
    temp_name=str(input("Tell me the name of the book you wanna remove: "))
    for book_del in books:
      if book_del['name']==temp_name:
        books.remove({"name":book_del['name'],"quantity":book_del['quantity'],"price":book_del['price']})
        print(f"The book \"{book_del['name']}\" has been removed from the list successfully.")
        nmuber_of_book-=1
        break
  elif (function==3):
    target=str(input("Tell me the name of the book you wanna update the quantity of: "))
    target_sequence=0
    for book_update in books: 
      if target == book_update['name']:
        temp_quantity=int(input("Tell me the quantity: "))
        temp_price=int(input("Tell me the price: "))
        books[target_sequence]={"name":target,"quantity":temp_quantity,"price":temp_price}
        print(f"The infos of {temp_name} is updated successfully: {temp_name}\'s price is {temp_price}, and it remains {temp_quantity}.")
        break
      target_sequence+=1
    print("That's not one of the books.")
  elif (function==4):
    for book in books:
      print(f"{book['name']}\'s price is {book['price']}, and it remains {book['quantity']}.")
  elif (function==5):
    break