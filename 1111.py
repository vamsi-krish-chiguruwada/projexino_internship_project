def howManySwaps(arr):
    a=arr
    swap=0
    if a==sorted(a):
        return(0)
    else:
        try:

            f=0
            r=0

            k=min(a)
            for i in range(len(a)):
                #print(i)
                if a[f]==k:
                    f+=1
                    k=min(a[1:])
                    r=f
                    #print("min on index incremented ",f)
                    #r+=1
                else:
                    for j in range(len(a)-1):
                        #print("j=",j)
                        if a[f]>a[r]:
                            #print("a[f]>a[r]",a[f],a[r],f,r)
                            #print(a,"before")
                            temp=a[f]
                            a[f]=a[r]
                            a[r]=temp

                            swap+=1
                            #print("after",a)
                        else:
                            r+=1
                            #print("r incrimented",r)
            if a==sorted(a):
                return(swap)
            else:
                return(swap+1)

        except:
            if a==sorted(a):
                return(swap)
            else:
                return(swap+1)
