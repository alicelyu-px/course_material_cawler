import urllib.request
import os
import re

#TODO: course website to scrawl from
url = 'http://inst.eecs.berkeley.edu/~ee16a/fa18/'

#TODO: regex.. you know
file_name_p = r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')'

content=urllib.request.urlopen(url).read().decode('utf8')
# get all hrefs
all_files=re.findall(file_name_p, content)
#TODO: change the filter as needed
files_needed=list(filter(lambda name: len(name)<30 and ('.pdf' in name or '.ipynb' in name or '.zip' in name), all_files))
with open('file_names.txt', 'w') as f:
    for l in files_needed:
        f.write(url+l+'\n')

