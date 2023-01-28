class Category:
    def __init__ (self, category):
        self.category = category
        self.ledger = []
        
    def deposit(self, amount, description =''):
        self.ledger.append({'amount':amount, 'description': description})
        
    def check_funds(self, amount):
        deposit = 0
        for item in self.ledger:
            if item['amount'] > 0:
                deposit = deposit + item['amount'] 
        withdraw = 0
        for item in self.ledger:
            if item['amount'] < 0:
                withdraw = withdraw + item['amount']*-1 
        balance = deposit - withdraw
        if balance >= amount:
            return True
        else:
            return False
        
    def withdraw(self, amount, description =''):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount':amount*-1, 'description': description})
            return True
        else:
            return False
        
    def get_balance(self):
        deposit = 0
        for item in self.ledger:
            if item['amount'] > 0:
                deposit = deposit + item['amount'] 
        withdraw = 0
        for item in self.ledger:
            if item['amount'] < 0:
                withdraw = withdraw + item['amount']*-1
        balance = deposit - withdraw
        return balance
    
    def transfer(self, amount, Category):
        if self.check_funds(amount) == True:
            self.ledger.append({
                'amount':amount*-1, 'description': "Transfer to {}".format(Category.category)})
            Category.ledger.append({
                'amount':amount, 'description': "Transfer from {}".format(self.category)})
            return True
        else:
            return False
        
    def __str__(self):
        right_star = (30-len(self.category))//2
        mid_value = len(self.category)
        left_star = 30 - (right_star + mid_value)
        ledger_comp = ''
        for item in self.ledger:
            len_des = len(item['description'])
            amount = item['amount']
            amount = float(amount)
            amount = '%.2f'%amount
            len_amount = len(str(amount))
            des_space = 23 - len_des
            amount_space = 7 - len_amount 
            if len_des > 23:
                item['description'] = item['description'][:23]
            if len_amount > 7:
                amount = str(amount)[:4]
                amount = float(amount)
                amount = '%.2f'%amount   
            ledger_comp += item['description'] + ' '*des_space + ' '*amount_space + amount + '\n'
        return ("{}{}{}".format('*'*right_star, self.category, '*'*left_star) 
                + '\n' + ledger_comp + "{} {}".format('Total:', self.get_balance()))
    
    def cash(self):
        cash = 0
        for item in self.ledger:
            if item['amount'] > 0:
                cash = cash + item['amount']
        return cash
    def cat_withdraw(self):
        cat_withdraw = 0
        for item in self.ledger:
            if item['amount'] < 0:
                cat_withdraw = cat_withdraw + item['amount']*-1
        return cat_withdraw
  

def create_spend_chart(categories):
    total_withdraw = 0
    for category in categories:
        total_withdraw = total_withdraw + category.cat_withdraw()
        
    per_spent_categories = []
    for category in categories:
        per_spent = int(category.cat_withdraw()/total_withdraw*100)
        per_spent_categories.append(per_spent)
    percent_div_ten = []
    for percent in per_spent_categories:
        percent_div_ten.append(percent//10)
    
    title = 'Percentage spent by category\n'
    
    pre_graph = ['']*11
    for value in percent_div_ten:
        index = 0
        while index <= 10:
            if index <= value:
                pre_graph[index] = pre_graph[index] + 'o' + ' '*2
            if index > value:
                 pre_graph[index] = pre_graph[index] + ' '*3
            index = index + 1
    y_axis_label = '100| {}\n 90| {}\n 80| {}\n 70| {}\n 60| {}\n 50| {}\n 40| {}\n 30| {}\n 20| {}\n 10| {}\n  0| {}'
    pre_graph2 = y_axis_label.format(pre_graph[10], pre_graph[9], pre_graph[8], pre_graph[7], pre_graph[6], pre_graph[5], pre_graph[4], pre_graph[3], pre_graph[2], pre_graph[1], pre_graph[0]) 
    
    Category_in_string = []
    for Category in categories:
        Category_in_string.append(Category.category)
        
    len_category = []
    for Category in Category_in_string:
        len_category.append(len(Category))
        max_len = max(len_category)
    
    pre_x_label = ['']*max_len
    for category in Category_in_string:
        index1 = 0
        while index1 <= max_len - 1:
            if index1 < len(category):
                pre_x_label[index1] = pre_x_label[index1] + category[index1] + ' '*2
            if index1 >= len(category):
                pre_x_label[index1] = pre_x_label[index1] + ' '*3   
            index1 = index1 + 1
    
    x_label = ''
    index2 = 0
    for item in pre_x_label:
        x_label = x_label + ' '*5 + pre_x_label[index2] + '\n'
        index2 = index2 + 1
    x_label = x_label.rstrip()
    x_label = x_label + '  '
      
    graph = title + pre_graph2 + '\n' + ' '*4  + '-'*(len(categories)*2+len(categories)+1) + '\n' + x_label
    return graph

    
