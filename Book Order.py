books =[
    {"name":"book1","price":100},
    {"name":"book2","price":200},
    {"name":"book3","price":300},
    {"name":"book4","price":400}
    ] #列表中含有字典
orders =[
    {"name":"book1","quantity":2},
    {"name":"book3","quantity":4},
    ] #列表中含有字典
total=0
for order in orders:
  for book in books:
    if book['name']==order['name']:
      total+=order['quantity']*book['price']
      break
if total >=1000:
  print (f"Yeah, you have a discount! Total amount is {total*0.9}.")
else:
  print (f"Total amount is {total}.")