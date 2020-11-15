studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

#TODO: create student grades dictionary,
#TODO: grade 91-100 is Outstanding, 81-90 is Exceeds Expectations, 71-80 is Acceptable, and 70 or lower fails.

studentGrades = {}

for name in studentScores:
    if studentScores[name] >= 91:
        studentGrades[name] = "Outstanding"
    elif studentScores[name] >= 81:
        studentGrades[name] = "Exceeds Expectations"
    elif studentScores[name] >= 71:
        studentGrades[name] = "Acceptable"
    else:
        studentGrades[name] = "Failed"

for name in studentGrades:
    print(name + ": " + studentGrades[name])