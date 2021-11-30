import os, sys
sys.argv.pop(0)
sys.argv.pop(0)
sys.argv.pop(0)
if(len(sys.argv) < 1):
    import help
    sys.exit(0)
os.system("sudo ufw default " + sys.argv[0])