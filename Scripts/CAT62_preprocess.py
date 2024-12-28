import os, csv, glob
from datetime import datetime
from tqdm import tqdm

#Directory and file pattern
directory = 'dataset/raw/Main/CAT062/'
processed_directory = 'dataset/processed/Main/CAT062/'
pattern = os.path.join(directory, "CAT062_*.csv")

headers_to_keep = [' REC-TIME-1970',' MSID',' trkid',' FPLID',' lat', ' lon',' heading[deg]',' speed[kn]',' alt(modec)[ft]', ' alt(tracked)[ft]']

def convert_unix_time(unix_timestamp):
    #Convert Unix epoch time to human-readable format
    return  datetime.utcfromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def process_header(header):
    indices_to_keep = [header.index(h) for h in headers_to_keep]
    rec_time_1970_index = header.index(' REC-TIME-1970')
    process_header = [header[i].strip() for i in indices_to_keep]
    return indices_to_keep, rec_time_1970_index, process_header

def process_row(row, indices_to_keep, rec_time_1970_index, msid_index, trkid_index):
    cleaned_row = [field.strip() for field in row]

    if cleaned_row[msid_index] in ['????????','']:
        cleaned_row[msid_index] = cleaned_row[trkid_index]

    if cleaned_row[rec_time_1970_index]:
        cleaned_row[rec_time_1970_index] = convert_unix_time(cleaned_row[rec_time_1970_index])

    processed_row = [cleaned_row[i] for i in indices_to_keep]
    return processed_row

def process_file(csv_file):
    filename = os.path.basename(csv_file)
    out_filename = os.path.join(processed_directory, filename)

    with open(csv_file, 'r', newline='') as infile, open(out_filename, 'w', newline='') as outfile:
        csv_reader = csv.reader(infile, delimiter=';')
        csv_writer = csv.writer(outfile)
        processed_row_count = 0

        header = next(csv_reader)
        indices_to_keep, rec_time_1970_index, processed_header = process_header(header)

        msid_index = header.index(' MSID')
        trkid_index = header.index(' trkid')

        csv_writer.writerow(processed_header)

        for row in csv_reader:
            csv_writer.writerow(process_row(row, indices_to_keep, rec_time_1970_index, msid_index, trkid_index))
            processed_row_count +=1
            if processed_row_count % 100000 == 0:
                print(f"{filename} rows processed: {processed_row_count}")

    print(f"Processed file saved to {out_filename}")
    print(f"Total rows in dataset: {out_filename} is {processed_row_count}")

for file in glob.glob(pattern):
        process_file(file, update_callback)