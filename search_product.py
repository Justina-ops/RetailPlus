#Extra Work
#Search Product: Extra function to allow staff to search for specific products they want to view and show information of the product.
#Programmer: Yew Kai Qian
#Date: 06/09/2025

def search_p(df):
    print('\n------------------------Retail Plus-------------------------')
    print('Option : menu : |3| Search product')
    print('='*60)

    #Truncate long name and description for better display  
    for i in range(len(df)):
        #If name is longer than 10 characters, show only the first 10 characters followed by '...'
        if len(df.loc[i, 'Name']) > 10:
            df.loc[i, 'Name'] = df.loc[i, 'Name'][:10] + '...'
          
        #If description is longer than 10 characters, show only the first 10 characters followed by '...'
        if len(df.loc[i, 'Description']) > 10:
            df.loc[i, 'Description'] = df.loc[i, 'Description'][:10] + '...'

    while True:
        print('Search by:')
        print('0. Quit\n1. Product ID\n2. Category\n3. Name\n4. Promotion Status\n5. Stock-level\n')
        try:
            opt = int(input('Please select an option (0-5): '))
            if opt == 0:
                break
            
            elif opt == 1:
                try:
                    ID = int(input('\nPlease enter a product ID: '))
                    result = df[df['Product ID'] == ID]

                    if len(result) == 0: 
                        print('\nNo product found with this ID.\n')
                    else:
                        #reset_index is used to reset the index of the DataFrame after sorting,
                        #and use the default one instead. 
                        #drop = True prevents the old index from being added as a column
                        print('\n', result.reset_index(drop = True), '\n')
                        break
                        
                except ValueError:
                    print('\nPlease enter a numeric value.\n')
                    
            elif opt == 2:
                category = input('\nCategory(Snacks / Beverages / Hygiene / Stationery): ').strip().capitalize()                
                if category == '': #make sure category is not empty
                  print('\nCategory cannot be empty.\n')
                  continue
                #make sure user input either Snacks / Beverages / Hygiene / Stationery
                elif category not in ['Snacks', 'Beverages', 'Hygiene', 'Stationery']:  
                  print('\nPlease enter either Snacks / Beverages / Hygiene / Stationery.\n')
                  continue
                
                result = df[df['Category'] == category]
                if len(result) == 0:
                    print('\nNo product found with this category.\n')
                else:
                    print('\n', result.reset_index(drop = True), '\n')
                    break

            elif opt == 3:
                name = input('\nPlease enter a product name: ').strip().capitalize()                
                if name == '': #make sure name is not empty
                  print('\nName cannot be empty.\n')
                  continue
                  
                result = df[df['Name'] == name]
                if len(result) == 0:
                    print('\nNo product found with this name.\n')
                else:
                    print('\n', result.reset_index(drop = True), '\n')
                    break
                    
            elif opt == 4:
                promotion = input('\nPromotion status(Y/N): ').strip().upper()                
                if promotion == '': #make sure promotion status is not empty
                  print('\nPromotion status cannot be empty.\n')
                  continue
                elif promotion not in ['Y', 'N']: #make sure user input either Y or N
                  print('\nPlease enter either Y or N.\n')
                  continue
                
                result = df[df['Promotion Status'] == promotion]
                if len(result) == 0:
                    print('\nNo product found with this promotion status.\n')
                else:
                    print('\n', result.reset_index(drop = True), '\n')
                    break
            
            elif opt == 5:
                stock = input('\nStock-level(Out of stock/Low/Medium/High): ').strip().lower()               
                if stock == '': #make sure stock-level is not empty
                  print('\nStock-level cannot be empty.\n')
                  continue
                #make sure user input either Out of stock/Low/Medium/High
                elif stock not in ['out of stock', 'low', 'medium', 'high']: 
                  print('\nPlease enter either Out of stock/Low/Medium/High.\n')
                  continue
                
                result = df[df['Stock-level'].str.lower() == stock]
                if len(result) == 0:
                    print('\nNo product found with this stock-level.\n')
                else:
                    print('\n', result.reset_index(drop = True), '\n')
                    break

            else:
                print('\nPlease enter either 0/1/2/3/4/5\n')
                    
        except ValueError:
            print('\nPlease enter a numeric value.\n')

             
           
                

                        
                        
        
