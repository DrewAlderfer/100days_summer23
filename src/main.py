import os
import csv
result = []
coco_link = "https://cocodataset.org/#explore?id="
with open("./image_log.csv", "r") as file:
    log_file = csv.reader(file, delimiter=',')
    # https://cocodataset.org/#explore?id=333407 
    header = "| day | cocoID | image link | drawing |\n| --- | --- | --- | --- |\n"
    last_day = 0
    img_counter = 0
    skip_first = 0
    result += header
    for row in log_file:
        if skip_first == 0:
            skip_first += 1
            continue
        day = int(row[0])
        if last_day != day:
            img_counter = 1
        else:
            img_counter += 1
        id_link = f"{coco_link}{row[1]}"
        line = f"| {day} | [{row[1]}]({id_link}) | [image_day{day:02d}_{img_counter:02d}]({row[2]}) | drawing... |\n"
        result.append(line)
        last_day = day
# print(result)
with open("./README.md", "r") as readme:
    r_lines = readme.readlines()
table_lines = []
for idx, line in enumerate(r_lines):
    if not line.startswith("|"):
        continue
    table_lines.append(idx)
print(table_lines[0], table_lines[-1])
file_head = r_lines[:table_lines[0]]
file_foot = r_lines[table_lines[-1] + 1:]

with open("./README.md", "w") as test:
    test.writelines(file_head)
    test.writelines(result)
    test.writelines(file_foot)





