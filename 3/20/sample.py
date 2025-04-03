a = 3
b = 5


#(1) 계산시 "//" 사용, "%" 사용한 예
print(b // a)
# => 1


print(b % a)
# => 2


#(2) round를 사용한 예
print(round(3.141592, 1))
# => 3.1


#(3) 계산 기호들의 우선순위가 들어가 사용된 예[(**) (-) (*,/,//,%) (+,-)를 모두 사용해서]
cal = (a**2 - 2 * b / 2) + -(b // 2 + a) - (b % a)
print(cal)
# => -3.0


#(4) " += " 또는 " *= " 이 들어간 예
an = 1
bn = 1
for i in range(1,11):
    an += i
    bn *= i
print(an,bn)
# => 56 3628800


#(5) 줄(line)이  넘어간 예, ( ) 와 W(\) 를 사용하여
print("Hello \nworld?")
# => Hello
#    world?

print(
    a +
    b +
    an +
    bn
)
# => 3628864


#(6) 나만의 함수를 하나 만드세요.
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
print(sigmoid(0))
# => 0.5


#(7) print 용법에서 "end =" 사용하여
end_t ="\n왜요?\n" 
print("A는 B야.",end=end_t)
print("A는 B니까.",end=end_t)
# =>  A는 B야.
#     왜요?
#     A는 B니까.
#     왜요?
