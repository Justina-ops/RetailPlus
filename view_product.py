#View product: To allow staff to view the current product inventory with sorting and ordering options
#Programmer: Yew Kai Qian
#Date: 27/08/2025

def view_inv(df):
      print('\n--------------Retail Plus----------------')
      print('Option : menu : |2| View inventory')
      print('='*60)
      
      #Truncate long name and description for better display  
      for i in range(len(df)):
          #If name is longer than 10 characters, show only the first 10 characters followed by '...'
          if len(df.loc[i, 'Name']) > 10:
              df.loc[i, 'Name'] = df.loc[i, 'Name'][:10] + '...'
              
          #If description is longer than 10 characters, show only the first 10 characters followed by '...'
          if len(df.loc[i, 'Description']) > 10:
              df.loc[i, 'Description'] = df.loc[i, 'Description'][:10] + '...'
                    
 
      #Loop to let the user view the product inventory with sorting options 
      while True:
            print('Sort by:')
            print('0. Quit\n1. Default\n2. Category\n3. Name\n4. Price\n5. Stock Quantity\n6. Promotion Status')
            print()
            try:
                  opt = int(input('Please select an option: '))
                  print()
                  if opt == 0:
                      #Exit the loop
                      break
                  
                  elif opt == 1:
                        #Print the original data frame
                        print(df)
                        break
                  
                  elif opt in (2,3,4,5,6):
                      #Map user input(sort by option) to corresponding column name
                      col_name = {2: 'Category', 3: 'Name', 4: 'Price', 5: 'Stock Quantity', 6: 'Promotion Status'}
                      col = col_name[opt]
                  
                      while True:
                          print('Order by:')
                          print('1. Ascending\n2. Descending')
                          print()
                          try:
                                order = int(input('Please select an option: '))
                                print()
                                if order == 1:
                                    #Sort data frame by the selected column(col) in ascending order
                                    #reset_index is used to reset the index of the DataFrame after sorting, and use the default one instead. 
                                    #drop = True prevents the old index from being added as a column
                                    print(df.sort_values(by = col, ascending = True).reset_index(drop = True))
                                    break
                              
                                elif order == 2:
                                    #Sort data frame by the selected column(col) in descending order
                                    print(df.sort_values(by = col, ascending = False).reset_index(drop = True))
                                    break
                              
                                else:
                                      #Make sure user input either 1 or 2
                                      print('Please input either 1 or 2.\n')
                                      continue
                                    
                          #Prevent system crash if user input non numeric value
                          except ValueError:
                                print('\nPlease enter a numeric value.\n')  
                                continue
                      #Exit inner loop after successful display
                      break

                  else:
                        #Make sure user input either 0/1/2/3/4/5/6
                        print('\nPlease input either 0/1/2/3/4/5/6.\n')
                        continue
                  
            #Prevent system crash if user input non numeric value      
            except ValueError:
                  print('\nPlease enter a numeric value.\n')  
    
       

