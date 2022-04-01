dict= {}
total=0
nOfData=0

while True:
    subject=str(input('Typing Subject(No subject = Just \'Enter\') : '))
    if len(subject) == 0:
        break
    score=int(input('%s\'s Score : ' % (subject)))
    print()
    if score >= 0:
        dict[subject] = score
        total=total+score
        nOfData=nOfData+1
    else:
        print('Type 0 or High')
        break

if len(dict) == 0:
    print('No data')
else:
    for printing in dict.keys():
        print('%s : %s' % (printing,dict[printing]))
    print()
    print('Average : %.2f' % (total/nOfData))