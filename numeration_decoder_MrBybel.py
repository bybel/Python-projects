#MrBybel's python numeration decoder
#06.09.2016

reponse = 'o'

def todecimal(starting_number, starting_base):
	#transform to a string to index it
	starting_result = 0
	starting_number_str = ''
	starting_number_str += str(starting_number)  #append each digit to the string
	starting_number_str = starting_number_str[::-1]  #reverse the string
	
	for i in range(0, len(starting_number_str)):
		starting_result += int(starting_number_str[i]) * pow(starting_base, i)
	print("      " + str(starting_result))
	print("          /          ")
	print("          \          ")
	print("          /          ")
	print("          \          ")
	print("          /          ")
	print("          \          ")
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
	
	
	
	
while True:
	if reponse == 'o' or 'O' or 'y' or 'Y':
		space_it_out = print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		binary_text = print("							01000010 01100001 01110011 01100101  01010100 01101111  01000010 01100001 01110011 01100101\n\n\n\n")
		print('''        BBBBBBBBBBBBBBBBB                                                                       tttt                                BBBBBBBBBBBBBBBBB                                                         
	B::::::::::::::::B                                                                   ttt:::t                                B::::::::::::::::B                                                        
	B::::::BBBBBB:::::B                                                                  t:::::t                                B::::::BBBBBB:::::B                                                       
	BB:::::B     B:::::B                                                                 t:::::t                                BB:::::B     B:::::B                                                      
	  B::::B     B:::::B  aaaaaaaaaaaaa      ssssssssss       eeeeeeeeeeee         ttttttt:::::ttttttt       ooooooooooo          B::::B     B:::::B  aaaaaaaaaaaaa      ssssssssss       eeeeeeeeeeee    
	  B::::B     B:::::B  a::::::::::::a   ss::::::::::s    ee::::::::::::ee       t:::::::::::::::::t     oo:::::::::::oo        B::::B     B:::::B  a::::::::::::a   ss::::::::::s    ee::::::::::::ee  
	  B::::BBBBBB:::::B   aaaaaaaaa:::::ass:::::::::::::s  e::::::eeeee:::::ee     t:::::::::::::::::t    o:::::::::::::::o       B::::BBBBBB:::::B   aaaaaaaaa:::::ass:::::::::::::s  e::::::eeeee:::::ee
	  B:::::::::::::BB             a::::as::::::ssss:::::se::::::e     e:::::e     tttttt:::::::tttttt    o:::::ooooo:::::o       B:::::::::::::BB             a::::as::::::ssss:::::se::::::e     e:::::e
	  B::::BBBBBB:::::B     aaaaaaa:::::a s:::::s  ssssss e:::::::eeeee::::::e           t:::::t          o::::o     o::::o       B::::BBBBBB:::::B     aaaaaaa:::::a s:::::s  ssssss e:::::::eeeee::::::e
	  B::::B     B:::::B  aa::::::::::::a   s::::::s      e:::::::::::::::::e            t:::::t          o::::o     o::::o       B::::B     B:::::B  aa::::::::::::a   s::::::s      e:::::::::::::::::e 
	  B::::B     B:::::B a::::aaaa::::::a      s::::::s   e::::::eeeeeeeeeee             t:::::t          o::::o     o::::o       B::::B     B:::::B a::::aaaa::::::a      s::::::s   e::::::eeeeeeeeeee  
	  B::::B     B:::::Ba::::a    a:::::assssss   s:::::s e:::::::e                      t:::::t    tttttto::::o     o::::o       B::::B     B:::::Ba::::a    a:::::assssss   s:::::s e:::::::e           
	BB:::::BBBBBB::::::Ba::::a    a:::::as:::::ssss::::::se::::::::e                     t::::::tttt:::::to:::::ooooo:::::o     BB:::::BBBBBB::::::Ba::::a    a:::::as:::::ssss::::::se::::::::e          
	B:::::::::::::::::B a:::::aaaa::::::as::::::::::::::s  e::::::::eeeeeeee             tt::::::::::::::to:::::::::::::::o     B:::::::::::::::::B a:::::aaaa::::::as::::::::::::::s  e::::::::eeeeeeee  
	B::::::::::::::::B   a::::::::::aa:::as:::::::::::ss    ee:::::::::::::e               tt:::::::::::tt oo:::::::::::oo      B::::::::::::::::B   a::::::::::aa:::as:::::::::::ss    ee:::::::::::::e  
	BBBBBBBBBBBBBBBBB     aaaaaaaaaa  aaaa sssssssssss        eeeeeeeeeeeeee                 ttttttttttt     ooooooooooo        BBBBBBBBBBBBBBBBB     aaaaaaaaaa  aaaa sssssssssss        eeeeeeeeeeeeee  ''')
		print("\n\n\n")
		print('''         ______           ______        _           _ 
	|  ___ \         (____  \      | |         | |
	| | _ | | ____    ____)  )_   _| | _   ____| |
	| || || |/ ___)  |  __  (| | | | || \ / _  ) |
	| || || | |      | |__)  ) |_| | |_) | (/ /| |
	|_||_||_|_|      |______/ \__  |____/ \____)_|
		                 (____/               \n''')
		welcome_text = input("				Welcome to MrBybel\'s numeration decoder! \n\n\n				Press ENTER to continue:   ")

		starting_number = input("				Please enter the starting number:  ")
		starting_base = int(input("				Please enter the starting base:  "))
		ending_base = int(input("				Please enter the end base:  "))

		fromdecimal(todecimal(starting_number, starting_base), ending_base)

		reponse = input("				Retry?:  ")
	else:
		exit()
