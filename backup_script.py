#!/usr/bin/env python3
"""
backup_script.py
Automates MySQL database backups using mysqldump.
Each backup file is timestamped for uniqueness.
Comments added throughout for learning purposes.
"""

# Import modules:
# subprocess for running shell commands,
# datetime for timestamp generation,
# os for filesystem operations.
import subprocess
import datetime
import os

# --- Configuration ---
# These variables define database connection and backup location.
DB_USER    = "root"             # MySQL username
DB_PASS    = "Secret5555"       # Password for the MySQL user
DB_HOST    = "127.0.0.1"        # Hostname or IP of the MySQL server
BACKUP_DIR = "./backups"        # Directory to store backup files
DB_NAME    = "school_db"        # Name of the database to back up
# ---------------------

def ensure_backup_dir():
    """
    Ensure that the backup directory exists.
    os.makedirs will create all intermediate-level directories needed
    and does nothing if the directory already exists (exist_ok=True).
    """
    os.makedirs(BACKUP_DIR, exist_ok=True)


def make_backup():
    """
    Perform the database backup:
    1. Generate a timestamped filename
    2. Build the mysqldump command
    3. Execute the command and write output to the file
    4. Print confirmation
    """
    # Create a timestamp string in format YYYYMMDD_HHMMSS
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Build the full path for the backup file
    filename = f"{BACKUP_DIR}/backup_{timestamp}.sql"

    # Construct the mysqldump command as a list of arguments
    # Using list form prevents shell injection risks
    cmd = [
        "mysqldump",              # The backup utility
        f"--user={DB_USER}",     # Username parameter
        f"--password={DB_PASS}", # Password parameter
        f"--host={DB_HOST}",     # Host parameter
        DB_NAME                    # The database to dump
    ]

    # Open the output file in write mode
    # subprocess.run will send its stdout here
    with open(filename, "w") as out:
        # Execute the dump command, write output to file
        # check=True ensures an exception is raised on failure
        subprocess.run(cmd, stdout=out, check=True)

    # Inform the user of success and file location
    print(f"Backup created: {filename}")


if __name__ == "__main__":
    # Entry point: ensure backup directory exists, then run backup
    ensure_backup_dir()
    make_backup()
