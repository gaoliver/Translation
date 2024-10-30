import os

def delete_json_files():
    folder_path = 'output'
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

delete_json_files()