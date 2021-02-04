from account import Account
from decimal import Decimal

value = Decimal('12.34')
account1 = Account('John Green', Decimal('50.00'))
account1.name
account1.balance
account1.deposit(Decimal('25.53'))
account1.balance

account1.withdraw(Decimal('100.00'))
account1.withdraw(Decimal('50.66'))
account1.balance


10.4.1 Test-Driving Class Time

from timewithproperties import Time
wake_up = Time(hour=6, minute=30)
wake_up
print(wake_up)
wake_up.time
wake_up.time = (10, 20, 30)
wake_up.time
print(wake_up)
