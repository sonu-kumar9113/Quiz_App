import getpass

# Dummy database to store users' credentials
user_db = {}

# Questions for the quizzes
questions = {
    'DSA': [
        {
            "question": "What is the time complexity of binary search in a sorted array?",
            "choices": ["A. O(n)", "B. O(log n)", "C. O(n^2)", "D. O(log n^2)"],
            "correct_answer": "B"
        },
        {
            "question": "Which of the following is a non-linear data structure?",
            "choices": ["A. Array", "B. Linked List", "C. Binary Tree", "D. Stack"],
            "correct_answer": "C"
        },
        {
            "question": "Which sorting algorithm has the best average case time complexity?",
            "choices": ["A. Bubble Sort", "B. Merge Sort", "C. Quick Sort", "D. Insertion Sort"],
            "correct_answer": "B"
        },
        {
            "question": "What does a stack follow?",
            "choices": ["A. LIFO", "B. FIFO", "C. FILO", "D. Both A and C"],
            "correct_answer": "D"
        },
        {
            "question": "Which algorithm is used to find the shortest path in a weighted graph?",
            "choices": ["A. Dijkstra", "B. BFS", "C. DFS", "D. Kruskal's Algorithm"],
            "correct_answer": "A"
        }
    ],
    'DBMS': [
        {
            "question": "What does DBMS stand for?",
            "choices": ["A. Data Base Management System", "B. Data Backup Management System", "C. Database Master System", "D. Data Backup Master System"],
            "correct_answer": "A"
        },
        {
            "question": "Which of the following is used for database backup?",
            "choices": ["A. SQL", "B. DDL", "C. DML", "D. DBMS Utilities"],
            "correct_answer": "D"
        },
        {
            "question": "What is a foreign key?",
            "choices": ["A. A key from a different table", "B. A primary key from the same table", "C. A unique key", "D. A key without constraints"],
            "correct_answer": "A"
        },
        {
            "question": "Which normalization form eliminates transitive dependency?",
            "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
            "correct_answer": "C"
        },
        {
            "question": "What is the purpose of a primary key?",
            "choices": ["A. To uniquely identify each record", "B. To define relationships", "C. To store metadata", "D. None of the above"],
            "correct_answer": "A"
        }
    ],
    'PYTHON': [
        {
            "question": "Which data type is used to store a sequence of characters in Python?",
            "choices": ["A. List", "B. String", "C. Tuple", "D. Dictionary"],
            "correct_answer": "B"
        },
        {
            "question": "Which of the following is a mutable data type?",
            "choices": ["A. String", "B. List", "C. Tuple", "D. Integer"],
            "correct_answer": "B"
        },
        {
            "question": "What is the correct syntax for defining a function in Python?",
            "choices": ["A. def function_name():", "B. function function_name():", "C. function_name def():", "D. def: function_name()"],
            "correct_answer": "A"
        },
        {
            "question": "Which of the following is not a valid Python keyword?",
            "choices": ["A. False", "B. class", "C. try", "D. exception"],
            "correct_answer": "D"
        },
        {
            "question": "How do you comment a single line in Python?",
            "choices": ["A. /* comment */", "B. # comment", "C. <!-- comment -->", "D. // comment"],
            "correct_answer": "B"
        }
    ]
}

# Function to register a new user
def register():
    print("---- Register ----")
    username = input("Enter username: ")
    if username in user_db:
        print("Username already exists!")
    else:
        password = input("Enter password: ")
        user_db[username] = password
        print("Registration successful!")

# Function to login
def login():
    print("---- Login ----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user_db and user_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

# Function to attempt a quiz
def attempt_quiz():
    print("Select quiz topic:")
    print("1) DSA")
    print("2) DBMS")
    print("3) Python")
    choice = input("Enter your choice (1/2/3): ")
    topic = ""
    if choice == "1":
        topic = "DSA"
    elif choice == "2":
        topic = "DBMS"
    elif choice == "3":
        topic = "PYTHON"
    else:
        print("Invalid choice!")
        return

    questions_list = questions[topic]
    score = 0

    for i, question in enumerate(questions_list, 1):
        print(f"Q{i}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        answer = input("Your answer: ").upper()
        if answer == question['correct_answer']:
            score += 1

    print(f"You scored {score}/{len(questions_list)} in {topic} quiz.")

# Function to show results (This can be extended to save results in a file/database)
def show_result():
    print("---- Your Results ----")
    print("No previous results available in this demo.")

# Main menu function
def main_menu():
    while True:
        print("\n----- Welcome to the Quiz Application -----")
        print("1) Registration")
        print("2) Login")
        print("3) Attempt Quiz")
        print("4) Show Result")
        print("5) Exit Quiz")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                continue
        elif choice == "3":
            if login():
                attempt_quiz()
        elif choice == "4":
            show_result()
        elif choice == "5":
            print("Thank you for using the Quiz Application!")
            break
        else:
            print("Invalid choice! Please try again.")

# Running the application
if __name__ == "__main__":
    main_menu()
  

