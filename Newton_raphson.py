#!/usr/bin/env python
epsilon=0.001
h=0.00001
def p1(x):
	return (x-1)*(x-2)*(x-3)

def p2(x):
	return x**2-25
def newton_raphson(p):
	g=0
	while abs(p(g))>epsilon:
                p_prime_g=(p(g+h)-p(g))/h
		g=g-p(g)/p_prime_g
        return g

if __name__=='__main__':
	print('the root of (x-1)*(x-2)*(x-3) is ',newton_raphson(p1))
	print('the root of x**2-25=0 is ',newton_raphson(p2))
	
