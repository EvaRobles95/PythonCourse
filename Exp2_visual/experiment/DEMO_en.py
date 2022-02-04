 # DEMO in english
""" RDK DEMO """
# run this before every experiment to familiarize participants with the task
# participants receive feedback in the form of green or red arrow border highlights

from psychopy import visual, core, event, sound
import random
import numpy as np
from psychopy import data, gui
from task_en import RDMDTask

# create window
# Test Window for programming
"""
win = visual.Window(size=[1600,1000],
                    fullscr=False, screen=0,
                    allowGUI=True, monitor='testMonitor', units='deg')

"""
# full screen option
win = visual.Window(size=[1920, 1080],
                    fullscr=True, screen=0,
                    winType='pyglet', allowGUI=True, 
                    monitor='testMonitor',units='deg')



# clear potential key strokes
event.clearEvents()
# set mouse cursor to invisible
win.mouseVisible = False

# some important params for timing
max_dot_duration = 950.0
break_duration = 950.0
mean_ms_per_frame, std_ms_per_frame, median_ms_per_frame=visual.getMsPerFrame(win, nFrames=60, showVisual=True)
max_dot_frames = int(max_dot_duration/mean_ms_per_frame)
break_duration=break_duration
break_duration_frames=int(break_duration/mean_ms_per_frame)

# fixation stimulus
fixation = visual.ImageStim(win=win, image='fixation.PNG', units='pix',size=(30,30),pos=[0.0,-2.0])

# create dotPatch stimulus
directions=[0, 180] # 0 = right, 180 = left!
dots = visual.DotStim(win=win,
                      name='dots',
                      nDots=200,
                      dotSize=3,
                      speed=0.07,
                      dir=0.0,
                      coherence=.5,
                      fieldPos=[0.0, 0.0],
                      fieldSize=22,
                      color=(0.8, 1.0, 0.8),
                      fieldShape='circle',
                      dotLife=15,
                      signalDots='same',
                      noiseDots='direction')

circle = visual.Circle(win, radius=1.5, edges=32, fillColor='grey', lineColor='grey')
# Matthias hat hier fieldSize = 10 and radius = 2

# display introductory instructions
message1= visual.TextStim(win, wrapWidth=30, pos=[0,2], text='You will see clouds with moving dots\nIn which direction do you think they move?\n"LEFT" or "RIGHT"?\nGive the answer by pressing the "up" or "down" key when the arrows appear on screen\nLet us start with some very simple examples.')
message2= visual.TextStim(win, wrapWidth=30, pos=[0,-2], text='Press space key when ready')

message1.draw()
message2.draw()
win.flip()
event.waitKeys(keyList=['space'])
event.clearEvents()

