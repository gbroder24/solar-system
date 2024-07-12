# Solar System App
![Solar System image](/documentation/images/ascii-art.PNG)
## The Solar System app is a personalized application for my domestic solar panel installation. Designed to log my housholds daily, monthly, yearly energy usage and view electrical utility bill savings based on my current rate. Programmed in the app is the display functionality where I can view what my daily, monthly energy use is, how much money I am saving per month. There is also a display to monitor how much you are paying back on the installed system.

### PP3 - Gary Broderick

------------------------------------------------------------------------------------
## [**Live Site**](assets/readme-files/welcome.png)
## [**Repository**](https://github.com/gbroder24/solar-system.git)

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

![Solar System Flowchart](/documentation/images/flowchart.png)