#MrBybel's python numeration decoder
#06.09.2016
space_it_out = print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
binary_text = print("01000010 01100001 01110011 01100101  01010100 01101111  01000010 01100001 01110011 01100101\n\n\n\n")
base_to_base_text = print('''  ____                   _          ____                 
 |  _ \                 | |        |  _ \                
 | |_) | __ _ ___  ___  | |_ ___   | |_) | __ _ ___  ___ 
 |  _ < / _` / __|/ _ \ | __/ _ \  |  _ < / _` / __|/ _ \
 | |_) | (_| \__ \  __/ | || (_) | | |_) | (_| \__ \  __/
 |____/ \__,_|___/\___|  \__\___/  |____/ \__,_|___/\___|
                                                         
														 
														 
														 
														 ''')
author_text = print('''  __  __        ____        _          _                                        _   _                   _                    _           
 |  \/  |      |  _ \      | |        | |                                      | | (_)                 | |                  | |          
 | \  / |_ __  | |_) |_   _| |__   ___| |  _ __  _   _ _ __ ___   ___ _ __ __ _| |_ _  ___  _ __     __| | ___  ___ ___   __| | ___ _ __ 
 | |\/| | '__| |  _ <| | | | '_ \ / _ \ | | '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __| |/ _ \| '_ \   / _` |/ _ \/ __/ _ \ / _` |/ _ \ '__|
 | |  | | |    | |_) | |_| | |_) |  __/ | | | | | |_| | | | | | |  __/ | | (_| | |_| | (_) | | | | | (_| |  __/ (_| (_) | (_| |  __/ |   
 |_|  |_|_|    |____/ \__, |_.__/ \___|_| |_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__|_|\___/|_| |_|  \__,_|\___|\___\___/ \__,_|\___|_|   
                       __/ |                                                                                                             
                      |___/                                                                                                              
					  
					  
					  
					  ''')
welcome_text = input("Welcome to MrBybel\'s numeration decoder! \n\n\n Press ENTER to continue:   ")

starting_number = input("Please enter the starting number:  ")
starting_base = int(input("Please enter the starting base:  "))
ending_base = int(input("Please enter the end base:  "))


def todecimal(starting_number, starting_base):
	#transform to a string to index it
	starting_result = 0
	starting_number_str = ''
	starting_number_str += str(starting_number)  #append each digit to the string
	starting_number_str = starting_number_str[::-1]  #reverse the string
	
	for i in range(0, len(starting_number_str)):
		starting_result += int(starting_number_str[i]) * pow(starting_base, i)
	print(starting_result)
	print("          /          ")
	print("          \          ")
	print("          /          ")
	print("          \          ")
	print("          /          ")
	print("          \          ")
	print("          /          ")
	return starting_result
	
	
def fromdecimal(starting_result, ending_base):
	ending_result = ''
	reversed_ending_result = ''
	quotient = starting_result
	while quotient != 0:
		reste = divmod(quotient, ending_base)[1]
		quotient = divmod(quotient, ending_base)[0]
		
		ending_result += str(reste)
		
	ending_result = ending_result[::-1]
	print("      " + ending_result)
	return ending_result
	
	
fromdecimal(todecimal(starting_number, starting_base), ending_base)