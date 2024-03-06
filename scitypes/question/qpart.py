class QuestionPart:
    """
    Represents a part of a question.

    Attributes:
        format (str): The format of the question part.
        question (str): The question text.
        answer (str): The answer to the question part.
        correct (bool): Indicates whether the answer is correct or not.
    """

    def __init__(self, format: str, question: str, answer: str, type: str):
        """
        Initializes a new instance of the QuestionPart class.

        Args:
            format (str): The format of the question part.
            question (str): The question text.
            answer (str): The answer to the question part.
        """
        self.format = format
        self.question = question
        self.answer = answer
        self.correct = False
        self.type = type
    def answer(self, gotcorrect: bool):
        """
        Sets the correctness of the answer.

        Args:
            gotcorrect (bool): Indicates whether the answer is correct or not.

        Returns:
            str: The answer to the question part.
        """
        self.correct = gotcorrect
        return self.answer