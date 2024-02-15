def xor(r,s):
    if r+s==0 or r+s==2:
        return False
    elif r+s==1:
        return True
        
r=int(input())
s=int(input())
resultado=xor(r,s)
print(resultado)

