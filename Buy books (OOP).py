class Purchaseable: 
    def purchase(self, quantity, price_per_unit): #self不會像一般的引數一樣被回傳數值 #這裡只有一個"方法"(.purchase)
        total_cost = quantity * price_per_unit
        return total_cost

class Spendable:
    def caculate_total_spent(self, purchases):
        total_spent = sum(purchases)
        return total_spent
    
class Discountable:
    def apply_discount(self, price, discount_percentage):
        discount_price = price * (1-discount_percentage/100)
        return discount_price
    
class Book(Purchaseable, Spendable, Discountable): #這個class裡面一共有兩個"方法"們
    def __init__(self, isbn, title, author, price, stock): #這些是書籍們的通用屬性
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        
    def display_info(self):
        return (f"Title: {self.title}, Author: {self.author}, Price: ${self.price:}")

#inventory=[] #元素的屬性依序為 isbn, title, author, price, stock
    

def main():
    #while True:
        
        # book[0] = Book("1234567890", "Python Programming", "John Doe", 29.99)
        # book[1] = Book("9876543210", "Data Science Handbook", "Jane Smith", 39.99)
    
        isbn=input("請輸入書籍的ISBN: ")
        title=input("請輸入書籍的標題: ")
        author=input("請輸入書籍的作者: ")
        price=float(input("請輸入書籍的價格: "))
        stock=int(input("請輸入庫存數量: "))
        book=Book(isbn, title, author, price, stock)
        #inventory.append(book)
        
        purchase_quantity = int(input("請輸入購買的數量: "))
        unit_price = book.price #取得 book1物件 的 Book類別 的 price屬性
        total_cost = book.purchase(purchase_quantity, unit_price) #Link to line 2 #使用"方法"，有點像是呼叫函數
        
        discount_percentage = int(input("請輸入折扣的百分比: "))
        discounted_price = book.apply_discount(book.price, discount_percentage)
        
        print (f"購買成功!\n書籍資訊: \n{book.display_info()}")
        print (f"購買數量: {purchase_quantity}")
        print (f"消費總金額: ${total_cost}")
        print (f"折扣後單價: ${discounted_price}")
        print (f"更新後庫存: {book.stock-purchase_quantity}")
    

if __name__ == "__main__": #底線有兩個
    main()