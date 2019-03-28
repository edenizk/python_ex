camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())#strip deletes \n

print(camelot_lines)
