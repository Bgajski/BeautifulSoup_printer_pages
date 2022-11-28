from datetime import date, datetime
from bs4 import BeautifulSoup
import requests
import csv

# printers:
printers = [
    'Printer_1'
]

for printer in printers:
    printer_01 = requests.session()

    # credentials:  
    payload_printer = {
        'i0017': '2',   # search the fields that indicates administrator number on the web interface        
        'i0019': '',    # enter password
    }

    Data = []

    # get data:
    printer_Enter01 = printer_01.post('', data=payload_printer)  # Enter ip address
    printer_Data01 = printer_01.get('')

    # parse data:
    parse_01 = BeautifulSoup(printer_Data01.content, 'lxml')

    # search tables and rows:
    search_Count01 = parse_01.find('div', attrs={'class': 'ModuleElement'})
    table_01 = search_Count01.find('tbody')
    rows_01 = search_Count01.find_all('tr')

    # open list with today's date:
    date = date.today()
    today_date = datetime.now().strftime('%m.%y')
    file_name = open('report_printed_' + today_date + '.csv', 'w')

    # write data into list:
    writer = csv.writer(file_name)
    writer.writerow(['Printer | Printed'])

    # loop trough tables and rows, strip and write data:
    for row in rows_01[0:2]:
        column_printed_01 = row.find_all('td')
        column_printed_01 = [ele.text.strip() for ele in column_printed_01]
        column_01 = ['Printer_1']
    writer.writerow([column_01, column_printed_01])

file_name.close()
