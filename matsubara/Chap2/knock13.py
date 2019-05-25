with open("col1.txt", "r", encoding="utf-8") as f1,\
     open("col2.txt", "r", encoding="utf-8") as f2,\
     open("marge.txt", "w", encoding="utf-8") as wfile:
    for line1, line2 in zip(f1.readlines(), f2.readlines()):
        wfile.write(line1.strip() + "\t" + line2)

