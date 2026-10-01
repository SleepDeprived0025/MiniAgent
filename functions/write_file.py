import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        path_to_file = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_path_2_file = os.path.commonpath([working_dir_abs,path_to_file]) == working_dir_abs
        if valid_path_2_file == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(path_to_file) == True :
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(file_path,exist_ok=True)
        with open(path_to_file, "w") as w:
            w.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"