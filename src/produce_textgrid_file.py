# -*- coding: utf-8 -*-



def produce_textgrid_file(detMtx,tgtfileName,exportParams):
    """
    Created on Tue Feb 14 13:13:42 2023
    algorithmic detections are used to produce a textgrid file that can be opened along with the new audio data
    @author: nstefana
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import tgt

    newtxt = tgt.core.TextGrid(filename=tgtfileName)
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