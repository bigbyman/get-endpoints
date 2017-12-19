import os, argparse
from colorama import init,Fore, Back, Style
init()


#function
def printController (file):
    nextLine = ""
    
    for line in file:

        if("@RequestMapping" in line):
            print(Fore.YELLOW + Style.BRIGHT + line.strip(' \n') + Style.RESET_ALL)
            print('{')

        elif("@GetMapping" in line):
            print('\n'+Fore.YELLOW + Style.BRIGHT +'\t'+line.strip(' \n') + Style.RESET_ALL)
            nextLine = next(file)
            print('\t'+nextLine.replace('public','').replace('{','').strip() + Style.RESET_ALL)
            
        elif("@PostMapping" in line):
            print('\n'+Fore.YELLOW + Style.BRIGHT +'\t'+line.strip(' \n') + Style.RESET_ALL)
            nextLine = next(file)
            print('\t'+nextLine.replace('public','').replace('{','').strip() + Style.RESET_ALL)
            
        elif("@RequestParam" in line):
            print('\t'+Fore.YELLOW + Style.BRIGHT +'\t'+line.strip(' \n') + Style.RESET_ALL)


    print('}')
    print('-----------------------------------------------\n')

#function
def printGrep(file, grepString):
    grepFound = False
    first = True;
    for line in file:
        if grepString in line or grepString.lower() in line:
            
            if("import" in line):
                continue
            if("class" in line):
                continue
            if("return" in line):
                continue
            if("private" in line):
                continue
            if first is True:
                print(Style.BRIGHT)
                first=False
            print(Fore.GREEN + filename.replace('.java','') + '\t ' + Style.BRIGHT + line.replace('public','').strip(' \n')+Style.RESET_ALL)
            grepFound = True
    return grepFound

#setup
parser = argparse.ArgumentParser(description="Endpoints script")
parser.add_argument("--name", help="pick one controller")
parser.add_argument("--c", help="show all controllers", action='store_true')
parser.add_argument("--grep", help="print all lines containing string")
args, leftovers = parser.parse_known_args()

if args.name is not None:
    controllerName = (args.name)
else:
    controllerName = ""
    
path = '' #your path

controllerFound = False
grepFound = False
fileCounter=1
#script
for filename in os.listdir(path):
    with open(path+'/'+filename) as file:
        
        if args.c is True:
            print(str(fileCounter)+ ' - ' +Fore.GREEN + Style.BRIGHT +  filename.replace('.java','').replace('Controller','')+Style.RESET_ALL+"Controller")
            fileCounter = fileCounter + 1
        elif args.grep is not None and args.name is not None:
            if(args.name in filename):
                controllerFound = True
                grepFound = printGrep(file, args.grep)
        elif args.grep is not None:
            controllerName = ""
            if grepFound is False:
                grepFound = printGrep(file, args.grep)
            else:
                printGrep(file,args.grep)
            controllerFound=True
        else:
            if controllerName in filename:
                controllerFound = True
                print(Style.BRIGHT + Fore.GREEN + filename)
                printController(file)
                
if controllerFound is False and args.c is not True:
   print("Controller "+controllerName+" not found")
if grepFound is False and args.grep is True:
    print("Grep "+args.grep+" not found")

