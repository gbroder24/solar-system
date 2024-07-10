import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from collections import defaultdict
import prettytable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('solar_system')


def view_daily_data():
    """
    View daily data from the terminal.
    """
    print("Viewing daily data...\n")
    daily_worksheet = SHEET.worksheet("daily")
    data = daily_worksheet.get_all_values()
    for row in data:
        print(", ".join(row))  # Print each row of daily data
    print("\n")


def get_daily_data():
    """
    Get daily figures input from the user.
    """
    while True:
        print("Please enter daily energy use data.\n")
        print("Format: Day Month Year, Consumed (kW), Export (kW), Import (kW).\n")
        print("Example: 3 Jun 2024, 5.154, 20.698, 6.354\n")

        data_str = input("Enter your data here: \n")
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

    # Validate duplicate date format (Day Month Year)
    daily_date = datetime.strptime(values[0].strip(), "%d %b %Y")
    daily = SHEET.worksheet("daily")
    dates = daily.col_values(1)
    new_dates_list = dates[1:]
    count = new_dates_list.count(values[0])

    if count == 1:
        print(f"Duplicate date entered, you provided {values[0]}.\n")
        return False

    # Validate date format (Day Month Year)
    try:
        daily_date = datetime.strptime(values[0].strip(), "%d %b %Y")
    except ValueError:
        print("Invalid date format. Please use Day Month Year format.")
        print("(e.g., 3 Jun 2024).\n")
        return False
    
    # Validate daily energy data (Consumed (kW), Export (kW), Import (kW))
    try:
        new_list = values[1:]
        [float(value) for value in new_list]
    except ValueError as e:
        print(f"Invalid data: {e}.\n")
        print("Invalid energy data. Please enter a valid number.\n")
        return False

    return True
    

def validate_project_data(data):
    """
    Validate project data input.
    """

    # Validate project data format (€)
    try:
        val_list = data[0]
        [float(value) for value in val_list]
    except ValueError:
        print("\nInvalid project data format. Please use correct format.")
        print("(e.g., 1000.00).\n")
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


def calculate_month():
    """
    Calculate month based on the daily data.
    """
    print("Calculating monthly data...\n")
    daily_worksheet = SHEET.worksheet("daily")
    daily_data = daily_worksheet.get_all_values()[1:]  # Skipping header row
    grouped_data = defaultdict(lambda: {
        "consumed": 0,
        "exported": 0,
        "imported": 0,
        "count": 0
    })

    # Group data by month and calculate total energy use
    for row in daily_data:
        date_str = row[0].strip()
        # Adjust date string to include the day if only month is provided
        if len(date_str.split()) == 1:
            date_str = f"1 {date_str}"  # Assuming first day of the month
        daily_date = datetime.strptime(date_str, "%d %b %Y")
        month_year = daily_date.strftime("%B %Y")
        consumed = float(row[1])
        exported = float(row[2])
        imported = float(row[3])
        grouped_data[month_year]["consumed"] += consumed
        grouped_data[month_year]["exported"] += exported
        grouped_data[month_year]["imported"] += imported
        grouped_data[month_year]["count"] += 1

    for month_year, info in grouped_data.items():
        consumed = info["consumed"]
        exported = info["exported"]
        imported = info["imported"]
        monthly_saving = ((consumed - imported) * 0.2887) + (exported * 0.24)
        grouped_data[month_year]["savings"] = monthly_saving

    return grouped_data
        
    
def update_monthly_worksheet():
    """
    Update the monthly sheet with the calculated month data.
    """
    monthly = SHEET.worksheet("monthly")

    # Calculate progress
    month_data = calculate_month()
    
    print("Updating monthly worksheet...\n")

    month_list = []
    
    # Update monthly sheet for each month
    for month_year, info in month_data.items():
        month_list.append(month_year)
        monthly.update([[a] for a in month_list], "A2")
        month_cells = monthly.findall(month_year)
        if month_cells:
            row_index = month_cells[0].row
            monthly.update_cell(row_index, 2, info["consumed"])
            monthly.update_cell(row_index, 3, info["exported"])
            monthly.update_cell(row_index, 4, info["imported"])
            monthly.update_cell(row_index, 5, info["savings"])
        else:
            print(f"Error: Month {month_year} not found in progress sheet.")
            
    print("Monthly worksheet updated successfully.\n")


def calculate_project_payback():
    """
    Calculate project payback based on available data.
    """
    monthly = SHEET.worksheet("monthly")
    values = monthly.col_values(5)
    new_values = values[1:]
    nums_list = [float(value) for value in new_values]
    month_savings = [num for num in nums_list]
    total_months = sum(month_savings)
    
    while True:
        print("Please enter project cost.\n")
        print("Format: Project Cost (€).\n")
        print("Example: 5000.00\n")
        project_str = input("Enter your data here: \n")
        #validate input project str
        if validate_project_data(project_str):
            print('\nProject data is valid.\n')
            break
 
    print("Calculating project payback...\n")

    payback = total_months - float(project_str)

    return payback


