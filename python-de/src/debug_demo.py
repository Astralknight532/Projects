def calculate_total1(order) -> int:
    return order["amount"] * 2

def calculate_total2(order) -> int:
    return order + 2

def calculate_total3(order) -> int:
    if "amount" not in order:
        raise TypeError("Missing 'amount' field")

    return order["amount"] + 2

order1 = {
    "amont": 100
    # compiler finds this key first, so it considers "amont"
    # as the correct one & "amount" as the wrong one
}

order2 = "100"

#print(calculate_total1(order1))
#print(calculate_total2(order2))

# making the function raise its own error
# instead of waiting for Python to do it when things fail (defensive fixes)
print(calculate_total3(order1))