class Car: #car를 만들기 위한 거푸집
    color="" 
    speed=0

    def upSpeed(self,value):
        self.speed+=value

    def downSpeed(self,value):
        self.speed-=value
    
myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0



myCar1.upSpeed(200)
if myCar1.speed>=150:
    myCar1.speed=150
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다."%(myCar1.color,myCar1.speed))

