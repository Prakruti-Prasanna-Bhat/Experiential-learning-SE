"""Manage tower maintenance records using an in-memory SQLite database."""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE towers "
    "(id INTEGER PRIMARY KEY, site TEXT, "
    "last_service INTEGER, faults INTEGER)"
)


def add_tower(site, last_service, faults=0):
    """Add a tower and its maintenance information to the database."""
    conn.execute(
        "INSERT INTO towers (site, last_service, faults) VALUES (?, ?, ?)",
        (site, last_service, faults),
    )
    conn.commit()


def service_tower(tower_id, year):
    """Service a tower and return whether the update succeeded."""
    try:
        conn.execute(
            "UPDATE towers "
            "SET last_service = ?, faults = 0 "
            "WHERE id = ?",
            (year, tower_id),
        )
        conn.commit()
        return True
    except sqlite3.Error:
        print("service failed")
        return False


def overdue(year):
    """Return sites overdue for service by at least two years."""
    rows = conn.execute("SELECT site, last_service FROM towers").fetchall()
    result = []
    for site, last in rows:
        if year - last >= 2:
            result.append(site)
    return result


def risk_level(tower_id):
    """Return the tower risk level based on recorded faults."""
    row = conn.execute(
        "SELECT faults FROM towers WHERE id = ?",
        (tower_id,),
    ).fetchone()
    if row[0] > 3:
        return "high"
    return "normal"


def snapshot():
    """Return a snapshot of all tower records."""
    return conn.execute("SELECT * FROM towers").fetchall()


def main():
    """Run a demonstration of the tower maintenance system."""
    add_tower("Ridge-A", 2021, 5)
    add_tower("Coast-B", 2024)

    service_count = int(service_tower(2, 2025))

    total = len(snapshot())

    print(
        overdue(2025),
        risk_level(1),
        total,
        service_count,
    )


if __name__ == "__main__":
    main()
