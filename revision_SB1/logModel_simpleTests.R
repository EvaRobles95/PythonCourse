# basic tests of manipulations


# import lme4 module for mixed models
library(lme4)
library(emmeans)
library(MuMIn)
library(optimx)

# read data - auditory
data_aud <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp1_auditory//exp1_model1_auditory.csv")

# read data - visual
data_vis <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp2_visual//exp2_model1_visual.csv")

# TEST 1: CUE

patsy_cue_aud <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + target_z  + cue_z'

cue_aud <- glmer(patsy_cue_aud, data=data_aud, 
                    family=binomial('logit'), 
                    control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))



# save model in summary text file for later manip. in python
sink('cue_aud.txt')
print(summary(cue_aud))
sink()


# TEST 2: BLOCK

patsy_block_aud <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + target_z  + block_type_z * resp_1_z'

block_aud <- glmer(patsy_block_aud, data=data_aud, 
                   family=binomial('logit'), 
                   control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

sink('block_aud.txt')
print(summary(block_aud))
sink()

# TESTS ON VISUAL DATA
patsy_cue_vis <- 'response ~ (1|sbj_id) + (1|Block:sbj_id) + target_z  + cue_z'


cue_vis <- glmer(patsy_cue_vis, data=data_vis,
                    family=binomial('logit'),
                    control=glmerControl(optimizer='optimx', optCtrl = list(method='nlminb')))


# save model summary in text file
sink('cue_vis.txt')
print(summary(cue_vis))
sink()

# TEST block type on visual data

patsy_block_vis <- 'response ~ (1|sbj_id) + (1|Block:sbj_id) + target_z  + block_type_z * resp_1_z'

block_vis <- glmer(patsy_block_vis, data=data_vis, 
                   family=binomial('logit'), 
                   control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

sink('block_vis.txt')
print(summary(block_vis))
sink()
