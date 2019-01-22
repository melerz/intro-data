import pandas as pd
import os

if __name__=="__main__":
    all_files = os.listdir("years")
    list = []
    for json_file in all_files:
        df = pd.read_json("years/"+json_file, orient='index')
        list.append(df)
    frame = pd.concat(list, axis = 0, ignore_index = True)
    frame.to_csv("all_years.csv",sep='\t',encoding='utf-8')