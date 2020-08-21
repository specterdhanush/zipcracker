import zipfile
from tqdm import tqdm


def graphics():
    print('''\033[1;31;40m  



   |---------------------------------------------------------------------------------------------|
   |---------------------------------------------------------------------------------------------|
   |                                                                                             |
   |                                                                                             |
   |   ==============  ||    ||^^^^^^^^        cc cc cc                               ||   ((    |
   |             ===   ||    ||      ^^       cc                                      ||  ((     |
   |           ===     ||    ||^^^^^^^^       cc           rrrrr   *aaaa*     cccc    ||((       |
   |        ===        ||    ||               cc           rr      aa  aa    cc       ||  ((     |
   |    ============   ||    ||                cc cc cc    rr      *aaaa*aa   cccc    ||    ((   |
   |                                                                                             |
   |                                                                                             |
   |---------------------------------------------------------------------------------------------|  
   |---------------------------------------------------------------------------------------------|author:@spectradhanush
                                                                                                 verson=V1.0
      ''')
graphics()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
zip=input('\033[1;34;40m Enter the name of the zip_file : ')
print(' %%You have selected%% : '+zip)
print("=============================================")
print("==============================================")
file=input('\033[1;34;40m Enter the name of the wordlist_file : ')
print(' %%You have selected%% : '+file)
print("=============================================")
print("=============================================")

wordlist = file
zip_file=zip

zip_file =zipfile.ZipFile(zip_file)
num_words = len(list(open(wordlist, "rb")))

print("\033[1;32;40m Total passwords in the wordlist :",'\033[1;37;40m',num_words)

print("=============================================")

print('\033[1;33;40mctrl+z => exit')
print("")
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist,total=num_words,unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
            print(word)
        except:
            continue
        else:
            print("\033[1;31;40m [$$ Password_found $$] :",word.decode().strip())

            exit(0)
print(" ##Password not found,try with different wordlist##")