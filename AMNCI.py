# AMNCI value is calculated by assuming (a,b) and (b,a) as same and counting them only once in calculation phase
from collections import defaultdict as dd
method_names=[]
count=dd(int)
#Calculates AMNCI values 
def calculate_amnci(method_names):          
    for i in method_names:
        count[i]+=1
    amnci=0
    
    for j in set(method_names):
        amnci+=(count[j]*(count[j]-1))/2
    return (1-(amnci/len(method_names)))
        
#Removes numerical suffix from string
def remove_numsuffix(temp):
    index=len(temp)-1
    while index>=0 and not temp[index].isalpha():
        index-=1
    temp=temp[:index+1]
    return temp
#Finds Cannonical Form of String 
def cannonical(temp):
    temp=temp.replace("_",'')
    temp=remove_numsuffix(temp)
    temp=temp.upper()
    return temp
#checks if character is operator or not
def is_operator(x):
    if x=='=' or x=='-' or x==':' or x=='/' or x=='*' or x=='%' or x=='.' or x=='^' or x=='&' or x=='|':
        return True
    return False

def process(line):
    is_fun=False        #Variable maintained to check that given variable is function or not
    if '(' in line:
        open_para=line.index('(')
        if ')' in line:
            closed_para=line.index(')')
        else:           #If there is no closed parenthesis then it's not function
            return
        index=closed_para+1
        if index==len(line):
            line+=';'
        while line[index]==' ':     #In c++ closed parenthesis should be followed by ; or {
            index+=1
        if line[index]==';' or line[index]=='{':
            is_fun=True
    else:               #If there is no open parenthesis then it's not function
        return
    if not is_fun:
        return 
    name=''
    index=open_para-1
    while line[index]!=' ' and index>=0 and not is_operator(line[index]):       #If it's function then extract method name from that line
        name+=line[index]
        index-=1
    method_names.append(name[::-1])
    return

input_file=input("Enter Input File Name if any\n")
print()
try:
    f=open(input_file,'r')
except:
    print("##Opening Default Input File##")
    f=open("input.cpp",'r')
program=f.read()
program=program.replace('\n','')
program_lines=program.split(';')
for line in program_lines:
    process(line)
method_names=list(set(method_names))
for i in range(0,len(method_names)):
    temp=method_names[i]
    temp=cannonical(temp)
    method_names[i]=temp
AMNCI=calculate_amnci(method_names)
print("API Method Name Confusion Index is: ")
print(AMNCI)
f.close()
