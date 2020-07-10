import CleanData

## select path for new folder as shown below - leaving the last blacklash off
selected_directory_root= "./Desktop"
selected_folder_name= "Data3"
selected_directory = selected_directory_root + "/" + selected_folder_name
new_folder_path_root = CleanData.create_folder(selected_directory)

## enter path for data folder- leaving the last blacklash on
data_directory = "./Desktop/10 RawData/"
CleanData.file_rename(data_directory,new_folder_path_root)
