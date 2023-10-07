class Discountable: 
    def apply_discount(self, price, discount_percentage): #折後單價
        discount_price = price * (discount_percentage/100)
        return discount_price
    
class Book(Discountable): #書籍屬性 #Book類別的物件可重複使用apply_discount方法
    def __init__(self, isbn, title, author, price, stock): 
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        
    def display_info(self): #顯示書籍資料
        return (f"標題: {self.title}, 作者: {self.author}, 單價: ${self.price}, ISBN: {self.isbn} 目前剩餘庫存: {self.stock}")

inventory = [] #元素的屬性依序為 isbn, title, author, price, stock
cart = [] #這是購物車

def add_inventory():
    isbn=input("請輸入書籍的ISBN: ")
    title=input("請輸入書籍的標題: ")
    author=input("請輸入書籍的作者: ")
    price=float(input("請輸入書籍的價格: "))
    stock=int(input("請輸入庫存數量: "))
    book=Book(isbn, title, author, price, stock)
    inventory.append(book)
    
def find_inventory(index):
    for target in inventory:
        if (index == target.title) or (index == target.isbn):
            return target


def main():
    
    #輸入五種以上書籍名稱與折扣
    info_quantity = 0
    while True: 
        print ("請輸入書籍資訊。 ")
        add_inventory()
        info_quantity+=1
        if info_quantity >= 5: #記得改回5
            choice=input("剛剛那是最後一本書嗎? 是請按1，不是請按任意鍵: ")
            if choice == "1":
                break
    discount=int(input("請輸入商品折扣折數(%): "))
    
    #輸出剛剛輸入過的資訊
    print ("書籍資訊: ")
    for book in inventory:
        print (f"{book.display_info()}\n")
    print (f"總金額折扣折數: {discount}%")

    #輸入購買清單
    purchase_quantity = 0
    total = 0
    while True: 
        index = input("請輸入欲購買之書籍資訊: ")
        for target in inventory:
            if (index == target.title) or (index == target.isbn):
                quantity = int(input("請輸入欲購買之數量: "))
                #print (target.title)
                total += target.price * quantity
                if quantity<=target.stock:
                    target.stock-=quantity
                    cart.append(target)
                    purchase_quantity+=1
                    #print(cart[0].title)
                    print (f"total:{total}")
                else:
                    print ("庫存不足，再試一次。")
        if purchase_quantity >= 2: 
            choice=input("剛剛那是最後一本書嗎? 是請按1，不是請按任意鍵: ")
            if choice == "1":
                break

    #結帳
    print ("Successfully checked out! \n書籍資訊:\n")
    for book in cart:
        print (f"{book.display_info()}")
    print (f"消費總金額: ${total}\n折扣後總金額: ${total*discount/100}")


if __name__ == "__main__": #底線有兩個
    main()