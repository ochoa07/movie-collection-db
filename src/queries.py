# queries.py — contains all database operations (CRUD) for Barbie movies
from typing import List, Optional
from .db import connect

def list_movies() -> List[dict]:
    """Return all Barbie movies in the database."""
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, title, year, genre, theme, character, rating, watch_link, added_at "
            "FROM barbie_movies ORDER BY id;"
        ).fetchall()
    return [dict(r) for r in rows]

def add_movie(title: str, year: Optional[int], genre: Optional[str],
              theme: Optional[str], character: Optional[str],
              rating: Optional[float], watch_link: Optional[str]) -> int:
    """Insert a new Barbie movie and return its ID."""
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO barbie_movies (title, year, genre, theme, character, rating, watch_link) "
            "VALUES (?, ?, ?, ?, ?, ?, ?);",
            (title, year, genre, theme, character, rating, watch_link),
        )
        conn.commit()
        return cur.lastrowid

def update_movie(movie_id: int, title=None, year=None, genre=None,
                 theme=None, character=None, rating=None, watch_link=None) -> int:
    """Update a Barbie movie. Only updates fields that are provided."""
    fields, params = [], []
    if title: fields.append("title = ?"); params.append(title)
    if year: fields.append("year = ?"); params.append(year)
    if genre: fields.append("genre = ?"); params.append(genre)
    if theme: fields.append("theme = ?"); params.append(theme)
    if character: fields.append("character = ?"); params.append(character)
    if rating is not None: fields.append("rating = ?"); params.append(rating)
    if watch_link: fields.append("watch_link = ?"); params.append(watch_link)
    if not fields: return 0
    params.append(movie_id)

    with connect() as conn:
        cur = conn.execute(f"UPDATE barbie_movies SET {', '.join(fields)} WHERE id = ?;", params)
        conn.commit()
        return cur.rowcount

def delete_movie(movie_id: int) -> int:
    """Delete a Barbie movie by ID."""
    with connect() as conn:
        cur = conn.execute("DELETE FROM barbie_movies WHERE id = ?;", (movie_id,))
        conn.commit()
        return cur.rowcount

def search_movies(title_sub=None, min_year=None, max_year=None,
                  genre=None, theme=None, character=None) -> List[dict]:
    """Search Barbie movies by title, year range, genre, theme, or character."""
    clauses, params = [], []
    if title_sub:
        clauses.append("title LIKE ?"); params.append(f"%{title_sub}%")
    if min_year:
        clauses.append("year >= ?"); params.append(min_year)
    if max_year:
        clauses.append("year <= ?"); params.append(max_year)
    if genre:
        clauses.append("genre = ?"); params.append(genre)
    if theme:
        clauses.append("theme = ?"); params.append(theme)
    if character:
        clauses.append("character = ?"); params.append(character)

    where = "WHERE " + " AND ".join(clauses) if clauses else ""
    with connect() as conn:
        rows = conn.execute(
            f"SELECT id, title, year, genre, theme, character, rating, watch_link, added_at "
            f"FROM barbie_movies {where} ORDER BY rating DESC, year DESC;",
            params,
        ).fetchall()
    return [dict(r) for r in rows]

def filter_by_date(start_iso: str, end_iso: str) -> List[dict]:
    """Filter Barbie movies by added_at date range (stretch challenge)."""
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, title, year, genre, theme, character, rating, watch_link, added_at "
            "FROM barbie_movies WHERE added_at BETWEEN ? AND ? ORDER BY added_at;",
            (start_iso, end_iso),
        ).fetchall()
    return [dict(r) for r in rows]