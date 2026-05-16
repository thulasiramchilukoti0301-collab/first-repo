def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'


def compute_average(*scores):
    return sum(scores) / len(scores)


def print_report(name, *scores, department="CSE"):
    avg = compute_average(*scores)
    grade = get_grade(avg)

    print("Name:", name)
    print("Department:", department)
    print("Marks:", scores)
    print("Average:", avg)
    print("Grade:", grade)

print_report("Ram", 85, 90, 78)
print_report("Sai", 70, 65, 60, 75, department="ECE")