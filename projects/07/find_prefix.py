''' A program that finds the longest common prefix of two strings.
October 25, 2016
Homework 7 Exercise 7.3
@author Ian Christensen (igc2) '''

# Create a function that receives two strings and returns the common prefix.
def common_prefix(string_one, string_two):
    ''' A function that compares two strings, determines the common prefix and returns the result. '''
    
    # Create necessary variables.
    prefix_results = ''
    character = 0
    
    # Begin while loop to compare strings.
    while character <= (len(string_one) - 1) and character <= (len(string_two) - 1):
        
        # Begin if statement to compare the characters of the two strings.
        if string_one[character] == string_two[character]:
            
            # Add appropriate values to the variables.
            prefix_results += string_one[character]
            character += 1
            
        # Once the prefix has been found exit the if statement.
        else:
            break
        
    # Return the results and exit the function.
    return prefix_results

# Create a function that runs tests on the function named common_prefix.
def test_common_prefix():
    ''' A function that calls common_prefix, tests the results, and prints a boolean expressions. '''
    assert(common_prefix('', '') == '')
    assert(common_prefix('abc123', '') == '')
    assert(common_prefix('abcDefg', 'abcdefg') == 'abc')
    assert(common_prefix('abcde5g', 'abcdefg') == 'abcde')
    assert(common_prefix('12345f7', '1234567') == '12345')
test_common_prefix()

# Create a user input for common_prefix.
print(common_prefix(input('Please enter first string: '), input('Please enter second string: ')))