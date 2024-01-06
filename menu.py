import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'Search All Books',
    2: 'Search by Title',
    3: 'Search by Publisher',
    4: 'Search by Price Range',
    5: 'Search by Title and Publisher'
}

def search_all_books():
    results = book_dao.findAll()
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item['ISBN'], item['title'])
    print("The end of books.")

def search_by_title():
    title = input("What is the exact book title that you are looking for?\n")
    results = list(book_dao.findByTitle(title))
    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("The title you wanted does not exist in our database.")
    print("The end.")

def print_search_menu():
    print("Search Books")
    for key in search_menu_options.keys():
        print(str(key)+'.', search_menu_options[key], end="  ")
    print()
    print("End of search options")
    print()

def search_by_publisher():
    publisher = input("Enter the publisher's name: ")
    results = book_dao.findByPublisher(publisher)
    if results:
        print("Books published by", publisher)
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("No books found for the publisher", publisher)
    print("The end.")

def search_by_price_range():
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    results = book_dao.findByPriceRange(min_price, max_price)
    if results:
        print("Books within price range", min_price, "to", max_price)
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("No books found within the price range.")
    print("The end.")

def search_by_title_and_publisher():
    title = input("Enter the book title: ")
    publisher = input("Enter the publisher's name: ")
    results = book_dao.findByTitleAndPublisher(title, publisher)
    if results:
        print("Books matching title and publisher")
        for item in results:
            print(item['ISBN'], item['title'])
    else:
        print("No books found matching the title and publisher.")
    print("The end.")

def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()

def option1():
    print("Add a new publisher")
    name = input("Publisher name: ")
    phone = input("Publisher phone: ")
    city = input("Publisher city: ")
    book_dao.addNewPublisher(name, phone, city)
    print("Publisher added successfully")

def option2():
    print("Add a new book")
    isbn = input("ISBN: ")
    title = input("Title: ")
    year = int(input("Year: "))
    published_by = input("Published by: ")
    previous_edition = input("Previous edition ISBN (leave blank if none): ")
    price = float(input("Price: "))
    previous_edition = None if previous_edition == '' else previous_edition
    book_dao.addNewBook(isbn, title, year, published_by, previous_edition, price)
    print("Book added successfully")

def option3():
    print("Edit an existing book")
    isbn = input("Enter the ISBN of the book to edit: ")
    print("Enter the new details for the book (leave blank to keep unchanged)")

    updated_data = {}
    title = input("New title (press enter to skip): ")
    year = input("New year (press enter to skip): ")
    published_by = input("New publisher (press enter to skip): ")
    previous_edition = input("New previous edition ISBN (press enter to skip): ")
    price = input("New price (press enter to skip): ")

    # Create a dictionary of the updated fields
    if title:
        updated_data['title'] = title
    if year:
        try:
            updated_data['year'] = int(year)
        except ValueError:
            print("Year must be a number.")
            return
    if published_by:
        updated_data['published_by'] = published_by
    if previous_edition:
        updated_data['previous_edition'] = previous_edition
    if price:
        try:
            updated_data['price'] = float(price)
        except ValueError:
            print("Price must be a number.")
            return

    # Call the editBook function and print the result
    result_message = book_dao.editBook(isbn, updated_data)
    print(result_message)

def option4():
    print("Delete a book")
    isbn = input("Enter the ISBN of the book to delete: ")
    book_dao.deleteBook(isbn)
    print("Book deleted successfully")

def option5():
    print_search_menu()
    search_option = int(input("Enter your search choice: "))
    if search_option == 1:
        search_all_books()
    elif search_option == 2:
        search_by_title()
    elif search_option == 3:
        search_by_publisher()
    elif search_option == 4:
        search_by_price_range()
    elif search_option == 5:
        search_by_title_and_publisher()
    else:
        print("Invalid search option.")

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks for using our database services! Bye')
            sys.exit(0)
        else:
            print('Invalid option. Please enter a number between 1 and 6.')
