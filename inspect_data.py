import csv

with open("Patani Settlement UTM32.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("number of rows:", len(rows))
print("columns:", list(rows[0].keys()))

values = []
for row in rows:
    values.append(float(row["uniq_id"]))

print("smallest:", min(values))
print("largest:", max(values))
print("count:", len(values))

values = []
for row in rows:
    values.append(float(row["lgacode"]))

print("smallest:", min(values))
print("largest:", max(values))
print("count:", len(values))

values = []
for row in rows:
    raw = row["uniq_id"]
    if raw == ":":
        continue
    if raw == "":
        continue
    try:
        values.append(float(raw))
    except:
        continue

print("smallest:", min(values))
print("largest:", max(values))
print("count:", len(values))

import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row["uniq_id"]
        if raw == " ":
            continue
        if raw == ":":
            continue
        if raw == "":
            continue
        try:
            values.append(float(raw))
        except:
            continue

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }

result = inspect_column("Patani Settlement UTM32.csv", "uniq_id")
print(result)


result1 = inspect_column("Patani Settlement UTM32.csv", "fid")
print("fid:", result1)

result2 = inspect_column("Patani Settlement UTM32.csv", "area_wrong")
print("lgacode:", result2)