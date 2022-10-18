state = 'y'
#hexadecimal code reference dictionary key-int: value-str
code = {0:'0',
            1:'1',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9',
            10:'A',
            11:'B',
            12:'C',
            13:'D',
            14:'E',
            15:'F'
            }
#hexadecimal decode reference dictionary key-str: value-int
decode = {'0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15
            }




#Title and coversion menu
def title():
    print("\n\nRadix converter")
    print("===============\n")
    print("+-------------------------------------------------+")
    print("|Conversion menu:                                 |")
    print("|                                                 |")
    print("|Binary(2)  Octal(8)  Decimal(10)  Hexadecimal(16)|")
    print("|                                                 |")
    print("|     (10) => (2), (10) => (8), (10) => (16)      |")
    print("|                                                 |")
    print("|     (2) => (10), (2) => (8), (2) => (16)        |")
    print("|                                                 |")
    print("|     (8) => (2), (8) => (10), (8) => (16)        |")
    print("|                                                 |")
    print("|     (16) => (2), (16) => (8), (16) => (10)      |")
    print("|                                                 |")
    print("+-------------------------------------------------+\n\n")


#Displaying step-by-step
def showsteps():
    print("\n")
    s1="______"
    s2="_______"

    for i in range(len(x)):
        print(to_base,"|",x[i],"=>",y[i])
    

#Function to convert decimal to binary
def decimal_to_binary(n):

    rem=[]
    bin = ''
    while n !=0:
        x.append(n)
        y.append(n%2)
        rem.append(n%2)
        n = int(n/2)
    for i in range(len(rem)):
        bin = bin+str(rem.pop(-1))
    return bin


#Function to convert decimal to octal
def decimal_to_octal(n):

    rem=[]
    oct = ''
    while n !=0:
        x.append(n)
        y.append(n%8)
        rem.append(n%8)
        n = int(n/8)
    for i in range(len(rem)):
        oct = oct+str(rem.pop(-1))
    return oct


#Function to convert decimal to hexadecimal
def decimal_to_hex(n):

    rem=[]
    hex = ''
    while n!=0:
        x.append(n)
        y.append(n%16)
        h_code = code.get(n%16)
        rem.append(h_code)
        n = int(n/16)
    for i in range(len(rem)):
        hex = hex+str(rem.pop(-1))
    return hex


#Function to convert binary to decimal
def binary_to_decimal(bin):

    d = []
    decimal = 0
    a = -1
    for i in range(len(bin)):
        d.append(decode.get(bin[a]))
        decimal = (d[i]*(2**i))+decimal
        a-=1
    return decimal


#Function to convert octal to decimal
def octal_to_decimal(oct):

    o = []
    decimal = 0
    a = -1
    for i in range(len(oct)):
        o.append(decode.get(oct[a]))
        decimal = (o[i]*(8**i))+decimal
        a-=1
    return decimal


#Function to convert hexadecimal to decimal
def hex_to_decimal(hex):

    h = []
    decimal = 0
    a = -1
    for i in range(len(hex)):
        h.append(decode.get(hex[a]))
        decimal = (h[i]*(16**i))+decimal
        a-=1
    return decimal


title()


while state=='y' or state=='Y':

    x=[]
    y=[]





    #Inputing number base type
    base = eval(input("Enter the radix/base of the Number to be converted :"))

    #numerical input for decimal input and string input for binary, octal and hexadecimal inputs
    if base == 10:
        
        num = eval(input("Enter the Number to be converted: "))
    else:
        
        num = input("Enter the Number to be converted: ")

    #Required output base type
    to_base = eval(input("Enter the radix/base to be converted into : "))





    #Checking wheather input base is of binary, if true then checking for output base type
    if base==2:

        if to_base==2:
            print("{} (binary) = {} (binary)".format(num,num))

        elif to_base==10:
            #conversion from input binary to decimal output
            print("{} (binary) = {} (decimal)".format(num,binary_to_decimal(num)))

        elif to_base==8:
            #conversion from input binary to decimal then decimal to octal output
            output=decimal_to_octal(binary_to_decimal(num))
            print("{} (binary) = {} (octal)".format(num,output))

        elif to_base==16:
            #conversion from input binary to decimal then decimal to hexadecimal
            output=decimal_to_hex(binary_to_decimal(num))
            print("{} (binary) = {} (hexadecimal)".format(num,output))

        else:
            #invalid conversion type for to_base variable value other than, 2,10,8 or 16
            print("Invalid conversion!!!")


    #Checking wheather input base is of decimal, if true then checking for output base type
    elif base==10:

        if to_base==2:
            #conversion from input decimal to binary output
            output = decimal_to_binary(num)
            print("{} (decimal) = {} (binary)".format(num,output))

        elif to_base==10:
            print("{} (decimal) = {} (decimal)".format(num,num))

        elif to_base==8:
            #conversion from input decimal to octal output
            output = decimal_to_octal(num)
            print("{} (decimal) = {} (octal)".format(num,output))

        elif to_base==16:
            #conversion from input decimal to hexadecimal output
            output = decimal_to_hex(num)
            print("{} (decimal) = {} (hexadecimal)".format(num,output))

        else:
            #invalid conversion type for to_base variable value other than, 2,10,8 or 16
            print("Invalid conversion!!!")
        
        step=input("Do you want to see steps? (y/n)\n")
        
        if step=='y' or step=='Y':
            showsteps()


    #Checking wheather input base is of octal, if true then checking for output base type
    elif base==8:

        if to_base==2:
            #conversion from input octal to decimal then decimal to binary
            output = decimal_to_binary(octal_to_decimal(num))
            print("{} (octal) = {} (binary)".format(num,output))

        elif to_base==10:
            #conversion from input octal to decimal output
            output = octal_to_decimal(num)
            print("{} (octal) = {} (decimal)".format(num,output))

        elif to_base==8:
            print("{} (octal) = {} (octal)".format(num,num))

        elif to_base==16:
            #conversion from input octal to decimal then decimal to hexadecimal
            output = decimal_to_hex(octal_to_decimal(num))
            print("{} (octal) = {} (hexadecimal)".format(num,output))

        else:
            #invalid conversion type for to_base variable value other than, 2,10,8 or 16
            print("Invalid conversion!!!")


    #Checking wheather input base is of hexadecimal, if true then checking for output base type
    elif base==16:

        if to_base==2:
            #conversion from input hexadecimal to decimal then decimal to binary
            output = decimal_to_binary(hex_to_decimal(num))
            print("{} (hexadecimal) = {} (binary)".format(num,output))

        elif to_base==10:
            #conversion from input hexadecimal to decimal output
            output = hex_to_decimal(num)
            print("{} (hexadecimal) = {} (decimal)".format(num,output))

        elif to_base==8:
            #conversion from input hexadecimal to decimal then decimal to octal
            output = decimal_to_octal(hex_to_decimal(num))
            print("{} (hexadecimal) = {} (octal)".format(num,output))

        elif to_base==16:
            print("{} (hexadecimal) = {} (hexadecimal)".format(num,num))

        else:
            #invalid conversion type for to_base variable value other than, 2,10,8 or 16
            print("Invalid conversion!!!")


    #If input base type is none of binary,ocatal,decimal or hexadecimal then invalid base type message
    else:
        print("Invalid base type!!!")
    
    
    state = input("\n\nDo you want to use the converter again? (y/n)\n")

print("Thank you for using the program")

