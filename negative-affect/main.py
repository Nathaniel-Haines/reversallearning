from pain_regression_allsubjs import *

rlPain=RLPain()

rlPain.fMRI_dir='/Users/benjaminsmith/GDrive/joint-modeling/reversal-learning/behavioral-analysis/data/preprocessed'
rlPain.onset_dir='/Users/benjaminsmith/GDrive/joint-modeling/reversal-learning/behavioral-analysis/data/runfiles'
rlPain.decoder_file='/Users/benjaminsmith/GDrive/joint-modeling/reversal-learning/behavioral-analysis/data/pain_decoder.pkl'
rlPain.compile_pain_decoder()

sid=113
rid=1
nifti_file = rlPain.fMRI_dir + '/sub' + str(sid) + 'ReversalLearningPunishrun' + str(rid)
onset_file = rlPain.onset_dir + '/runfiledetail20170820T001729_s' + str(sid) + '_punishment_r' + str(
    rid) + '.txt'
#print(rlPain.get_trialtype_pain_regressors(nifti_file,onset_file))

rlPain.process_detailed_regressors()
#rlPain.process_detailed_regressors()
