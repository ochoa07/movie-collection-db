# app.py — CLI interface for the Barbie Movie Collection Database
from .db import init_db
from .queries import list_movies, add_movie, update_movie, delete_movie, search_movies, filter_by_date

def show(rows):
    """Pretty-print Barbie movie rows."""
    if not rows:
        print("(no results)")
        return
    for r in rows:
        print(f"[{r['id']}] {r['title']} ({r['year'] or 'N/A'}) | "
              f"Genre={r['genre'] or '-'} | Theme={r['theme'] or '-'} | "
              f"Character={r['character'] or '-'} | Rating={r['rating'] or '-'} | "
              f"Link={r['watch_link'] or '-'} | Added={r['added_at']}")

def ask_int(prompt, allow_blank=True):
    val = input(prompt).strip()
    if allow_blank and val == "": return None
    try: return int(val)
    except ValueError: return None

def ask_float(prompt, allow_blank=True):
    val = input(prompt).strip()
    if allow_blank and val == "": return None
    try: return float(val)
    except ValueError: return None

def main():
    init_db()  # make sure table exists

    while True:
        print("\n=== Barbie Movie Collection ===")
        print("1) List movies")
        print("2) Add movie")
        print("3) Update movie")
        print("4) Delete movie")
        print("5) Search movies")
        print("6) Filter by date range (stretch)")
        print("0) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show(list_movies())
        elif choice == "2":
            title = input("Title: ")
            year = ask_int("Year: ")
            genre = input("Genre: ")
            theme = input("Theme (Princess, Fairytale, etc.): ")
            character = input("Main Character (Barbie, Ken, etc.): ")
            rating = ask_float("Rating (0–10): ")
            watch_link = input("Watch link (YouTube, Netflix, etc.): ")
            new_id = add_movie(title, year, genre, theme, character, rating, watch_link)
            print(f"Added Barbie movie with ID {new_id}")
        elif choice == "3":
            movie_id = ask_int("Movie ID to update: ", allow_blank=False)
            title = input("New title (blank=skip): ") or None
            year = ask_int("New year (blank=skip): ")
            genre = input("New genre (blank=skip): ") or None
            theme = input("New theme (blank=skip): ") or None
            character = input("New character (blank=skip): ") or None
            rating = ask_float("New rating (blank=skip): ")
            watch_link = input("New watch link (blank=skip): ") or None
            count = update_movie(movie_id, title, year, genre, theme, character, rating, watch_link)
            print(f"Updated {count} row(s)")
        elif choice == "4":
            movie_id = ask_int("Movie ID to delete: ", allow_blank=False)
            count = delete_movie(movie_id)
            print(f"Deleted {count} row(s)")
        elif choice == "5":
            title_sub = input("Search title contains: ") or None
            min_year = ask_int("Min year: ")
            max_year = ask_int("Max year: ")
            genre = input("Genre: ") or None
            theme = input("Theme: ") or None
            character = input("Character: ") or None
            show(search_movies(title_sub, min_year, max_year, genre, theme, character))
        elif choice == "6":
            start = input("Start date (YYYY-MM-DD): ").strip() + " 00:00:00"
            end = input("End date (YYYY-MM-DD): ").strip() + " 23:59:59"
            show(filter_by_date(start, end))
        elif choice == "0":
            print("Goodbye, Barbie fan!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()