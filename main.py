import utils.interpac as interpac
import sciparse.qformer as qformer
import sciparse.qparse as qparse
import utils.d_inputman as inputmanager
import utils.tts
import utils.audio.soundplay as soundplay
import time
interman = interpac.InterMan()
questionformer = qformer.QFormer()
textconv = utils.tts.TextConverter()
player = soundplay.SoundPlayer()
textconv.convert("Time is up!", "timeup.mp3")
def doquestion():
    # Get the question
    jsond = interman.sendGet("https://scibowldb.com/api/questions/random").json()
    parser = qparse.QParser(jsond)
    tossup = parser.getTossup()
    bonus = parser.getBonus()
    # Form question
    qtext = questionformer.createQText(tossup, tossup.format, tossup.question)
    qanswer = questionformer.createQAnswer(tossup.answer)
    # Play question
    #textconv.convert(qtext, "question.mp3")
    #player.play("question.mp3")
    # Form answer
    #time.sleep(5)
    player.play("timeup.mp3")
    # Wait for kp
    
    textconv.convert(qanswer, "answer.mp3")
    player.play("answer.mp3")
doquestion()