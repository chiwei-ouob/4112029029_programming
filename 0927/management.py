import inventory_module as im
#記得檢查inventory_module的py檔是否有在同一資料夾中

def main():
    while True:
        print("\n進銷存系統\n1.新增物品\n2.移除物品\n3.查看庫存\n4.退出程式")
        choise=input("請選擇操作: ")
        if choise=="1":
            item_name=input("請輸入物品名稱: ")
            quantity=int(input("請輸入數量: "))
            im.add_item(item_name, quantity) #引用模組im的函式add_item
        elif choise=="2":
            item_name=input("請輸入物品名稱: ")
            quantity=int(input("請輸入數量: "))
            im.remove_item(item_name, quantity)
        elif choise=="3":
            im.view_inventory()
        elif choise=="4":
            break
if __name__ == "__main__": #底線有兩個
    main()