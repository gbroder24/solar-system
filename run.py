import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('solar_system')


def get_daily_data():
    """
    Get daily figures input from the user.
    """
    while True:
        print()
        print("Please enter daily energy use data from yesterday.\n")
        print("Format: Day Month Year, Consumed (kW), Export (kW), Import (kW).\n")
        print("Example: 3 Jun 2024, 5, 20, 6\n")

        data_str = input("Enter your data here: ")
        print()

        daily_data = data_str.split(",")
        
        if validate_daily_data(daily_data):
            print('Data is valid.\n')
            break
    
    return daily_data


def validate_daily_data(values):
    """
    Validate daily data input.
    """
    if len(values) != 4:
        print(f"Exactly 4 values required, you provided {len(values)}.")
        return False
    
    # Validate workout date format (Day Month Year)
    try:
        daily_date = datetime.strptime(values[0].strip(), "%d %b %Y")
    except ValueError:
        print("Invalid date format. Please use Day Month Year format.")
        print("(e.g., 3 Jun 2024).")
        return False
    
    # Validate daily energy data (Consumed (kW), Export (kW), Import (kW))
    try:
        new_list = values[1:]
        [int(value) for value in new_list]
    except ValueError as e:
        print(f"Invalid data: {e}.\n")
        print("Invalid energy data. Please enter a valid number.")
        return False

    return True


def update_daily_worksheet(data):
    """
    Update daily worksheet, add new row with the list data provided
    """
    print("Updating daily worksheet...\n")
    daily_worksheet = SHEET.worksheet("daily")
    daily_worksheet.append_row(data)
    print("Daily worksheet updated successfully.\n")


def update_monthly_worksheet(data):
    """
    Update monthly worksheet, add new row with the list data provided
    """
    print("Updating monthly worksheet...\n")
    monthly_worksheet = SHEET.worksheet("monthly")
    monthly_worksheet.append_row(data)
    print("Monthly worksheet updated successfully.\n")


def calculate_monthly_worksheet(daily_row):
    """
    Calculate monthly energy use
    """
    print("Calculating monthly data...\n")
    
    monthly = SHEET.worksheet("monthly").get_all_values()
    monthly_row = monthly[-1]
    new_monthly_row = monthly_row[1:]
    new_daily_row = daily_row[1:]

    monthly_data = []
    for month, day in zip(new_monthly_row, new_daily_row):
        month_data = int(month) + day
        monthly_data.append(month_data)
    
    return monthly_data


def calculate_monthly_savings(month_row):
    """
    Calculate monthly savings
    """
    print("Calculating monthly savings...\n")
    monthly = SHEET.worksheet("monthly").get_all_values()
    monthly_row = monthly[-1]
    str_month = monthly_row[1:]
    monthly_num = [int(value) for value in str_month]
    consumed = monthly_num[0]
    exported = monthly_num[1]
    imported = monthly_num[2]
    
    grid = (consumed - imported) * 0.2287
    saving = grid + (exported * 0.24)
    print(f"This months's savings:  €{saving}")


def main():
    """
    Run all program functions
    """
    daily_energy_data = get_daily_data()
    str_list = daily_energy_data[1:]
    num_list = [int(value) for value in str_list]
    new_daily_list = []
    new_daily_list.append(daily_energy_data[0])
    new_daily_list.extend(num_list)
    update_daily_worksheet(new_daily_list)
    new_monthly_data = calculate_monthly_worksheet(new_daily_list)
    monthly_list = []
    monthly_list.append(daily_energy_data[0])
    monthly_list.extend(new_monthly_data)
    update_monthly_worksheet(monthly_list)
    calculate_monthly_savings(monthly_list)
    


print("Welcome to Solar System Data Automation")
main()