try:
    with open("missing_file.csv", "r") as f:
        data = f.read()
except FileNotFoundError:
    with open("MISSING_FILE.csv", "r") as f:
        data = f.read()
    print("File not found: pipeline cannot proceed")
finally:
    print("cleanup complete")