import numpy
import math
print("Enter the number of rows and columns of the matrix ")
r = int(input())
c = int(input())
lis=[]
l=[]
for i in range(c):
        print("Enter column vector ",i+1)
        lis = []
        for j in range(r):
                num = int(input())
                lis.append(num)
        l.append(lis)
print("A:")
print(numpy.transpose(l))
org = numpy.multiply(l,1) 
q = [l[0]]
z=[]
for i in range(1,len(l)):
	v=[]
	for w in range(len(l[0])):
		v.append(0)
	sum=0
	for j in range(i):
		p=[]
		for w in range(len(l[0])):
			p.append(0)
		k=numpy.dot(l[i],q[j])/numpy.dot(q[j],q[j])
		for t in range(len(q[j])):
			p[t]=q[j][t]*k
		v=numpy.add(v,p)
	v=numpy.subtract(l[i],v)
	q.append(v)
for i in range(len(q)):
	sum=0
	for h in range(len(q[i])):
		sum = q[i][h]**2+sum
	sum = sum**0.5
	for j in range(len(q[i])):
		q[i][j]/=sum
q = numpy.transpose(q)
org = numpy.transpose(org)
r = numpy.dot(numpy.transpose(q),org)
print("Q:")
print(q)
print("R:")
print(r)
