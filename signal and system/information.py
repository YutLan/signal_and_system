import copy
import itertools
import numpy as np

#input matrix
IM=[[0,0,0,0,0,0,0,0,0,0,0,0]]
l2=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(l2)):
    l3=copy.deepcopy(l2)
    l4=copy.deepcopy(l2)
    l3[i]=-1
    l4[i]=1
    #print(l3)
    #print(l4)
    IM.append(l3)
    IM.append(l4)



#def Check(l1,l2):
    #print(l1)
   # print(l2)
   # flag=1
   # for i in range(12):
        #print(t(l[i][0]))
       # if int(l1[i][0])==0 and  int(l1[i][1])==0 and int(l1[i][2])==0:
       #     return 0

    #for i in range(11):
      #  for j in range(i+1,12):
         #   flag=1
            #print(l1[i],l1[j])
         #   for ii in range(3):
          #      if l1[i][ii]!=l1[j][ii]:
         #           flag=0
        #    if flag==1:
               # return 0
            #flag=1

    #for i in range(2,25,2):
        #for ii in range(3):
            #print(i)
           # print(l2[i-1][ii])
            #print(l2[i][ii])
            #print(l1[(int(i/2)-1)][ii])
            #print(ii)
         #   print(type(l2[i][ii]))
          #  print(type(l1[(int(i/2)-1)][ii]))
            #if l2[i][ii]==l1[(int(i/2)-1)][ii]:
                #print("true")
            #print(l1[i/2-1])
           # if l2[i-1][ii]==-l1[int(i/2-1)][ii] and l2[i][ii]==l1[int(i/2-1)][ii]:
               # print(1)
          #      continue
          #  else:
           #     return 0
   # return 1

def Check1(l1,l2):
   # print(l1)
    #print("\n")

   # print(l2)
   # flag=1
    for i in range(24):
        for ii in range(i+1,25):
            flag=1
            for iii in range(3):
              #  print (l2[i][iii],'\t',l2[ii][iii])
                if l2[i][iii]!=l2[ii][iii]:
                    flag=0
            #print("\n")
            if flag==1:
                #print('return 0')
                return 0

    #for i in range(11):
    #    for j in range(i+1,12):
     #       flag=1
            #print(l1[i],l1[j])
     ##       for ii in range(3):
      #          if l1[i][ii]!=l1[j][ii]:
      #              flag=0
    #        if flag==1:
     #           return 0
    #        flag=1


  #  for i in range(2,25,2):
   #     for ii in range(3):
            #print(i)
         #   print(l2[i-1][ii])
          #  print(l2[i][ii])
           # print(l1[(int(i/2)-1)][ii])
           # print(ii)
         #   print(type(l2[i][ii]))
          #  print(type(l1[(int(i/2)-1)][ii]))
           # if l2[i][ii]==l1[(int(i/2)-1)][ii]:
              #  print("true")
            #print(l1[i/2-1])
         #   if l2[i-1][ii]==-l1[int(i/2-1)][ii] and l2[i][ii]==l1[int(i/2-1)][ii]:
               # print(1)
         #       continue
         #   else:
         #       return 0
    return 1

l=[]
TT=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,13):
    l.append(i)
#tranformation matrix
TM=[[-1,-1,-1,-1,1,1,1,1,0,0,0,0]]
#print (TM())
#print (l)
count=0
Codelist=[]
for i  in list(itertools.combinations(l,4)):
   # print(list(i))
    #print(list(i))
    l2=copy.deepcopy(l)
    for ii in list(i):
        l2.remove(ii)

   # print(l2)
    for iii in list(itertools.combinations(l2,4)):
#        print(list(i))
#       print(list(iii))
#        print('\n')
        count+=1
        l3=copy.deepcopy(TT)
        for j in list(i):
            l3[j-1]=-1
        for jj in list(iii):
            l3[jj-1]=1
        Codelist.append(l3)




def check(Codelist,TM,IM):
    count=0
    count2=1000000
    count3=0
    myfile=open("result.txt","w")
    for i in Codelist:
        for ii in Codelist:
            TM1=copy.deepcopy(TM)
            TM1.append(i)
            TM1.append(ii)
        #print(TM1)
            TM1=np.array(TM1)
        ##print(TM1.transpose())
        #print(np.dot(IM,TM1.transpose()))
            count+=1

            if (Check1(TM1.transpose(),np.dot(IM,TM1.transpose())))==1:
                count3+=1
                myfile.write(str(count3)+" "+(str(TM1.transpose())))
                print(TM1.transpose())
                print(count)

            else:
                if count>count2:
                    count2*=2
                    print(str(count2)+" Error")
    print("result find "+str(count))

check(Codelist,TM,IM)

#print(count)
#print(Codelist)

#print (list(itertools.permutations(TM(),12)))

