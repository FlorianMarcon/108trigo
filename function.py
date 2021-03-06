from matrix import *

iteration = 70

def factorielle(nb):
	a = 1
	while nb != 0:
		a = a * nb
		nb = nb - 1
	return (a)

def cosinus(matrix):
	i = 0
	tmp = Square_Matrix(matrix.size, [0] * matrix.size)
	while i != iteration:
		tmp = tmp + (pow(-1, i) * (matrix ** (2 * i)) / factorielle(2 * i))
		i = i + 1
	return (tmp)

def cosinus_hyperbolique(matrix):
	i = 0
	tmp = Square_Matrix(matrix.size, [0] * matrix.size)
	while i != iteration:
		tmp = tmp + ((matrix ** (2 * i)) / factorielle(2 * i))
		i = i + 1
	return (tmp)

def sinus(matrix):
	i = 0
	tmp = Square_Matrix(matrix.size, [0] * matrix.size)
	while i != iteration:
		tmp = tmp + (pow(-1, i) * (matrix ** ((2 * i) + 1)) / factorielle((2 * i) + 1))
		i = i + 1
	return (tmp)

def sinus_hyperbolique(matrix):
	i = 0
	tmp = Square_Matrix(matrix.size, [0] * matrix.size)
	while i != iteration:
		tmp = tmp + ((matrix ** ((2 * i) + 1)) / factorielle((2 * i) + 1))
		i = i + 1
	return (tmp)

def exponentielle (matrix):
	i = 0
	tmp = Square_Matrix(matrix.size, [0] * matrix.size)
	while i != iteration:
		tmp = tmp + ((matrix ** i) / factorielle(i))
		i = i + 1
	return (tmp)
