#the vowel counter

phrase = input("input your phrase:  ")

a = 'a'
A = 'A'
e = 'e'
E = 'E'
i = 'i'
I = 'I'
o = 'o'
O = 'O'
u = 'u'
U = 'U'
y = 'y'
Y = 'Y'

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
y_count = 0


def count_them():
    if a or A in phrase:
        global a_count += 1

    if e or E in phrase:
        global e_count += 1

    if i or I in phrase:
        global i_count += 1

    if o or O in phrase:
        global o_count += 1

    if u or U in phrase:
        global u_count += 1

    if y or Y in phrase:
        global y_count += 1


    print("There is \n %d X a \n %d X e \n %d X d \n %d X o \n %d X d \n %d X y" % \
          {a_count, e_count, i_count, o_count, u_count, y_count})


count_them()
