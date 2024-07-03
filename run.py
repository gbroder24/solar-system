import gspread
from google.oauth2.service_account import Credentials

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
    print("Please enter daily energy use data from yesterday.")
    print("Format: Day, Month, Year, Consumed (kW), Export (kW), Import (kW)")
    print("Example: 3,June,2024,6,-11,8\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_daily_data()