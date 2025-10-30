# A simple CLI based quiz game in python

def run_quiz():
    print("🎉 Welcome to the python CLI quiz game")
    name = input("Enter your name:")
    print(f"Hi {name}! Let's begin...\n")

    score = 0   #Initialize score

    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": {'a': '.py', 'b': '.pt', 'c': '.pyt', 'd': '.python'},
            "answer": 'a'
        },
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": {'a': '// comment', 'b': '# comment', 'c': '-- comment', 'd': '/* comment */'},
            "answer": 'b'
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": {'a': 'function', 'b': 'fun', 'c': 'def', 'd': 'define'},
            "answer": 'c'
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": {'a': '6', 'b': '8', 'c': '9', 'd': '5'},
            "answer": 'b'
        },
        {
            "question": "What is the capital of India?",
            "options": {'a': 'Delhi', 'b': 'Mumbai', 'c': 'Kolkata', 'd': 'Chennai'},
            "answer": "a"
        },
        {
            "question": "What is 5 + 3?",
            "options": {'a': '6', 'b': '8', 'c': '9', 'd': '7'},
            "answer": "b"
        },
        {
            "question": "Who developed Python?",
            "options": {'a': 'James Gosling', 'b': 'Elon Musk', 'c': 'Guido van Rossum', 'd': 'Tim Cook'},
            "answer": "c"
        } 
    ]


    for q in questions:
        print(q["question"])
        for key in q["options"]:
            print(f"{key} . {q['options'][key]}")
    
        answer = input("Your answer (a/b/c/d):").lower()
        if answer == q['answer']:
            print("✅ correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The answer is {q['answer']}.\n")


    print(f"🎯 You got {score} out of {len(questions)} correct!")

    if score == len(questions):
        print("🏆 Excellent Job!")
    elif score >= len(questions) // 2:
        print("👍 Good effort!")
    else:
        print("📘 Keep Practicing!")

    while True:
        run_quiz()
        play_again = input("\n Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing ! Goodbye 👋")
            break