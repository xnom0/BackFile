#!/usr/bin/python3
import sys
import requests

# Couleurs ANSI
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
FAIL = '\033[91m'
RESET = '\033[0m'

# Bannière
BANNER = """
 /$$$$$$$                      /$$       /$$$$$$$$ /$$ /$$
| $$__  $$                    | $$      | $$_____/|__/| $$
| $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$| $$       /$$| $$  /$$$$$$
| $$$$$$$  |____  $$ /$$_____/| $$  /$$/| $$$$$   | $$| $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$      | $$$$$$/ | $$__/   | $$| $$| $$$$$$$$
| $$  \ $$ /$$__  $$| $$      | $$_  $$ | $$      | $$| $$| $$_____/
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$| $$      | $$| $$|  $$$$$$$
|_______/  \_______/ \_______/|__/  \__/|__/      |__/|__/ \_______/
BackFile can find backup files on web servers.

Version 1.0
Created By Tristan Manzano / X-no
"""

# Extensions et fichiers à tester
EXTENSIONS = [
    ".bak", ".backup", ".bck", ".save", ".sav", ".copy", ".old", ".orig", ".tmp", ".temp",
    ".back", ".bkp", ".bac", ".swp", ".swo", ".swn", ".~", ".1", ".2", ".inc", ".tar",
    ".gz", ".tar.gz", ".zip", ".rar", ".7z", ".bz2", ".tgz", ".z", ".sql", ".sqlite",
    ".db", ".dbf", ".mdb", ".bak.sql", ".sql.gz", ".sql.bak", ".php", ".php~", ".php.bak",
    ".php.old", ".php.inc", ".php.swp", ".html", ".html~", ".html.bak", ".htm", ".asp",
    ".aspx", ".jsp", ".txt", ".log", ".conf", ".cfg", ".config", ".ini", ".env", ".env.bak",
    ".env.save", ".xml", ".xml.bak", ".json", ".json.bak", ".yaml", ".yml", ".properties",
    ".sh", ".bash", ".sql~", ".dump", ".data", ".dat", ".bak2", ".bak3", ".DS_Store",
    ".db_store", ".git", ".svn", ".htaccess", ".htpasswd", ".gitignore", ".lock", ".md",
    ".markdown", ".rst", ".bakup", ".archive", ".tar.bz2", ".zipx", ".pem", ".key", ".crt",
    ".cer", ".csr", ".pfx", ".pub", ".ssh", ".id_rsa", ".doc", ".docx", ".xls", ".xlsx",
    ".pdf", ".ppt", ".pptx", ".rtf", ".BAK", ".BACKUP", ".BCK", ".SAVE", ".SAV", ".COPY",
    ".OLD", ".ORIG", ".TMP"
]
AUTO_FILES = ["install", "login", "admin", "wp-config", "test", "backup", "back", "admin.inc",
              "inc", "administrateur", "administrator", "config", "conf", "cnf", "configuration",
              "index", ""]
SUFFIXES = ["", ".html", ".php"]

def scan_files(url, filename=None):
    """Scanne les fichiers sur le serveur avec les extensions données."""
    if not url.endswith("/"):
        url += "/"

    files_to_test = AUTO_FILES if filename is None else [filename]
    found = 0

    # Calcul du nombre total de requêtes
    total_requests = len(files_to_test) * len(EXTENSIONS) * len(SUFFIXES)
    current_request = 0

    print(f"{'='*60}\n{OKBLUE}Scanning {url} [{'Auto' if filename is None else filename}]{RESET}\n")

    for file in files_to_test:
        for ext in EXTENSIONS:
            for suffix in SUFFIXES:
                test_url = f"{url}{file}{suffix}{ext}"
                try:
                    r = requests.get(test_url, timeout=5)
                    if r.status_code == 200:
                        found += 1
                        print(f"{OKGREEN} - File Found: {OKBLUE}{test_url}{RESET}")
                except (requests.exceptions.RequestException, KeyboardInterrupt):
                    print(f"{FAIL}Error or interrupted at {test_url}{RESET}")
                    return found

                # Mise à jour du pourcentage de progression
                current_request += 1
                progress = (current_request / total_requests) * 100
                bar_length = 30  # Longueur de la barre de progression
                filled = int(bar_length * progress // 100)
                bar = '█' * filled + '-' * (bar_length - filled)
                # Formatage fixe pour éviter le décalage
                print(f"\rProgress: |{bar}| {progress:>5.1f}%", end="", flush=True)

    print(f"\n\n{'='*60}\nFiles Found: {found}\n{'='*60}")
    return found

def help_menu():
    """Affiche le menu d'aide."""
    print(f"Usage:\n")
    print("  backfile.py [URL] [FILE]")
    print("  Ex: backfile.py http://example.com index\n")
    print("  backfile.py [URL] --auto")
    print("  Ex: backfile.py http://example.com --auto\n")
    print("Auto mode tests: login, admin, wp-config, test, backup, etc.\n")

def main():
    """Point d'entrée principal."""
    try:
        print(BANNER)
        url = sys.argv[1]
        mode = sys.argv[2] if len(sys.argv) > 2 else None

        if mode == "--auto":
            scan_files(url)
        elif mode:
            scan_files(url, mode)
        else:
            help_menu()
    except IndexError:
        help_menu()

if __name__ == "__main__":
    main()
