import inventory_module as im

def main():
    while True:
        print("\n圖書管理系統\n1.新增書籍\n2.借閱書籍\n3.查尋書籍\n4.歸還書籍\n5.退出程式")
        choise=input("請選擇操作: ")
        if choise=="1":
            title=input("請輸入書籍名稱: ")
            author=input("請輸入作者姓名: ")
            date=input("請輸入書籍出版日期: ")
            ISBN=input("請輸入書籍ISBN編號: ")
            quantity=int(input("請輸入增加數量: "))
            im.add_item(title, author, date, ISBN, quantity) #引用模組im的函式
        elif choise=="2":
            item_index=input("請輸入書籍名稱或ISBN編號: ")
            im.borrow_item(item_index)
        elif choise=="3":
            im.view_inventory()
        elif choise=="4":
            item_index=input("請輸入書籍名稱或ISBN編號: ")
            im.return_item(item_index)
        elif choise=="5":
            break

if __name__ == "__main__": #底線有兩個
    main()