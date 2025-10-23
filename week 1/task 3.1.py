"""Take names of 5 students and store them in a list.
Sort the list alphabetically, reverse it, and display both versions.
Store each student’s marks for 3 subjects in a tuple.
Create a dictionary mapping each student’s name to their marks tuple.
Calculate and display each student’s average marks using the dictionary.
Use a set to find all unique marks scored by any student and display the total count, highest, and lowest marks.
Ask the user to enter a feedback sentence, and perform string operations to:
Display the total number of characters.
Convert it to uppercase, lowercase, and title case.
Count how many times the word “good” appears.
Display the reversed sentence."""

#get names of the student
name=list(map(str,input("enter names of the students: ").split()))
name.sort() #sort in ascending
print(name)
name.sort(reverse=True)#sort in descending
print(name)
stu_dict={}
for i in name:
    a=tuple(map(int,input(f"enter 3 marks of {i}: ").split()))#get marks as tuples
    stu_dict[i]=a #store as key value pairs
print(stu_dict)
print("unique marks:")
marks=[]
for i in stu_dict:
    marks.append(stu_dict[i])
print(set(marks))#print unique mark values of the students

sent=input("enter sentence: ")
print(f"total number of characters:{len(sent)}")
print(sent.upper())
print(sent.lower())
print(sent.capitalize())
print(sent.count("good"))
print(sent[::-1])# print reverse of the string