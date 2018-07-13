#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:26:08 2018

@author: Fenglu Xu
"""

# In[] read audio features 
import re
import pandas as pd 
def readAudioFeatures(filename,segments):
    features = []
    with open(filename, 'r') as content_file:
        for l in content_file:
            if "noname" not in l:
                continue
            l = l.replace('\n','')
            segments = segments.replace('.csv','')
            l = l.replace('noname',segments)
            features = l.split(',')
            #pd.to_numeric(features)
            #features = re.findall(r"[-+]?\d*\.\d+|\d+",l)
            print len(features)
    return features

def MoiveAudioFeatures(moive_segments_path,moive_segments_files):
    moiveAudioFeatures = []
    moive_segments_files.sort()
    for segments in moive_segments_files:
            # segments -> segment name
            segment_file = moive_segments_path+'/' + segments
            features = readAudioFeatures(segment_file,segments)
            print segments
            moiveAudioFeatures.append(features)
    return moiveAudioFeatures

# In[] read attributes names
def readAttributes(filename):
    attribute_name = []
    with open(filename, 'r') as content_file:
        for l in content_file:
            if "attribute" not in l:
                continue
            words = l.split(' ')
            attribute_name.append(words[1])
    return attribute_name
 
 # In[]
import os
os.chdir('/Users/xuecho/Desktop/multi/2018') 
fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir

audio_files_dir = fileDir + '/Part1-Audio_features/audio_features'
print audio_files_dir

moive_files = os.listdir(audio_files_dir) 

filename = audio_files_dir + '/MEDIAEVAL18_00/MEDIAEVAL18_00_00000.csv'
attribute_name = readAttributes(filename)
print len(attribute_name) #1584   
# In[]
moive_files.remove('.DS_Store') #run once
moive_files.sort()

for file in moive_files:
    # file -> moive name
    print file
    moive_segments_path = audio_files_dir + '/' + file
    moive_segments_files = os.listdir(moive_segments_path) 
    moive_segments_files.remove('.DS_Store') #run once
    movie_features = MoiveAudioFeatures(moive_segments_path,moive_segments_files)
    movie_features_df = pd.DataFrame(data = movie_features,columns=attribute_name)
    movie_features_df.to_csv(fileDir+'/audio_features/'+file+'.csv',index = False)   

            
            
            
    
    