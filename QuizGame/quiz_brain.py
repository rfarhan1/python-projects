class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_ques(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_ans, ques_ans):
        if user_ans.lower() != ques_ans.lower():
            print(f"You got it wrong")

        else:
            print("You got it right")
            self.score += 1

        print(f"The correct answer was: {ques_ans}.\nYour current score is: {self.score}/{(self.question_number + 1)}")
        print("")
        print("")

