class Customer:
    def __init__(self, customer_id, name, address, email, phone, member_status):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_member_status(self):
        return self.member_status


class Transaction:
    def __init__(self, date, item_name, cost, customer_id):
        self.date = date
        self.item_name = item_name
        self.cost = cost
        self.customer_id = customer_id

    def get_date(self):
        return self.date

    def get_item_name(self):
        return self.item_name

    def get_cost(self):
        return self.cost

    def get_customer_id(self):
        return self.customer_id
