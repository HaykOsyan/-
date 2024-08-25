a = [i for i in range(2, 10)]

rows = [print(" ".join(f"{x} * {y} = {str(x*y)} \t"if  (x!=6 or y !=2)  else "\n" f"{x} * {y} = {str(x*y)} \t" for x in a[i:i+4])) for i in range(0, len(a), 4) for y in range(2, 11)]


    
