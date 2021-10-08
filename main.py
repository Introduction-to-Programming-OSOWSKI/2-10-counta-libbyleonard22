#WRITE YOUR CODE IN THIS FILE

def countA(w):

    total = 0

    for i in range(0, len(w)):
        if w[i] == "a":
            return "a"

print(countA("armadillo"))