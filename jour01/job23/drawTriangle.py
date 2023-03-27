def draw_triangle(h):
    for i in range(h-1):
        print(" " * (h - i - 1) + "/" + " " * (2*i) + "\\")
    print("/" + "_" * (h-1)*2 + "\\")

draw_triangle(10)
