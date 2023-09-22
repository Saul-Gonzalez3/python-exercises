def is_two(char):
    if char in (2, '2', 2.0):
        return True
    else:
        return False
    
def is_vowel(somestring):
    #check that the arg is a str
    if type(somestring) == str:
        
        # if the str is 1 char and a letter
        if len(somestring) == 1 and somestring.isalpha():
            
            #return bool ans to: lower-letter in vowel list?
            return somestring.lower() in list('aeiou')
        
        #return false if string fails 1 alpha-char length
        else:
            return False
        
    # returns false if input is not a str    
    else:
        return False
    
def get_letter_grade(num):
    grade = ''
    if num in range(60):
        grade = "F"
    elif num in range(61,69):
        grade = "D"
    elif num in range(70,79):
        grade = "C"
    elif num in range(80,89):
        grade = "B"
    else:
        grade = "A"
    print(grade)
    

def is_consonant(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return (not is_vowel(somestring))
        else:
            return False
    else: 
        return False


def word(string):
    vowels = ["a", "e", "i", "o", "u"]
    if string[0] not in vowels:
        x = string.capitalize()
        print(x)
    else:
        return False
    
def calculate_tip(tip_percentage = float, bill_total = float):
    return tip_percentage * bill_total

    
def apply_discount(num, num2):
    o_price = num
    disc_perc = num2
    return (o_price - (o_price * disc_perc))



def handle_commas(fakenum):
    if type(fakenum) == str:
        stripfakenum = fakenum.replace(",", "")
        if stripfakenum.isdigit():
            return int(stripfakenum)
        else:
            return False
    else:
        False


def remove_vowels(string):
    a = []
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string:
        if letter not in vowels:
            a.append(letter)
    final_string = ''.join(a)
    return final_string


def normalize_name(somestring):
    # intialize an empty string called newstring
    newstring = ""
    
    # Iterate over each char in somestring after removing leading & trailing whitespace
    for letter in somestring.strip():
        
        # check if the char is alphanum or a space
        if letter.isalnum() or letter == " ":
            
            #if it is, append ch to the newstring
            newstring += letter
    # iterate over ea char in the newstring
    for letter in newstring:
        #check if the char is alphabetic
        if letter.isalpha():
            #if alpha char is found, exit the loop
            break
        else:
            #if the char is not alphanum, remove it from the beginning of the newstring
            newstring = newstring[1:]
            
    #convert the newstring to lowercase & replace any spaces with underscores
    #then return the mod newstring as the result
    return newstring.lower().replace(" ", "_")


def cumulative_sum(oldlist):
    newlist= []
    c_sum = 0
    for num in oldlist:
        c_sum += num
        #print(f"cumulative: {c_sum}")
        newlist.append(c_sum)
        #print(f"newlist: {newlist}")
    return newlist



from functions import calculate_tip
print(calculate_tip(.30, 29))






    


        
