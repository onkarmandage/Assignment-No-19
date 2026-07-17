from functools import reduce
def filterx(No):
    return No>=70 and No<=90

def mapx(No):
    return No+10

def reducex(No1,No2):
    return No1*No2

def main():
    
    N=int(input("Enter the no of element: "))
    Data=[]
    print("Enter the element ")
    for i in range(N):
        Value=int(input())
        Data.append(Value)

    print("input number data is",Data)
    FData=list(filter(filterx,Data))
    print(FData)

    MData=list(map(mapx,FData))
    print(MData)

    RData=reduce(reducex,MData)
    print(RData)

if __name__=="__main__":
    main()