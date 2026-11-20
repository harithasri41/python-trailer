
name = input("Enter student name: ")

telugu = int(input("Enter Telugu marks: "))
english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))

total = telugu + english + maths
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
