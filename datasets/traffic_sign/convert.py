import os
import os



# Specify the folder path
folder_path = r"datasets\traffic_sign\traffic_Data\DATA"

# Get all the directory names in the folder
directories = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

# Iterate through the directory names
for directory in directories:
    # Get the first 3 characters of the directory name
    first_3_letters = directory[:3].zfill(3)

    # Create the new folder name
    new_folder_name = first_3_letters

    # Create the new folder path
    new_folder_path = os.path.join(folder_path, new_folder_name)

    # Check if the new folder already exists
    if not os.path.exists(new_folder_path):
        # Create the new folder
        os.makedirs(new_folder_path)
        print(new_folder_name)

    # Rename the original directory and move it to the new folder
    os.rename(os.path.join(folder_path, directory), os.path.join(new_folder_path, directory))












# # Specify the folder path
# folder_path = r"datasets\traffic_sign\traffic_Data\TEST"

# # # Get all the directory names in the folder
# # directories = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
# # Get all paths of files if they end with ".png"
# file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")]

# # Iterate through the directory names
# for directory in file_paths:
#     # Get the first 3 characters of the directory name
#     # Specify the file path
#     # file_path = "/c:/Users/navan/Desktop/OneDrive - vit.ac.in/year-3, winter semester/Deep Learning/Lab/VITC_DL/datasets/traffic_sign/TEST"

#     # Split the file path into components
#     components = directory.split('\\')

#     # Get the second last component
#     second_last_component = components[-1]

#     # Get the first 3 letters after the second last component
#     first_3_letters = second_last_component[:3]

#     new_folder_name = first_3_letters
#     # Print the result
#     # print(components)
#     # print(directory)
    
#     # Create the new folder path
#     new_folder_path = os.path.join(folder_path, new_folder_name)
#     # print(new_folder_path)
#     # Check if the new folder already exists
#     if not os.path.exists(new_folder_path):
#         # Create the new folder
#         os.makedirs(new_folder_path)
#         print(new_folder_name)
    
#     # Rename the original directory and move it to the new folder
#     os.rename(directory, new_folder_path + '\\' + second_last_component)