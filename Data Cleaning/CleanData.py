import os
from shutil import copyfile
import numpy as np
import pandas as pd

def create_folder(directory):
    new_directory= directory
    try:
        if not os.path.exists(directory):
           os.makedirs(new_directory)
           print("New folder created at"+ new_directory)
        else :
            print( "Folder name exist, select a different name" )


    except OSError:
        print('Error: creating directory.'+ new_directory)
    return new_directory
# rename function copies selected cols and save into selected file name
# root_directory containing devices folder->device->person->posture
def file_rename(directory,new_folder_path):
    root_directory= directory
    new_folder_path_root= new_folder_path
    with os.scandir(root_directory) as devices:
        current_device_id = 1
        for device_name in devices:
            current_device = device_name.name
            print("the current device folder is " + current_device)
            with os.scandir((root_directory+current_device)) as person:
                for person_name in person:
                    current_person = person_name.name
                    print("the current device folder is " + current_device + " the current person is "+ current_person)
                    with os.scandir((root_directory +current_device +"/"+ current_person)) as posture_file:
                        current_session = 1
                        current_posture_id = 1
                        for posture in posture_file:
                            current_posture = posture.name
                            if current_posture_id == 4:
                                current_posture_id = 1
                            print(
                                "the current device folder is " + current_device +
                                "the current person is " + current_person +
                                "the current session is" + str(current_session)+
                                "the current posture is " + current_posture
                            )
                            print(current_posture)
                            current_file_path = root_directory + current_device + "/" + current_person + "/" + current_posture
                            new_file_name = str(current_device_id) + "_" + current_person + "_" + str(
                                current_session) + "_" + str(current_posture_id) + ".txt"
                            new_file_path= new_folder_path_root+"/"+ new_file_name
                            print(current_file_path)
                            temp_data = np.genfromtxt(current_file_path, dtype='str', delimiter=',',
                                                      comments="{", usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
                            temp_dataframe = pd.DataFrame(data=temp_data[1:, 0:], columns=temp_data[0, 0:])

                            temp_dataframe.to_csv(new_file_path)
                            current_posture_id = current_posture_id + 1
                            current_session = current_session + 1
        current_device_id = current_device_id +1






