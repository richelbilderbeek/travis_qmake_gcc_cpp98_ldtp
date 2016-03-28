import ldtp, ooldtp
from ldtp import *
from ooldtp import *
from time import sleep
from subprocess import call
from subprocess import os

#os.system("xterm -hold -e './travis_qmake_gcc_cpp98_ldtp' &")

print 'Opening application'

stream = os.popen("xterm -hold -e './travis_qmake_gcc_cpp98_ldtp' &")

print 'Obtaining frm'

#frm = ooldtp.context('travis_qmake_gcc*')
#print 'Wait for GUI to exists'
#frm.waittillguiexist()
sleep(1)

print 'Enter text'

enterstring('travis_qmake_gcc*', 'Hello world<enter>', 'Go!')
enterstring('travis_qmake_gcc*', 'Hello world<enter>')
enterstring('Hello world<enter>')
pastetext('Hello world<enter>')

print 'Break'
generatekeyevent('<ctrl>C')

print 'Done'
