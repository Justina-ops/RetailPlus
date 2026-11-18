#Main menu: To navigate user to the specify function according to the code entered. 
#Programmer: Chan Yi Yang 
#Date: 27/08/2025

import register
import login
import add_product
import view_product
import search_product
import edit_product
import delete_product
import inventory_ordering_system
import print_inventory_ordering_system
import generate_report
import datetime
import warnings
import pandas as pd

warnings.filterwarnings('ignore', category = UserWarning, module = 'openpyxl')
from openpyxl.styles import Alignment, Font
from openpyxl import load_workbook
data_file = 'RetailPlus.xlsx'
wb = load_workbook(data_file)
ws = wb['Product_Inventory']
ws2 = wb['Inventory_Order']
cols = [0,1,2,3,4,5,6,7]

register.register()
login.login()

def menu():
    
    while True:
        print('Retail Plus Inventory System')
        print('001 - Add new product\n002 - View current inventory\n003 - Search product\n004 - Edit product information\n005 - Delete product\n006 - Inventory ordering\n007 - Print inventory order\n008 - Generate monthly report\n009 - Exit system')
        print()
        
        code=input('Enter code(001-009): ')
        
        if code == '001':
            add_product.add_p(ws,wb,data_file)
            
        elif code == '002':
            df = pd.read_excel(data_file, sheet_name = 'Product_Inventory', header = 2, usecols = cols)
            
            #Display all columns and rows, and adjust the display width to avoid truncation
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)  
            pd.set_option('display.width', None)
            view_product.view_inv(df)

        elif code == '003':
            df = pd.read_excel(data_file, sheet_name = 'Product_Inventory', header = 2, usecols = cols)
            #Display all columns and rows, and adjust the display width to avoid truncation
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)  
            pd.set_option('display.width', None)            
            search_product.search_p(df)
            
        elif code == '004':
            edit_product.edit_p(ws, wb, data_file)
            
        elif code == '005':
            delete_product.delete_p(ws, wb, data_file)
            
        elif code == '006':
            info = pd.read_excel(data_file, header=2, sheet_name='Product_Inventory')
            info1 = pd.read_excel(data_file, header=2, sheet_name='Inventory_Order')
            day = datetime.date.today()
            time = datetime.datetime.now().time()
            inventory_ordering_system.next_available_row(ws2, start_row=4)
            inventory_ordering_system.order_sys(info, info1, ws2, wb, data_file, day, time, Alignment, Font) 
                       
        elif code == '007':
            print_inventory_ordering_system.print_o(data_file)
            
        elif code == '008':
            generate_report.inv_report(ws, ws2, wb, data_file)
            
        elif code == '009':
            print('Thank you for using ^_^ ---> Exiting')           
            break
        
        else:
            print('Invalid input')
            print('='*60)

        print()    
            
menu()

        



    



    
        
    