# params and list needed for the trials
trials = np.arange(1,11) # testtrial number for the demo change here to make it longer/ shorter
demoKeys = []
########################################################################################################
""" THE EASY TRIALS """
correct_easy = 0
for t in trials:
    win.mouseVisible = False
    n_dot_frames = 0
    # here draw 1 dotpatch with coherence = 1
    dots.setDir(random.choice(directions))
    dots.setFieldCoherence(0.5)

    event.clearEvents()

    while n_dot_frames < max_dot_frames:
        
        dots.draw()
        circle.draw()
        fixation.draw()
        win.flip()
        n_dot_frames+=1

    fixation.draw()
    win.flip()
    core.wait(0.5)
    # response window parameters 
    orientations = [270,90] # 270 = Pfeil nach rechts, 90 = Pfeil nach links
    
    pos1, pos2 = random.sample(orientations, 2)
    img_up = visual.ImageStim(win=win,image="arrow.png",units="pix",ori=pos1,pos=(0,250))
    img_down = visual.ImageStim(win=win,image="arrow.png",units="pix",ori=pos2,pos=(0,-250))
    
    border_up_correct = visual.ShapeStim(win, vertices=img_up.verticesPix, units='pix',lineColor='limegreen')
    border_down_correct = visual.ShapeStim(win, vertices=img_down.verticesPix, units='pix',lineColor='limegreen')

    border_up_wrong = visual.ShapeStim(win, vertices=img_up.verticesPix, units='pix',lineColor='red')
    border_down_wrong = visual.ShapeStim(win, vertices=img_down.verticesPix, units='pix',lineColor='red')

    # set arrow orientations randomly per position
    img_up.setOri(pos1)
    img_down.setOri(pos2)

    # flip that
    event.clearEvents()
    
    messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
    messageA.draw()
    img_up.draw()
    img_down.draw()
    fixation.draw()
    win.flip()
    try: 
        response =  event.waitKeys(keyList=['up','down','escape'])
        demoKeys.append(response)

        # feedback screen: highlight border colors of arrow image... in red or green
        if demoKeys[-1][0]=='up':
            if dots.dir==0 and img_up.ori==270.0 or dots.dir==180 and img_up.ori==90.0:
                event.clearEvents()
                fixation.draw()
                border_up_correct.autoDraw=True
                img_up.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                correct_easy += 1
            elif dots.dir==0 and img_up.ori==90.0 or dots.dir==180 and img_up.ori==270.0:
                event.clearEvents()
                fixation.draw()
                border_up_wrong.autoDraw=True
                img_up.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                

        elif demoKeys[-1][0] == 'down':
            if dots.dir==0 and img_down.ori==270.0 or dots.dir==180 and img_down.ori==90.0:
                event.clearEvents()
                fixation.draw()
                border_down_correct.autoDraw=True
                img_down.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                correct_easy += 1
            elif dots.dir==0 and img_down.ori==90.0 or dots.dir==180 and img_down.ori==270.0:
                event.clearEvents()
                fixation.draw()
                border_down_wrong.autoDraw=True
                img_down.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()

        elif demoKeys[-1][0] == 'escape':
            win.close()
            core.quit()
            
        core.wait(1)
        border_down_correct.autoDraw=False
        border_up_correct.autoDraw=False
        border_down_wrong.autoDraw=False
        border_up_wrong.autoDraw=False

        fixation.draw()
        win.flip()
        core.wait(0.5)

        
    except TypeError:
        pass  

messageB = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text=('Correct: %i' % correct_easy))
messageC = visual.TextStim(win, wrapWidth=30, pos=[0,0], height=1, text=('Outof: %i' % len(trials)))
messageB.draw()
messageC.draw()
win.flip()
core.wait(2.5)

    
    
