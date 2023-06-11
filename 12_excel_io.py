# reading an excel file
import pandas
df = pandas.read_excel('data/00_sample_excel.xlsx', engine='openpyxl')
print(df)