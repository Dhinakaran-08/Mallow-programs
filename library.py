def books():
    book = []
    def add():
        name = input("Enter the book name :")
        author = input("Enter the author name :")
        date = (input("Enter the date of issue :"))
        pub = int(input("Enter the published year :"))
        boo = {'name':name,
               'author':author,
               'date':date,
               'published':pub
        }
        book.append(boo)
        print("Book added successfully\n")
    def view():
        if len(book) == 0:
            print("Library has no books\n")
            return
        else:
            for detail in book:
                print(f"name : {detail['name']} author : {detail['author']} date : {detail['date']} published : {detail['published']}\n")
            print("These are the list of books\n")
    def delete():
        if len(book) == 0:
            print("Library has no books\n")
            return
        else:
            for detail in book:
                print(f"name : {detail['name']} author : {detail['author']} date : {detail['date']} published : {detail['published']}\n")
            dele = input("Enter the book name to delete : ")
            found = False
            for det in book:
                if det['name'] == dele:
                    book.remove(det)
                    found = True
                    break
            if found:
                print("Deleted successfully\n")
            else:
                print("name not fount\n")
    flag1=True
    while(flag1):
        print("***Book menu***")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Back to Main Menu")
        n1 = int(input("Enter your choice in book :"))
        match n1:
            case 1:
                add()
            case 2:
                view()
            case 3:
                delete()
            case 4:
                flag1 = False
print("***Library management system***")
flag = True
while(flag):
    print("1. Book Management")
    print("2. Member Management")
    print("3. Issue/Return Books")
    print("4. Exit")
    n = int(input("Enter your choice :"))
    match n:
        case 1:
            books()
        case 4:
            flag = False
        case _:
            print("Enter the valid choice\n")