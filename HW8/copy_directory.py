import shutil

def copy_data(source_file, target_file):
    try:
        shutil.copyfileobj(source_file, target_file)
        print(f"Data copied from {source_file} to {target_file}")
    except Exception as e:
        print(f"Error occurred while copying data: {e}")

source_file = "C:/Users/ASUS/Documents/Python/GBPYHW/HW8/data_1.txt"
target_file = "C:/Users/ASUS/Documents/Python/GBPYHW/HW8/data_2.txt"

copy_data(source_file, target_file)