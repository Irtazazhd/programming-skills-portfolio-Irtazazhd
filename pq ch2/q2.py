# Taking the number of courses and total marks as input
num_courses = int(input("Enter the number of courses: "))
total_marks = float(input("Enter total marks (Enter 500 for default): "))

# Getting course marks from the user
course_marks = [float(input(f"Enter marks for course {i+1}: ")) for i in range(num_courses)]

# Calculating average and percentage
average = sum(course_marks) / num_courses
percentage = (sum(course_marks) / total_marks) * 100

# Displaying the results
print(f"Average marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
