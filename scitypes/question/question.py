import scitypes.question.bonus
import scitypes.question.tossup
class Question:
    """
    Represents a question object.

    Args:
        qdata (scitypes.question.tossup): The tossup data for the question.
        bdata (scitypes.question.bonus): The bonus data for the question.
        uri (str): The URI of the question.

    Attributes:
        qdata (scitypes.question.tossup): The tossup data for the question.
        bdata (scitypes.question.bonus): The bonus data for the question.
        uri (str): The URI of the question.
    """

    def __init__(self, qdata: scitypes.question.tossup, bdata: scitypes.question.bonus, uri: str):
        self.qdata = qdata
        self.bdata = bdata
        self.uri = uri

    def getQuestion(self):
        """
        Returns the tossup data for the question.

        Returns:
            scitypes.question.tossup: The tossup data for the question.
        """
        return self.qdata

    def getBonus(self):
        """
        Returns the bonus data for the question.

        Returns:
            scitypes.question.bonus: The bonus data for the question.
        """
        return self.bdata