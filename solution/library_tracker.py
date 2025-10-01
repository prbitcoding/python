class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"borrowed '{self.title}. copies left: {self.copies}")
        else:
            print(f"sorry {self.title} is  not available")

    def return_book(self):
        self.copies += 1
        print(f" thanks Returned '{self.title}, copies available: {self.copies}")

book1 = Book("man jane", "total", 2)
book1.borrow()         
book1.borrow()          
book1.borrow()              
book1.return_book()     
