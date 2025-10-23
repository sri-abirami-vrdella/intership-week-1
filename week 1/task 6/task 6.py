"""Create a Python program that uses file handling to
read student data from a CSV file, process it, and write formatted
reports into a text file — all using context managers (with statement)."""

import csv
import pandas as pd
with open('students.csv', 'w') as csvf:
    csvf.write("name,maths,english,science\n")
    csvf.write("alice,85,62,85\n")
    csvf.write("bob,85,62,85\n")
    csvf.write("charlie,95,62,85\n")
    csvf.write("dheena,85,92,85\n")

data = [
    ['sam',98,33,56],
    ['dev',77,99,90]
]

with open('students.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)

with open('students.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        print(data)

with open('students.csv', 'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

with open("students.csv", "r", newline='') as csvf:
    a= csv.reader(csvf)
    dict_reader=list(a)


dict_reader[0].append("total_mark")
dict_reader[0].append("average_mark")
dict_reader[0].append("grade")
print(dict_reader)

for student in dict_reader[1:]:
    total_mark=float(student[1])+float(student[2])+float(student[3])
    avg=total_mark/3
    grade='0'
    if avg>=80:
        grade="A"
    elif 60<=avg<70:
        grade="B"
    else:
        grade="C"

    student.append(total_mark)
    student.append(avg)
    student.append(grade)
    with open("students.csv", 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(dict_reader)
for row in dict_reader:
    print(row)
print("-------student report------")
for they in dict_reader[1:]:
    print(f"name:{they[0]}\n"
          f"maths:{they[1]},science:{they[2]},english:{they[3]}\n"
          f"totalmark:{they[4]} | averagemark:{they[5]} | grade:{they[6]}\n"
          f"-------------------------------")

print("summary:")
print(f"total students:{len(dict_reader)}\n"
      f"class average{(pd.read_csv("students.csv", usecols=["average_mark"])["average_mark"].sum()) / len(dict_reader):.2f}\n"
      f"highest average {max(pd.read_csv("students.csv", usecols=["average_mark"])["average_mark"]):.2f}\n"
      f"lowest average {min(pd.read_csv("students.csv", usecols=["average_mark"])["average_mark"]):.2f}")
