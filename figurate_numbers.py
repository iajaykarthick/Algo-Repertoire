def draw_art(starting_space, n):
    if starting_space == n:
        return
        
    draw_art(starting_space+1, n)
    space = " " * starting_space
    art = "1 " * (n - starting_space)
    print(f"{space}{art}")    

def Gnomon(size, start=1):
    if start > size:
        return

    Gnomon(size, start+1)
    i = size
    
    for _ in range(size):
        if i == start:
            print((str(i) + " ") * i, end="")
            break
        print(str(i) + " ", end="")
        i -= 1
    print()
        
            
Gnomon(20)
    
    
    
# draw_art(0, 50)


