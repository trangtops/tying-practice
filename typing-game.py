import argparse
import csv
import msvcrt 
#from colorama import init, Fore
import subprocess
#init(autoreset=True)
subprocess.call('', shell=True)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to vocab txt file")
ap.add_argument("-n", "--number", default=5, help="number of words per line")
ap.add_argument("-l", "--length", default=20, help="total number of words")
ap.add_argument("-s", "--start", default=0, help="word number to start")
args = vars(ap.parse_args())
N_WORDS = int(args["number"])
LENGTH = int(args["length"])
START = int(args["start"])

kanji = []
hiragana = []
meaning = []
with open(args['input'], mode='r', encoding="UTF-8", errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for word in csv_reader:
        kanji.append(word[0])
        hiragana.append(word[1])
        meaning.append(word[2])


for i in range(START, START+LENGTH):
    output = hiragana[i] + ' ' + kanji[i] + ' ' + meaning[i]
    print('                                                                           ', end='\r')
    print(output)
    print('                                                                           ', end='\r')
    #print(Fore.GREEN, end='')
    input()
    print('\033[3F')

    #a = msvcrt.getch()