# Egyptian National ID Analyzer

This Python script analyzes **Egyptian National IDs** to extract personal information such as the date of birth, gender, governorate of birth, and birth sequence. It also checks if the ID is valid.

## Features

- **ID Validation**: Ensures the entered National ID is 14 digits long.
- **Date of Birth Extraction**: Determines the exact date of birth from the ID.
- **Gender Identification**: Identifies the gender based on the ID.
- **Governorate Identification**: Maps the governorate code to the corresponding governorate name.
- **Birth Sequence**: Displays the birth order on the given date.
- **Calendar View**: Shows a calendar for the birth month and year.
- **Age Calculation**: Calculates the user's current age as of 2024.

## How It Works

The script processes the National ID through several steps:
1. **Input**: The user enters their **name** and **National ID**.
2. **Validation**: The script checks if the ID is valid (14 digits).
3. **Information Extraction**:
   - Extracts the **date of birth**, **gender**, and **governorate**.
   - Displays the **birth sequence** for that specific day.
   - Shows a **calendar** of the birth month and year.
   - Calculates the **user's age**.
