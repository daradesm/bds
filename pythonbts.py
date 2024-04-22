print('(1)',5*"-","How many records are in the file?",15*'-')
f=open('D:\Python\dna2.fasta','r')
seqs={}
for line in f:
    line=line.rstrip()
    if line[0]=='>':
        fname=line.split()
        name=fname[0][1:]
        seqs[name]=''
    else:
        seqs[name]=seqs[name]+line
print(len(seqs))

print('(2)',5*"-"," What are the lengths of the sequences in the file?",15*'-')
lens={}
for i in seqs:
    lens[i]=len(seqs[i])
for i in lens:
    print(i, lens[i], sep=' - ')

print(5*"-","What is the longest sequence and what is the shortest sequence?",15*'-')
minimums=[]
maximums=[]
for i in lens:
    if lens[i]==min(lens.values()):
        minimums.append(i)
    elif lens[i]==max(lens.values()):
        maximums.append(i)
print('the shortest seq = ',min(lens.values()))
print('the longest seq = ',max(lens.values()))

print(5*"-","Is there more than one longest or shortest sequence?",15*'-')
print(5*"-","What are their identifiers?",15*'-')
print('There are %i of minimums:' % (len(minimums)),*minimums)
print('There are %i of maximums:' % (len(maximums)),*maximums)