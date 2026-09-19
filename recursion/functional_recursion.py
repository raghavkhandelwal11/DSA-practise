#Sum of 1 to N [parametized]

def func1(sum, i, N):
    if i > N:
        print(sum);
        return;
    func1(sum+i, i+1, N);

func1(0, 1, 10);
