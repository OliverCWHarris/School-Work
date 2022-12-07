filmfile=open('films.txt','r')
filmrec=filmfile.readline()
while filmrec != '':
    field=filmrec.split(',')
    id=field[0]
    title=field[1]
    rating=field[3]
    duration=field[4]
    genre=field[5]
    if rating=='G':
        print(id,title,rating,duration)
    filmrec=filmfile.readline()
filmfile.close()