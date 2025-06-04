def caesar(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

while(True):
	choice=int(input("Enter 1 if encrypt \n 2 if decrypt\n 3 for exit:"))
	if(choice==1 or choice==2 ):
		word=input("Enter the word:")
		shift=int(input("Enter the shift key:"))
		if(shift>=0 and shift <=26):
			if(choice==1):
				print(caesar(word, shift))
			elif(choice==2):
				print(caesar(word, shift,False))
		else:
			print("Enter a valid shift:")
	elif(choice==3):
		print("Good bye!")
		break	
	else:
		print("Enter a valid choice!!")
 

