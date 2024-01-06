from pymongo_connector import collection

def addNewPublisher(name, phone, city):
    new_publisher = {
        "name": name,
        "phone": phone,
        "city": city
    }
    collection.publishers.insert_one(new_publisher)  

def addNewBook(isbn, title, year, published_by, previous_edition, price):
    new_book = {
        "ISBN": isbn,
        "title": title,
        "year": year,
        "published_by": published_by,
        "previous_edition": previous_edition,
        "price": price
    }
    collection.insert_one(new_book)

def editBook(isbn, updated_data):
    # Sanitize the input to remove empty strings, which can unset fields in the document
    updated_data = {k: v for k, v in updated_data.items() if v not in [None, "", " "]}
    
    # Check if there is anything to update
    if not updated_data:
        return "No updates provided."

    try:
        result = collection.update_one({"ISBN": isbn}, {"$set": updated_data})
        if result.matched_count == 0:
            return f"No book found with ISBN: {isbn}"
        elif result.modified_count == 0:
            return f"Book with ISBN {isbn} found, but no new information was updated."
        else:
            return f"Book with ISBN {isbn} updated successfully."
    except Exception as e:
        return f"An error occurred while updating the book: {e}"

def deleteBook(isbn):
    try:
        result = collection.delete_one({"ISBN": isbn})
        if result.deleted_count == 0:
            print(f"No book found with ISBN: {isbn}")
        else:
            print(f"Book with ISBN {isbn} deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def findByPublisher(publisher_name):
    results = collection.find({"published_by": publisher_name})
    return results

def findByPriceRange(min_price, max_price):
    results = collection.find({"price": {"$gte": min_price, "$lte": max_price}})
    return results 

def findByTitleAndPublisher(title, publisher):
    results = collection.find({"title": title, "published_by": publisher})
    return results

def findAll():
    results = collection.find()
    return results


def findByTitle(book_title):
    results = collection.find({'title': book_title})
    return results
