##progrm to perform some useful operations on simple matrices##
import numpy as np
print("1.linalg.dot,returns dot product")
a=np.array([1,2,1,2])
b=np.array([1,2,1,2])
d=np.dot(a,b)
print("a=",a,"\n","b=",b,"\n","result=",d)
print("2.linalg.multi_dot,returns dot product of multiple arrays")
l=np.array([[1,2],[3,4]])
m=np.array([[1,2],[1,2]])
n=np.array([[1,2],[1,2]])
print("zero matrix with 3*3=",np.zeros([3,3]))
print("identity matrix with 3*3=",np.eye(3,3))
print("l=",l,"\n","m=",m,"\n","n=",n,"\n","result=",np.linalg.multi_dot([l,m,n]))
print("3.linalg.vdot,returns dot product")
print("a=",a,"\n","b=",b,"\n","result=",np.vdot(a,b))
print("4.numpy.matmul,returns multiplication of two matrices")
print("l=",l,"\n","m=",m,"\n","result=",np.matmul(l,m))
print("5.numpy.linalg.matrix_pow,returns some n power of a matrix")
print("power=",2)
print("l=",l,"\n","result=",np.linalg.matrix_power(l,2))
print("6.numpy.linalg.eig,returns eigen values and right eigen vectors of a square matrix")
print("l=",l,"\n","result=",np.linalg.eig(l))
print("7.numpy.linalg.eigh,returns the eigen values and eigen vectors of real symmetric matrix")
print("l=",l,"\n","result=",np.linalg.eigh(l))
print("8.numpy.linalg.eigvals,returns the eigen values of a general matrix")
print("l=",l,"\n","result=",np.linalg.eigvals(l))
print("9.numpy.linalg.eigvalsh,returns the eigen values of a real symmetric matrix")
print("l=",l,"\n","result=",np.linalg.eigvalsh(l))
print("10.numpy.linalg.det,returns the determinant of a matrix")
print("l=",l,"\n","result=",np.linalg.det(l))
print("11.numpy.linalg.slogdet,returns the sign and logarithm values of determinant of a matrix")
print("l=",l,"\n","result=",np.linalg.slogdet(l))
print("12.numpy.linalg.matrix_rank,returns the rank of a matrix")
print("l=",l,"\n","result=",np.linalg.matrix_rank(l))
print("13.numpy.trace,returns the diagonal elements sum of a matrix")
print("l=",l,"\n","result=",np.trace(l))
print("14.numpy.diag,returns the diagonal elements of a matrix in a new matrix")
print("l=",l,"\n","result=",np.diag(l))
print("15.numpy.diagonal,returns the diagonal elements in a matrix")
print("l=",l,"\n","result=",np.diagonal(l))
print("16.numpy.triu,returns the upper triangle of a matrix")
print("l=",l,"\n","result=",np.triu(l))
print("17.numpy.tril,returns the lower triangle of a matrix")
print("l=",l,"\n","result=",np.tril(l))
print("18.numpy.linalg.inv,returns the inverse of matrix")
print("l=",l,"\n","result=",np.linalg.inv(l))
print("19.numpy.linalg.solv,returns the leanear solutions matrix")
print("solve the two linear matrices")
s=np.array([2,3])
print("l=",l,"\n","s=",s,"\n","result=",np.linalg.solve(l,s))
print("20.cross product of vectors(2D matrix)")
print("l=",l,"\n","m=",m,"\n","result=",np.cross(l,m))
print("21.numpy.linalg.tensorsolve")
print("we use this for equations like AX=B where A,B are matrices,x is identity matrix")
print("operations on matrices")
print("1.addition")
print("a=",a,"\n","b=",b,"\n","result=",(a+b))
print("2.substraction")
print("a=",a,"\n","b=",b,"\n","result=",(a-b))
print("3.product")
print("a=",a,"\n","b=",b,"\n","result=",(a*b))
print("4.division")
print("a=",a,"\n","b=",b,"\n","result=",(a/b))
print("5.maximum in array")
print("a=",a,"\n","result=",np.max(a))
print("6.minimum in array")
print("a=",a,"\n","result=",np.min(a))
print("7.transpose")
print("l=",l,"\n","result=",np.transpose(l))
print("These are some useful operations on matrix only\n***Thank you****")

















