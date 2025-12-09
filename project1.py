import os

AVAILABLE = "available.txt"
ISSUED = "issued.txt"


def initialize_files():
    if not os.path.exists(AVAILABLE):
        open(AVAILABLE, "w").close()

    if not os.path.exists(ISSUED):
        open(ISSUED, "w").close()


def read_file_dict(filename):
    """Reads file into a dictionary {book: count}"""
    data = {}
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        if "|" in line:
            book, count = line.strip().split("|")
            data[book.strip()] = int(count.strip())
    return data


def write_file_dict(filename, data):
    f = open(filename, "w")
    for book, count in data.items():
        f.write(f"{book} | {count}\n")
    f.close()


def view_books():
    print("\n--- Available Books ---")
    available = read_file_dict(AVAILABLE)
    if not available:
        print("(none)")
    else:
        for book, count in available.items():
            print(f"{book} - Copies Available: {count}")

    print("\n--- Issued Books ---")
    issued = read_file_dict(ISSUED)
    if not issued:
        print("(none)")
    else:
        for book, count in issued.items():
            print(f"{book} - Copies Issued: {count}")
    print()


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

    # update numbers
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

        choice = input("Enter choice: ").strip()

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


if __name__ == "__main__":
    initialize_files()
    menu()

