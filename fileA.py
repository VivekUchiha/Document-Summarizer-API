import re

def clean_Txt():  
    with open('c:/Users/arath/Desktop/Document-Summarizer-API/xxx.txt') as f:
       clean_cont = f.read().splitlines()
    shear=[i.replace('\xe2\x80\x9c','') for i in clean_cont ]
    shear=[i.replace('\xe2\x80\x9d','') for i in shear ]
    shear=[i.replace('\xe2\x80\x99s','') for i in shear ]
    shears = [x for x in shear if x != ' ']
    shearss = [x for x in shears if x != '']
    #print(shearss)
    dubby=[re.sub("[^a-zA-Z]+", " ", s) for s in shearss]
    print(dubby)
  

if __name__=='__main__': 
    clean_Txt()


