"""
File: boggle.py
Name: Johnson
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program searches all vocabularies in boggle game for the letters input by user.
	"""
	start = time.time()
	####################
	num_row = 1
	all_letters = {}
	for i in range(4):
		row = input(f"{num_row} row of letters: ")
		row = row.split()
		for letter in row:
			if not letter.isalpha() or len(letter) > 1:
				print('Illegal input')
				return
		all_letters[num_row-1] = row
		num_row += 1
	if len(all_letters) == 4:
		boggle(all_letters)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(all_letters):
	dic = read_dictionary()
	total = [0]
	boggle_helper(all_letters, [], [], [], total, dic)
	print(f'There are {total[0]} words in total.')


def boggle_helper(all_letters, ans, all_ans, all_location, total, dic):
	"""
	all_letters: dic{int:lst}
	ans: lst[str]
	all_ans: lst[str]
	all_location: lst[lst[int]]
	total: lst[int]
	dic: set
	"""
	if ''.join(ans) in dic and ''.join(ans) not in all_ans:
		all_ans.append(''.join(ans))
		print(f'Found"{"".join(ans)}"')
		total[0] += 1
	if not has_prefix(''.join(ans), dic):
		pass
	else:
		for i in range(len(all_letters)):
			for j in range(len(all_letters[i])):
				# choose
				if [i, j] in all_location:
					continue
				if len(all_location) >= 1:
					if not all_location[-1][0]-1 <= i <= all_location[-1][0]+1:
						continue
					if not all_location[-1][1]-1 <= j <= all_location[-1][1]+1:
						continue
				ans.append(all_letters[i][j])
				all_location.append([i, j])
				# explore
				boggle_helper(all_letters, ans, all_ans, all_location, total, dic)
				# un-choose
				ans.pop()
				all_location.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python set
	"""
	with open(FILE, 'r') as f:
		dictionary = set()
		for line in f:
			vocabularies = line.split()
			for vocab in vocabularies:
				if len(vocab) >= 4:
					dictionary.add(vocab)
	return dictionary


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for vocab in dic:
		if vocab.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
