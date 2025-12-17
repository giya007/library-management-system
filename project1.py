import os
def view_books():
        AVAILABLE_BOOKS=open("available.txt",'r')
        print("----------AVAILABLE BOOKS-------------")
        print("BOOK ID | NAME | AUTHOR")
        for i in AVAILABLE_BOOKS:
            print(i.strip())
        AVAILABLE_BOOKS.close()
        print('\n')
        print("---------ISSUED BOOKS--------------")
        ISSUED_BOOKS=open("issued.txt",'r')
        print("BOOK ID | NAME | AUTHOR")
        for i in ISSUED_BOOKS:
            print(i.strip())
        ISSUED_BOOKS.close()
def add_book():
        f2=open("available.txt",'a+')
        book=[]
        book.append(int(input("Enter book ID:")))
        book.append(input("Enter book name:"))
        book.append(input("Enter author name:"))
        f2.writelines(str(book)+'\n')
        print("Book added successfully")
        f2.close()
def issue_book():
   book_id=input("Enter book ID:")
   ln=len(book_id)
   f3=open("available.txt",'r')
   f4=open("issued.txt",'w')
   f5=open("temp.txt",'w')
   check=0
   for line in f3:
      if check==0:
         if line[1:ln+1]==book_id and line[ln+1].isdigit()==False:
            check=1
            f4.write(line)
            continue
         else:
            f5.write(line)
      else:
         f5.write(line)
   f3.close()
   f4.close()
   f5.close()
   if check==1:
      print("Book issued successfully")
   else:
      print("No such book")
   os.remove("available.txt")
   os.rename("temp.txt","available.txt")
def return_book():
    book_id=input("Enter book ID:")
    ln=len(book_id)
    f6=open("issued.txt",'r')
    f7=open("available.txt",'w')
    f8=open("temp.txt",'w')
    check=0
    for line in f6:
        if check==0:
            if line[1:ln+1]==book_id and line[ln+1].isdigit()==False:
                check=1
                f7.write(line)
                continue
            else:
                f8.write(line)
        else:
            f8.write(line)
    f6.close()
    f7.close()
    f8.close()
    if check==1:
        print("Book returned successfully")
    else:
        print("No such book")
    os.remove("issued.txt")
    os.rename("temp.txt","issued.txt")
ans='y'
while ans in('y','Y'):
       print("==== Library Management System ====")
       print("1.View Books")
       print("2.Add Book")
       print("3.Issue Book")
       print("4.Return Book")
       print("5.Exit")
       choice=input("Enter choice:")
       if choice=="1":
           view_books()
       elif choice=="2":
           add_book()
       elif choice=="3":
           issue_book()
       elif choice=="4":
           return_book()
       else:
           print("Invalid choice")
       ans=input("Do you wish to continue?(Y/N):")
    









