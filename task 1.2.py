#advanced learning

name=input("Enter your name: ")
age=int(input("Enter your age: "))
s1,s2,s3,s4,s5=map(float,input("Enter Mark of All 5 subjects: ").split())
total_mark=s1+s2+s3+s4+s5

print("\n----student performance ---\n")
print(f"total mark:{total_mark:.2f}")
print(f"percentage mark:{(total_mark*100)/500:.2f}%")
print(f"maximum mark:{max(s1,s2,s3,s4,s5):.2f}")
print(f"minimum mark:{min(s1,s2,s3,s4,s5):.2f}")
