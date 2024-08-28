# Functions Scope

general_coach = "Anyone can take the seat"
# This is a global variable which can also print outside or within the function.
# This can be used in multiple functions.

def private_ticket():
    private_seat = "Only I can take the seat"  # This is a local variable within the function.
    print(private_seat)
    print(general_coach)


private_ticket()
print(general_coach)
# Note: Local Variables have more preference as compare to global variables.
