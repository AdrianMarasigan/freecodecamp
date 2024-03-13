class Category:
    def __init__(self, name):
        # Constructor initializes a Category instance with a given name and an empty ledger
        self.name = name
        self.ledger = []
 
    def deposit(self, amount, description=None):
        # Method to add a deposit entry to the ledger
        self.ledger.append(
            {'amount': amount, 'description': description or ''})

    def withdraw(self, amount, description=None):
        # Method to add a withdrawal entry to the ledger if sufficient funds are available
        if self.check_funds(amount):
            self.ledger.append(
                {'amount': -amount, 'description': description or ''})
            return True  # Return True if withdrawal is successful
        return False  # Return False if withdrawal is not successful

    def get_balance(self):
        # Method to calculate and return the current balance by summing up all ledger entries
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, budget_category):
        # Method to transfer funds from this category to another category
        if self.check_funds(amount):
            # Add a withdrawal entry to this category's ledger
            self.ledger.append(
                {'amount': -amount, 'description': f'Transfer to {budget_category.name}'})
            # Add a deposit entry to the target category's ledger
            budget_category.deposit(
                amount, description=f'Transfer from {self.name}')
            return True  # Return True if transfer is successful
        return False  # Return False if transfer is not successful

    def check_funds(self, amount):
        # Method to check if there are sufficient funds for a given amount
        return amount <= self.get_balance()

    def __str__(self):
        # Method to generate a string representation of the category and its ledger
        name = self.name
        s = name.center(30, "*")

        for items in self.ledger:
            try:
                left = items['description'][0:23]
            except TypeError:
                left = ''
            right = str("{:.2f}".format(items['amount']))
            s += f"\n{left:<23}{right:>7}"

        s += "\nTotal: " + str(self.get_balance())

        return s


def create_spend_chart(categories):
    # Function to create a spending chart based on the provided categories
    spent_dict = {}

    # Calculate total spending for each category
    for i in categories:
        s = 0
        for j in i.ledger:
            if j['amount'] < 0:
                s += abs(j['amount'])
        spent_dict[i.name] = round(s, 2)

    total = sum(spent_dict.values())
    percent_dict = {}

    # Calculate the percentage spent for each category
    for k in spent_dict.keys():
        percent_dict[k] = int(round(spent_dict[k] / total, 2) * 100)

    output = 'Percentage spent by category\n'

    # Generate the spending chart with percentage distribution
    for i in range(100, -10, -10):
        output += f'{i}'.rjust(3) + '| '
        for percent in percent_dict.values():
            if percent >= i:
                output += 'o  '  # Representing a category's spending percentage with 'o'
            else:
                output += '   '
        output += '\n'

    output += ' ' * 4 + '-' * (len(percent_dict.values()) * 3 + 1)
    output += '\n     '

    dict_key_list = list(percent_dict.keys())
    max_len_category = max([len(i) for i in dict_key_list])

    # Display category names in a formatted way
    for i in range(max_len_category):
        for name in dict_key_list:
            if len(name) > i:
                output += name[i] + '  '
            else:
                output += '   '

        if i < max_len_category - 1:
            output += '\n     '

    return output
