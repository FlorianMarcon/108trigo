'''/*
** EPITECH PROJECT, 2017
** 103cypher
** File description:
** classe Matrix
*/'''

from math import sqrt
from copy import copy, deepcopy

class Square_Matrix:
	def __init__(self, size, argument):
		self.size = size
		self.argument = argument
		self.matrice = self.define_matrice(size)
		self.put_in_matrix(argument)
	def put_in_matrix(self, argu):
		i = 0
		a = 0
		for s in argu:
			self.matrice[a][i] = float(s)
			i = i + 1
			if i == self.size:
				i = 0
				a = a + 1
	def define_matrice(self, size):
		i = 0
		matrice = [0] * size
		while i != int(size):
			matrice[i] = [0] * int(size)
			i = i + 1
		return (matrice)

	def dup_matrice(self):
		matrix = Square_Matrix(self.size, self.argument)
		return (matrix)

	def define_matrice_identity(self):
		matrice = Square_Matrix(self.size, [0] * self.size)
		i = 0
		while i != matrice.size:
			matrice.matrice[i][i] = 1
			i = i + 1
		return (matrice)




	def inverse(self):
		r = -1
		j = 0
		tmp_matrice = self.dup_matrice()
		inverse_matrice = self.define_matrice_identity(self.size)
		while j != self.size:
			k = tmp_matrice.search_max(j)
			if tmp_matrice.matrice[k][j] != 0:
				r = r + 1
				tmp_matrice.normalisation(k, j)
				tmp_matrice.swap(k, r)
				tmp_matrice.simplification(r, j)
			j = j + 1
	def sub(self, r, i, j):
		cols = 0
		var = 0
		pivot = self.tmp_matrice[i][j]
		while cols != self.cols:
			var = self.tmp_matrice[r][cols] * pivot
			self.tmp_matrice[i][cols] = self.tmp_matrice[i][cols] - var
			var = self.inverse_matrice[r][cols] * pivot
			self.inverse_matrice[i][cols] = self.inverse_matrice[i][cols] - var
			cols = cols + 1
	def simplification(self, r, j):
		i = 0
		while i != self.size:
			if i != r:
				self.sub(r, i, j)
			i = i + 1
	def search_max(self, j):
		i = j
		var = i
		while i != self.size:
			if abs(self.tmp_matrice[i][j]) > abs(self.tmp_matrice[var][j]):
				var = i
			i = i + 1
		return (var)
	def normalisation(self, k, j):
		pivot = self.tmp_matrice[k][j]
		i = 0
		while i != self.cols:
			self.tmp_matrice[k][i] = self.tmp_matrice[k][i] / pivot
			self.inverse_matrice[k][i] = self.inverse_matrice[k][i] / pivot
			i = i + 1
	def swap(self, k, r):
		tmp = 0
		tmp2 = 0
		i = 0
		while i != self.cols:
			tmp = self.tmp_matrice[k][i]
			self.tmp_matrice[k][i] = self.tmp_matrice[r][i]
			self.tmp_matrice[r][i] = tmp
			tmp2 = self.inverse_matrice[k][i]
			self.inverse_matrice[k][i] = self.inverse_matrice[r][i]
			self.inverse_matrice[r][i] = tmp2
			i = i + 1



	def calcul(self, other, lines, cols):
		size = self.size
		i = 0
		somme = 0
		while i < size:
			somme = somme + (self.matrice[lines][i] * other.matrice[i][cols])
			i = i + 1
		return (somme)
	def multiplication_matrice(self, other):
		lines = 0
		cols = 0
		matrice = Square_Matrix(other.size, other.argument)
		while lines < matrice.size:
			cols = 0
			while cols < matrice.size:
				matrice.matrice[lines][cols] = self.calcul(other, lines, cols)
				cols = cols + 1
			lines = lines + 1
		return (matrice)
	def multiplication_float(self, other):
		lines = 0
		cols = 0
		matrice = Square_Matrix(self.size, self.argument)
		while lines < matrice.size:
			cols = 0
			while cols < matrice.size:
				matrice.matrice[lines][cols] = self.matrice[lines][cols] * other
				cols = cols + 1
			lines = lines + 1
		return (matrice)
	def __mul__(self, other):
		try:
			other == float(other)
		except:
			matrix = self.multiplication_matrice(other)
			return (matrix)
		matrix = self.multiplication_float(other)
		return (matrix)
	def __rmul__(self, other):
		try:
			other == float(other)
		except:
			return (self)
		matrix = self.multiplication_float(other)
		return (matrix)

	def __pow__(self, nb):
		i = 1
		if nb == 0:
			return (self.define_matrice_identity())
		matrix = self.dup_matrice()
		while i != nb:
			matrix = matrix * self
			i = i + 1
		return (matrix)

	def division_float(self, nb):
		lines = 0
		cols = 0
		matrice = self.dup_matrice()
		while lines < matrice.size:
			cols = 0
			while cols < matrice.size:
				matrice.matrice[lines][cols] = self.matrice[lines][cols] / nb
				cols = cols + 1
			lines = lines + 1
		return (matrice)

	def __truediv__(self, other):
		try:
			other == float(other)
		except:
			return (self)
		matrix = self.division_float(other)
		return (matrix)




	def addition_matrice(self, other):
		lines = 0
		cols = 0
		matrice = Square_Matrix(other.size, other.argument)
		while lines < matrice.size:
			cols = 0
			while cols < matrice.size:
				matrice.matrice[lines][cols] = self.matrice[lines][cols] + other.matrice[lines][cols]
				cols = cols + 1
			lines = lines + 1
		return (matrice)
	def addition_float(self, other):
		lines = 0
		cols = 0
		matrice = Square_Matrix(self.size, self.argument)
		while lines < self.size:
			cols = 0
			while cols < self.size:
				matrice.matrice[lines][cols] = self.matrice[lines][cols] + other
				cols = cols + 1
			lines = lines + 1
		return (matrice)
	def __add__(self, other):
		try:
			other == float(other)
		except:
			matrix = self.addition_matrice(other)
			return (matrix)
		matrix = self.addition_float(other)
		return (matrix)




	def substraction_matrice(self, other):
		lines = 0
		cols = 0
		matrice = self.define_matrice(self.size)
		matrice = Square_Matrix(other.size, other.argument)
		while lines < matrice.size:
			cols = 0
			while cols < matrice.size:
				matrice.matrice[lines][cols] = self.matrice[lines][cols] - self.matrice[lines][cols]
				cols = cols + 1
			lines = lines + 1
		return (matrice)
	def __sub__(self, other):
		try:
			other == float(other)
		except:
			matrix = self.substraction_matrice(other)
			return (matrix)
		matrix = self.substraction_float(other)
		return (matrix)
