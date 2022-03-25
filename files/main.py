__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from functools import cache
from importlib.resources import path
import os
from site import abs_paths
import zipfile

cwd = os.getcwd()
cache_folder = os.path.join(cwd, "cache")

# 1. clean_cache

def clean_cache():
    if os.path.exists(cache_folder) == True:
        os.remove(cache_folder)
    return os.mkdir(cache_folder)


# clean_cache()

# 2. cache_zip

def cache_zip(zip_path, dir_path):
    with zipfile.ZipFile(zip_path, "r") as unpack_zip:
        return unpack_zip.extractall(path = dir_path)


# cache_zip("hier stond het pad naar data.zip", "hier stond het pad naar cache")
# resultaat: 999 bestanden nu ook in cache

# 3. cached_files

def cached_files():
    abs_path = []
    files = os.listdir(cache_folder)
    for file in files:
        if file not in abs_path:
            abs_path.append(os.path.abspath(os.path.join(cache_folder, file)))
    return abs_path


# print(cached_files())

# 4. find_password

def find_password(paths):
    for files in paths:
        with open(files, "r") as read_file:
            content = read_file.read()
            if "password" in content:
                    print(content[108:137])
    

# find_password(cached_files())