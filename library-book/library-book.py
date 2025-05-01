class Library:
    def __init__(self):
        self.books = []
    def addBook(self, bookName):
        self.books.append(bookName)
    def showBooks(self):
        for book in self.books:
            print(book, "\n")

library = Library()

while True:
    action = input("⚙️ Please input 'add' to add book, 'show' to list all books, 'exit' to exit system: ")
    if "add"==action:
        bookName = input("➕ Please input new book name: ")
        library.addBook(bookName)
        print("✅ a new book added")
    elif "show"==action:
        print("📚")
        library.showBooks()
    elif "exit"==action:
        print("👋 byebye")
        exit()
    else:
        print("⚠️ invalid action")