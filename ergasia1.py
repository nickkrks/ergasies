def sumIntervals(a):

   
    akra=[]
     
    for i in range(len(a)):
       
        akra.append(a[i][0])
        akra.append(a[i][-1])

    akra.sort()


   
    eswterika=[]
    k=-1

    for i in range(len(a)):
        k= k+1
        for j in range(a[k][0]+1,a[k][-1]):            
                eswterika.append(j)


                
    a=set(akra)
    e=set(eswterika)
    
    a.difference_update(e)
    akr=list(a)


    print(eswterika)
    print(akra)
    s=0
    for i in range(0,len(akr)-1,2):

        s=akr[i+1]-akr[i]+s


    print("Το άθροισμα του μήκους των διαστημάτων είναι :",s)
    
