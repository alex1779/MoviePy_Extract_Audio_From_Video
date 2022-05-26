# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:26:15 2022

@author: Ale
"""

import argparse
from moviepy.editor import VideoFileClip


parser = argparse.ArgumentParser(description='Extract Audio from Video File')
parser.add_argument('-i','--img_path', help='Please specify path for image', required=True)
parser.add_argument('-o','--output_path', help='Please specify path for output', required=True)
opt = parser.parse_args()
pathIn = opt.img_path
pathOut = opt.output_path

def main(pathIn, pathOut):
    video = VideoFileClip(pathIn) 
    video.audio.write_audiofile(pathOut)
    print('Audio File Extracted Succesfully.')
    
if __name__ == '__main__':
    
    main(pathIn, pathOut)

