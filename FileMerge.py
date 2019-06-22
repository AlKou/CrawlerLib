#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:16:52 2018

Finished on Wed May 2 22:10:00 2018

@author: Al Kou

This script aims to merge the files of the same book downloaded by CrawlerLibDownload
"""
import os
from PyPDF2 import PdfFileReader,PdfFileWriter # "pip install PyPDF2" before using.

class pdfmerge():
    
    fsame = []
    pname = None
    fw = PdfFileWriter()
    fdir = '/users/al_gou/desktop/downfiles'

    def __init__(self):
        self

    def anylize(self): # Count files of the same book and output the result.
        flist = os.listdir(self.fdir)
        for i in range(len(flist)):
            flist[i] = flist[i][0:-6], flist[i][-6:-4], flist[i][-4:]
        
        fcount =  1   
        while len(flist) > 1:
            if flist[0][0] == flist[1][0]:
                fcount += 1
                flist.remove(flist[1])
            else:
                self.fsame.append((flist[0][0], fcount))
                print('{} files to be merged for {}'.format(fcount,flist[0][0]))
                flist.remove(flist[0])
                fcount = 1
        else:
            if flist[0][0] == self.fsame[-1][0]:
                print('{} files to be merged for {}'.format(fcount,flist[0][0]))
            else:
                self.fsame.append((flist[0][0], fcount))
                print('{} files to be merged for {}'.format(fcount,flist[0][0]))
       
      
    def name(self): # Firstly get the right file names for merging.
        for i in range(len(self.fsame)):
            pdfmerge.pname = self.fsame[i][0]
            self.fw = PdfFileWriter()# Writer can't be in the x loop, or it'll be cleared and only the last pdf will be processed correctly.
            if self.fsame[i][1] > 1:
                for x in range(self.fsame[i][1]):
                    if x < 9:
                        pdfmerge.fname = self.pname + '0' + str(x+1) +'.pdf'
                    else:
                        self.fname = self.pname + str(x+1) +'.pdf'
                    print('\n' + self.fname) 
                    pdfmerge.merge(self.fname) # Start to read and write pdf pages.
                print('----Successfully merged.----\n')
                
    def merge(self): # Merge files
        fr = PdfFileReader(open('/users/al_gou/desktop/downfiles/{}'.format(pdfmerge.fname),'rb'))
        pcount = fr.getNumPages()
        print('This doc has {} pages.\n'.format(pcount))
        for n in range(pcount):
            pdfmerge.fw.addPage(fr.getPage(n))
        pdfmerge.fw.write(open('/users/al_gou/desktop/downfiles/{}.pdf'.format(pdfmerge.pname),'wb'))

if __name__ == '__main__':
    Ex = pdfmerge()
    Ex.anylize()
    Ex.name()