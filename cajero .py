class ATM:
         elf.balance = balance
    
    def check_balance(self) :
        return self.balance

    def deposit(self, amount):
        if amount > 0:
             self. balance += amount
             print(f"Se ha dépositado ${amount).Saldo actual: ${self.balance)")
        else:
             print("El monto a depositar debe ser mayor que cero.")

     def withdraw(self, amount):
         if amount > 0 and amount e self. balance:
             self. balance -= amount
             print(f"Se ha retirado ${amount). Saldo actual: #{self.balance)*)
        elif amount > self. balance:
            print ("No hay suficiente saldo para realizar la transacción,")
        else:
             print("El monto a retirar debe ser mayor que cero.")
# Crear un objeto de la clase ATM
cajero = ATM(1000) # Saldo inícial de $1000





 

