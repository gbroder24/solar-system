# Solar System App
![ Solar System image ](/documentation/images/ascii-art.PNG)
## The Solar System app is a personalized application for my domestic solar panel installation. Designed to log my housholds daily, monthly, yearly energy usage and view electrical utility bill savings based on my current rate. Programmed in the app is the display functionality where I can view what my daily, monthly energy use is, how much money I am saving per month. There is also a display to monitor how much you are paying back on the installed system.

### PP3 - Gary Broderick

------------------------------------------------------------------------------------
## [ **Live Site** ](https://solar-system-f54a8eac54d6.herokuapp.com/)
## [ **Repository** ](https://github.com/gbroder24/solar-system.git)

## User Stories

### Project Goals

+ Provide a CLI app that is clear, concise and the process flows effortlessly.
+ Provide a CLI app that logs daily energy usage and solar generation.
+ Provide a CLI app that has a robust input validation quality software system.
+ Provide a CLI app that displays data to the user in a meaningful way.  

### User Goals

+ I want to log my daily energy usage and solar generation in a user friendly process.  
+ I want to easily understand how to input my data.
+ I want to recieve clear feedback when I input correct / incorrect data. 
+ I want to view my data and have it displayed in a clear and easy to understand format.

### Color Palette

The following colors were chosen for the app and ensure contrast is achieved in the main parts of the CLI. Colorama has been imported in to the run.py file to apply color to the terminal text. It makes the algorithm more intuitive and easy to understand.

+ Yellow is used for indicating the solar system app program starting screen and welcoming message.
+ Blue is used for indicating headings and user prompts in the terminal.
+ Green is used for indicating success or valid input from the user.
+ Red is used for indicating no data available, errors or invalid input from the user.

## Data Model

### Google Sheets Integration

The Solar System application interacts with Google Sheets to store daily and monthly energy usage that is consumed and imported from the grid. Solar generation data is also stored with monthly savings and project payback data. Data is stored in a tabular format.

### Worksheet Structure

The Google Sheets document contains three worksheets. One for storing daily energy usage and generation. The second to total monthly energy usage, generation and savings. The third to total the payback on the solar panel installed system. Each worksheet has columns for different data such as date, consumed, exported, imported, month year, savings and payback. It also includes calculated functionality in the monthly and payback worksheets.

### Daily Energy Use Data

Each daily energy use data entry includes the date, consumed (in kilowatts), Export (in kilowatts), Import (in kilowatts).

### Monthly Data

Monthly data is calculated based on the daily energy usage accumulated data. Consumed data, which is generated, is subtracted by imported data from the grid, the value from this then has the rate you buy applied. The exported data to the grid has the rate you sell applied. The summed calculation is stored in the savings column for each month of the year.

### Payback Data

Payback data is calculated based on the monthly savings accumulated data. Monthly savings is subtracted by project data, which is input from the user. The resulting calculation is stored in the payback worksheet cell and displayed to the terminal for user feedback. The value indicates if the user is making a deficit or a profit on the system.

### Data Validation

The application includes functions to validate input data to ensure it conforms to expected formats. Functions included are validating daily data and project data.

### User Interaction

A user interacts with the application through a terminal command line interface. User provides input for daily and project data, viewing daily and monthly data. A user can track their monthly savings month by month, year by year and payback on their investment.

### Data Processing

Data functions are programmed for calculating data, formatting data for display in tabular form, updating the Google Sheets document with new daily entries, monthly and payback updates.

## Flowchart

The following process flowchart was designed using Lucidchart in order to plan the process logic to be implemented in the algorithm.

![ Solar System Flowchart ](/documentation/images/flowchart.png)

## List of Features

### Welcoming Message

The user is greeted with a welcoming message to the Solar System app and a brief high level overview description.

![ Solar System Welcome Message ](/documentation/images/welcome-msg.PNG)

### Main Menu

The user is presented with an ordered list, is prompted to choose from a list of five options and to input their choice.

![ Solar System Main Menu ](/documentation/images/main-menu.PNG)

### Enter Daily Energy Data

The user can enter daily energy data including the date, consumed (in kilowatts), Export (in kilowatts), Import (in kilowatts).

![ Solar System Enter Daily Data ](/documentation/images/input-daily-energy-data.PNG)

### View Daily Energy Data

The user can view their daily energy data directly from the terminal. Data is displayed in a table format, programmed using the import prettytable. Table headings included are the date, consumed (in kilowatts), Export (in kilowatts), Import (in kilowatts).

![ Solar System View Daily Data ](/documentation/images/view-daily-data.PNG)

### View Monthly Energy Data and Savings

The user can view their monthly energy data and savings directly from the terminal. Data is displayed in a table format, programmed using the import prettytable. Table headings included are the date, consumed (in kilowatts), Export (in kilowatts), Import (in kilowatts) and savings (in euros).

![ Solar System View Monthly Data ](/documentation/images/monthly-data.PNG)

### Enter Project Cost

The user is prompted to input the cost of their installed solar panel system.

![ Solar System Enter Project Cost ](/documentation/images/project-cost.PNG)

### View Updated Project Cost

The user can view their updated project cost data directly from the terminal. Data is displayed in a table format, programmed using the import prettytable. Table heading included is the payback (in euros).

![ Solar System View Project Cost ](/documentation/images/project-payback.PNG)

### Navigate Application

The user is presented with an ordered list, is prompted to choose from a list of two options and to input their choice. The user can navigate to the main menu or exit the program after viewing data tables.

![ Solar System Navigation ](/documentation/images/navigation-options.PNG)

### Exit Application

The user gets a confirmation message that is displayed in the terminal when exiting the program.

![ Solar System Exit ](/documentation/images/exit.PNG)

## Future Features

### Edit or Delete Daily Entries 

Allow the user to edit or delete daily entries. Provides the user with more functionality after entering their data incase the wrong data was entered.

### Input Energy Rate

Allow the user to input their current energy rate when the rate changes. Rates are currently volatile and providing this functionality offers more accuracy in calculating savings and project cost.

## Tools and Technologies

+ Python3.  
+ MarkDown Readme.md file.  
+ [ Github ](https://github.com/about) Repository.  
+ [ Gitpod ](https://www.gitpod.io/about) IDE.  
+ [ Git ](https://git-scm.com/about) Version control.  
+ [ W3schools ](https://www.w3schools.com/) Python tips.  
+ [ CI Python Linter ](https://pep8ci.herokuapp.com/#) to validate code to PEP8 standard.  
+ [ Heroku ](https://id.heroku.com/) to deploy the application.  
+ [ PrettyTable ](https://pypi.org/project/prettytable/) library was used to display the data in table format.  
+ [ Colorama ](https://pypi.org/project/colorama/) library was used to apply color to the terminal text.  
+ [ Gspread ](https://pypi.org/project/gspread/) library was used to interface for working with Google Sheets.  
+ [ Time ](https://pypi.org/project/time/) library was used for the conversion of given time input into proper format.  
+ [ Date Time ](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) library was used for the conversion of given date and time input into proper format.  
+ [ Os ](https://docs.python.org/3/library/os.html) library was used to interact with the operating system to clear the terminal screen.  
+ [ Credentials ](https://pypi.org/project/credentials/) library was used to install credentials.  
+ [ Default Dictionary ](https://docs.python.org/3/library/collections.html) library was used to create dictionary. 
+ [Lucidchart](https://www.lucidchart.com/pages/) was used to create the process flowchart.  