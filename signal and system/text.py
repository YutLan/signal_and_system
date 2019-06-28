import numpy as np
import copy
l=[]
l.append([1,-1,0,1,-1,0,-1,-1,0,1,1,0])
l.append([0,1,1,1,-1,-1,1,0,0,0,-1,-1])
l.append([0,0,0,0,1,1,-1,1,-1,1,-1,-1])
[1,-1,1,0,0,1,0,-1,1,-1,0,-1]

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

l=np.array(l)
IM=np.array(IM)
#print(IM)
#print(l)

#print(IM)
#print(l)
#print(l.transpose())
#print (np.dot(IM,l.transpose()))
def Check(l1,l2):
    print(l1)
    print("\n")

    print(l2)
   # flag=1
    for i in range(24):
        for ii in range(i+1,25):
            flag=1
            for iii in range(3):
                print (l2[i][iii],'\t',l2[ii][iii])
                if l2[i][iii]!=l2[ii][iii]:
                    flag=0
            print("\n")
            if flag==1:
                print('return 0')
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
        #   print(1)


print (Check(l.transpose(),np.dot(IM,l.transpose())))


O=[1,-1,1,0,0,1,0,-1,1,-1,0,-1]
print(Codelist)
for i in Codelist:
    flag1=0
    for ii in range(12):
        if i[ii]!=O[ii]:
            flag1=1
    if(flag1==0):
        print(i)
