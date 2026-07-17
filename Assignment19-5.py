from functools import reduce
def filterx(Num):
    if Num<=1:
        return False
      
    for i in range(2,Num):
        if (Num%i==0):
             return False
    return True
        
def mapx(No):
    return No*2

def reducex(No1,No2):
    return No1 if No1>No2 else No2

def main():
    
    N=int(input("Enter the no of element: "))
    Data=[]
    print("Enter the element ")
    for i in range(N):
        Value=int(input())
        Data.append(Value)

    print("input number data is",Data)
    FData=list(filter(filterx,Data))
    print("output of filter",FData)

    MData=list(map(mapx,FData))
    print("output of map",MData)

    RData=reduce(reducex,MData)
    print("output of reduce",RData)

if __name__=="__main__":
    main()