Debugging

**Q. 다음 프로그램의 출력 결과는 무엇인가?**

```
a = 128; b = 2021

while b != 0:
    tmp = a % b
    a = b
    b = tmp

print(a)
```


Intuition
실행되는 순서에 따라 변수값이 어떻게 바뀌는 지를 따라가봅니다.


Algorithm
|  a  b  |
128  2021
2012 128
128  101
101  27
27   20
20   7
7    6
6    1
1    0


이 문제의 코드는, 사실 두 수의 최대공약수를 구하는 코드이기도 합니다. 이는 '유클리드 호제법' 이라는 이름으로 잘 알려져 있습니다. 
자세한 내용은 [여기] (https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95) 를 참고하세요.





파이썬 구현 방법 

1. 
def gcd(m,n):
	if m < n:
		m, n = n, m
	if n == 0:
		return m
    if m % n == 0:
		return n
	else:
		return gcd(n, m%n)

2. 
def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

3. 
def gcd(m,n):
    while n! = 0:
	    if m < n:
		    m, n = n, m
	    if n == 0:
		    return m
	    if m % n == 0:
		    return n

4.
def gcd(m,n):
    if n == 0:
        return m
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(m, n)
    else:
        return n


