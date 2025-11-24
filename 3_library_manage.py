import os

def read_books_from_file(filename):
    """
    Reads book data from a text file and returns a list of book dictionaries.
    Format per line:
    Title | Author | Genre | Year
    """
    books = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                parts = line.split("|")
                if len(parts) != 4:
                    print(f"Skipping invalid line: {line}")
                    continue

                title, author, genre, year = [p.strip() for p in parts]

                books.append({
                    "title": title,
                    "author": author,
                    "genre": genre,
                    "year": year
                })

        return books

    except FileNotFoundError:
        print(f"❌ Error: '{filename}' not found!")
        return []


def display_books(books):
    """
    Displays books in a formatted way
    """
    print("\n" + "="*70)
    print(" Library Collection")
    print("="*70 + "\n")

    for idx, book in enumerate(books, 1):
        print(f"{idx}. Title: {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Genre: {book['genre']}")
        print(f"   Year: {book['year']}\n")

    print("-"*70)
    print(f"📖 Total Books: {len(books)}")

    genres = sorted({book["genre"] for book in books})
    print(f"🏷️  Available Genres: {', '.join(genres)}")
    print("="*70)


def search_by_genre(books, target_genre):
    """
    Returns a list of books matching a specific genre
    """
    return [book for book in books if book["genre"].lower() == target_genre.lower()]


def save_library(books, output_file):
    """
    Saves the library list to a file
    """
    with open(output_file, "w") as file:
        for book in books:
            file.write(
                f"{book['title']} | {book['author']} | {book['genre']} | {book['year']}\n"
            )

    print(f"\n✓ Library saved to '{output_file}'")


def main():
    print("\n📚 Library Book Manager")
    print("Author: K Premila Singha\n")

    input_file = "input_files/library_data.txt"
    output_file = "output_files/library.txt"

    # Load books
    books = read_books_from_file(input_file)

    if not books:
        return

    # Display
    display_books(books)

    # Search for a specific genre
    genre = "Fiction"
    print(f"\n🔍 Searching for books in genre: {genre}")
    found = search_by_genre(books, genre)

    if found:
        print(f"Found {len(found)} book(s):")
        for b in found:
            print(f"  - {b['title']}")
    else:
        print("No books found.")

    # Save to file
    save_library(books, output_file)


if __name__ == "__main__":
    main()
