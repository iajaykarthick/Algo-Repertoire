import sys


def print_neatly(S, words, j):
    i = S[j]
    if i > 0:
        print_neatly(S, words, i-1)
    print(" ".join(words[i: j+1]))
    

def per_line_cost(M, L, i, j):
    
    width_occupied = 0
    
    for k in range(i, j+1):
        width_occupied += L[k]
        
    width_occupied = width_occupied + j - i
    
    cost = (M - width_occupied)**3
    
    if cost < 0:
        return sys.maxsize
    
    elif j == (len(L) - 1): # if j is the nth word
        return 0
    
    else:
        return cost
    
def minimize_cost_to_print_neatly(words, M):
    L = [len(word) for word in words]
    
    n = len(L)
    
    C = [sys.maxsize for _ in range(n)]
    S = [i for i in range(n)]
        
    for j in range(n):
        for i in range(j+1):
            if i == 0:
                prev_lines_cost = 0
            else:
                prev_lines_cost = C[i-1]
            cost = prev_lines_cost + per_line_cost(M, L, i, j)
            if cost < C[j]:
                C[j] = cost
                S[j] = i

    print_neatly(S, words, n-1)
    return C[n-1]
    

sentence = """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32."""
words = sentence.split()


print(f'The minimum cost is {minimize_cost_to_print_neatly(words, 80)}')

