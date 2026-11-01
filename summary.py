import csv

def read_rows(filename):
    # the three functions 
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, lgacode):
    values = []
    for row in rows:
        row = row[lgacode].strip()
        if row == "":
            continue
        values.append(float(row))
    return values

def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }


def summarise_all(filename, columns):
    # summarise_all
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

report = summarise_all("Patani Settlement UTM32.csv", ["fid","lgacode", ])
for column, stats in report.items():
    print(column, ":", stats)


rows = read_rows("Patani Settlement UTM32.csv")
# the line that runs it on my data
values = clean_values(rows, "lgacode")
result = summarise(values)
print(result)
