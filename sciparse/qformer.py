import sciparse.qutility
import scitypes.question.qpart

class QFormer(sciparse.qutility.QUtility):
    """
    A class that represents a question former.

    This class provides methods to create a formatted question text and answer.

    Attributes:
        None

    Methods:
        createQText(type: scitypes.question.qpart.QuestionPart, format: str, question: str) -> str:
            Creates a formatted question text.

        createQAnswer(answer: str) -> str:
            Creates a formatted answer.

    """

    def __init__(self):
        pass

    def createQText(self, type: scitypes.question.qpart.QuestionPart, format: str, question: str) -> str:
        """
        Creates a formatted question text.

        Args:
            type (scitypes.question.qpart.QuestionPart): The type of the question part.
            format (str): The format of the question.
            question (str): The question text.

        Returns:
            str: The formatted question text.

        """
        return f'''{type.type}\n{format}\n{question}'''

    def createQAnswer(self, answer: str) -> str:
        """
        Creates a formatted answer.

        Args:
            answer (str): The answer text.

        Returns:
            str: The formatted answer.

        """
        return f'''Correct Answer: \n{answer}'''