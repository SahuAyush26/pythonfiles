class Library:
    def __init__(self, book_name):
        self.book_name = book_name
        
    
    def add_to_shelf(self):
        global shelf
        shelf.append(self.book_name)
        global numberbooks
        numberbooks += 1
    
    @staticmethod
    def Show_Info():
        global numberbooks
        print(f"The list of books are {shelf}, and the number of books are : ", numberbooks)

    @staticmethod
    def check():
        if(len(shelf) == numberbooks):
            print("All is well")
        else:
            print("Something is wrong")
        
numberbooks = 0
shelf = []

book1 = Library("Harry potter") 
book1.add_to_shelf()
Library.Show_Info()
Library.check()






