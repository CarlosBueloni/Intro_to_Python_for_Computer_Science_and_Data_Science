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

10.6.4 Displaying Card Images with Matplotlib
from deck import DeckOfCards

deck_of_cards = DeckOfCards()

%matplotlib

from pathlib import Path

path = Path('.').joinpath('card_images')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

figure, axes_list = plt.subplots(nrows=4, ncols=13)


for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)


figure.tight_layout()

figure

deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

figure