def update_payback_worksheet(data):
    """
    Update payback worksheet.
    """
    payback_worksheet = SHEET.worksheet("payback")

    payback_list = []
    
    print("Updating payback worksheet...\n")

    # Update payback sheet
    payback_list.append(data)
    payback_worksheet.update([[val] for val in payback_list], "A2")
    
    print("Payback worksheet updated successfully.\n")


def display_daily_data(data):
    """
    Display daily data with a brief overview.
    """
    print("Here is your daily data:")
    print("Date: The date of your entered daily data.")
    print("Consumed (kW): The energy consumed during "
          "the day, in kilowatts.")
    print("Exported (kW): The energy exported to the grid "
          "during the day, in kilowatts.")
    print("Imported (kW): The energy imported from the grid "
          "during the day, in kilowatts.")

    if len(data) > 1:
        print("\n")  # Add a newline above the table
        table = prettytable.PrettyTable([
            "Date",
            "Consumed (kW)",
            "Exported (kW)",
            "Imported (kW)"
            ])
        for row in data[1:]:
            table.add_row(row)
        print(table)
        print()  # Add a single newline below the table

        while True:
            print("\nWhat would you like to do next?")
            print("1. Back to main menu")
            print("2. Exit")
            choice = input("Enter your choice (1 or 2): \n")
            print()

            if choice == '1':
                return 'main_menu'
            elif choice == '2':
                return 'exit'
            else:
                print("Invalid choice. Please enter either 1 or 2.")
    else:
        print("No daily data available.")
        return 'main_menu'


def display_month_data(data):
    """
    Display monthly data with a brief overview.
    """
    print("Here is your monthly data:")
    print("Month Year: The month and year of energy data.")
    print("Consumed (kW): The energy consumed during "
          "the month, in kilowatts.")
    print("Exported (kW): The energy exported to the grid "
          "during the month, in kilowatts.")
    print("Imported (kW): The energy imported from the grid "
          "during the month, in kilowatts.")
    print("Savings (€): The savings calculated during the month, in euros.")
          

    if len(data) > 1:
        print("\n")  # Add a newline above the table
        table = prettytable.PrettyTable([
            "Month Year",
            "Consumed (kW)",
            "Exported (kW)",
            "Imported (kW)",
            "Savings (€)"
            ])
        for row in data[1:]:
            table.add_row(row)
        print(table)
        print()  # Add a single newline below the table

        while True:
            print("\nWhat would you like to do next?")
            print("1. Back to main menu")
            print("2. Exit")
            choice = input("Enter your choice (1 or 2): \n")
            print()

            if choice == '1':
                return 'main_menu'
            elif choice == '2':
                return 'exit'
            else:
                print("Invalid choice. Please enter either 1 or 2.")
    else:
        print("No monthly data available.")
        return 'main_menu'


def display_project_data(data):
    """
    Display project data with a brief overview.
    """
    print("Here is your project data:")
    print("Payback (€): The balance of your project data, in euros.")

    if data:
        print("\n")  # Add a newline above the table
        table = prettytable.PrettyTable([
            "Payback (€)"
            ])
        
        table.add_row([data])
        print(table)
        print()  # Add a single newline below the table

        while True:
            print("\nWhat would you like to do next?")
            print("1. Back to main menu")
            print("2. Exit")
            choice = input("Enter your choice (1 or 2): \n")
            print()

            if choice == '1':
                return 'main_menu'
            elif choice == '2':
                return 'exit'
            else:
                print("Invalid choice. Please enter either 1 or 2.")
    else:
        print("No project data available.")
        return 'main_menu'


def print_menu():
    """
    Print the main menu options.
    """
    print("Main Menu:")
    print("1. Enter daily data")
    print("2. View daily data")
    print("3. View monthly data")
    print("4. Enter and View project payback")
    print("5. Exit")


def main():
    """
    Run all program functions
    """
    print("Welcome to Solar System Data Automation app!\n")
    print("The Solar System Data Automation app serves as my dedicated tool for\n"
          "logging and tracking my households daily and monthly energy use,\n"
          "savings and payback on the installed system.\n")


    while True:
        print_menu()
        choice = input("\nEnter your choice (1, 2, 3, 4 or 5): \n")
        print()


        if choice == '1':
            daily_energy_data = get_daily_data()
            str_list = daily_energy_data[1:]
            num_list = [float(value) for value in str_list]
            new_daily_list = []
            new_daily_list.append(daily_energy_data[0])
            new_daily_list.extend(num_list)
            update_daily_worksheet(new_daily_list)
            update_monthly_worksheet()


        elif choice == '2':
            daily_data = SHEET.worksheet("daily").get_all_values()
            action = display_daily_data(daily_data)
            if action == 'exit':
                print("Exiting the Solar System Data Automation App. Goodbye!")
                break


        elif choice == '3':
            month_data = SHEET.worksheet("monthly").get_all_values()
            action = display_month_data(month_data)
            if action == 'exit':
                print("Exiting the Solar System Data Automation App. Goodbye!")
                break


        elif choice == '4':
            project_data = calculate_project_payback()
            update_payback_worksheet(project_data)
            action = display_project_data(project_data)
            if action == 'exit':
                print("Exiting the Solar System Data Automation App. Goodbye!")
                break


        elif choice == '5':
            print("Exiting the Solar System Data Automation App. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")

    
main()