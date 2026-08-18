from pathlib import Path

# newer way of getting file paths (using os is an older method)
base_path = Path(__file__).resolve().parent.parent
data_path = base_path/"data"/"raw"

print(base_path)
print(data_path)