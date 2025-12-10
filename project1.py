import sys
book_inventory=open("available.txt","w")
book_inventory.write("Atomic Habits | James Clear | 2\n")
book_inventory.write("Fluent Python | Luciano Ramalho | 6\n")
book_inventory.write("Intoduction to Algorithms | Thomas H. Cormen | 4\n")
book_inventory.write("Power of Subconscious Mind | Joseph Murphy | 3\n")
book_inventory.write("Harry Potter and the Sorcerer's Stone | JK Rowling | 2\n")
book_inventory.close()
def view_books():
    book_inventory = open("available.txt", "w")
    books_view=book_inventory.read()
    print(books_viewbook)
    print("\n--- Issued Books ---")
    

def add_book():
    book = input("Enter book name to add: ").strip()
    copies = int(input("Enter number of copies: ").strip())

    available = read_file_dict(AVAILABLE)

    if book in available:
        available[book] += copies
    else:
        available[book] = copies

    write_file_dict(AVAILABLE, available)
    print(f"Added {copies} copies of '{book}'.\n")


def issue_book():
    book = input("Enter book name to issue: ").strip()
    copies = int(input("Enter copies to issue: ").strip())

    available = read_file_dict(AVAILABLE)
    issued = read_file_dict(ISSUED)

    if book not in available:
        print("Book not available.\n")
        return

    if available[book] < copies:
        print("Not enough copies available.\n")
        return

    # update numbers
    available[book] -= copies
    if available[book] == 0:
        del available[book]

    issued[book] = issued.get(book, 0) + copies

    write_file_dict(AVAILABLE, available)
    write_file_dict(ISSUED, issued)

    print(f"Issued {copies} copies of '{book}'.\n")


def return_book():
    book = input("Enter book name to return: ").strip()
    copies = int(input("Enter copies to return: ").strip())

    available = read_file_dict(AVAILABLE)
    issued = read_file_dict(ISSUED)

    if book not in issued or issued[book] < copies:
        print("Error: too many copies being returned or book never issued.\n")
        return

    issued[book] -= copies
    if issued[book] == 0:
        del issued[book]

    available[book] = available.get(book, 0) + copies

    write_file_dict(AVAILABLE, available)
    write_file_dict(ISSUED, issued)

    print(f"Returned {copies} copies of '{book}'.\n")


def menu():
    while True:
        print("==== Library Management System ====")
        print("1. View Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")
        input("Do you wish to continue?(True/False): ")

menu()






