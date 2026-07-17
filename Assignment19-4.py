from functools import reduce
def filterx(No):
    return No%2==0
        
def mapx(No):
    return No*No

def reducex(No1,No2):
    return No1+No2

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