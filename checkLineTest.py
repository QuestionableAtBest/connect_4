list = ["X","X","X","X","X"]
list2 = ["O","X","X","X","O"]
list3 = ["O","X","X","X","X"]
list4 = ["O","X","O","X","O"]
list5 = ["X","-","X","X","O","-","X","-","-","O"]
list6 = ["X","O","X","X","O","O","O","O","-"]
list7 = ["-","-","-","-","X"]
def check_connect4_line(line):
    """
    This function takes a list of characters (or a string) as argument = a line of discs.
    If the line contains 4 identical elements, return this element (= winning disc).
    Otherwise, return False.
    """
    start = 0
    end = 0
    while end < len(line):
        end = start + 4
        window = line[start:end]
        disc = window[0]
        if window.count(disc) == 4:
            return disc
        start += 1
    return False
print(check_connect4_line(list))
print(check_connect4_line(list2))
print(check_connect4_line(list3))
print(check_connect4_line(list4))
print(check_connect4_line(list5))
print(check_connect4_line(list6))
print(check_connect4_line(list7))