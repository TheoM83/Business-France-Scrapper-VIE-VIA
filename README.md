# Business-France_VIE_Scrapper
 Create an html file that can be easely searched referencing all actual VIE/VIA offers



# Description
This Python script, vie.py, is designed to perform a specific task related to processing job offers. It serves the purpose of extracting data from an HTML file containing job offers and presenting it in a readable format.

# Installation
Before running the script, ensure you have Python installed on your system. Additionally, make sure to install the required dependencies using pip:

pip install -r requirements.txt
Usage
To launch the application, execute the following command in your terminal or command prompt:

python .\vie.py -h       
usage: vie.py [-h] total_offers output_file

Script to retrieve offers from an API and save them to a CSV or HTML     
file.

positional arguments:
  total_offers  Total number of offers to retrieve
  output_file   Output file name (with extension)

options:
  -h, --help    show this help message and exit


# Example
python vie.py 3000 offres.html
This command will launch the application, making it accessible at http://localhost:3000.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or bug fixes.

# Disclaimer
This script is provided as is, without any warranty. Use it at your own risk.