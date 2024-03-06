import scitypes.question
import scitypes.question.bonus
import scitypes.question.tossup
import sciparse.qutility

class QParser(sciparse.qutility.QUtility):
    """
    A class that parses a JSON object representing a question and provides methods to retrieve different question types.

    Args:
        jsond (dict): A dictionary representing the JSON object of the question.

    Attributes:
        jsond (dict): The JSON object of the question.
        uri (str): The API URL associated with the question.
        src (str): The source of the question.
        question (None): The question itself.

    """

    def __init__(self, jsond):
        self.jsond = jsond["question"]
        self.uri = self.jsond["api_url"]
        self.src = self.jsond["source"]
        self.question = None

    def getTossup(self):
        """
        Retrieves a Tossup question object.

        Returns:
            Tossup: A Tossup question object.

        """
        format = self.jsond["tossup_format"]
        question = self.jsond["tossup_question"]
        answer = self.jsond["tossup_answer"]
        return scitypes.question.tossup.Tossup(format=format, question=question, answer=answer)

    def getBonus(self):
        """
        Retrieves a Bonus question object.

        Returns:
            Bonus: A Bonus question object.

        """
        format = self.jsond["bonus_format"]
        question = self.jsond["bonus_question"]
        answer = self.jsond["bonus_answer"]
        return scitypes.question.bonus.Bonus(format=format, question=question, answer=answer)
