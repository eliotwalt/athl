import pandas as pd
import argparse
from datetime import datetime
import os

to_drop = ['Rang', 'Société', 'Nat.', 'Date_naiss.','Compétition', 
            'Lieu', 'discipline', 'catégorie', 'NH*']
years = list(range(2006, datetime.now().year))
disciplines = ['800', '1500', '3000', '3000steeple', '5000', '10000']

def h_or_f(x):
    if x.upper() in ['H', 'F']:
        return x.upper()
    else:
        argparse.ArgumentTypeError(f'Value `{x}` invlaid')

def discipline(x):

    global disciplines
    if x in disciplines:
        return x
    else:
        argparse.ArgumentTypeError(f'Value `{x}` invlaid')

def get_opt(disciplines):

    p = argparse.ArgumentParser()
    p.add_argument('--file', '-f', type=str, required=True,
                   help='Path to csv file to transform')
    p.add_argument('--category', '-c', type=h_or_f, required=True,
                   help='Category (\'H\' or \'F\')')
    p.add_argument('--discipline', '-d', type=discipline, required=True,
                   help='discipline ({})'.format(disciplines))
    return p.parse_args()

def rm_duplicates(df):

    if df.columns.duplicated().any()==False:
        return df
    
    else :
        col_name = df.columns[df.columns.duplicated()]        
        min_value = df[col_name].iloc[0].min()
        df = df.loc[0, ~df.columns.duplicated()]       

        return df

def main():

    global years
    global to_drop
    global disciplines

    opt = get_opt(disciplines)

    source_df = pd.read_csv(opt.file)
    to_drop = [td for td in to_drop if td in source_df.columns]

    simple_df = source_df.drop(to_drop, axis=1)
    simple_df.Date = pd.to_datetime(simple_df.Date).dt.year
    athlets = list(set(simple_df.Nom))

    results_df = pd.DataFrame(columns=['Nom']+years)
    for i, athlet in enumerate(athlets):
        tmp_df = simple_df.loc[simple_df.Nom==athlet].drop(['Nom'], axis=1)
        tmp_df = tmp_df.set_index(tmp_df.Date).drop(['Date'], axis=1)
        tmp_df = tmp_df.T 
        tmp_df['Nom'] = athlet
        tmp_df.reset_index(inplace=True, drop=True)
        tmp_df = rm_duplicates(tmp_df)
        results_df = results_df.append(tmp_df, ignore_index=True)

    p1 = os.path.join(os.path.dirname(__file__), opt.discipline)
    path = os.path.join(p2, f'{opt.category}_result_by_athlet.csv'))

    if not os.path.isdir(p1):
        os.mkdir(p1)
    results_df.to_csv(path, index=False)
    print(f'saved in `{path}`')

if __name__ == '__main__':
    main()