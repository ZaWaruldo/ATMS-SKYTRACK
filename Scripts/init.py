import os

base_dirs ="dataset"
process_types=["processed","raw"]
locations=["Main"]
categories = {
    "processed": ["CAT004","CAT062","Statistics"],
    "raw": ["CAT004","CAT062"]
}

for process_type in process_types:
    for location in locations:
        for category in categories.get(process_type,[]):
            directory = os.path.join(base_dirs,process_type,location,category)
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            else:
                print(f"Directory {directory} already exists.")