import pandas as pd
from etl import extracting
from etl import transforming


if __name__ == "__main__":

    dataset = pd.DataFrame()
    
    df = extracting()
    df_covid = transforming(df)
    print(df_covid)
