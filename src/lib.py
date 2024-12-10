
# -*- coding: utf-8 -*-
"""
Implementation of all required sub-routines for the Seabird GUI

@author psar
"""
import sys


params = {'Fs0':24000 , 'Fs':16000, 'durationInSeconds' : 0.96, 'ftrSize': 0, 'hopSize':0,  'Nclasses':3, 'probThreshold':1.0, 'batchSize4inference':64}
params['ftrSize'] = int(params['durationInSeconds']*params['Fs'])
params['hopSize']=int(params['Fs']*0.48 )

import pandas as pd

def produce_textgrid_file(detMtx,tgtfileName,exportParams):
    """
    Created on Tue Feb 14 13:13:42 2023
    algorithmic detections are used to produce a textgrid file that can be opened along with the new audio data
    @author: nstefana
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import tgt

    newtxt = tgt.core.TextGrid(filename='tgtfileName')
    scopolitier = tgt.core.IntervalTier(start_time = 0.0, end_time=detMtx['durationInSeconds'], name='scopoli')
    yelkouantier = tgt.core.IntervalTier(start_time = 0.0, end_time=detMtx['durationInSeconds'], name='yelkouan')
    
    for m in range(np.shape(detMtx['scopoli'])[0]): 
        scopolitier.add_annotation(tgt.core.Interval(detMtx['scopoli'][m,0], detMtx['scopoli'][m,1], text = 'b' ))
        
    for m in range(np.shape(detMtx['yelkouan'])[0]): 
        yelkouantier.add_annotation(tgt.core.Interval(detMtx['yelkouan'][m,0], detMtx['yelkouan'][m,1], text = 'b' ))
        
    newtxt.add_tier(scopolitier) 
    newtxt.add_tier(yelkouantier)
    path2saveTextgrid = (exportParams['pathToSaveTextgrids'] + '/' + tgtfileName + '.textgrid')
    tgt.io.write_to_file(newtxt, path2saveTextgrid)
    
    return


def load_wav_part(wavFileName, start, stop):
       import librosa       
       import numpy as np
       from parameters_Yamnet import params
       y, _ = librosa.load(wavFileName, sr=params['Fs0'], mono=False, \
                            offset = start, duration=stop-start)
       return y, params['Fs0'], start


def create_timestamp(eventTime): 
       minutes,seconds=divmod(eventTime,60)  
       hours, minutes=divmod(minutes,60) 
       
       s=format(int(seconds), '02d')
       m=format(int(minutes), '02d')
       h=format(int(hours), '02d')
              
       return h,m,s  
       
       
def save_wav_with_timestamp(y, sr, pathToSave, origWavFileName, timeOffset, normalize=True, suffix=''):
       import os
       import soundfile as sf
       import numpy as np
       
       hours,minutes,seconds=create_timestamp(timeOffset)
       wavTitleOnly = origWavFileName.split('\\')[-1].rstrip(".wav")   
       instanceName=(f"{pathToSave}\\{wavTitleOnly}_{hours}h{minutes}m{seconds}s{suffix}.wav")
       # print(instanceName)
       if normalize:
              y=y-np.mean(y,1)[:, np.newaxis]
              RMSin = np.sqrt(np.sum(y**2, 1)/y.shape[1])
              y = 0.05*y/RMSin[:, np.newaxis]
       sf.write(os.path.join(pathToSave,instanceName),y.T,params['Fs'])  
       return 
       
def save_multiple_segments_from_wav(array, sr, pathToSave, wavFileName, suffix=''):
       for (start, stop) in array:
              y, sr, start = load_wav_part(wavFileName, start, stop)
              save_wav_with_timestamp(y, sr, pathToSave, wavFileName, timeOffset=start, normalize=False, suffix='')
              
def detections_save_as_wav(detections_dict, pathToSave, wavFileName):
    for cl in detections_dict.keys():
        if cl not in ['scopoli', 'yelkouan', 'overlap']:
            continue
        suffix = '' #"_" + cl[0].upper()
        save_multiple_segments_from_wav(detections_dict[cl], params['Fs0'], f"{pathToSave}\\{cl.capitalize()}", wavFileName, suffix = suffix)
              
def detections_save_as_tgt_single(detections_dict, folderOUT, wavFilePath):
       exportParams = {'pathToSaveTextgrids': folderOUT.rstrip("\\")}
       wav_name = wavFilePath.split("\\")[-1].rstrip(".wav")
       produce_textgrid_file(detections_dict,wav_name,exportParams)
       return 

def detections_to_DF(detections, wavFilePath, df = pd.DataFrame()):
       for cl in detections.keys():
              if cl=='durationInSeconds': continue
              con2 = cl=='noise'
              con1 = detections[cl].ndim<2
              if con1 or con2: continue       
              to_append = pd.DataFrame(detections[cl], columns=["start", "stop"])
              to_append['class'] = cl.capitalize()
              wav_path_split = wavFilePath.split("\\")
              to_append['wavPath'], to_append['wavFile'] = ("\\").join(wav_path_split[:-1]), wav_path_split[-1]              
              # df = df.append(to_append, ignore_index=True)
              df = pd.concat([df, to_append], ignore_index=True)
              df=df.round(3)
       return df



def multi_Yamnet_new(params, wavFilePath, classificationMatrix, folderOUT, modelFolderPath, model, extract_wavs, extract_tgs):
       import sys, os

       os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
       try:
              from detect_from_wavfile_multilabel_Yamnet import detect_from_wavfile_multilabel_Yamnet
       except Exception as e:
              print("Error in importing necessary libraries. Check if all files are in place.':", err)
       print(u'\u2794 ' + f"Analyzing file {wavFilePath}...")
       try:
              modelFilePath = modelFolderPath.rstrip("/").rstrip("\\") + "\\" + model
              detections = detect_from_wavfile_multilabel_Yamnet(modelPath=modelFilePath, \
                     params=params, wavFilePath=wavFilePath)#, classificationMatrix=classificationMatrix)               
       except Exception as err:
              print("Error in function 'multi_Yamnet_new':", err)
       try:
              df = detections_to_DF(detections, wavFilePath)
       except Exception as err:
              print("Error in function 'df = detections_to_DF':", err)
       try:
              if extract_wavs:
                     detections_save_as_wav(detections, folderOUT, wavFilePath)
       except Exception as err:
              print("Error in function 'detections_save_as_wav':", err)

       try:
              if extract_tgs:
                     detections_save_as_tgt_single(detections, folderOUT, wavFilePath)
                     
       except Exception as err:
              print("Error in function 'detections_save_as_tgt':", err)
              
       wav_name = wavFilePath.split("\\")[-1].rstrip(".wav")
       df.to_csv(f'{folderOUT}\\detections\\{wav_name}.csv', index=False)
       print(u'\u2713 ' + f"Analysis of file {wavFilePath} has been completed.")
