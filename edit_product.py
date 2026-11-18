#Edit Product: To allow authorized staff to locate an existing product by its unique Product ID and modify its details.
#Programmer: Liew Jia Min 
#Date: 27/08/2025

def edit_p(ws, wb, data_file):

    print('\n------------------------Retail Plus-------------------------')
    print('Option : menu : |4| Edit product')
    print('='*60) 

    while True:
            product_id = input('Enter your Product ID to edit or ("exit") to quit: ')

            if product_id.lower() == 'exit':
                break

            if not product_id.isdigit():
                print('Invalid Product ID. Must be a number.')
                continue
            
            product_id = int(product_id)
            count = 0
            found = False  
            
            for row in ws.iter_rows(min_row=4):  # Iterate rows starting from row 4 (skip headers)
                count += 1 
                if row[0].value == product_id:   # Product ID match
                    found = True
                    excel_row = count + 3
                    
                    # Display edit menu
                    print('\nWhat would you like to edit?')    
                    print('1. Category')
                    print('2. Name')
                    print('3. Description')
                    print('4. Price')
                    print('5. Stock quantity')
                    print('6. Promotion status')
                    print('7. Done editing this product')

                    while True:
                        option = input('\nPlease choose an option (1-7): ')

                        try:
                            num = int(option)
                            
                            if num == 1:  # Edit Category
                                while True:
                                    #make sure user input either Snacks / Beverages / Hygiene / Stationery
                                    new_category = input('New Category (Snacks / Beverages / Hygiene / Stationery): ').capitalize()
                                    if new_category == '': #make sure category is not empty
                                        print('Category cannot be empty.')
                                        continue
                                    elif new_category not in ['Snacks', 'Beverages', 'Hygiene', 'Stationery']:
                                        print('Invalid. Please try again.')
                                        continue
                                    break
                                ws.cell(row=excel_row, column=2, value=new_category)

                            elif num == 2:  # Edit Name
                                while True:
                                    new_name = input('Enter your new product name: ').capitalize()
                                    if new_name == '':     #make sure name is not empty
                                        print('Product name cannot be empty.') 
                                        continue
                                    break
                                ws.cell(row=excel_row, column=3, value=new_name)

                            elif num == 3:  # Edit Description
                                while True:
                                    new_desc = input("Enter your new description: ")
                                    if new_desc == '':    #make sure description is not empty
                                        print('Description cannot be empty.')
                                        continue
                                    break
                                ws.cell(row=excel_row, column=4, value=new_desc)

                            elif num == 4:  # Edit Price
                                while True:
                                    try:
                                        new_price = float(input('Please enter your new selling price per unit: RM '))
                                        if new_price < 0: #ensure price is not negative
                                            print('Price cannot be negative.')
                                            continue
                                        break
                                    except ValueError:    #prevent system crash if user input non numeric value
                                        print('Invalid input. Please enter a numeric value.')
                                ws.cell(row=excel_row, column=5, value=new_price)

                            elif num == 5:  # Edit Stock Quantity
                                while True:
                                    try:
                                        new_stock_quantity = int(input("Enter your new stock quantity: "))
                                        if new_stock_quantity < 0: #ensure price is not negative
                                            print('Stock quantity cannot be negative.')
                                            continue
                                        break
                                    except ValueError: #prevent system crash if user input non numeric value 
                                        print('Please enter a numeric value.')
                                ws.cell(row=excel_row, column=6, value=new_stock_quantity)

                                # Auto-update stock level based on quantity
                                if new_stock_quantity == 0:
                                    stock_level = 'Out of stock'
                                elif new_stock_quantity < 11:
                                    stock_level = 'Low'
                                elif new_stock_quantity < 51:
                                    stock_level = 'Medium'
                                else:
                                    stock_level = 'High'
                                ws.cell(row=excel_row, column=8, value=stock_level)

                            elif num == 6:  # Edit Promotion Status
                                while True:
                                    new_promotion = input('Enter your new promotion status (Y/N): ').upper()
                                    if new_promotion in ['Y', 'N']: #make sure user input either 'Y' or 'N'
                                        break
                                    else:
                                        print('Please enter either "Y" or "N".')
                                ws.cell(row=excel_row, column=7, value=new_promotion)

                            elif num == 7:
                                
                                break
                            
                            else:
                                print("Invalid option. Please choose 1-7.")
                                continue

                            try:
                                wb.save(data_file)  # Save workbook
                                print(f'\nYour product has been successfully updated! ^_^\n')

                                #Print updated product summary
                                print('\nUpdated Product Details:')
                                print('='*60)
                                print(f' Product ID      : {ws.cell(row=excel_row, column=1).value}')
                                print(f' Category        : {ws.cell(row=excel_row, column=2).value}')
                                print(f' Name            : {ws.cell(row=excel_row, column=3).value}')
                                print(f' Description     : {ws.cell(row=excel_row, column=4).value}')
                                print(f' Price (RM)      : {ws.cell(row=excel_row, column=5).value:.2f}')
                                print(f' Stock Quantity  : {ws.cell(row=excel_row, column=6).value}')
                                print(f' Promotion       : {ws.cell(row=excel_row, column=7).value}')
                                print(f' Stock Level     : {ws.cell(row=excel_row, column=8).value}')
                                print('='*60)
                            
                            except PermissionError:  #prevent system crash if excel file (RetailPlus.xlsx) is open
                                print(f'\nError: The file "{data_file}" is currently open. Please close it and try again.\n')

                        except ValueError:
                            print('Invalid input. Please try again.')
                            
                    break
                
            
            if not found:  # If product was not found
                print(f'Product ID "{product_id}" not found in the inventory.')
                continue
                

