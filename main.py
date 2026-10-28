import os
from pyjamas_data import Database
os.makedirs("output", exist_ok=True)
path = "output/count.txt"
count = int(open(path).read()) + 1 if os.path.exists(path) else 1
open(path, "w").write(str(count))
print(f"This is run number {count}")
if os.path.exists("data/message.txt"):
    print("Your text message says:", open("data/message.txt").read().strip())

# Read and print the latest row of testingTable from Supabase
db = Database("SUPABASE")
latest = db.row("SELECT * FROM testingTable ORDER BY id DESC LIMIT 1")
if latest:
    print("Latest row of testingTable:", latest)
else:
    print("testingTable v2 is empty - no rows to show.")
