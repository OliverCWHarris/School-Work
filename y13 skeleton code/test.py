Score=5
#username=input('enter your name\n>')
with open('high score table.txt','r') as f:
    score_list=[]
    iterate=f.readlines
    for i in range (0,len(iterate)):
        line=f.readline
        line=line.strip('\n')
        score_list.append(line)
    print(score_list)
