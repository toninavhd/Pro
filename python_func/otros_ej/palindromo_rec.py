def is_palindrome(text):
	text = text.lower().replace(' ', '')
	if len(text) < 2:
    	return True
	elif text[0] != text[-1]:
    	return False
	else:
    	return is_palindrome(text[1:-1])
