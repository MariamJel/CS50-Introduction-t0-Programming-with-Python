from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    f = sys.argv[2]
elif len(sys.argv) == 1:
    f = random.choice(fonts)
   
