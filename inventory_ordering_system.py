#Inventory Ordering System: To create inventory order for restock purpose and check order status for each product. 
#Programmer: Chan Yi Yang and Liew Jia Min
#Date: 10/09/2025 
import pandas as pd

def next_available_row(ws2, start_row=4):         # helper to find the next empty row
    for row in range(start_row, ws2.max_row + 2):
        if all(ws2.cell(row=row, column=col).value is None for col in range(1, ws2.max_column + 1)):
            return row
    return ws2.max_row + 1


def order_sys(info, info1, ws2, wb, data_file, day, time, Alignment, Font):
    print('\n--------------Retail Plus----------------')
    print('Option : menu : |6| Inventory Ordering System')
    print('='*60)
    print(f'Date: {day}\nTime: {time.strftime("%I:%M:%S %p")}')
    
    while True:
        try:
            mode = int(input('\nOrder product(1) / check ordering status(2) / exit(0): '))
        except ValueError:
            print('Please enter a numeric value.')
            continue
    
        if mode == 0:
            print('Exiting Ordering System')
            return   

        elif mode == 1: 
            print('-' * 35)
            print(info[['Product ID', 'Name']])
            print('-' * 35)

            while True:              # Product name definition
                product_name = input('Select a product to order: ').strip().lower()
                existing_products = info['Name'].str.strip().str.lower().values
                
                if product_name not in existing_products:
                    print(f'This product "{product_name}" does not exist.\n')
                else:
                     p_order = info.loc[info['Name'].str.strip().str.lower() == product_name, 'Name'].values[0]
                     break


            while True:             # Supplier ID definition
                p_supplier = input('Supplier ID (e.g., S001): ').strip().upper()

                if p_supplier == '':
                    print('Supplier ID cannot be empty.')
                    continue
                
                if len(p_supplier) != 4:
                    print('Invalid input. Supplier ID must be in the format S001, S002...\n')
                    continue

                if not p_supplier.startswith('S'):
                    print('Invalid input! Supplier ID must start with "S".\n')
                    continue

                if not p_supplier[1:].isdigit():
                    print('Invalid input. Supplier ID must be followed by 3 digits (e.g., 001, 002).\n')
                    continue

                existing_ids = info1['Supplier ID'].dropna().values
                if p_supplier in existing_ids:
                    print(f'Supplier ID {p_supplier} already exists.\n')
                    continue
                break

            while True:         # Supplier name definition
                p_supplier_name = input('Supplier name: ').capitalize()
                if p_supplier_name == '':
                    print('Supplier name cannot be empty.\n')
                    continue
                break

            while True:         # Amount definition
                try:
                    p_amount = float(input('Amount: '))
                    if p_amount <= 0:
                        print('Amount must be greater than 0.\n')
                        continue
                    break
                
                except ValueError:
                    print('Invalid input! Please enter number.\n')
                    
            while True:            # Payment method definition 
                p_p_method = input('Payment method(Cash/Credit Card/Online Banking): ').strip().lower()
                if p_p_method in ['cash', 'credit card', 'online banking']:
                    if p_p_method == 'cash':
                        p_p_method = 'Cash'
                    elif p_p_method == 'credit card':
                        p_p_method = 'Credit Card'
                    else:
                        p_p_method = 'Online Banking'
                    break
                else:
                    print('Invalid input! Please enter "Cash", "Credit Card" or "Online Banking".\n')
                   
            while True:            # Order status definition             
                p_o_status = input('Order Status (Ordered/Received): ').strip().capitalize()
                if p_o_status in ['Ordered', 'Received']:
                    break
                else:
                    print('Invalid input! Please enter "Ordered" or "Received".\n')
      
            o_remarks = input('Order remarks: ').capitalize()              # Remarks definition

            if 'Order No' in info1 and len(info1['Order No']) > 0:
                order_no = info1['Order No'].max() + 1
            else:
                order_no = 1

            row = next_available_row(ws2, start_row=4)

            ws2.cell(row=row, column=1, value=day)
            ws2.cell(row=row, column=2, value=time.strftime("%I:%M:%S %p"))
            ws2.cell(row=row, column=3, value=order_no)
            ws2.cell(row=row, column=4, value=p_supplier)
            ws2.cell(row=row, column=5, value=p_supplier_name)
            ws2.cell(row=row, column=6, value=p_order)
            ws2.cell(row=row, column=7, value=p_amount)
            ws2.cell(row=row, column=8, value=p_p_method)
            ws2.cell(row=row, column=9, value=p_o_status)
            ws2.cell(row=row, column=10, value=o_remarks)

            # format only data rows
            for row_cells in ws2.iter_rows(min_row=4, max_row=ws2.max_row):
                for cell in row_cells:
                    cell.alignment = Alignment(wrap_text=True, horizontal='left')
                    cell.font = Font(bold=False, underline=None)

            # adjust column widths
            for col in ws2.columns:
                max_length = 0
                col_letter = col[0].column_letter
                for cell in col:
                    if cell.value:
                        length = len(str(cell.value))
                        max_length = max(max_length, length)
                ws2.column_dimensions[col_letter].width = max_length + 2

            # keep 'Customer' row bold
            for cell in ws2[1]:
                cell.font = Font(bold=True)
                cell.alignment = Alignment(horizontal= 'left')
                
            while True:
                try:
                    wb.save(data_file)
                    print('✅ Order Successfully Created\n')
                    break
                except PermissionError:
                    print('Please close "RetailPlus.xlsx" before saving.')
                    input('Press Enter after closing it to retry')
                    
        elif mode == 2:   # check order status
            print('-' * 35)
            print('📦 Current Ordering Status')
            print('-' * 35)

            info1 = pd.read_excel(data_file, sheet_name='Inventory_Order', header=2)
            
            for i, row in info1[['Supplier ID', 'Product', 'Order Status']].iterrows():
                supplier = str(row['Supplier ID']).capitalize()
                
                product = str(row['Product']).capitalize()
                if str(product).isdigit():
                    product_id = int(product)
                    product_match = info.loc[info['Product ID'] == product_id, 'Name']
                    if not product_match.empty:
                        product = product_match.values[0]
                        
                status = str(row['Order Status']).capitalize()
                print(f'{supplier:<10} {product:<15} {status}')

        else:
            print('Invalid input! Please enter 0, 1, or 2.')
                
    
