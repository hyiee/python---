a=int(input("2,8,10,16 진수를 선택하세요:"))
b=input("값을 입력하세요:")
if a==2:
    c=int(b,2)
if a==8:
    c=int(b,8)
if a==10:
    c=int(b,10)
if a==16:
    c=int(b,16)

print("2진수:",bin(c))
print("8진수:",oct(c))
print("10진수:",c)
print("16진수:",hex(c))