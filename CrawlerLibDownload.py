#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 23:02:04 2018

@author: Al Kou
"""

from urllib import request,parse
import re
# Input key word, fill the form, submit and obtain the result list.
url = 'http://www.wul.waseda.ac.jp/kotenseki/search.php'
post = parse.urlencode({'cndbn':input('請輸入檢索詞：'),'szlmt':'500'})
post = post.encode("utf-8")

res = request.urlopen(url,post)
con = res.read()
con = con.decode('utf-8')

# Open the result URL one by one to detail page and find the link directing to download page
htre = re.findall(r'http://www.wul.waseda.ac.jp/kotenseki/html/.{1,50}index.html',con)
for i in range(len(htre)):
  addr = request.urlopen(htre[i])
  addr_read = addr.read().decode('utf-8')
  addr_con = re.findall(r'http://archive.wul.waseda.ac.jp.{1,90}/',addr_read)
  
  # Obtain the title of the book for downloading
  fname = re.findall(r'<TITLE>\n.{1,100}\n</TITLE>', addr_read)[0].split('\n')[1].split()[0].split('.')[0]
  print(fname)
  
  # Open the pdf download page link, open it and find the pdf download link 
  req_dpage = request.urlopen(addr_con[0])
  dpage_read = req_dpage.read().decode('SHIFT_JIS')
  dpage_con = re.findall(r'href=.{1,50}\.pdf',dpage_read)
  for x in range(len(dpage_con)):
      print(len(dpage_con[x:]))
      dcon_par = dpage_con[x].split('/')[-1]
      if '"' in dcon_par:
        dcon_par = dpage_con[x].split('"')[-1]
      dcon_split = dcon_par.split('_')
      dcon_split[-1] = dcon_split[-1].split('.')[-2]
      # print(dcon_par)
      # print(dcon_split)
      
      # Re-construct download url
      if len(dcon_split) == 3:
        rurl = dcon_split[0] + '/' + dcon_split[0] +  '_' + dcon_split[1] + '/'  + dcon_split[0] + '_' +  dcon_split[1] + '_' +  dcon_split[2] + '/'  + dcon_split[0] + '_' +  dcon_split[1] + '_' +  dcon_split[2] + '.pdf'
      elif len(dcon_split) == 2:
        rurl = dcon_split[0] + '/' + dcon_split[0] + '_' +  dcon_split[1] + '/' + dcon_split[0] + '_' +  dcon_split[1] + '.pdf'
      else:
        pass       
      durl = 'http://archive.wul.waseda.ac.jp/kosho/'+ rurl
      print(durl)
      print('\nDownloading...')
      # Download file
      f = request.urlopen(durl)
      fread = f.read()
      fdown = open('/users/al_gou/desktop/Downfiles/{}{}.pdf'.format(fname,dcon_split[-1][-2:]),'wb')
      fdown.write(fread)
  print('\nDownload completed!\n-------------')