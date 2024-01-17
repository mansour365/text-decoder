
"""
How this function works.
The file "decoder.py" and the text file "coding_qual_input.txt" need to be in the same directory.


The function accepts a text file as an argument in the form of a string.
It takes the string and converts it into a real file path using "Path" from the "pathlib" library.
Next, an empty dictionary is created in order to store the number-word pairs that span each line in the text file.
The "number" variable and "addVaraible" are initialized; they will be used to calculate the next number to search for in the dictionary.
A "finalString" variable is created. It will be used to return the final decoded string to the user.


The function opens the text file in read mode. It then goes through the file line by line. Each line is split into two parts.
The number portion and the word portion. These two portions are added as {key:value} pairs to the dictionary.


Once the full dictionary is created, we run a loop to check if the specific number we are searching for is found in the dictionary.
The number is searched as a dictionary key, and the returned value is the associated word.
The returned word is then appended to the finalString variable. Next, we increment the number to search for by adding "addvariable" to it.
AddVairable itself will also be incremented, since the pyramid gets wider the further we go down.
When the while loop cannot find the number as a key in the dictionary, we then know that we have found all the words in the decoded message.
The final string is then returned by the function.

"""

from pathlib import Path   #library to easily open file from a path


def decode(message_file):
    filePath = Path(__file__).with_name(message_file) #set the file path
    my_dictionary = {} #create an empty dictionary to store the number-word pairs
    number = 1   #current number to search for in the pyramid
    addVariable = 2   #variable used to increment the specific number to search for 
    finalString = ""  #final string returned to the user

    with filePath.open(mode='r') as file: #open file in read mode, "with statement" manages file stream
        for line in file: #loop through each line in txt file
            words = line.split(" ", 1) #split each line into seperate number and word
            key = words[0].strip() #number portion is the key
            value = words[1].strip() #word portion is the value
            my_dictionary[key] = value  #add the {"key":"value"} pair to the dictionary

        #Check dictionary using the calculated number as a key
        while (str(number) in my_dictionary): #check if key exists in dictionary
            returnedWord = my_dictionary[str(number)] #the key (number) returns a value (word)
            finalString = finalString +' '+returnedWord #append the returned word to final string
            number += addVariable #increment the number to search for
            addVariable += 1 #increment the increment variable
        
        return finalString #return final string to user

    
print( decode('coding_qual_input.txt') )