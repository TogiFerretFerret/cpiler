import scitypes.question.qpart

class Bonus(scitypes.question.qpart.QuestionPart):
    """
    Represents a bonus question part.

    Attributes:
        format (str): The format of the bonus question.
        question (str): The bonus question.
        answer (str): The correct answer to the bonus question.
        answered (bool): Indicates whether the bonus question has been answered.
        correct (bool): Indicates whether the answer to the bonus question is correct.
        ptworth (int): The point worth of the bonus question.

    Methods:
        __init__(format, question, answer): Initializes a new instance of the Bonus class.
    """

    def __init__(self, format: str, question: str, answer: str):
        self.format = format
        self.question = question
        self.answer = answer
        self.answered = False
        self.correct = False
        self.ptworth = 10
        super().__init__(format, question, answer, "Bonus")