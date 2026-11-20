import math

def print_level_summary(n: int):
    level = 0
    subproblems = 1
    current_size = n
    total_accumulated_work = 0

    while current_size >= 1:
        total_work = int(current_size * subproblems)
        total_accumulated_work += total_work
       
        if level == 0:
            size_str = f"{current_size}"
        else:
            prev_size = current_size * 2
            size_str = f"{prev_size}/2 = {current_size}"
        print(
            f"level : {level:<2} | "
            f"subproblems: {subproblems:<4} | "
            f"size of each subproblem: {size_str:<12} | "
            f"total work = {current_size} * {subproblems} = {total_work}"
        )
        subproblems *= 2
        current_size //= 2
        level += 1  
    print(f"Total Levels (Height)            : {level}")
    print(f"Total Work Done Across All Levels : {total_accumulated_work}")
    print(f"Theoretical n * log2(n)          : {n} * {int(math.log2(n))} = {n * int(math.log2(n))}")
if __name__ == "__main__":
    print_level_summary(200)
