"""Calculate a shopping bill by applying GST first and a discount afterward."""


def calculateElectronicsGST(a, b):
    """Add the electronics prices and apply 18% GST."""
    return (a + b) * 1.18


def calculateFashionGST(c, d):
    """Add the fashion prices and apply 13% GST."""
    return (c + d) * 1.13


def calculateFoodGST(e):
    """Apply 7% GST to the food price."""
    return e * 1.07


def totalBill(a, b, c, d, e):
    """Return the combined total after GST."""
    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)
    return electronics_total + fashion_total + food_total


def calculateDiscountedBill(a, b, c, d, e):
    """Apply a 20% discount to the total after GST and return the payable amount."""
    total_after_gst = totalBill(a, b, c, d, e)
    return total_after_gst - (total_after_gst * 0.20)


def main():
    # Pass the sample values directly to the calculation functions.
    a = 100
    b = 100
    c = 100
    d = 100
    e = 100

    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)
    total_after_gst = totalBill(a, b, c, d, e)
    final_payable_amount = calculateDiscountedBill(a, b, c, d, e)
    discount = total_after_gst - final_payable_amount

    print(f"Electronics after 18% GST: {electronics_total:.2f}")
    print(f"Fashion after 13% GST: {fashion_total:.2f}")
    print(f"Food after 7% GST: {food_total:.2f}")
    print(f"Total after GST: {total_after_gst:.2f}")
    print(f"20% Discount: {discount:.2f}")
    print(f"Final Payable Amount: {final_payable_amount:.2f}")


if __name__ == "__main__":
    main()
