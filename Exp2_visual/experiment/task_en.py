from psychopy import visual, event, core
import random
from psychopy import sound


class RDMDTask():
    def __init__(self, fixation_duration, max_dot_duration, min_iti_duration, break_duration):

        #Full Screen option (for my Fujitsu office screen)
        self.win = visual.Window(size=[1920, 1080],
                    fullscr=True, screen=0,
                    winType='pyglet', allowGUI=True, 
                    monitor='testMonitor',units='deg')
       

        # make mouse cursor invisible and clear potential previous key strokes
        self.win.setMouseVisible=False
        event.clearEvents()

        # Measure frame rate
        self.mean_ms_per_frame, std_ms_per_frame, median_ms_per_frame=visual.getMsPerFrame(self.win, nFrames=60, showVisual=True)

        # Frames for fixation
        self.fixation_duration=fixation_duration
        self.fixation_frames=int(fixation_duration/self.mean_ms_per_frame)

        # Frames for DotStim, assessed in run_task also. 
        self.max_dot_duration=max_dot_duration
        self.max_dot_frames=int(max_dot_duration/self.mean_ms_per_frame)

        # Minimum inter-trial interval frames, also set in run_task
        self.min_iti_duration=min_iti_duration
        self.min_iti_frames=int(min_iti_duration/self.mean_ms_per_frame)

        # some params determining break duration, are taken from run_task script 
        self.break_duration=break_duration
        self.break_duration_frames=int(break_duration/self.mean_ms_per_frame)

        # fixation stimulus (in the beginning)
        """
        self.fixation = visual.PatchStim(self.win,units='deg',
            tex=None,mask='circle',sf=0,size=0.1,name='fixation',
            autoLog=False,color=[1,1,1])
        """

        self.fixation = visual.ImageStim(win=self.win, image='fixation.PNG', units='pix',size=(30,30),pos=[0.0,-2.0])

        # create the DOTPATCH! 
        self.dots = visual.DotStim(
            win=self.win,
            name='dots',
            nDots=200,              # von 950 in der ersten Runde auf 400 runter
            dotSize=3,              # in pixels (from 2 to 3)
            speed=0.07,             # in units per frame
            dir=0.0,                # set in runTrial
            coherence=.3,           # start coherence value which is later staircased/ set
            fieldPos=[0.0, 0.0],    # central on screen
            fieldSize=22,           # unit: visual degrees
            color=(0.8, 1.0, 0.8),  # white          
            fieldShape='circle',    # other option: sqr (square)           
            dotLife=15,             # in frames, Matthias hat hier 12 (30 in first wave)
            signalDots='same',      # signal dots are the same as on the previous frame (recommended)
            noiseDots='direction',  # location is other option which means: noise dots appear in random location on each frame. 
        )

        self.training_message = visual.TextStim(self.win, wrapWidth=30, pos=[0,3])

        # computing RT
        self.rt_clock = core.Clock()
        self.stim_onset_clock = core.Clock()

        self.circle = visual.Circle(self.win, radius=1.5, edges=32, fillColor='grey', lineColor='grey')

    def display_instructions(self): 
        instr = 'Welcome to this motion perception experiment!\nAs usual, use the arrow keys to indicate motion direction.\nThe voice will help you with this task!\nSpace key when ready'
        message1 = visual.TextStim(self.win, wrapWidth=30, pos=[0,0], text=instr)
        message1.draw()
        self.win.flip()
        event.waitKeys() # pause until there is a keypress

    def display_feedback(self, perc_correct, mean_hard_rt, correct_per_min):
        message2 = visual.TextStim(self.win, wrapWidth=30, pos=[0,8], text='Block feedback')
        message3 = visual.TextStim(self.win, wrapWidth=30, pos=[0,6], text='Percent correct: %.2f %%' % perc_correct)
        message4 = visual.TextStim(self.win, wrapWidth=30, pos=[0,4],
            text='Correct/min: %.2f' % correct_per_min)
        message5 = visual.TextStim(self.win, wrapWidth=30, pos=[0,2],
            text='Average response time in hard conditions: %.2f ms' % mean_hard_rt)
        message6 = visual.TextStim(self.win, wrapWidth=30, pos=[0,1], text='Space key to finish block')
        message2.draw()
        message3.draw()
        message4.draw()
        message5.draw()
        message6.draw()
        self.win.flip()
        event.waitKeys() #pause until there's a keypress

    def display_break(self):
        message1 = visual.TextStim(self.win, wrapWidth=30, pos=[0,2], text='Short break!')
        message2 = visual.TextStim(self.win, pos=[0,0],text='Press space key when ready')
        for f in range(self.break_duration_frames):
            message1.draw()
            self.win.flip() # this one seems to make trouble.
        message1.draw()
        message2.draw()
        self.win.flip()
        event.waitKeys()



         ####################################### T R I A L S #######################################
        
        ###########################################################################################
        
        ####################################### T R I A L S #######################################
        
    def runTrial(self, coherence, direction, cue_valid, training=False):
        # set direction and coherence, arguments passed over from run_task script
        self.dots.setDir(direction)
        self.dots.setFieldCoherence(coherence)

        valid = cue_valid

        # draw fixation
        for f in range(self.fixation_frames):
            self.fixation.draw()
            self.win.flip()

        n_dot_frames = 0      # counter for how many times the dots were refreshed before response
        extra_iti_frames=0    # extra frames for ITI to make trials all same length        
        event.clearEvents()   # clear any potential key strokes before starting
        allKeys=[]

        """ PLAY AUDITORY CUE """

        left = sound.Sound(value='left_en.wav', name='left') 
        right = sound.Sound(value='right_en.wav', name='right')
        
        if valid == 1: # the cue is valid
            if direction == 180: # LEFT
                onset_tone = core.getAbsTime()
                left.play()
                
            elif direction == 0: # RIGHT
                onset_tone = core.getAbsTime()
                right.play()
                
        elif valid == 0: # the cue is not valid
            if direction == 180:
                onset_tone = core.getAbsTime()
                right.play()
                
            elif direction == 0:
                onset_tone = core.getAbsTime()
                left.play()
                

        """ ----- """
        
        # jittered random waiting time between sound and rdk onset
        waitTime = random.uniform(0.75,1)
        core.wait(waitTime)    
        
        # DRAW THE DOT PATCHES
        onset_rdk= core.getAbsTime()               
        while len(allKeys) == 0 and n_dot_frames < self.max_dot_frames: 
            self.dots.draw() # draw stimulis
            self.circle.draw() # draw circle around fixation
            self.fixation.draw()
            self.win.flip()
            n_dot_frames+=1
        end_rdk = core.getAbsTime()   
            
       
        ##############  RESPONSE WINDOW ##############  
        self.fixation.draw()
        self.win.flip()
        core.wait(0.5) 
        # set some intial variables for the response window
        orientations = [270,90] #270: right, 90: left
        
        pos1, pos2 = random.sample(orientations, 2)

        img_up = visual.ImageStim(win=self.win,image="arrow.png",units="pix",
                               ori=pos1,pos=(0, 250))
        img_down = visual.ImageStim(win=self.win,image="arrow.png",units="pix",
                                ori=pos2,pos=(0, -250))
        border_up = visual.ShapeStim(self.win, vertices=img_up.verticesPix, units='pix',
                                  lineColor='black')
        border_down = visual.ShapeStim(self.win, vertices=img_down.verticesPix, units='pix',
                                   lineColor='black')
        """ This is if you want to use feedback"""
        """
        border_up_correct = visual.ShapeStim(self.win, vertices=img_up.verticesPix, units='pix',
                                             lineColor='limegreen')
        border_down_correct = visual.ShapeStim(self.win, vertices=img_down.verticesPix, units='pix',
                                               lineColor='limegreen')
        border_up_wrong = visual.ShapeStim(self.win, vertices=img_up.verticesPix, units='pix',
                                           lineColor='red')
        border_down_wrong = visual.ShapeStim(self.win, vertices=img_down.verticesPix, units='pix',
                                             lineColor='red')
        """

        # now present it on the screen
        img_up.setOri(pos1)
        img_down.setOri(pos2)

        self.rt_clock.reset() # reset RT clock before presentation of response win
        onset_responseWin = core.getAbsTime()
        while len(allKeys) == 0:
            messageA = visual.TextStim(self.win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
            messageA.draw()
            img_up.draw()
            self.fixation.draw()
            img_down.draw()
            event.clearEvents()
            self.fixation.draw()
            self.win.flip()
            
            # get response, make it time stamped
            allKeys=event.waitKeys(maxWait=3, keyList=['up','down','escape'], timeStamped=self.rt_clock)
            key_press = core.getAbsTime()
            
            if len(allKeys) > 0 == True: 
                rt=self.rt_clock.getTime()
                print('Response time: %.2f' % rt)
                print(allKeys)

        
        # feedback screen: highlight border colors of arrow image...
        messageA = visual.TextStim(self.win, wrapWidth=30, pos=[0,2], height=1, text='Direction?')
        if allKeys[0][0]=='up':
            # feedback
            #if direction==0 and img_up.ori==270.0 or direction==180 and img_up.ori==90.0:
            response_key = 0 #up_key
            event.clearEvents()
            border_up.autoDraw=True
            self.fixation.draw()
            img_up.draw()
            messageA.draw()
            self.win.flip()
            core.wait(0.5)
            self.fixation.draw()
            self.win.flip()
            response = allKeys[0][0]
            """ # feedback: 
            elif direction==0 and img_up.ori==90.0 or direction==180 and img_up.ori==270.0:
                event.clearEvents()
                self.fixation.draw()
                border_up_wrong.autoDraw=True
                img_up.draw()
                messageA.draw()
                self.win.flip()
                core.wait(0.5)
                self.fixation.draw()
                self.win.flip()
                response = allKeys[0][0]
            """

        elif allKeys[0][0] == 'down':
            #if direction==0 and img_down.ori==270.0 or direction==180 and img_down.ori==90.0:
            response_key = 1 #down_key
            event.clearEvents()
            self.fixation.draw()
            border_down.autoDraw=True
            img_down.draw()
            messageA.draw()
            self.win.flip()
            core.wait(0.5)
            self.fixation.draw()
            self.win.flip()
            response = allKeys[0][0]

            """ feedback:
             elif direction==0 and img_down.ori==90.0 or direction==180 and img_down.ori==270.0:
                self.fixation.draw()
                border_down_wrong.autoDraw=True
                img_down.draw()
                messageA.draw()
                self.win.flip()
                core.wait(0.5)
                self.fixation.draw()
                self.win.flip()
                response = allKeys[0][0]
            """

        # feedback
        #border_up_correct.autoDraw=False
        #border_down_correct.autoDraw=False
        #border_up_wrong.autoDraw=False
        #border_down_wrong.autoDraw=False
        border_up.autoDraw=False
        border_down.autoDraw=False
        
        self.fixation.draw()
        self.win.flip()

        # jittered random waittime between last response and onset of next auditory cue
        waittime = random.uniform(0.75,1)
        core.wait(waittime)
        
        # Categorize responses as correct or incorrect and then add them to stairHandler
        correct = 0 # if not updated in loop later, this stays zero (incorrect)
        

        if len(allKeys):
            # just in case there is no pyglet
            #if not self.wintype == 'pyglet':
            allKeys[0][1] = self.rt_clock.getTime()

            # unpack all keys takin the first press in the list
            thisKey=allKeys[0][0].upper()
            rt = allKeys[0][1]
            if thisKey == 'UP': 
                print(direction, thisKey, "img_up:", img_up.ori)
                if direction==0 and img_up.ori==270.0:
                    correct=1
                    print('CORRECT')
                elif direction==180 and img_up.ori==90.0:
                    correct=1
                    print('CORRECT')
            elif thisKey == 'DOWN':
                print(direction, thisKey, "img_right:", img_down.ori)
                if direction==0 and img_down.ori==270.0: 
                    correct=1
                    print('CORRECT')
                elif direction==180 and img_down.ori==90.0:
                    correct=1
                    print('CORRECT')
                # abort experiment
            elif thisKey in ['ESCAPE']:
                core.quit()
            if correct == 0:
                print('Categorized as INCORRECT')

                event.clearEvents()
             # Update number of ITI frames
            extra_iti_frames+=self.max_dot_frames-n_dot_frames

            # blank screen
            for i in range(self.min_iti_frames+extra_iti_frames):
                self.fixation.draw()
                self.win.flip()

            return correct, valid, onset_rdk, end_rdk, onset_tone, onset_responseWin, rt, response_key, key_press

    def quit(self):
        self.win.close()
        core.quit()   
