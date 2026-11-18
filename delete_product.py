#Delete Product: Check records in excel and delete product record to the need
#Programmer: Leong Di Hao
#Date: 27/08/2025

def delete_p(ws,wb,data_file):
    print('\n--------------Retail Plus----------------')
    print('Option : menu : |5| Delete product')
    print('='*60)

    #Check records in excel
    print('Records:')
    for row in ws.iter_rows(min_row=4, max_row=ws.max_row, values_only=True): #Check start from fourth line for accuracy
        print(row[0], row[1], row[2])

    while True:
        #Enter product id which one want to delete 
        del_ID = input('Select Product ID or type "exit" to delete: ').strip()
        if del_ID.lower() == 'exit':
            print('Delete operation cancelled.')
            return
        
        if not del_ID:#Input of delete id cannot be empty
            print('DEL_ID cannot be empty. Please try again')
            continue
        
        if not del_ID.isdigit():#Input of  delete id cannot be alphabet or special symbols(example:@,%)
            print('DEL_ID must be number. Please try again')
            continue
        
        del_ID = int(del_ID)

        #Check the delete id(Input) can be find or not in excel records
        #For loop function is use to read records in excel and ensure that must be read start from fourth line
        exists = any(row[0] == del_ID for row in ws.iter_rows(min_row=4, max_row=ws.max_row, values_only=True))
        if not exists:
            print('DEL_ID not found. Please try again"')
            continue
        break

    row_idx = 4
    while row_idx <= ws.max_row: #While loop function is read all records
        #If else function check which one product id is same with delete id(Input)
        if ws.cell(row=row_idx, column=1).value == del_ID: 
            ws.delete_rows(row_idx, 1)
        else: 
            row_idx += 1

    try:
        wb.save(data_file)
        print(f'Product ID {del_ID} is deleted.')
    except PermissionError:
        print(f'Could not save "{data_file}". Please make sure the file is closed in Excel and try again.')


