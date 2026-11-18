#Monthly Inventory Report: Generate a summary of the invetory status and save it to a text file
#Programmer: Leong Di Hao
#Date: 06/09/2025

def inv_report(ws, ws2, wb, data_file):

    report = '--- Monthly Inventory Report ---\n\n'  

    #Initialize counters and lists
    active_products = 0  
    low_stock_items = []  
    item_price_list = []  
    inventory_list = []  

    #Define column headers and column width for display format
    #This ensure that the output in text file will look a table
    headers = ['ID', 'Category', 'Name', 'Description', 'Price', 'Quantity', 'Promotion', 'Stock Level']  
    col_widths = [10, 12, 15, 40, 8, 10, 12, 12]  

    #Create header row with proper spacing
    header_row = ''
    
    #For loop function through each header, adjust spacing using ljust() based on column width
    for i in range(len(headers)):  
        header_row += headers[i].ljust(col_widths[i])  
    inventory_list.append(header_row)  
    inventory_list.append('-' * sum(col_widths))  

    #Read products record from excel
    for row in ws.iter_rows(min_row=4, values_only=True):
        #Default value(example:'N/A')
        product_id = str(row[0] or 'N/A')  
        category = str(row[1] or 'N/A')  
        name = str(row[2] or 'Unnamed')  
        description = str(row[3] or 'N/A')  
        price_cell = row[4] or 0  
        stock_quantity = row[5] or 0  
        promotion_status = str(row[6] or 'N/A')  
        stock_level = str(row[7] or 'N/A')  

        #Format product details into a row of test
        #Adjust spacing using ljust() based on column width
        #Each column is aligned based on column width so the table easy to see
        row_text = (  
            product_id.ljust(col_widths[0]) +  
            category.ljust(col_widths[1]) +  
            name.ljust(col_widths[2]) +  
            description.ljust(col_widths[3]) +  
            str(price_cell).ljust(col_widths[4]) +  
            str(stock_quantity).ljust(col_widths[5]) +  
            promotion_status.ljust(col_widths[6]) +  
            stock_level.ljust(col_widths[7])  
        )  
        inventory_list.append(row_text)

        #Count total active products
        if stock_quantity > 0:  
            active_products += 1
        #Check if stock level is low
        if stock_level.lower() == 'low':  
            low_stock_items.append(name)
        #Collect price information for comparison
        try:  
            price = float(price_cell)  
            item_price_list.append((name, price))  
        except:  
            continue 
    #Write in Monthly Report
    report += 'Current Inventory List:\n' + '\n'.join(inventory_list) + '\n\n'  
    report += 'Total Active Products: ' + str(active_products) + '\n'  
    report += 'Products with Low Stock: ' + (', '.join(low_stock_items) if low_stock_items else 'None') + '\n'

    #Find cheapest and most expensive items
    if item_price_list:
        cheapest_name = item_price_list[0][0]
        cheapest_price = item_price_list[0][1]
        expensive_name = item_price_list[0][0]
        expensive_price = item_price_list[0][1]
        for name, price in item_price_list:
            if price < cheapest_price:
                cheapest_name = name
                cheapest_price = price
            if price > expensive_price:
                expensive_name = name
                expensive_price = price

        #Write in Monthly Report
        report += f'Lowest Priced Item: {cheapest_name} (RM{cheapest_price:.2f})\n'  
        report += f'Highest Priced Item: {expensive_name} (RM{expensive_price:.2f})\n'  
    else:
        report += 'No valid price data found.\n' 

    #Count total suppliers from inventory order sheet(excel)
    #set() function cannot be repeated, so can use to calculate number of supplier
    suppliers = set()  
    for row in ws2.iter_rows(min_row=4, values_only=True):  
        supplier = row[4]  
        if supplier:  
            suppliers.add(str(supplier))  
    report += f'Total Suppliers: {len(suppliers)}\n'  

    #Find the product with maximum stock 
    max_quantity = -1  
    best_stocked_item = '' 
    for row in ws.iter_rows(min_row=4, values_only=True):  
        name = row[2]  
        quantity = row[5]  
        if quantity and quantity > max_quantity:  
            max_quantity = quantity  
            best_stocked_item = name  
    if best_stocked_item:  
        report += f'Best Stocked Item: {best_stocked_item} ({max_quantity})\n' 

    #Check which product has the highest order count for fastest depleting
    order_count = {}  
    for row in ws2.iter_rows(min_row=4, values_only=True):  
        product = row[5]  
        quantity = row[6] if len(row) > 6 else None  
        if product and quantity:  
            order_count[product] = order_count.get(product, 0) + quantity  
    if order_count:  
        fastest_item = max(order_count, key=order_count.get)  
        report += f'Fastest-Depleting Item: {fastest_item} ({order_count[fastest_item]})\n'   

    f = open('Monthly_Report.txt','w')
    f.write(report)
    f.close()

    print('\n--------------Retail Plus----------------')
    print('Option : menu : |8| Generate report')
    print('='*60)
    print('Report generated successfully in "Monthly_Report.txt".')
