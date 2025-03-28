a=int(input("입력할 수식을 계산하러면 1, 두 수 사이의 합을 구하려면 2를 눌러주세요:"))

if a==1:
    b=input("수식을 입력해주세요:")
    f=eval(b)
    print(b,"결과는",f,"입니다.")

elif a==2:
    c=int(input("첫번째 숫자 입력:"))
    d=int(input("두번째 숫자 입력:"))
    e=(c+d)*(d-c+1)/2
    print(c,"+...+",d,"는", e,"입니다.")
