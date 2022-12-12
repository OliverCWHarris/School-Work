gapcount=0
previouscharspace=False
sentence=['g','o','o','d',' ',' ','t','o',' ','g','o']

for i in range(1,len(sentence)):
    if sentence[i]==" ":
        if previouscharspace==False:
            gapcount=gapcount+1
        previouscharspace=True
    else:
        previouscharspace=False
print(gapcount)