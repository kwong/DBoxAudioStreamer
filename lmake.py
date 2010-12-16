# lmake.py v0.1
# Generates playlist to be parsed by web media player 

import os
from ID3 import *

mp3files = filter(lambda x: x.endswith('.mp3'), os.listdir("./"))
chunk = ''

for file in mp3files:
    id3info = ID3("./"+file)
    title = id3info.artist + " - " + id3info.title
    if (title == " - "): title = file
    chunk += """
    <track>
        <location>%s</location>
        <info>%s</info>
    </track>""" % ("./"+file, title)

full_dump = """<?xml version="1.0"?>
<playlist>%s
</playlist>""" % chunk

outfile = open("./playlist.txt","w")
outfile.write(full_dump)
outfile.close()
raw_input("\n\nCompleted! Press \'Enter\' to continue.")







