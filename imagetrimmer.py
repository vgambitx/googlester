#-------------------------------------------------------------------------------
# Name:        imagetrimmer
# Purpose:
#
# Author:      vGamBIT
#
# Created:     10.01.2016
# Copyright:   (c) vGamBIT 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PIL import Image
import os, file_lister
def main():
    input_folder = 'google.com.ua'
    output_folder = 'trim_google.com.ua'
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    all_files = file_lister.file_lister(input_folder).get_files_list()
    for file in all_files:
        image = Image.open(file).convert('RGB')
        image.crop((250, 300, 760, 840)).save(output_folder + '/' + os.path.basename(file))


if __name__ == '__main__':
    main()
