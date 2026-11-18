#Print Inventory Ordering System: To allow users to search for a specific inventory order, view its details and save it
#Programmer: Liew Jia Min
#Date: 11/09/2025

import pandas as pd

class RetailPlusOrder:
    def __init__(self, data_file): 
        self.data_file = data_file      # Initialise the system with the Excel file name
        self.orders = None              # Hold the DataFrame after loading


    def load_orders(self):
        try:                            # Read from Excel, starting from the 3rd row
            self.orders = pd.read_excel(self.data_file, sheet_name='Inventory_Order', header=2)          
            if self.orders is None or len(self.orders) == 0: # Show message while DataFrame is empty
                print('No order found.\n')
                return
            
        except PermissionError:          # Show error when Excel file is still open
            print(f'Cannot read "{self.data_file}", file may be open in Excel. Please close it first.\n')
            return
        
        except Exception:
            print('Error while reading order file.\n')
            return

    def get_order(self, order_no):
        if 'Order No' not in self.orders.columns:     # Check if required column exists
            print('"Order No" column not found. Columns are:', list(self.orders.columns))
            return

        order = self.orders[self.orders['Order No'] == order_no]      # Filter DataFrame where 'Order No' equals input

        if len(order) == 0:               # If no such order, show available order numbers
            print(f'Order {order_no} not found.\n')

            lst = []
            for v in self.orders['Order No']:
                if str(v) != 'nan' and v not in lst:
                    lst.append(v)
            print('Available orders:', lst)
            return
        return order.iloc[0]              # Return the first matched row (Series object)

    def print_order(self, o):
        remarks = o['Remarks']
        if str(remarks) == 'nan':         # replace nan with blank
            remarks = ''
            
        print(f'Order No    : {o["Order No"]}')
        print(f'Date        : {str(o["Date"])[:10]}')
        print(f'Time        : {o["Time"]}')
        print(f'Supplier ID : {o["Supplier ID"]}')
        print(f'Supplier    : {o["Supplier Name"]}')
        print(f'Product     : {o["Product"]}')
        print(f'Amount      : {o["Amount"]}')
        print(f'Payment     : {o["Payment Method"]}')
        print(f'Status      : {o["Order Status"]}')
        print(f'Remarks     : {remarks}\n')
            
    def save_all_orders(self):
        filename = 'All_Inventory_Orders.txt'
        try:
            f = open(filename, 'w', encoding='utf-8')   # overwrite instead of append
            f.write('--- Retail Plus - All Inventory Orders ^_^ ---\n\n')

            # Define headers (columns you want in the report)
            headers = ['Order No', 'Date', 'Time', 'Supplier ID', 'Supplier Name', \
                       'Product', 'Amount', 'Payment Method', 'Order Status', 'Remarks']
            
            # Define column widths (adjust as needed so table looks neat)
            col_widths = [10, 12, 12, 12, 18, 15, 8, 15, 15, 15]

            # Build header row
            header_row = ''
            for i in range(len(headers)):
                header_row += headers[i].ljust(col_widths[i])
            f.write(header_row + '\n')
            f.write('-' * sum(col_widths) + '\n')

            # Write each order as a row
            for _, o in self.orders.iterrows():
                remarks = o['Remarks']
                if str(remarks) == 'nan':
                    remarks = ''

                row_text = (str(o['Order No']).ljust(col_widths[0]) +
                            str(o['Date'])[:10].ljust(col_widths[1]) +
                            str(o['Time']).ljust(col_widths[2]) +
                            str(o['Supplier ID']).ljust(col_widths[3]) +
                            str(o['Supplier Name']).ljust(col_widths[4]) +
                            str(o['Product']).ljust(col_widths[5]) +
                            str(o['Amount']).ljust(col_widths[6]) +
                            str(o['Payment Method']).ljust(col_widths[7]) +
                            str(o['Order Status']).ljust(col_widths[8]) +
                            remarks.ljust(col_widths[9]))
                
                f.write(row_text + "\n")

            f.close()
            print(f'\nAll orders have been exported as a report to "{filename}".\n')

        except Exception:
            print('Error while saving all orders.')

        
    def run(self):                              #Main menu
        print('\n--------------Retail Plus----------------')
        print('option : menu : |7| Print Inventory Ordering System')
        print('=' * 60)

        self.load_orders()                        # Load Excel orders
        if self.orders is None or len(self.orders) == 0:
            return

        print('-' * 60)
        print('Retail Plus Inventory Order ')
        print('-' * 60)

        while True:                                  #Option
            print('Options:')
            print('1. Print all orders to text file')
            print('2. Search and print the order')
            print('0. Quit\n')

            try:
                choice = int(input('Enter your option: '))

                if choice == 0:                       #Return back to main menu
                    return   
 
                elif choice == 1:                     #Save all inventory orders
                    self.save_all_orders()
  
                elif choice == 2:                     #Choose the specific order you want
                    try:
                        order_no = int(input('Enter Order No: '))
                    except ValueError:
                        print('Invalid input. Please try again.\n')
                        continue

                    o = self.get_order(order_no)       # Get the order
                    if o is None:
                        continue
                
                    self.print_order(o)                # Print and save order

                else:
                    print('Invalid option. Please try again.\n')

            except ValueError:
                print('Invalid input. Please try again.\n')
                           
def print_o(data_file):
    system = RetailPlusOrder(data_file)
    system.run()
