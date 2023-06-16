import csv
import os
import shutil


def move_files_from_csv(csv_filename):
    my_dict = {}
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                if row[0] == 'id':
                        continue
                file_name = f"./train/{row[0]}.jpg"
                folder_name = f"./dogs/{row[1]}"
                if os.path.exists(file_name):
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                    if folder_name in my_dict:
                        my_dict[folder_name] += 1
                        if my_dict[folder_name] > 50:
                            continue
                    else:
                        my_dict[folder_name] = 0
                    destination = os.path.join(folder_name, os.path.basename(f"{my_dict[folder_name]}.jpg"))
                    shutil.move(file_name, destination)
                else:
                    print(f"File '{file_name}' does not exist.")
            else:
                print("Invalid row format in CSV.")
        print(my_dict)


if __name__ == '__main__':
    move_files_from_csv("./labels.csv")
