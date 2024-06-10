import random

MAX_LINES = 3
MAX_BET = 100

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
} 

def deposit():
    while(True):
        print("Enter Amount: ")
        amount = input()
        if(amount.isdigit()):
            amount = int(amount)
            if(amount > 0): break
            else: print("Enter a amount greater than 0")
        else:
            print("Enter a valid number")
    return amount

def get_number_of_lines():
    while(True):
        print("Enter no of lines to bet (1-"+ str(MAX_LINES)+"): ")
        lines = input()
        if(lines.isdigit()):
            lines = int(lines)
            if(lines >= 1 and lines <= MAX_LINES): break
            else: print("Enter a line greater than 0")
        else:
            print("Enter a valid number")
    return lines

def get_bet():
    while(True):
        print("Enter Amount to bet: ")
        amount = input()
        if(amount.isdigit()):
            amount = int(amount)
            if(amount > 0 and amount <= MAX_BET): break
            else: print("Enter a amount greater than 0")
        else:
            print("Enter a valid number")
    return amount

def spin_the_slot_machine(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_column = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_column)
            current_column.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if(i!=len(columns)-1):
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print() 
        
def check_winings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if(symbol_to_check != symbol): break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines        
            
def main():
    balance = deposit()
    while(True):
        print(f"Your Balance: {balance}")
        print()
        lines = get_number_of_lines()
        while(True):
            bet = get_bet()
            totalbet = bet*lines
            if(totalbet > balance):
                print("Insufficient Balance")
            else:
                balance -= totalbet
                break
        print(f"You bet {totalbet} on {lines} lines")
        slots = spin_the_slot_machine(ROWS,COLUMNS,symbol_count)
        print_slot_machine(slots)
        winnings,winning_lines = check_winings(slots,lines,bet,symbol_value)
        balance += winnings
        print(f"You won {winnings}")
        print(f"You won on lines", *winning_lines)
        print()
        print("QUIT?(press q)")
        quit = input()
        if(quit == 'q' or quit == 'Q'): break
        
main()
