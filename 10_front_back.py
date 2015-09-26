
# Given a string, return a new string where the first and last chars have been exchanged. 

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
	str_len = len(str)
	if str_len > 1:
		new_str = list(str)
		new_str[0] = str[str_len - 1]
		new_str[str_len - 1] = str[0]
		return "".join(new_str)
	else:
		return str

# sol 2

def front_back(str):
	if len(str) <= 1:
		return str

		mid = str[1:len(str)-1]  # can be written as str[1:-1]

	# last + mid + first
	return str[len(str)-1] + mid + str[0]