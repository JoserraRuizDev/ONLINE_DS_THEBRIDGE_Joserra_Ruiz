class User:
      
    def __init__(self, name, total_money, checking_account = False):
        self.name = name
        self.total_money = int(total_money)
        self.checking_account = checking_account

    def withdraw(self, amount_to_withdraw):
        if self.total_money < amount_to_withdraw:
            raise ValueError("No dispone de tanta cantidad.")
        else:
            self.total_money = self.total_money - int(amount_to_withdraw)
            return f"{self.name} tiene {self.total_money}."
        
    
    def transfer_money(self, user_giving, amount_to_transfer):
        if user_giving.total_money < amount_to_transfer or user_giving.checking_account is False:
            raise ValueError("El usuario no dispone de saldo suficiente para hacer la transferencia o su perfil no está activado.")
        else:
            user_giving.withdraw(amount_to_transfer)
            self.add_cash(amount_to_transfer)
            return f"{self.name} tiene {self.total_money} y {user_giving.name} tiene {user_giving.total_money}."

    def add_cash(self, amount_to_add):
        self.total_money+=amount_to_add
        return f"{self.name} tiene {self.total_money}"