from colorama import Fore, Style

QUIZ_DATA = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

RETRY_THRESHOLD = 2


def ask_question(question: str, correct_answer: str) -> (bool, str):
    response = input(f"{question} ").strip()
    return response.lower() == correct_answer.lower(), response


def display_failures(failures):
    print("\n" + "-" * 20)
    print("Here are the questions you got wrong:")
    for idx, item in enumerate(failures, 1):
        print(f"{idx}. {Fore.RED}{item['question']}{Style.RESET_ALL}")
        print(f"   Your answer: {Fore.RED}{item['response']}{Style.RESET_ALL}")
        print(f"   Correct answer: {Fore.GREEN}{item['answer']}{Style.RESET_ALL}")
        print("." * 20)


def run_quiz():
    while True:
        correct = 0
        failures = []

        print("\nWelcome to the Star Wars Quiz!\n")
        for item in QUIZ_DATA:
            is_correct, response = ask_question(item["question"], item["answer"])
            if is_correct:
                correct += 1
            else:
                failures.append({
                    "question": item["question"],
                    "answer": item["answer"],
                    "response": response
                })

        total = len(QUIZ_DATA)
        incorrect = total - correct

        print("\n" + "-" * 20)
        print(f"You got {correct} right and {incorrect} wrong.")
        print("-" * 20)

        if failures:
            display_failures(failures)

        if incorrect > RETRY_THRESHOLD:
            retry = input("You got more than 2 questions wrong. Try again? (y/n): ").lower()
            if retry != "y":
                break
        else:
            print("Congratulations! You passed the quiz.")
            break


if __name__ == "__main__":
    run_quiz()
