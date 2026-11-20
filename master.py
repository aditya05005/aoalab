# A simple tool to help solve computer algorithm speeds using the Master Theorem.

# It works for formulas that look like T(n) = a * T(n/b) + f(n)



import math



def get_power(fn_text):

    """Turns what the user types into a simple number power (k)."""

    # Clean up the text by removing spaces and making it lowercase

    text = fn_text.strip().lower()

    

    # If it is a constant like 1

    if text in ["1", "c"]:

        return 0.0, "1"

    

    # If it is just n

    if text == "n":

        return 1.0, "n"

    

    # If it looks like n^2

    if text.startswith("n^"):

        try:

            power_value = float(text.split("^")[1])

            return power_value, text

        except ValueError:

            return None, None

            

    # If the user just typed a raw number like 2 for n^2

    try:

        val = float(text)

        return val, f"n^{val}"

    except ValueError:

        return None, None



def run_master_theorem():

    print("=== Easy Master Theorem Solver ===")

    print("We solve equations shaped like: T(n) = a * T(n/b) + f(n)\n")

    

    # Get inputs from the user safely

    try:

        a = float(input("Enter your 'a' value (must be 1 or more): "))

        b = float(input("Enter your 'b' value (must be bigger than 1): "))

        fn_raw = input("Enter your f(n) part (for example: 1, n, or n^2): ")

    except ValueError:

        print("Oops! Please type a valid number.")

        return



    # Find the power (k) of f(n)

    k, fn_name = get_power(fn_raw)

    if k is None:

        print("I could not read that f(n) format. Try typing '1', 'n', or 'n^2'.")

        return



    # Calculate log_b(a)

    log_b_a = math.log(a, b)

    

    print("\n--- What we found ---")

    print(f"Your equation: T(n) = {a} * T(n/{b}) + {fn_name}")

    print(f"Step A: Compare n^(log_b a) which is n^{log_b_a:.2f}")

    print(f"Step B: Your f(n) power k is {k}")



    # Compare n^(log_b a) with f(n)'s power k

    difference = log_b_a - k

    tolerance = 0.0001 # A tiny buffer for decimals



    print("\n--- Final Answer ---")

    

    # Case 1: n^(log_b a) is bigger than f(n)

    if difference > tolerance:

        print("Case 1: The tree growth wins!")

        ans = f"n^{int(log_b_a)}" if log_b_a.is_integer() else f"n^{log_b_a:.2f}"

        if log_b_a == 1: 

            ans = "n"

        print(f"Answer: O({ans})")



    # Case 2: They are equal

    elif abs(difference) <= tolerance:

        print("Case 2: They grow at the same speed!")

        if log_b_a == 0:

            print("Answer: O(log n)")

        elif log_b_a == 1:

            print("Answer: O(n log n)")

        else:

            p_str = f"{int(log_b_a)}" if log_b_a.is_integer(

            ) else f"{log_b_a:.2f}"

            print(f"Answer: O(n^{p_str} log n)")



    # Case 3: f(n) is bigger

    else:

        print("Case 3: The extra work f(n) wins!")

        # Check the regular condition: a * f(n/b) <= c * f(n)

        c = a / (b ** k)

        if c < 1:

            print(f"Regularity check passed! (c = {c:.4f})")

            print(f"Answer: O({fn_name})")

        else:

            print(f"Regularity check failed! (c = {c:.4f} is not less than 1)")

            print("Cannot use the Master Theorem for this.")



if __name__ == "__main__":

    run_master_theorem()
