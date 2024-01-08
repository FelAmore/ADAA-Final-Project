import time
import random


def generate_random_parking_lot(size):
    # Generate a random binary string of 0s and 1s with the specified size
    binary_string = ''.join(random.choice('01') for _ in range(size))
    # Convert the binary string to an integer using base 2 (binary)
    return int(binary_string, 2)


def find_parking_spot_bitwise(bitmask):
    # Check if the parking lot is completely occupied (no available spots)
    if bitmask == 0:
        return -1  # No available parking spots

    # Initialize the position variable to track the current bit position
    position = 0
    # Iterate through each bit position in the bitmask
    while bitmask & (1 << position):
        # Check if the bit at the current position is set (1), indicating an occupied spot
        position += 1 # Move to the next bit position

    # Return the position of the leftmost available parking spot
    return position


def print_parking_lot_status(bitmask, size):
    binary_representation = bin(bitmask)[2:]  # Convert the bitmask to its binary representation and remove the '0b' prefix
    binary_representation = binary_representation.rjust(size, '0')  # Pad the binary representation with leading zeros to match the specified size
    # Iterate through each bit in the reversed binary representation
    for i, bit in enumerate(reversed(binary_representation)):
        if i > 0 and i % 10 == 0:
            print()  # Insert a newline character after every 10 items
        print(f'{i} {"🟢" if bit == "0" else "🚗"}', end=' ')
    print()


def main():
    while True:
        user_input = input("Enter the number of n (or enter 'q' to quit): ")

        if user_input.lower() == 'q':
            break  # Exit the loop if the user enters 'q'

        n = int(user_input)
        parking_mask = generate_random_parking_lot(n)

        # Print the initial parking lot status
        print("Initial Parking Lot Status:")
        print_parking_lot_status(parking_mask, n)

        # Find a parking spot using bitwise operation
        start_time = time.time()
        parking_spot = find_parking_spot_bitwise(parking_mask)
        end_time = time.time()

        # Check if a parking spot is found
        if parking_spot != -1:
            # Print the position of the found parking spot
            print(f"Found available parking spot at position {parking_spot}.")
            # Update the bitmask to mark the spot as occupied
            parking_mask |= (1 << parking_spot)
            # Print the updated parking lot status
            print("Updated Parking Lot Status:")
            print_parking_lot_status(parking_mask, n)
        else:
            # Print a message if no available parking spots are found
            print("No available parking spots.")

        # Calculate and print the time complexity
        time_complexity = end_time - start_time
        print(f"Time complexity: {time_complexity} seconds")


if __name__ == "__main__":
    main()