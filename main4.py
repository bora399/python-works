#Hackerrank Nested Lists solution

nameScore=[]
scores=[]
for _ in range(int(input("How many students do you want to write ? "))):
    name = input("What is the name of the student ? ")
    score = float(input("What is the student's score ? "))
    nameScore+=[[name,score]]
    scores+=[score]
b=sorted(list(set(scores)))[1] 
#print(sorted(list(set(scores))))
#print(b)
#print(sorted(nameScore))
for a,c in sorted(nameScore):
     if c==b:
            print(a)
