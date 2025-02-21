class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False
        # return self.question_number < len(self.question_list) - same as above but shorter

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question)

    def check_answer(self, answer, current_question):
        if answer.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("I am sorry. You got it wrong.")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")