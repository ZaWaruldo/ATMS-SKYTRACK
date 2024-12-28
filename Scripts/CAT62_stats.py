import os
import pandas as pd

#Process CAT062 folder
cat062_folder = 'dataset/processed/Main/CAT062'
cat062_stats = []

for file in os.listdir(cat062_folder):
    if file.startswith("CAT062_"):
        filepath = os.path.join(cat062_folder, file)
        df = pd.read_csv(filepath)

        date = file.split("_")[-1].replace("RDR", "").replace("am.csv","").replace("pm.csv", "")
        period = file[:-4][-2:]
        unique_trkid= df['trkid'].nunique()
        unique_msid= df['MSID'].nunique()

        cat062_stats.append([date, period, unique_msid, unique_trkid, len(df)])

columns = ['Date', 'period','Unique MSID', 'Unique trkid', 'Total Records']

df_cat062 = pd.DataFrame(cat062_stats, columns=columns)
df_cat062['Date'] = pd.to_datetime(df_cat062['Date'], format='%Y%m%d').dt.date
df_cat062.to_csv(f'dataset/processed/Main/Statistics/CAT062_stats.csv', index=False)
