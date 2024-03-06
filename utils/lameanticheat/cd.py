import utils.moo.meow

class CheatMan:
    """
    The CheatMan class represents a cheat detection system.

    Attributes:
        None

    Methods:
        runCAD(times=1, infinite=True): Run the CAD (Cheating Already Detected) process.
        runCD(): Run the CD (Cheating Detected) process.
    """

    def __init__(self):
        pass

    def runCAD(times=1, infinite=True):
        """
        Run the CAD (Cheating Already Detected) process.

        Args:
            times (int, optional): The number of times to run the CAD process. Defaults to 1.
            infinite (bool, optional): Whether to run the CAD process infinitely. Defaults to True.
        """
        if infinite:
            while True:
                utils.moo.meow.imacow()
        for i in range(times):
            utils.moo.meow.imacow()

    def runCD(playermeta):
        """
        Detects for Cheats. Checks if the player's metadata violates certain conditions.

        Args:
            playermeta (dict): A dictionary containing the player's metadata, including 'hp', 'atk', 'def', 'lvl', and 'client'.

        Returns:
            bool: True if any of the conditions are violated, False otherwise.
        """
        if playermeta['hp'] > 10000 or playermeta["atk"] > 10000 or playermeta["def"] > 10000 or playermeta["lvl"] > 1000 or not (playermeta["client"] == "vanilla" or playermeta["client"] == "anvil"):
            return True
        return False
    def runCD(playermeta):

        if playermeta['hp']>10000 or playermeta["atk"]>10000 or playermeta["def"]>10000 or playermeta["lvl"]>1000 or not (playermeta["client"]=="vanilla" or playermeta["client"]=="anvil"):
            return True
        return False