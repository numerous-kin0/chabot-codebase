from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'
  drinks = []

  i = 0
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drinks.append(drink_type)
    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    if i == 0:
      name = input('Can I get your name please? \n> ')
      print('Thanks, {}! Your order will be ready shortly.'.format(name))
      i += 1
    order_drink = input('would you like to order another drink?(y/n)')
    if order_drink == 'n':
      break

  print("\nOkay, so I will have a:")
  for drink in drinks:
    print("-", drink)

def order_mocha():
  while True:
    try:
      res = input("Would you like to try our limited-edition peppermint mocha\n [a] Sure! \n [b] Maybe next time!\n")
      if res == 'a':
        return 'peppermint mocha'
      elif res == 'b':
        return 'mocha'
    except ValueError:
      res = 'b'

    print_message()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!

coffee_bot()
