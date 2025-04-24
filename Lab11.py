import matplotlib.pyplot as plt
import os
import math

students_file = 'data/students.txt'

assignments_file = 'data/assignments.txt'

submissions_folder = 'data/submissions'


def load_students():
    students = {}

    with open(students_file, 'r', encoding='latin-1') as f:
        for line in f:
            student_id = line[:3]

            name = line[3:].strip()

            students[name] = student_id

    return students


def load_assignments():
    assignments = {}

    with open(assignments_file, 'r', encoding='latin-1') as f:
        lines = f.read().splitlines()

        i = 0

        while i < len(lines):
            name = lines[i].strip()

            id_ = lines[i + 1].strip()

            points = int(lines[i + 2].strip())

            assignments[id_] = {'name': name, 'points': points}

            i += 3

    return assignments


def load_submissions():
    file_contents = {}

    for filename in os.listdir(submissions_folder):

        if filename.endswith(".txt"):

            file_path = os.path.join(submissions_folder, filename)

            try:

                with open(file_path, "r", encoding="latin-1") as file:

                    file_contents[filename] = file.read()



            except UnicodeDecodeError as e:

                print(f"Error reading file {filename}: {e}")

                # Handle error or skip the file if necessary

    return file_contents


def student_grade(name):
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()

    if name not in students:
        print("Student not found")
        return

    student_id = students[name]

    total_percent = 0
    count = 0

    for val in submissions.values():
        sid, aid, percent = val.strip().split('|')
        if sid == student_id:
            total_percent += float(percent)
            count += 1

    if count == 0:
        print("No submissions found for this student.")
        return

    average_percent = total_percent / count
    print(f"{(math.floor(average_percent))}%")


def assignment_statistics(name):
    assignments = load_assignments()

    submissions = load_submissions()

    assignment_id = None

    for aid, data in assignments.items():

        if data['name'] == name:
            assignment_id = aid

            break

    if not assignment_id:
        print("Assignment not found")

        return

    scores = []

    for key, val in submissions.items():

        sid, aid, percent = val.strip().split('|')

        if aid == assignment_id:
            scores.append(float(percent))

    print(f"Min: {round(min(scores))}%")

    print(f"Avg: {math.floor(sum(scores) / len(scores))}%")

    print(f"Max: {round(max(scores))}%")


def assignment_graph(name):
    assignments = load_assignments()

    submissions = load_submissions()

    assignment_id = None

    for aid, data in assignments.items():

        if data['name'] == name:
            assignment_id = aid

            break

    if not assignment_id:
        print("Assignment not found")

        return

    scores = []

    for key, val in submissions.items():

        sid, aid, percent = val.strip().split('|')

        if aid == assignment_id:
            scores.append(float(percent))

    plt.hist(scores, bins=[0, 25, 50, 75, 100], edgecolor='black')

    plt.title(f'Histogram for {name}')

    plt.xlabel('Score (%)')

    plt.ylabel('Number of Students')

    plt.show()


def main():
    print("1. Student grade")

    print("2. Assignment statistics")

    print("3. Assignment graph")

    choice = input("\nEnter your selection: ")

    if choice == '1':

        name = input("What is the student's name: ")

        student_grade(name)







    elif choice == '2':

        name = input("What is the assignment name: ")

        assignment_statistics(name)







    elif choice == '3':

        name = input("What is the assignment name: ")

        assignment_graph(name)


if __name__ == "__main__":
    main()
