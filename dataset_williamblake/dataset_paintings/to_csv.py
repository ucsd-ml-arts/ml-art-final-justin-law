import pandas as pd

df = pd.read_excel('painting_dataset_2018.xlsx')  # sheetname is optional
df.to_csv('download.csv', index=False)  # index=False prevents pandas to write row index