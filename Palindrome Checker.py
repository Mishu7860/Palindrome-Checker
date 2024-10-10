def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for uniformity
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
input_string = input("Enter a word or phrase: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
