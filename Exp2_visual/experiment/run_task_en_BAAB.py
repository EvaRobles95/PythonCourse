# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:20:35 2021

@author: annae
"""

from psychopy import data, gui, core
from psychopy.data import TrialHandler
from task_en import RDMDTask
import random
from psychopy import sound, visual
import itertools
import numpy as np
import pdb #debugger


"""
BAABABBA DESIGN 
"""

dirs = (0,1)
cohs = (0,1,2,3,4,5)

# function to run one block. 
def run_block(fileName, expInfo, task, coherence_levels):
    # open datafile to write
    data_file = open(fileName + '.csv', 'w')
    # write headers
    data_file.write('Trial,Block,block_type,coherence,motionDirection,response,correct,cueValid,response_key,onset_rdk,end_rdk,onset_tone,onset_responseWin,rt,key_press\n')
    # create empty list for trials that is filled with coherence levels and trials later
    trial_list = []

    # number of trials
    ntrials = 96 # for testing, change this to 48. 
    # number of coherence levels
    ncoherences = len(coherence_levels)
    # repetitions per possible combination
    ncoh_per_dir = (ntrials/2) / 2 / ncoherences

    """some functions """
    
    ##########################################################################
    ## MAKE TRIAL LIST: repetitive condition
    ##########################################################################
    def make_repeatlist():
        while True:
            directions = np.hstack((np.random.randint(2), -np.ones((int(ntrials/2) - 1), int)))
            for t in range(1, int(ntrials/2)):
                if random.random() > 0.8:
                    directions[t] = 0 if directions[t - 1] == 1 else 1
                else:
                    directions[t] = directions[t - 1]
            if np.sum(directions == 0) == np.sum(directions == 1):
                break
        return directions

    ##########################################################################
    ## MAKE TRIAL LIST: neutral condition
    ##########################################################################
    def make_neutrallist():
        while True:
            directions = np.hstack((np.random.randint(2), -np.ones((int(ntrials/2) - 1), int)))
            for t in range(1, int(ntrials/2)):
                if random.random() > 0.5:
                    directions[t] = 0 if directions[t - 1] == 1 else 1
                else:
                    directions[t] = directions[t - 1]
            if np.sum(directions == 0) == np.sum(directions == 1):
                break
        return directions
    
    ##########################################################################
    ## Build TrialHandler Structure for psychopy task
    ## repetitive condition
    ##########################################################################   
    def build_rep_block(block_nr):
        
        directions_1 = make_repeatlist()
        directions_2 = make_repeatlist()
        directions = np.append(directions_1,directions_2)
        
        # make a vector for coherences
        coherences_1 = -np.ones(int(ntrials/2), int)
        coherences_2 = -np.ones(int(ntrials/2), int)
        
        # assign both directions the coherences randomly and repeat ncoh_per_dir times
        # first half of block
        coherences_1[directions_1 == 0] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        coherences_1[directions_1 == 1] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        # second half of block
        coherences_2[directions_2 == 0] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        coherences_2[directions_2 == 1] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        # stack it together    
        coherences = np.append(coherences_1,coherences_2)
        # random permutation of cue valid
        dirs = (0,1)
        cohs = (0,1,2,3,4,5)
        # init empty vectors for cuevalid
        cuevalid_1 = -np.ones(int(ntrials/2),int)
        cuevalid_2 = -np.ones(int(ntrials/2),int)
        # loop over directions and coherences to distribute the invalid cues evenly over half-blocks    
        for d in dirs:
            for c in cohs:
                cuevalid_1[(directions_1==d) & (coherences_1==c)] = np.random.permutation((0,1,1,1)) #(0,1) for testing, change these to 0.1
                cuevalid_2[(directions_2==d) & (coherences_2==c)] = np.random.permutation((0,1,1,1)) #(0,1) for testing, change these to 0.1
        
        # stack it together for the full block trialnumber
        cue_valid = np.append(cuevalid_1, cuevalid_2)
        # get the actual directions the visual.DotStim can work with 
        map_directions = {0: 0, 1: 180}
        # build the trial lists
        
        trial_list_repeat = [{'coherence': coherence_levels[coherences[t]], 'direction': map_directions[directions[t]], 'cue_valid': cue_valid[t]} for t in range(ntrials)]
        
        return TrialHandler(trial_list_repeat, 1, extraInfo=expInfo, method='sequential')
     
     
    ##########################################################################
    ## Build TrialHandler Structure for psychopy task
    ## neutral condition
    ##########################################################################
    def build_neut_block(block_nr): 
        
        dirs = (0,1)
        cohs = (0,1,2,3,4,5)
        # make direction vectors
        directions_3 = make_neutrallist()
        directions_4 = make_neutrallist()
        directions = np.append(directions_3, directions_4)
        # make a vector for coherences
        coherences_1 = -np.ones(int(ntrials/2), int)
        coherences_2 = -np.ones(int(ntrials/2), int)
        # assign both directions the coherences randomly
        # first half of block
        coherences_1[directions_3 == 0] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        coherences_1[directions_3 == 1] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        # second half of block
        coherences_2[directions_4 == 0] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        coherences_2[directions_4 == 1] = np.random.permutation(np.repeat(range(ncoherences), ncoh_per_dir))
        # stack it together    
        coherences = np.append(coherences_1,coherences_2)
        # random permutation of cue valid
        cuevalid_1 = -np.ones(int(ntrials/2),int)
        cuevalid_2 = -np.ones(int(ntrials/2),int)
        # loop over directions and coherences to distribute the invalid cues evenly over half-blocks    
        for d in dirs:
            for c in cohs:
                cuevalid_1[(directions_3==d) & (coherences_1==c)] = np.random.permutation((0,1)) #(0,1,1,1) CHENGA
                cuevalid_2[(directions_4==d) & (coherences_2==c)] = np.random.permutation((0,1)) #(0,1,1,1) CHANGE
    
        # stack it together for the full block trialnumber
        cue_valid = np.append(cuevalid_1, cuevalid_2)
        # get the actual directions the visual.DotStim can work with 
        map_directions = {0: 0, 1: 180}
        # build the trial lists
        trial_list_alternate = [{'coherence': coherence_levels[coherences[t]], 'direction': map_directions[directions[t]], 'cue_valid': cue_valid[t]} for t in range(ntrials)]
        # return complete trial handler object
        
        return TrialHandler(trial_list_alternate, 1, extraInfo=expInfo, method='sequential')
    
    # create all TrialHandler objects that we need   
    trial_handler_repeat_1 = build_rep_block(1)
    trial_handler_repeat_2 = build_rep_block(2)
    trial_handler_repeat_3 = build_rep_block(3)
    trial_handler_repeat_4 = build_rep_block(4)
    
    trial_handler_alternate_1 = build_neut_block(1)
    trial_handler_alternate_2 = build_neut_block(2)
    trial_handler_alternate_3 = build_neut_block(3)
    trial_handler_alternate_4 = build_neut_block(4)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #                               VISIBLE TRIALS BEGIN HERE                                           #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # STEP 1: instructions
    task.display_instructions()
    
    # clock for keeping track of trial timings
    task_clock = core.Clock()
    block_counter = 1
    
    def run_alternate_block(trial_handler_alternate, data_file):
        
        # set trial counters to zero
        total_correct=0
        trial_counter=0
        block_clock = core.Clock()
        
        try:
        
            for trial_idx,trial in enumerate(trial_handler_alternate):
                block = 0 #random
                trial_counter+=1
                # run trial
            
                try: 
                    correct, valid, onset_rdk, end_rdk, onset_tone, onset_responseWin, rt, response_key, key_press = task.runTrial(trial['coherence'], trial['direction'], trial['cue_valid'])
                except(TypeError):
                    # TypeError raised when maxWait for keypress was exceeded.
                    # you will find the following values in the datafile when sbj missed response. 
                    correct=99
                    rt = 99
                    response_key = 99
                    pass
                
    
                if trial['direction']==180:
                    response = trial['direction'] if correct==1 else 0
                elif trial['direction']==0:
                    response = trial['direction'] if correct==1 else 180
    
                trial_handler_alternate.addData('response', correct) 
                trial_handler_alternate.addData('rt', rt)
                data_file.write('%i,%i,%i,%.4f,%i,%i,%i,%i,%i,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f\n' % (trial_counter, block_counter, block, trial['coherence'], trial['direction'], response, correct, trial['cue_valid'], response_key, onset_rdk, end_rdk, onset_tone, onset_responseWin, rt, key_press))
    
                #update block stats
                total_correct+=correct
            
            
            trial_handler_alternate.saveAsPickle(fileName) # the .psydat file
            print('Experiment so far took %0.2f minutes.' % (task_clock.getTime()/60.0))
            print('This block took %0.2f minutes.' % (block_clock.getTime()/60.0))
    
        except:
            print('Whoops! Something went wrong!')
            trial_handler_alternate.saveAsPickle(fileName) # the .psydat file
            data_file.close()
            print('Data saved!\n')
            task.win.close()
    
        task.display_break()
        
        
    def run_repeat_block(trial_handler_repeat, data_file): 
        
        # set trial counters to zero
        total_correct=0
        trial_counter=0
        block_clock = core.Clock()
        
        try:
            for trial_idx, trial in enumerate(trial_handler_repeat):
                block = 1 # weighted
                trial_counter+=1
                try:
                    correct, valid, onset_rdk, end_rdk, onset_tone, onset_responseWin, rt, response_key, key_press = task.runTrial(trial['coherence'], trial['direction'], trial['cue_valid'])
                except (TypeError):
                    correct=99
                    rt = 99
                    response_key = 99
                    pass
    
                if trial['direction']==180:
                    response = trial['direction'] if correct==1 else 0
                elif trial['direction']==0:
                    response = trial['direction'] if correct==1 else 180
    
                trial_handler_repeat.addData('response', correct)
                trial_handler_repeat.addData('rt', rt)
                data_file.write('%i,%i,%i,%.4f,%i,%i,%i,%i,%i,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f\n' % (trial_counter, block_counter, block, trial['coherence'], trial['direction'], response, correct, trial['cue_valid'], response_key, onset_rdk, end_rdk, onset_tone, onset_responseWin, rt, key_press))
    
                total_correct += correct
    
    
            print('Experiment so far took %0.2f minutes' % (task_clock.getTime()/60.0))
            print('This block took %0.2f minutes.' % (block_clock.getTime()/60.0))
            trial_handler_repeat.saveAsPickle(fileName) 
    
        except:
            print('Whoops! Something went wrong!')
            data_file.close() # close and write csv file
            trial_handler_repeat.saveAsPickle(fileName)
            print('Data saved.\n')
            
            task.win.close()
    
        task.display_break()
        
        
    # ABBABAAB format, where A is alternate (neutral) and B is repetitive
    run_repeat_block(trial_handler_repeat_1, data_file=data_file) # B
    block_counter+=1
    print('# # # # # Block 1 (repetitive) done # # # # #')
    
    run_alternate_block(trial_handler_alternate_1, data_file=data_file) # A
    block_counter+=1
    print('# # # # # Block 2 (neutral) done # # # # #')
    
    run_alternate_block(trial_handler_alternate_2, data_file=data_file) # A
    block_counter+=1
    print('# # # # # Block 3 (neutral) done # # # # #')
    
    run_repeat_block(trial_handler_repeat_2, data_file=data_file) # B
    block_counter+=1
    print('# # # # # Block 4 (repetitive) done # # # # #')
    
    run_alternate_block(trial_handler_alternate_3, data_file=data_file) # A
    block_counter+=1
    print('# # # # # Block 5 (neutral) done # # # # #')
    
    run_repeat_block(trial_handler_repeat_3, data_file=data_file) # B
    block_counter += 1
    print('# # # # # Block 6 (repetitive) done # # # # #')
    
    run_repeat_block(trial_handler_repeat_4, data_file=data_file) # B
    block_counter += 1
    print('# # # # # Block 7 (repetitive) done # # # # #')
    
    run_alternate_block(trial_handler_alternate_4, data_file=data_file) # A
    block_counter+= 1 
    print('# # # # # Block 8 (neutral) done # # # # #')
    
    data_file.close()
    print('Data saved - Experiment done! Bravo')

    
if __name__ == "__main__":
    
    # INSERT Coherence values HERE # # # # #
    coherence_levels = [0.0005, 0.0162, 0.0315, 0.0792, 0.1991, 0.5 ]

    expInfo = {
        'subject': '',
        'dateStr': data.getDateStr(),
        'condition': ''}

    # dialoge
    dlg = gui.DlgFromDict(
        expInfo,
        title='RDMD',
        fixed=['dateStr'])

##################################  PARAMETERS  ######################################
    
    fixation_duration=200.0
    # Display dots for max of 1s
    max_dot_duration=950.0 
    # Min ITI of 1s
    min_iti_duration=500.0
    # break duration of 15s
    break_duration=15000.0
    
    task=RDMDTask(fixation_duration, max_dot_duration, min_iti_duration, break_duration)

    fileName = '%s.%s.' % (expInfo['subject'], expInfo['dateStr'] )
      
    run_block(fileName, expInfo, task, coherence_levels)

    task.quit()