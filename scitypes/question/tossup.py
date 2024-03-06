import scitypes.question.qpart

class Tossup(scitypes.question.qpart.QuestionPart):
    """
    Represents a toss-up question in a quiz or game.

    Attributes:
        format (str): The format of the toss-up question.
        question (str): The text of the toss-up question.
        answer (str): The correct answer to the toss-up question.
        answered (bool): Indicates whether the toss-up question has been answered.
        correct (bool): Indicates whether the answer to the toss-up question is correct.
        ptworth (int): The point worth of the toss-up question.
    """

    def __init__(self, format: str, question: str, answer: str):
        self.format = format
        self.question = question
        self.answer = answer
        self.answered = False
        self.correct = False
        self.ptworth = 5
        super().__init__(format, question, answer, "Tossup")