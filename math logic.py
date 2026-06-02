print("1. Calculation Data Function (Math Logic)")
def calculate_data(marks):
    #calculate sum and average of 5 subjects
    total = sum(marks)
    average =total/5
    #result logic: pass if all marks ar more than 33 or more
    result = "Pass"
    for m in marks:
        if m<33:
            result="fail"
            break
       #Grade logic based on average marks
        if average>=90:
            grade='A'
        elif average>=75:
            grade='B'
        elif average>50:
            grade='C'
        else:
            grade='D'
    return total,average,result,grade
# Example
marks = []
for i in range(1,6):
    mark = int(input(f"Enter marks for subject{i}:"))
    marks.append(mark)
total,average,result,grade=calculate_data(marks)

print("'\n---Result---")
print("Total Marks:",total)
print("Average Marks:", round(average,2))
print("Result:", result)
print("Grade:", grade)
