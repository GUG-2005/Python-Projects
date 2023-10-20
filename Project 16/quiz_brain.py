class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < 12:
            return True
        else:
            return False

    def next_method(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        inp = input(f"Q.{self.question_number} {current_question.text} (True/ False)? ")
        self.check_answer(inp, current_question.answer)

    def check_answer(self, ua, ca):
        if ua.lower() == ca.lower():
            print("You've got your answer right")
            self.score += 1
            print(f"Your score is {self.score}")
        else:
            print("This was a mistake!")
            print(f"The correct answer is {ca}")
            print(f"Your score is {self.score}")