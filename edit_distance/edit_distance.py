# -*- coding: utf-8 -*-
from __future__ import division
import time
start = time.time
class arithmetic():
	
	def __init__(self):
		pass
	def levenshtein(self,first,second):
		if len(first) > len(second):
			first,second = second,first
		if len(first) == 0:
			return len(second)
		if len(second) == 0:
			return len(first)
		first_length = len(first) + 1
		second_length = len(second) + 1
		distance_matrix = [range(second_length) for x in range(first_length)] 
		#print distance_matrix
		for i in range(0,first_length):
			for j in range(0,second_length):
				deletion = distance_matrix[i-1][j] + 1
				insertion = distance_matrix[i][j-1] + 1
				substitution = distance_matrix[i-1][j-1]
				if first[i-1] != second[j-1]:
					substitution += 1
				distance_matrix[i][j] = min(insertion,deletion,substitution)
		if(len(first)>len(second)):
			max_length = len(first)
		else:
			max_length = len(second)

		print "所得矩阵为："
		for y in range(1,first_length):
			for x in range(1,second_length):
				print distance_matrix[y][x],
				print ' ',
			print
		sim = 1- distance_matrix[first_length-1][second_length-1]/max_length
		print "相似度为："
		print sim
		print distance_matrix[first_length-1][second_length-1]

		#return distance_matrix[first_length-1][second_length-1]
	
if __name__ == "__main__":
	arith = arithmetic()
	s1 = "abcd"
	s2 = "abcef"
	a = str(open('1.txt','r').read())
	b = str(open('2.txt','r').read())
	arith.levenshtein(s1,s2)
	
