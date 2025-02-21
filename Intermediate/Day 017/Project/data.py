# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {
#         "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
#         "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

import requests
import html

def get_user_input():
    user_difficulty = input("Choose difficulty (easy, medium, hard, or random): ").strip().lower()
    if user_difficulty not in ["easy", "medium", "hard"]:
        user_difficulty = ""

    num_of_questions = input("How many questions would you like? (Pick a number): ").strip()
    while not num_of_questions.isdigit() or int(num_of_questions) <= 0:
        print("Invalid input. Please enter a number greater than 0.")
        num_of_questions = input("How many questions would you like? (Pick a number): ").strip()

    categories = {
        "1": "General Knowledge", "2": "Entertainment: Books", "3": "Entertainment: Film", "4": "Entertainment: Music",
        "5": "Entertainment: Musicals & Theatres", "6": "Entertainment: Television", "7": "Entertainment: Video Games",
        "8": "Entertainment: Board Games", "9": "Science & Nature", "10": "Science: Computers",
        "11": "Science: Mathematics",
        "12": "Mythology", "13": "Sports", "14": "Geography", "15": "History", "16": "Politics", "17": "Art",
        "18": "Celebrities", "19": "Animals", "20": "Any Category"
    }

    print("Categories:")
    for num, cat in categories.items():
        print(f"{num}: {cat if cat else 'Any Category'}")

    category_choice = int(input("Choose a category (1-20): ").strip())
    # category = categories.get(category_choice, "")

    return num_of_questions, user_difficulty, category_choice

number_of_questions, difficulty, category = get_user_input()

url = f"https://opentdb.com/api.php?amount={number_of_questions}"
if difficulty:
    url += f"&difficulty={difficulty}"
if category <= 19:
    url += f"&category={category + 8}"
url += "&type=boolean"

response = requests.get(url)
data = response.json()

if not data["results"]:
    print("No questions were found for the selected category/difficulty. Please try again.")
    exit()
question_data = [
    {"text": html.unescape(q["question"]), "answer": q["correct_answer"]}
    for q in data["results"]
]
