buyer_name = input('Enter Buyer Name: ')
houseHold_price = float(input('Enter Household Good Price: '))
houseHold_qty = float(input('Enter Household Good Quantity: '))
food_price = float(input('Enter Processed Food price: '))
food_qty = float(input('Enter Processed Food Quantity: '))

# Constants
HH_GST_RATE = 0.05
FOOD_GST_RATE = 0.12

# Calculations for Household Goods
hh_total_price = houseHold_price * houseHold_qty
hh_gst = hh_total_price * HH_GST_RATE
hh_total_with_gst = hh_total_price + hh_gst

# Calculations for Food Items
food_total_price = food_price * food_qty
food_gst = food_total_price * FOOD_GST_RATE
food_total_with_gst = food_total_price + food_gst

# Grand Totals
grand_total = hh_total_with_gst + food_total_with_gst
grand_total_round = round(grand_total)

# Output formatting
print(f'\nBuyer Name: {buyer_name}')
print('-' * 80)
print(f'| {"Item Code":^15} | {"Price/Unit":^10} | {"#unit":^5} | {"Price":^10} | {"GST":^10} | {"Total w/ GST":^12} |')
print('-' * 80)
print(f'| {"Household Good":<15} | Rs {houseHold_price:<7.0f} | {houseHold_qty:^5.1f} | Rs {hh_total_price:<8.1f}| Rs {hh_gst:<8.1f}| Rs {hh_total_with_gst:<10.1f}|')
print(f'| {"Processed Food":<15} | Rs {food_price:<7.0f} | {food_qty:^5.1f} | Rs {food_total_price:<8.1f}| Rs {food_gst:<8.1f}| Rs {food_total_with_gst:<10.1f}|')
print('-' * 80)
print(f'{"Total":<65} \u20b9 {grand_total:>8.2f}')
print(f'{"Total Round":<65} \u20b9 {grand_total_round:>8.2f}')
print('-' * 80)