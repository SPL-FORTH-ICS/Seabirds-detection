# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:04:10 2019
apply on whole audio recording. mono approach
is designed for multiclass (4 classes) and singlelabel experiments 
"""

import numpy as np
import librosa
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import tensorflow as tf
from trainable_yamnet import get_retrained_yamnet
# from feature_extraction_from_textgrid_Yamnet import define_idx_borders

from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

def define_idx_borders(Ns,params):
    idxBorders=[]
    Nframes=0
    startIdxs=np.arange(0,Ns,params['hopSize'],dtype=int)
    endIdxs=startIdxs+params['ftrSize']
    validBorders=np.argwhere(endIdxs<=Ns)
    Nframes=len(validBorders)
    idxBorders=np.zeros((Nframes,2),dtype=int)
    for n in range(Nframes):
        idxBorders[n,:]=[startIdxs[n],endIdxs[n]]
        
    if Nframes==0:
        print('Nframes=0 occured')

    return Nframes,idxBorders   

#%%
def create_timestamp(eventTime): 
    minutes,seconds=divmod(eventTime,60)  
    hours, minutes=divmod(minutes,60) 
    s=format(int(seconds), '02d')
    m=format(int(minutes), '02d')
    h=format(int(hours), '02d')
        
    return h,m,s   

#%%
def detect_from_wavfile_multilabel_Yamnet(modelPath, params, wavFilePath): #classification matrix removed
       
    frameIdx2time = float(1.0/params['Fs']) 
    detectedSegments={'scopoli':np.zeros((0,2)), 'yelkouan':np.zeros((0,2)), 'noise':np.zeros((0,2)), 'durationInSeconds':300.0}
   
    graph = tf.Graph()
    with graph.as_default():
        
        model = get_retrained_yamnet(modelPath, input_duration = 0.96, num_classes = params['Nclasses'], activation_layer = 'sigmoid')

    #%%    
        y, dum = librosa.load(wavFilePath, sr=params['Fs'], mono=False)
        Nd = np.ndim(y)
        Ns = np.max(np.shape(y))
        detectedSegments['durationInSeconds'] = Ns/params['Fs']
        Nframes,idxBorders=define_idx_borders(Ns,params)
        
        if Nd==2:
            predProbsL, predProbsR = infer_from_stereo(y, Nframes, idxBorders, detectedSegments,params, model)
        elif Nd==1:
            predProbsL, predProbsR = infer_from_mono(y, Nframes, idxBorders, detectedSegments,params, model)
        elif Nd>2:
            predProbsL, predProbsR = infer_from_mono(y[0,:], Nframes, idxBorders, detectedSegments,params, model)
#%%  exploit multilabel information
        
        for n in range(Nframes):
            scopoliDetected = (predProbsL[n,0]+predProbsR[n,0]>params['probThreshold'])
            yelkouanDetected = (predProbsL[n,1]+predProbsR[n,1]>params['probThreshold'])        
            
            if scopoliDetected:
                detectedSegments['scopoli']=np.vstack((detectedSegments['scopoli'], frameIdx2time*idxBorders[n,:]))

            if yelkouanDetected:
                detectedSegments['yelkouan']=np.vstack((detectedSegments['yelkouan'], frameIdx2time*idxBorders[n,:]))

            if not scopoliDetected and not yelkouanDetected:
                detectedSegments['noise']=np.vstack((detectedSegments['noise'], frameIdx2time*idxBorders[n,:]))  

#%%%%%%%%%%%%%%%%%%%%%%%%%                
        m=1             
        while m < np.shape(detectedSegments['scopoli'])[0]:
            if detectedSegments['scopoli'][m,0]<=detectedSegments['scopoli'][m-1,1]:
                detectedSegments['scopoli'][m-1,1]=detectedSegments['scopoli'][m,1]
                detectedSegments['scopoli']=np.delete(detectedSegments['scopoli'],m,axis=0)
            else:
                m+=1
    
        m=1             
        while m < np.shape(detectedSegments['yelkouan'])[0]:
            if detectedSegments['yelkouan'][m,0]<=detectedSegments['yelkouan'][m-1,1]:
                detectedSegments['yelkouan'][m-1,1]=detectedSegments['yelkouan'][m,1]
                detectedSegments['yelkouan']=np.delete(detectedSegments['yelkouan'],m,axis=0)
            else:
                m+=1
                
        m=1             
        while m < np.shape(detectedSegments['noise'])[0]:
            if detectedSegments['noise'][m,0]<=detectedSegments['noise'][m-1,1]:
                detectedSegments['noise'][m-1,1]=detectedSegments['noise'][m,1]
                detectedSegments['noise']=np.delete(detectedSegments['noise'],m,axis=0)
            else:
                m+=1            
        
    return detectedSegments
    
#%%
def infer_from_stereo(y, Nframes, idxBorders, detectedSegments, params, model):
    sIN0 = y[0,:]
    sIN0=sIN0-np.mean(sIN0)    
    sIN1 = y[1,:]
    sIN1=sIN1-np.mean(sIN1)            
    
    tempL = np.zeros((params['batchSize4inference'],params['ftrSize']))
    tempR = np.zeros((params['batchSize4inference'],params['ftrSize']))        
    predProbsL=np.zeros((0, params['Nclasses']),dtype=float)
    predProbsR=np.zeros((0, params['Nclasses']),dtype=float)        
    idx = 0

    for n in range(Nframes):

        temp0 = sIN0[idxBorders[n,0]:idxBorders[n,1]]    
        temp1 = sIN1[idxBorders[n,0]:idxBorders[n,1]]    
        if idx != params['batchSize4inference']:
            tempL[idx,:]= 10*temp0/np.linalg.norm(temp0)
            tempR[idx,:]= 10*temp1/np.linalg.norm(temp1)
            idx+=1
        else:
            predProbsL= np.append(predProbsL,0.5*model.predict(tempL),axis=0)
            predProbsR= np.append(predProbsR,0.5*model.predict(tempR),axis=0)
            tempL[0,:]= 10*temp0/np.linalg.norm(temp0)
            tempR[0,:]= 10*temp1/np.linalg.norm(temp1)
            idx=1
        
    NeventsLeft = Nframes - np.shape(predProbsL)[0]
    if NeventsLeft > 0:
        predProbsL= np.append(predProbsL,0.5*model.predict(tempL[:NeventsLeft,:]),axis=0)
        predProbsR= np.append(predProbsR,0.5*model.predict(tempR[:NeventsLeft,:]),axis=0)            
            
    return predProbsL, predProbsR
#%%
def infer_from_mono(sIN, Nframes, idxBorders, detectedSegments, params, model):
    sIN=sIN - np.mean(sIN)    

    tempL = np.zeros((params['batchSize4inference'],params['ftrSize']))
    predProbsL=np.zeros((0, params['Nclasses']),dtype=float)
    idx = 0

    for n in range(Nframes):

        temp0 = sIN[idxBorders[n,0]:idxBorders[n,1]]    
        if idx != params['batchSize4inference']:
            tempL[idx,:]= 10*temp0/np.linalg.norm(temp0)
            idx+=1
        else:
            predProbsL= np.append(predProbsL,model.predict(tempL),axis=0)
            tempL[0,:]= 10*temp0/np.linalg.norm(temp0)
            idx=1
        
    NeventsLeft = Nframes - np.shape(predProbsL)[0]
    if NeventsLeft > 0:
        predProbsL= np.append(predProbsL,model.predict(tempL[:NeventsLeft,:]),axis=0)
        predProbsR= np.zeros(np.shape(predProbsL))
            
    return predProbsL, predProbsR            