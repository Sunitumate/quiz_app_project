import json
import random

def load_questions(filename="questions.json"):
    with open(filename, "r") as f:
        return json.load(f)

def start_quiz(questions):
    score = 0
    random.shuffle(questions)
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")
        try:
            answer = int(input("Your answer (1-4): "))
            if q['options'][answer - 1] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print("❌ Invalid input. Skipping question.")
    print(f"\n🎯 Your final score: {score}/{len(questions)}")

def main():
    print("🧠 Welcome to the Python Quiz App!")
    questions = load_questions()
    start_quiz(questions)

if __name__ == "__main__":
    main()