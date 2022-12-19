def do_op_for_numbers(operator, x, y):
    if(operator == '+'):
        return x + y
    elif(operator == '-'):
        return x - y
    elif(operator == 'x'):
        return x * y
    elif(operator == '/'):        
        try:
            return x / y
        
        except ZeroDivisionError:
            return 0
    elif(operator == '^'):
        return x**y
    else:
        return "wrong operator used"

def remove_from_list(my_list, indices):
    return ""

#Tests
# test for do_op_for_numbers: print(do_op_for_numbers('/', 5, 0))
    
