'''
 When a functionm calls itself then it is called recursion.
'''

def greet():
    print('raghav');
    # greet(); infinite recursion


greet();


'''
Stack overflow Error will occur when you try to run infinite recursion.
If ther are more than 987 (default) recursion calls than it is stack overflow in python.


'''

# print name four times


def func(count):
    if count == 4:
        return;
    print('Raghav');
    count = count + 1;
    func(count);

func(0);

'''
 Ther are two types of recursion, first is head recursion: when you do the job first and then call function again.

 tail recursion is when you call the function first and then do the job.
'''
