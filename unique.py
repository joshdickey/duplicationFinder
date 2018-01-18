#!/usr/bin/python

import sys
import re

def main():
    if len(sys.argv) != 3:
        print ('Usage: unique MASTERLIST INPUTLIST')
        exit (1)
    
    try:

        masterNames = {}
        master = []
        newUsers = []
        with open(sys.argv[1], 'r') as masterFile:
            print('-----')
            cnt = 0
            for line in masterFile:
                
                name = removeTabsNewLines(line)
                print('line {}: content: {}'.format(cnt,name))
                
                master.append(name)
                cnt += 1
            print('-----')  
        with open(sys.argv[2], 'r') as inputFile:
            cnt = 0
            for line2 in inputFile:
                         
                name2 = removeTabsNewLines(line2)
                print('line {}: content: {}'.format(cnt,name2))
                newUsers.append(name2)
                cnt += 1
            
        print()
        print('----List of names that need to be added to the master list----')
        
        #create new file containing only the uniqe names in list 2
        with open("C:\\Users\\jdickey\\Desktop\\itemsToAdd.txt", 'w') as myFile:
            for element in newUsers:
                if element not in master:
                    myFile.write(element + "\n")
                    print (element)
                    #print ((set(newUsers)-set(master)))
                         
        
    except Exception as e:
        print ('Error opening input file {}'.format(e))
        exit(1)

def removeTabsNewLines(name):
    newName = re.sub(r'^[ \t]+|[\t)+|[\n]', ' ', name)
    newName = newName.strip()
    return newName

if __name__ == '__main__':
    main()
