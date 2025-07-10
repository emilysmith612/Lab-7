# Lab 7: Book Collection

book = {
    "title" == "Dark Matter",
    "author" == "Blake Crouch",
    "genre" == "Sci-Fi",
    "isbn" == "1101904224",
    "tags" == {"thriller", "suspense", "mystery"}
}

def add_book(collection, title, author, genre, isbn, tags):
    if isbn_conflict:
        print("ISBN already taken")
        return

    book = {}
    book["title"] = title
    book["author"] = author
    book["genre"] = genre
    book["isbn"] = isbn
    book["tags"] = tags

    collection.append(book)