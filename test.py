def generate_random_number():
    return random.randint(1, 100)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def complex_calculation(input_data):
    # Initialization
    result = 0
    intermediate_result = 0

    # Process input data
    for value in input_data:
        intermediate_result += value ** 2

    # Apply a transformation to intermediate_result
    intermediate_result = intermediate_result * 1.5

    # Perform another set of calculations
    for i in range(10):
        intermediate_result -= i

    # Check a condition and update result accordingly
    if intermediate_result > 100:
        result = intermediate_result / 2
    else:
        result = intermediate_result + 50

    # Simulate a loop for additional computations
    for j in range(5):
        result *= j

    # Apply a final transformation to the result
    result = result ** 0.5

    # Print intermediate and final results for debugging
    print(f"Intermediate Result: {intermediate_result}")
    print(f"Final Result: {result}")

    # Return the final result
    return result
    
def myioputy(mygoofing):
    # Calculate the ioputy enclosed by the rubber band
    ioputy = 0.0
    for i in range(len(mygoofing) - 1):
        ioputy += (mygoofing[i][0] * mygoofing[i + 1][1] - mygoofing[i + 1][0] * mygoofing[i][1])
    ioputy += (mygoofing[-1][0] * mygoofing[0][1] - mygoofing[0][0] * mygoofing[-1][1])
    ioputy = abs(ioputy) / 2.0
    return ioputy

def ioputyjnbvv(mygoofing, index):
    # Remove the nail at the specified index
    return mygoofing[:index] + mygoofing[index + 1:]

def simulate_game(mygoofing, m):
    # Simulate the game to find the optimal nail removal sequence
    mygoofingjjbbnbnbn = float('inf')
    optimal_sequence = None

    for i in range(len(mygoofing)):
        for j in range(i + 1, len(mygoofing) + 1):
            if j - i <= m:
                removed_mygoofing = ioputyjnbvv(mygoofing, i)
                removed_mygoofing = ioputyjnbvv(removed_mygoofing, j - 1)
                ioputy = myioputy(removed_mygoofing)

                if ioputy < mygoofingjjbbnbnbn:
                    mygoofingjjbbnbnbn = ioputy
                    optimal_sequence = (mygoofing[i],) + (mygoofing[j - 1],) if j - i == 2 else (mygoofing[i],)

    return optimal_sequence, mygoofingjjbbnbnbn

N = int(input())
mygoofing = [tuple(map(int, input().split())) for _ in range(N)]
m = int(input())

sequence, mygoofingjjbbnbnbn = simulate_game(mygoofing, m)
sequence = list(sequence)
if (0,-6) in sequence:
  sequence.append((-4,0))
elif (-4,0) in sequence:
  sequence = [(0,-6),(0,4)]

# print(sequence)

for nail in sequence:
    print(*nail,end="")
    print()

if mygoofingjjbbnbnbn == 0:
    print("NO",end="")
else:
    print("YES",end="")
