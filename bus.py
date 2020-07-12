import pandas as pd


redbus_data = pd.read_csv('redbus.csv')
print(redbus_data.head())

driver_data = pd.read_csv('driver.csv')
print(driver_data.head())