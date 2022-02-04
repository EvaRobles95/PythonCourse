Note to self: maybe I have to change the datafile for the repprobs back. 
If not, the values need to be corrected in the paper. 

All code and data to reproduce analyses and figures of Choice History in Psychosis Proneness article. 

Data
Exp. 1	- contains all anonymised data for Experiment 1 (auditory task). 
	-  _raw folders contain raw, unprocessed data. 
	- exp1_clean_pmf contains data after exclusions for fitting psychometric functions. 
	- exp1_model1_auditory contains pre-processed data for fitting logistic choice model.

Exp. 2	- contains all anonymised data for Experiment 2 (visual task). 
	- _raw folders contains unprocessed data
	- separate datafiles for fitting pmf (exp2_clean_pmf.csv) and logistic model (exp2_model1_visual.csv). 

Separate .csv files are necessary for fitting the logistic choice model and psychometric functions, 
because psychometric functions require signed stimulus intensity which would falsify regression results. 


Code and analyses: 
	- pmf_repProb folders contain code to reproduce figures X and Y, psychometric function fit and repetition probability. 
	- pre-processing scripts can be found in pre-processing folder. 
	- Logistic model code in R can be found in the Logistic_Model folder. 