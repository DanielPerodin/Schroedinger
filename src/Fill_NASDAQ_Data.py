import pandas as pd

def main():
    file_path = input("Enter the path to the file: ")
    df = pd.read_csv(file_path)
    df = df.drop_duplicates(subset = 'Date')
    df['Date'] = pd.to_datetime(df['Date'])
    range_date = pd.date_range(start = df['Date'].min(), end = df['Date'].max())
    df = df.set_index(keys = 'Date')
    df = df.reindex(labels=range_date, method = 'bfill')
    df = df.reset_index()
    df.rename(columns={'index':'Date'}, inplace=True)
    df.to_csv("./Data/NASDAQ/Cocoa_filled.csv",index=False)
    
main()