import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        path_to_file = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_path_2_file = os.path.commonpath([working_dir_abs,path_to_file]) == working_dir_abs
        if valid_path_2_file == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(path_to_file) == True :
            return f'Error: File not found or is not a regular file: "{file_path}"'
        MAX_CHARS = 10000

        with open(path_to_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"