######################################################################################################    
""" THE HARD TRIALS """
message6= visual.TextStim(win, wrapWidth=30, pos=[0,2], text='Sometimes it is less clear!\nJust make a guess then')
message6.draw()
message2.draw()
win.flip()
event.waitKeys(keyList=['space'])
# 5 trials of hard ones...
correct_hard = 0
for t in trials:
    win.mouseVisible=False
    n_dot_frames = 0
    # here draw 1 dotpatch with coherence = 1
    dots.setDir(random.choice(directions))
    dots.setFieldCoherence(0.08)

    event.clearEvents()

    while n_dot_frames < max_dot_frames:
        
        dots.draw()
        circle.draw()
        fixation.draw()
        win.flip()
        n_dot_frames+=1

    fixation.draw()
    win.flip()
    core.wait(0.5)
    
    # response window parameters 
    orientations = [270,90] # 270 = Pfeil nach rechts, 90 = Pfeil nach links
    
    pos1, pos2 = random.sample(orientations, 2)
    img_up = visual.ImageStim(win=win,image="arrow.png",units="pix",ori=pos1,pos=(0,250))
    img_down = visual.ImageStim(win=win,image="arrow.png",units="pix",ori=pos2,pos=(0,-250))
    border_up_correct = visual.ShapeStim(win, vertices=img_up.verticesPix, units='pix',lineColor='limegreen')
    border_down_correct = visual.ShapeStim(win, vertices=img_down.verticesPix, units='pix',lineColor='limegreen')

    border_up_wrong = visual.ShapeStim(win, vertices=img_up.verticesPix, units='pix',lineColor='red')
    border_down_wrong = visual.ShapeStim(win, vertices=img_down.verticesPix, units='pix',lineColor='red')

    # set arrow orientations randomly per position
    img_up.setOri(pos1)
    img_down.setOri(pos2)

    # flip that
    event.clearEvents()
    
    messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
    messageA.draw()
    img_up.draw()
    img_down.draw()
    fixation.draw()
    win.flip()
    try: 
        response =  event.waitKeys(keyList=['up','down','escape'])
        demoKeys.append(response)

        # feedback screen: highlight border colors of arrow image... in red or green
        if demoKeys[-1][0]=='up':
            if dots.dir==0 and img_up.ori==270.0 or dots.dir==180 and img_up.ori==90.0:
                event.clearEvents()
                fixation.draw()
                border_up_correct.autoDraw=True
                img_up.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                correct_hard += 1
            elif dots.dir==0 and img_up.ori==90.0 or dots.dir==180 and img_up.ori==270.0:
                event.clearEvents()
                fixation.draw()
                border_up_wrong.autoDraw=True
                img_up.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()

        elif demoKeys[-1][0] == 'down':
            if dots.dir==0 and img_down.ori==270.0 or dots.dir==180 and img_down.ori==90.0:
                event.clearEvents()
                fixation.draw()
                border_down_correct.autoDraw=True
                img_down.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                correct_hard += 1
            elif dots.dir==0 and img_down.ori==90.0 or dots.dir==180 and img_down.ori==270.0:
                event.clearEvents()
                fixation.draw()
                border_down_wrong.autoDraw=True
                img_down.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()

        elif demoKeys[-1][0] == 'escape':
            win.close()
            core.quit()
            
        core.wait(1)
        border_down_correct.autoDraw=False
        border_up_correct.autoDraw=False
        border_down_wrong.autoDraw=False
        border_up_wrong.autoDraw=False

        fixation.draw()
        win.flip()
        core.wait(0.5)

        
    except TypeError:
        pass

messageB = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text=('Correct: %i' % correct_hard))
messageC = visual.TextStim(win, wrapWidth=30, pos=[0,0], height=1, text=('Outof: %i' % len(trials)))
messageB.draw()
messageC.draw()
win.flip()
core.wait(2.5)

#######################################################################################################
""" NOW WITH VOICES """
tone = []
voicetrials = np.arange(1,16) # number of TRIALS, change here to make them longer or shorter
message5 = visual.TextStim(win, wrapWidth=30, pos=[0,2], text='Later, voices will help you with the task\nAlso, there is limited time to make your decision: 3 seconds.')
message5.draw()
message2.draw()
win.flip()
event.waitKeys(keyList=['space'])
win.flip()
core.wait(0.5)

