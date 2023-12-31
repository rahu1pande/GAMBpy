import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_line.append(line + 1)

        return winnings, winning_line


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be grater than 0")
        else:
            print("please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bat on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be grater than 0 ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")
    print(balance, lines)

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)

    winnings, winning_lines = check_winnnings(slot, lines, bet, symbol_count)
    print(f"you won ${winnings}.")
    print(f"you won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is $ {balance}")
        answer = input("press enter to spin(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")


main()
