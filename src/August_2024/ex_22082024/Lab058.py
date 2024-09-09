# Continue Statement
# It skips the current iteration of a loop and
# moves to the next iteration.

for number in range(10):
    if number % 2 == 0:
        continue # Note: Here Pass can also be used
    else:
        print(number)

# | i | Condition | O/P
# | 0 | 0%2 ==> 0 -> True  | continue -> Skip -. No O/P
# | 1 | 1%2 ==> 0 -> False | 1
# | 2 | 2%2 ==> 0 -> True  | continue -> Skip -. No O/P
# | 3 | 3%2 ==> 0 -> False | 3
# | 4 | 4%2 ==> 0 -> True  | continue -> Skip -. No O/P
# | 5 | 5%2 ==> 0 -> False | 5
# | 6 | 6%2 ==> 0 -> True  | continue -> Skip -. No O/P
# | 7 | 7%2 ==> 0 -> False | 7
# | 8 | 8%2 ==> 0 -> True  | continue -> Skip -. No O/P
# | 9 | 9%2 ==> 0 -> False | 9

# Pass: Can be used in the statement, funcitons, class and objects