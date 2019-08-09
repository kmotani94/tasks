def reverseAlternateChar(string, k, l): 
    i = 0
      
    while i < len(string): 
        if (i + k > l): 
            break
  
        temp = string[i:i + k]
        string = string[:i] + temp[::-1] + string[i + k:]

        i += 2 * k 
      
    return string; 

if __name__ == '__main__':
	string = input("Enter input string: ")
	print("Result:", reverseAlternateChar(string, 2, len(string))) 