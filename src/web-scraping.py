"""
In the following steps, we are doing the Web Scraping for fetching the
details of the Organization.

Step 1: load imports
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

""" Step 2: creating object for Excel Sheet """
wb1 = Workbook()

"""Step 3 : creating Sheet in Excel"""
sheet1 = wb1.add_sheet('Sheet 1')

"""Step 4: Variables for Columns and Rows to handle the loop"""
col = 0
row = 0

"""Step 5: Variable for Path of Excel Sheet containing the dataset to used for Scraping"""
loc = ("~/git/git.c-w-m/nlp_dev/src/web_scraping/src/websites.xls")

""">Note: Google Chrome Version 88.0.4324.182 (Official Build) (64-bit)"""

"""Step 6: Variable for setting the test web browser drivers location"""
driver = webdriver.Chrome('/usr/bin/chromedriver')

"""Step 7: Workbook object to read the Dataset from excel"""
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

"""Step 8: traversing the Dataset"""
# Continue the Loop till end
for i in range(sheet.nrows):
    cin = sheet.cell_value(i, 0)
    name = sheet.cell_value(i, 1)

    # Step 9: URL that is to web scraped
    # HiddenData is the URL of website to be webscrapped
    # brackets ‘{ }’ represents the data for parameters to the website URL
    stuff_in_string = "https://HiddenData/{}/{}".format(name, cin)

    # Step 10: Sending data of URL to the Web browser
    driver.get(stuff_in_string)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Step 11: Data for actual Website Tags that has to scraped and Data has
    # to be fetched
    #
    # Example:
    # https://thinksproutinfotech.com
    # If we want to get the Thinksprout Infotech Name from my Organisation
    # website URL
    # Right Click on the Webpage — > click inspect (or Ctrl+Shift+I)

    content1 = soup.find('div', {"class": " elementor-widget-container"})
    article = ''

    # Step 12: Exporting Data to New Excel-Sheet
    # #another Loop in our previous for loop
    for i in content1.findAll('p'):
        article = i.text
        print(article)
        sheet1.write(row, col, article)
        wb1.save('data2.csv')
        row += 1

    # Step 13: Closing the Test Chrome Browser
    # #outside the second for loop i.e inside second first for loop
    driver.quit()

    # This Loop will continue until the whole data from the dataset is parsed.
