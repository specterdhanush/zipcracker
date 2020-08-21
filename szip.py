import zipfile
from tqdm import tqdm


def graphics():
    print('''\033[1;31;40m 
 |--------------------------------------------------------------------------|
 |--------------------------------------------------------------------------|
 |                                                                          |
 |                                                                          |
 |============  ||  ||^^^^^^^^    cc cc c                        ||   ((    |
 |        ===   ||  ||      ^^   cc                              ||  ((     |
 |      ===     ||  ||^^^^^^^^  cc         rrrrr  *aaaa*    cccc ||((       |
 |   ===        ||  ||           cc         rr    aa  aa   cc    ||  ((     |
 |===========   ||  ||            cc cc c  rr    *aaaa*aa   cccc ||    ((   |
 |--------------------------------------------------------------------------|
 |                                             Join this Discord :          |
 |                                             https://discord.gg/VVEPpU    |
 |--------------------------------------------------------------------------|
      ''')
graphics()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("impotent :\nkeep your zipfile and wordlist in this folder(zipcracker)")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
zip_file=input('\033[1;34;40m Enter the name of the zip_file : ')#taking input(zipfile)
print(' %%You have selected%% : '+zip_file)
print("=============================================")
print("==============================================")
wordlist=input('\033[1;34;40m Enter the name of the wordlist_file : ')#taking input(wordlist)
print(' %%You have selected%% : '+wordlist)
print("=============================================")
print("=============================================")
zip_file =zipfile.ZipFile(zip_file)
num_words = len(list(open(wordlist, "rb")))

print("\033[1;32;40m Total passwords in the wordlist :",'\033[1;37;40m',num_words)

print("=============================================")

print('\033[1;33;40mctrl+z => exit')
print("")
print("plz wait..")
print("")
with open(wordlist, "rb") as wordlist:

    for word in tqdm(wordlist,total=num_words,unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("\033[1;31;40m[$$Your_Password:] :",word.decode().strip())

            exit(0)
print("##Password not found,try with different wordlist##")