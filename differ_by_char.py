# differ_by_char
def main():
    pass
    n=input().split()
    k=list(n[0])
    j=list(n[1])
    l=int(n[2])
    flag=0
    for i in k:
        for o in j:
            if(i==o):
                pass
            elif(i!=o):
                flag+=1
        else:
            break
    if (flag==l):
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
