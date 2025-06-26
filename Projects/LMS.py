class Library:
    def __init__(self,book,author,price):
        self.book = book
        self.author = author
        self._price = price

    def get_book(self):
        return self.book
    def get_author(self):
        return self.author
    
    def set_author(self,name):
        self.author = name
    def set_price(self,amount):
        self._price = amount

    def display(self):
        print(f"Book name is {self.book}, author of the book is {self.author}, book price is {self._price}")

book1 = Library("Merchant of Venice","Shakespeare",500)
book1.set_price(600)
print(book1.get_author())
book1.display()
book2 = Library("Maths","Aryabhatta",1000)
print(book2.get_book())
book2.set_price(1050)
book2.set_author("Arya")
book2.display()

