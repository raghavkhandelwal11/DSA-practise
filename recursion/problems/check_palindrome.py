
def check_palindrome(str, left=0, right=0):

    if left == 0 and right == 0: 
        right = len(str)-1;
    elif(left == right):
        return True;
    elif(left > right):
        return True;

    if str[left] == str[right]:
        return check_palindrome(str, left+1, right-1)
    else:
        return False;


print(check_palindrome('GenrneG'));