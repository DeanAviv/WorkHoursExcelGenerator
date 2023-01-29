import xlwt
from datetime import datetime, timedelta

def generate_excel_sheet(month, year):
    # Create a new workbook
    workbook = xlwt.Workbook()

    # Add a new sheet to the workbook
    sheet = workbook.add_sheet('Sheet1')

    # Write the header row
    sheet.write(0, 0, 'Day')
    sheet.write(0, 1, 'Date')
    sheet.write(0, 2, 'Work Hours')

    # Set the default work hours
    work_hours = 9

    # Calculate the number of days in the given month and year
    num_days = (datetime(year, month + 1, 1) - datetime(year, month, 1)).days

    # Keep track of the current row in the sheet
    current_row = 1

    # Write the data for each day of the month
    for i in range(num_days):
        # Calculate the date for this day
        date = datetime(year, month, 1) + timedelta(days=i)

        # Skip weekends (Saturday and Sunday)
        if date.weekday() not in [4, 5]:
            day_name = date.strftime('%A')
            sheet.write(current_row, 0, day_name)
            sheet.write(current_row, 1, date.strftime('%b %d, %Y'))
            sheet.write(current_row, 2, work_hours)
            current_row += 1

    # Save the workbook to a file
    workbook.save(f'{month}-{year}.xls')

# Example usage
generate_excel_sheet(1, 2023)
