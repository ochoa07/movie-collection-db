# Barbie Movie Collection Database

A Python + SQLite program that manages a collection of Barbie movies.
It demonstrates relational database concepts by allowing you to create, query, add, update, and delete Barbie movies, plus filter them by the date they were added.

Each Barbie movie record includes:
* Title
* Year
* Genre
* Theme (Princess, Fairytale, Fashion, etc.)
* Main Character (Barbie, Ken, Skipper, etc.)
* Rating (0–10)
* Watch link (YouTube trailer, Netflix, etc.)
* Added date/time (auto generated)


## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone or download this repository.
2. Open the folder in VS Code.
3. Create and activate a Python virtual environment: (python -m venv .venv)(.\.venv\Scripts\activate)
4. Run the program from the terminal: (python -m src.app)

Instructions for using the software:

1. Run the program and choose from the menu options:
* 1 → List all Barbie movies
* 2 → Add a new Barbie movie (title, year, genre, theme, character, rating, watch link)
* 3 → Update a movie by ID
* 4 → Delete a movie by ID
* 5 → Search Barbie movies (by title, year, genre, theme, or character)
* 6 → Filter movies by date added (stretch challenge)
* 0 → Exit the program
2. Add Barbie movies to grow your collection.
3. Query, update, or delete movies as needed.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.10+
* VS Code with the Python extension
* SQLite (via Python’s built-in sqlite3 library)
* Git (to publish the repo on GitHub)
* Optional: DB Browser for SQLite for viewing the database visually.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Tutorial – W3Schools](https://www.w3schools.com/sql/sql_intro.asp)
* [Reltional Dtabases](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-relational-database)
* [Barbie Movies ](https://en.wikipedia.org/wiki/List_of_Barbie_films)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Create a seed script with sample Barbie movies
* [ ] Build a webpage to display and search Barbie movies
* [ ] Add aggregate queries (e.g., average rating of Barbie princess movies)
* [ ] Implement multiple tables (e.g., separate table for characters) with joins