correct_voice = 0
for v in voicetrials:
    n_dot_frames = 0
    dots.setDir(random.choice(directions))
    dots.setFieldCoherence(0.75)

    # Now with sounds
    if dots.dir == 0: # RECHTS
        rechts = sound.Sound(value='right_en.wav', name='rechts') 
        links = sound.Sound(value='left_en.wav', name='links')
        tone.append( random.choices([rechts, links], [1, 0.0]))
    elif dots.dir == 180: # Links
        rechts = sound.Sound(value='right_en.wav', name='rechts')
        links = sound.Sound(value='left_en.wav', name='links')
        tone.append( random.choices([rechts, links], [0.0, 1]))

    tone[-1][0].play()
    core.wait(0.8)

    while n_dot_frames < max_dot_frames:
        win.mouseVisible=False
        dots.draw()
        circle.draw()
        fixation.draw()
        win.flip()
        n_dot_frames+=1

    fixation.draw()
    win.flip()
    win.mouseVisible=False
    core.wait(0.5)
    
    # response window parameters 
    orientations = [270,90] # 270 = Pfeil nach rechts, 90 = Pfeil nach links
    
    pos1, pos2 = random.sample(orientations, 2)
    img_up = visual.ImageStim(win=win,image="arrow.png",units="pix",ori=pos1,pos=(0,250))
    img_down = visual.ImageStim(win=win,image="arrow.png",units="pix",ori=pos2,pos=(0,-250))
    border_up_correct = visual.ShapeStim(win, vertices=img_up.verticesPix, units='pix',lineColor='limegreen')
    border_down_correct = visual.ShapeStim(win, vertices=img_down.verticesPix, units='pix',lineColor='limegreen')

    border_up_wrong = visual.ShapeStim(win, vertices=img_up.verticesPix, units='pix',lineColor='red')
    border_down_wrong = visual.ShapeStim(win, vertices=img_down.verticesPix, units='pix',lineColor='red')

    # set arrow orientations randomly per position
    img_up.setOri(pos1)
    img_down.setOri(pos2)

    # flip that
    event.clearEvents()
    
    messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
    messageA.draw()
    img_up.draw()
    img_down.draw()
    fixation.draw()
    win.mouseVisible = False
    win.flip()
    try: 
        response =  event.waitKeys(maxWait=3, keyList=['up','down','escape'])
        demoKeys.append(response)

        # feedback screen: highlight border colors of arrow image... in red or green
        if demoKeys[-1][0]=='up':
            if dots.dir==0 and img_up.ori==270.0 or dots.dir==180 and img_up.ori==90.0:
                event.clearEvents()
                fixation.draw()
                border_up_correct.autoDraw=True
                img_up.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                correct_voice += 1
            elif dots.dir==0 and img_up.ori==90.0 or dots.dir==180 and img_up.ori==270.0:
                event.clearEvents()
                fixation.draw()
                border_up_wrong.autoDraw=True
                img_up.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()

        elif demoKeys[-1][0] == 'down':
            if dots.dir==0 and img_down.ori==270.0 or dots.dir==180 and img_down.ori==90.0:
                event.clearEvents()
                fixation.draw()
                border_down_correct.autoDraw=True
                img_down.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()
                correct_voice += 1
            elif dots.dir==0 and img_down.ori==90.0 or dots.dir==180 and img_down.ori==270.0:
                event.clearEvents()
                fixation.draw()
                border_down_wrong.autoDraw=True
                img_down.draw()
                messageA = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
                messageA.draw()
                win.flip()

        elif demoKeys[-1][0] == 'escape':
            win.close()
            core.quit()

            
        core.wait(1)
        border_down_correct.autoDraw=False
        border_up_correct.autoDraw=False
        border_down_wrong.autoDraw=False
        border_up_wrong.autoDraw=False

        fixation.draw()
        win.flip()
        core.wait(0.5)

        
    except TypeError:
        pass

messageB = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text=('Correct: %i' % correct_voice))
messageC = visual.TextStim(win, wrapWidth=30, pos=[0,0], height=1, text=('Outof: %i' % len(voicetrials)))
messageB.draw()
messageC.draw()
win.flip()
core.wait(2.5)

#
"""
50, 30, 20 coherence und Stimmen probabilistisch!
Noch ein paar klare runs machen!
"""

###################################################################################################  
""" FINAL REMARKS """

messageC = visual.TextStim(win, wrapWidth=30, pos=[0,2], height=1, text='The voices will not be this reliable all the time\nYou completed the demo!')
messageD = visual.TextStim(win, wrapWidth=30, pos=[0,0], height=1, text='Press space bar to finish demo')
messageC.draw()
messageD.draw()

win.flip()
win.mouseVisible=False
event.waitKeys(keyList=['space'])

print(demoKeys)
win.close()
core.quit()


