import os, click
from colorama import init,Fore, Back, Style
from time import sleep

#function
def printController (file):
    nextLine = ""
    
    for line in file:

        sleep(0.1)
        if("@RequestMapping" in line):
            click.echo(Fore.YELLOW + Style.BRIGHT + line.strip(' \n') + Style.RESET_ALL)
            click.echo('{')

        elif("@GetMapping" in line):
            click.echo('\n'+Fore.YELLOW + Style.BRIGHT +'\t'+line.strip(' \n') + Style.RESET_ALL)
            nextLine = next(file)
            click.echo('\t'+nextLine.replace('public','').replace('{','').strip() + Style.RESET_ALL)
            
        elif("@PostMapping" in line):
            click.echo('\n'+Fore.YELLOW + Style.BRIGHT +'\t'+line.strip(' \n') + Style.RESET_ALL)
            nextLine = next(file)
            click.echo('\t'+nextLine.replace('public','').replace('{','').strip() + Style.RESET_ALL)
            
        elif("@RequestParam" in line):
            click.echo('\t'+Fore.YELLOW + Style.BRIGHT +'\t'+line.strip(' \n') + Style.RESET_ALL)


    click.echo('}')
    click.echo('-----------------------------------------------\n')

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
                click.echo(Style.BRIGHT)
                first=False
            click.echo(Fore.GREEN + filename.replace('.java','') + '\t ' + Style.BRIGHT + line.replace('public','').strip(' \n')+Style.RESET_ALL)
            grepFound = True
    return grepFound

#setup
@click.command()
@click.option('--name', default=None, help="Print controller")
@click.option('--l', is_flag=True, help="List all controllers")
@click.option('--grep', default=None, help="Print all lines containing string")
def cli(name, l, grep):
    click.echo("Rollin...")
    sleep(0.5)
    path = "controller"
    controllerFound = False
    grepFound = False
    fileCounter=1
    if name:
        click.echo("Searching for "+name+" controller")
        sleep(0.5)
    for filename in os.listdir(path):
        with open(path+'/'+filename) as file: 
            if l:
                click.echo(str(fileCounter)+ ' - ' +Fore.GREEN + Style.BRIGHT +  filename.replace('.java','').replace('Controller','')+Style.RESET_ALL+"Controller")
                fileCounter = fileCounter + 1
            elif grep is not None and name is not None:
                if(name in filename):
                    controllerFound = True
                    grepFound = printGrep(file, grep)
            elif grep is not None:
                if grepFound is False:
                    grepFound = printGrep(file, grep)
                else:
                    printGrep(file,grep)
                controllerFound=True
            else:
                if name is not None and name in filename:
                    controllerFound = True
                    click.echo(Style.BRIGHT + Fore.GREEN + filename)
                    printController(file)
    if controllerFound is False and name is not None:
        click.echo(Fore.RED + Style.BRIGHT+"Controller "+name+" not found")
    if grepFound is False and grep is True:
        click.echo(Fore.RED + Style.BRIGHT+"Grep "+grep+" not found")
