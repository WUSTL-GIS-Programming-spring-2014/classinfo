import numpy
a = numpy.array([1,2,3])
b = numpy.array([4,5,6])
print a+b, a-b, a*b, a/b
print a.min(), a.max(), b.min(), b.max()
print numpy.shape(a), numpy.shape(b)
c = numpy.append(a,b)
d = c.reshape(2,3)
print c, d
