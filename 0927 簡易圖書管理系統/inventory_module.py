inventory=[]
    # inventory是列表，其元素為字典，標籤依序為title/author/date/ISBN/quantity
    
def add_item(title, author, date, ISBN, quantity):
    # target_sequence=0
    # for target in inventory: #target是字典
    #     if title == target["title"]:
    #         inventory[target_sequence]["quantity"]+=quantity
    #     else:
            inventory.append({"title":title,"author":author,"date":date,"ISBN":ISBN,"quantity":quantity})
        # target_sequence+=1 #已完成，若輸入重複的書名則照樣新增一個字典

def borrow_item(index):
    target_sequence=0
    for target in inventory:
        if (index == target["title"]) or (index == target["ISBN"]):
            if target["quantity"]>=1:
                inventory[target_sequence]["quantity"]-=1
                print("成功借閱")
                break
            else:
                print("書籍庫存不足")
                break
        target_sequence+=1

def return_item(index):
    target_sequence=0
    for target in inventory:
        if (index == target["title"]) or (index == target["ISBN"]):
            inventory[target_sequence]["quantity"]+=1
            print("成功歸還")
            break
        target_sequence+=1

# def find_item_by_name (title):
#     for target in inventory:
#         if title in inventory:
#             return 1
#         else:
            # return 0 #用不到，暫時捨棄

def view_inventory():
    for book in inventory:
        print(f"書名: {book['title']} 作者: {book['author']} 出版日期: {book['date']} ISBN編號: {book['ISBN']} 庫存數量: {book['quantity']}")

