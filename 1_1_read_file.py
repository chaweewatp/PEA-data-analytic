import pandas as pd
from tqdm import tqdm


# #read invouce
# PATH = 'DataSource/invoice.csv'
# chunksize = 5000
#
# for df_chunk in tqdm(pd.read_csv(PATH, chunksize=chunksize), desc='read invoice file'):
#     #do something
#     # print(len(df_chunk))
#     pass




PATH = 'DataSource/payment2017.csv'
chunksize = 5000
for df_chunk in tqdm(pd.read_csv(PATH, chunksize=chunksize), desc='read payment2017 file'):
    #do something
    # print(df_chunk.head())
    pass



PATH = 'DataSource/payment2018.csv'
chunksize = 5000
for df_chunk in tqdm(pd.read_csv(PATH, chunksize=chunksize), desc='read payment2018 file'):
    #do something
    # print(df_chunk.head())
    pass
