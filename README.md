# RowDeletionScripts
Scripts for deleting specific rows in CSV and Excel files based on cell values.

This repository hosts two scripts designed for deleting specific rows in CSV and Excel files. The Python script is used for CSV files, while the VBA (Visual Basic for Applications) script is tailored for Excel files. Both scripts target rows where the last column's evaluated value is equivalent to '1'.

## Features
- **Python Script:** Removes rows in a CSV file where the last column's value is '=1.0/1.0'.
- **VBA Script:** Deletes rows in an Excel sheet where the last column's evaluated formula equals 1.

## Getting Started

### Prerequisites for Python Script
- Python 3.x
- pandas library, can be installed via pip:
- pip install pandas
  
### Using the Python Script
1. **Load the CSV file** into the script by specifying the file path.
2. **Run the script** to filter out and remove specific rows.
3. **The modified CSV file** is saved, excluding the specified rows.

### Prerequisites for VBA Script
- Microsoft Excel with VBA support.

### Using the VBA Script
1. **Open the Excel workbook** where you need to delete rows.
2. **Press Alt + F11** to open the VBA editor.
3. **Insert a new module** and paste the VBA script into it.
4. **Run the script** to delete rows where the last column's evaluated formula equals 1.

## Contributing
Contributions to enhance these scripts are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Contact
For any queries or contributions, please open an issue in the GitHub repository.


