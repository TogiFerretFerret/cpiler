import utils.interpac as interpac
import sciparse.qformer as qformer
import sciparse.qparse as qparse
import utils.d_inputman as inputmanager
interman = interpac.InterMan()
questionformer = qformer.QFormer()
def doquestion():
    # Get the question
    jsond = interman.sendGet("https://scibowldb.com/api/questions/random").json()
    parser = qparse.QParser(jsond)
    tossup = parser.getTossup()
    bonus = parser.getBonus()
doquestion()