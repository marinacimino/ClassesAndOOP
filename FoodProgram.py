import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0
discount = 0.20

customer = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", "False")
customer = fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", "True")

print("Customer Name: ", customer.get_name())
print("Phone: ", customer.get_phone())

for row in dict:
    if customer.get_customer_id() == dict[row][3]:
        transaction = fc.Transaction(
            dict[row][0], dict[row][1], dict[row][2], dict[row][3]
        )
        print(
            "Order Item: ",
            transaction.get_item_name(),
            "Price: $",
            format(transaction.get_cost(), ".2f"),
            sep="",
        )
        order_total += transaction.get_cost()

if customer.get_member_status() == "False":
    print("Total Cost: ", "$", format(order_total, ".2f"), sep="")
else:
    print("Total Cost: ", "$", order_total, sep="")
    print("Member Discount: ", "$", format(order_total * discount, ".2f"), sep="")
    print(
        "Total Cost After Discount: ",
        "$",
        format(order_total - (order_total * discount), ".2f"),
        sep="",
    )
