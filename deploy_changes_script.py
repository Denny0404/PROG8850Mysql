#!/usr/bin/env python3
"""
deploy_changes_script.py
Automates deployment of schema changes to a MySQL database.
Reads SQL from a file and applies it statement by statement.
Comments added throughout to explain the logic.
"""

import mysql.connector  # Connector for MySQL
import sys             # For exiting with error codes

# --- Configuration ---
# DB_CONFIG holds connection parameters for mysql.connector
DB_CONFIG = {
    "user": "root",        # MySQL username
    "password": "Secret5555",  # MySQL password
    "host": "127.0.0.1",  # Database host (IP or hostname)
    "database": "school_db"  # Default database to use
}
# Path to the SQL file containing schema changes (e.g., CREATE/ALTER statements)
SQL_FILE = "changes.sql"
# ---------------------

def load_sql(filename):
    """
    Read the entire SQL file into a string.
    Returns:
        str: Contents of the SQL file
    """
    with open(filename, "r") as f:
        return f.read()


def apply_changes(sql):
    """
    Apply SQL statements to the database.
    Splits the SQL content on semicolons to handle multiple statements.
    Args:
        sql (str): The raw SQL script contents
    """
    # Connect to the database using provided configuration
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()

    # Split the script into individual statements by ';'
    for statement in sql.split(";"):
        stmt = statement.strip()  # Remove leading/trailing whitespace
        if stmt:
            # Execute each non-empty statement, re-append semicolon
            cursor.execute(stmt + ";")
            # Print out a truncated preview for confirmation
            print(f"Executed: {stmt[:50]}...")

    # Commit all changes to make them permanent
    cnx.commit()
    # Close cursor and connection to free resources
    cursor.close()
    cnx.close()
    print("All changes deployed.")


if __name__ == "__main__":
    # Script entrypoint: load the SQL and apply it, handling errors
    try:
        sql = load_sql(SQL_FILE)
        apply_changes(sql)
    except Exception as e:
        # Print error to stderr for visibility, exit with non-zero status
        print(f"Error during deployment: {e}", file=sys.stderr)
        sys.exit(1)
