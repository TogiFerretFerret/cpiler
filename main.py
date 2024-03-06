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
pts = 0
textconv.convert("Time is up!", "timeup.mp3")
textconv.convert("Correct!", "correct.mp3")
textconv.convert("Incorrect!", "incorrect.mp3")
textconv.convert("Early answer!", "earlyanswer.mp3")
def saypts():
    textconv.convert(f"You have {pts} points.", "points.mp3")
    player.play("points.mp3")
def doquestion():
    global pts
    # Say num pts
    saypts()
    # Get the question
    jsond = interman.sendGet("https://scibowldb.com/api/questions/random").json()
    parser = qparse.QParser(jsond)
    tossup = parser.getTossup()
    bonus = parser.getBonus()
    # Form question
    qtext = questionformer.createQText(tossup, tossup.format, tossup.question)
    qanswer = questionformer.createQAnswer(tossup.answer)
    # Play question
    textconv.convert(qtext, "question.mp3")
    player.play("question.mp3")
    # Form answer
    earlyanswer = False
    for i in range(50):
        if inputmanager.get() == " ":
            earlyanswer = True
            break
        time.sleep(0.1)
    if not earlyanswer:
        player.play("timeup.mp3")
    else:
        player.play("earlyanswer.mp3")
    # Wait for kp
    inputmanager.waitforreturn()
    textconv.convert(qanswer, "answer.mp3")
    player.play("answer.mp3")
    # Wait for kp
    inp = inputmanager.getchars(chars=["y", "n"])
    if inp == "y":
        pts += tossup.ptworth
        player.play("correct.mp3")
        saypts()
        # Form bonus
        qtext = questionformer.createQText(bonus, bonus.format, bonus.question)
        qanswer = questionformer.createQAnswer(bonus.answer)
        # Play bonus
        textconv.convert(qtext, "question.mp3")
        player.play("question.mp3")
        # Form answer
        earlyanswer = False
        for i in range(20):
            if inputmanager.get() == " ":
                earlyanswer = True
                break
            time.sleep(1)
        if not earlyanswer:
            player.play("timeup.mp3")
        else:
            player.play("earlyanswer.mp3")
        # Wait for kp
        inputmanager.waitforreturn()
        textconv.convert(qanswer, "answer.mp3")
        player.play("answer.mp3")
        # Wait for kp
        inp = inputmanager.getchars(chars=["y", "n"])
        if inp == "y":
            pts += bonus.ptworth
            player.play("correct.mp3")
            saypts()
        else:
            player.play("incorrect.mp3")
            saypts()
    else:
        player.play("incorrect.mp3")
        if earlyanswer:
            pts -= tossup.ptworth
        saypts()

while True:
    doquestion()
    inputmanager.waitforreturn()