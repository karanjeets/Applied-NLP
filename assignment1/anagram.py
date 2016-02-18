import sys

# This will contain all anagrams of the string
anagrams = []

# Swaps the character 'x' with 'y' in string 'value'
def swap(value, x, y):
	tmp = value[x]
	value[x] = value[y]
	value[y] = tmp
	return value


# Computes the anagram recursively using Divide and Conquer
def compute_anagram(value, low, high):
	if low == high:
		anagrams.append(''.join(value))

	else:
		for i in xrange(low, high):
			value = swap(value, low, i)
			compute_anagram(value, low + 1, high)
			value = swap(value, low, i)


# This is where it all begins
def main():
	
	# Reading string from the argument
	value = sys.argv[1]
	
	# Computing Anagrams
	compute_anagram(list(value), 0, len(value))
	
	# Sorting anagrams
	anagrams.sort()

	# Writing anagrams to file
	with open('anagram_out.txt', 'w') as ftxt:
		for i in range(0, len(anagrams)):
			ftxt.write(anagrams[i] + "\n")


if __name__ == "__main__":
	main()
	#print >>sys.stderr, "\nIncorrect number of arguments. Aborting"