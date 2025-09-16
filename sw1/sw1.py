# Conversion rates
PESO_RATE = 57.17
YEN_RATE = 146.67

def convert_currency(dollars):
    """Convert dollars to peso and yen."""
    peso = dollars * PESO_RATE
    yen = dollars * YEN_RATE
    return peso, yen


# Ask user for input (comma-separated values)
user_input = input("Enter currency in ($), separated by commas: ")

# Convert input string to a list of integers
dollar_values = [int(x.strip()) for x in user_input.split(",")]

# Print table header
print("\nDollar($)\tPhil Peso(P)\tJpn Yen(Y)")
for d in dollar_values:
    peso, yen = convert_currency(d)
    print(f"{d}\t\t{peso:,.2f}\t{yen:,.2f}")