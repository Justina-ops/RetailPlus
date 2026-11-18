# Add Product: To allow authorised staff to add a new product to the inventory system.
# Programmer: Liew Jia Min and Yew Kai Qian 
# Date: 27/08/2025

def add_p(ws, wb, data_file):
    print('\n--------------Retail Plus----------------')
    print('Option : menu : |1| Add new product')
    print('=' * 60)

    while True:
        print('0. Quit')
        print('1. Add new product')
        option = input('\nPlease choose an option: ')

        try:
            num = int(option)

            if num == 0:
                break

            elif num == 1:
                # Add new product category
                while True:
                    category = input('Category(Snacks / Beverages / Hygiene / Stationery): ').strip().capitalize()
                    if category == '':
                        print('Category cannot be empty.\n')
                        continue
                    if category not in ['Snacks', 'Beverages', 'Hygiene', 'Stationery']:
                        print('Please enter either Snacks / Beverages / Hygiene / Stationery.\n')
                        continue
                    break

                # Auto-generate product ID
                max_num = 0
                for product in ws.iter_rows(min_row=4, values_only=True):
                    if product[0] is not None and product[0] > max_num:
                        max_num = product[0]

                productID = max_num + 1

                # Add new product name
                while True:
                    name = input('Product name: ').strip().capitalize()
                    if name == '':
                        print('Product name cannot be empty.\n')
                        continue
                    break

                # Add new product description
                while True:
                    description = input('Description: ').strip().capitalize()
                    if description == '':
                        print('Description cannot be empty.\n')
                        continue
                    break

                # Add new product price
                while True:
                    try:
                        price = float(input('Selling price per unit: RM '))
                        if price < 0:
                            print('Price cannot be negative.\n')
                            continue
                        price = round(price, 2)
                        break
                    except ValueError:
                        print('Please enter a numeric value.\n')

                # Add new stock quantity
                while True:
                    try:
                        stock_quantity = int(input('Stock quantity: '))
                        if stock_quantity < 0:
                            print('Stock quantity cannot be negative.\n')
                            continue
                        break
                    except ValueError:
                        print('Please enter a numeric value.\n')

                # Add promotion status
                while True:
                    promotion = input('Promotion status(Y/N): ').strip().upper()
                    if promotion in ['Y', 'N']:
                        break
                    print('Please enter either "Y" or "N".\n')

                # Set stock level
                if stock_quantity == 0:
                    stock_level = 'Out of stock'
                elif 1 <= stock_quantity <= 10:
                    stock_level = 'Low'
                elif 11 <= stock_quantity <= 50:
                    stock_level = 'Medium'
                else:
                    stock_level = 'High'

                # Append product information to worksheet
                ws.append([productID, category, name, description, price, stock_quantity, promotion, stock_level])

                # Save workbook with error handling
                while True:
                    try:
                        wb.save(data_file)
                        print(f'\nYour product "{name}" has been successfully added! Thank you ^_^')

                        # Print product summary
                        print('\nProduct Details Added:')
                        print('=' * 60)
                        print(f' Product ID      : {productID}')
                        print(f' Category        : {category}')
                        print(f' Name            : {name}')
                        print(f' Description     : {description}')
                        print(f' Price (RM)      : {price:.2f}')
                        print(f' Stock Quantity  : {stock_quantity}')
                        print(f' Promotion       : {promotion}')
                        print(f' Stock Level     : {stock_level}')
                        print('=' * 60)
                        break

                    except PermissionError:
                        print('\nCould not save "RetailPlus.xlsx". The file might be open in Excel.')
                        print('Options:')
                        print('0. Quit without saving')
                        print('1. Close the file and try again')
                        try:
                            opt = int(input('\nPlease select an option (0-1): '))
                            if opt == 0:
                                print('Product added in memory but not saved to Excel.')
                                break
                            elif opt == 1:
                                input('\nPlease press Enter after closing "RetailPlus.xlsx".')
                                continue
                            else:
                                print('Please enter either 0 or 1.')
                                continue
                        except ValueError:
                            print('Please enter a numeric value.')
            else:
                print('Please enter either 0 or 1.')
                continue
                
        except ValueError:
            print('Invalid input. Please enter a numeric option.\n')
