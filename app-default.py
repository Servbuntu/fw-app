import os, sys
sys.argv.pop(0)
sys.argv.pop(0)
sys.argv.pop(0)
if(len(sys.argv) < 1):
    import help
    sys.exit(0)
ports = ""
for i in sys.argv:
    ports += i + " "
os.system("sudo ufw app default " + ports)