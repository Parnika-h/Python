import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.q_list = q_list
        self.score = 0

    def ask(self):
        item = self.q_list[self.question_no]
        self.ans = item.ans
        return f"Q.{self.question_no+1}: {html.unescape(item.text)}"

    def still_has_q(self):
        return self.question_no != len(self.q_list)

    def check_ans(self, user):
        if user.lower() == self.ans.lower():
            self.score += 1
            self.question_no += 1
            return True
        else:
            self.question_no += 1
            return False

