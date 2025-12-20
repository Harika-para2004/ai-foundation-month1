skills = ["Python", "Data Analysis", "Machine Learning", "Deep Learning"]
skills.append("AI Ethics")

print("Updated skills:", skills)

for skill in skills:
    print(skill)

#dictionary
employee = {
    "name" : "Harika",
    "age" : 21,
    "dept" : "React"
}

print(employee.items())

for key, value in employee.items():
    print(key , ":", value)
