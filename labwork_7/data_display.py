import re
import pandas as pd
from colorama import Fore, Style
from tabulate import tabulate

# from labwork_7.api_data import APIData
from labwork_7.errors import Error
from labwork_7 import variables


class DataDisplay:

    def display_data_as_table(self, data, color, choose=1):
        if data:
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', 20)
            df = pd.DataFrame(data)
            if choose == 1:
                df['login'] = df['login'].apply(lambda x: x['username'])
                df['address'] = df['address'].apply(lambda x: x['street'])
                df['company'] = df['company'].apply(lambda x: x['name'])

                return self.columns_table(df, color)
            if choose == 2:
                return self.columns_table(df, color)
        else:
            return variables.no_data

    def columns_table(self, df, color):
        colored_columns = [f"{color}{col}{Style.RESET_ALL}" for col in df.columns]
        df = df.map(lambda x: x if isinstance(x, float) or len(str(x)) <= 20 else str(x)[:20 - 3] + '...')
        return tabulate(df, headers=colored_columns, tablefmt='psql', showindex=False)

    def display_data_as_list(self, data, color, choose=1):
        if data:
            df = pd.DataFrame(data)

            if choose == 1:
                df['login'] = df['login'].apply(lambda x: x['username'])
                df['address'] = df['address'].apply(lambda x: x['street'])
                df['company'] = df['company'].apply(lambda x: x['name'])
                return self.columns_list(df, color)
            if choose == 2:
                for col in df.columns:
                    if df[col].dtype == 'object':
                        df[col] = df[col].astype(str).str.slice(0, 50)
                return self.columns_list(df, color)
        else:
            return variables.no_data

    def columns_list(self, df, color):
        result = ""
        for index, row in df.iterrows():
            for col, value in row.items():
                result += f"{color}{col}{Style.RESET_ALL}: {value}\n"
            result += "\n"
        return result


    def remove_color_tags(self, text):
        clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
        return clean_text
