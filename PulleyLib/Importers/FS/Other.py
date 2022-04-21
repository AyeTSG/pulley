# PulleyLib.Importers.FS.Other
# Imports misc files from FS

# Pulley is licensed under GNU GPLv3.

import os
import shutil
import PulleyLib.Logging as PulleyLog

from pathlib import Path

def import_file(file_path, depot_path, config_handle, profile):
    # Get the file
    abs_filepath_in = os.path.abspath(config_handle["profiles"][profile]["content_dir"] + "/" + file_path)
    abs_filepath_out = os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_path)
    abs_filedir_out = os.path.join(*Path(abs_filepath_out).parts[:-1])

    # Create the directory structure
    if (os.path.exists(abs_filedir_out) == False):
        os.makedirs(abs_filedir_out)

    # Copy the file
    if (os.path.exists(abs_filepath_in)):
        shutil.copy(abs_filepath_in, abs_filepath_out)

    PulleyLog.FSImport("Successfully imported '" + file_path + "'\n")
    return

def import_file_noLog(file_path, depot_path, config_handle, profile):
    # Get the file
    abs_filepath_in = os.path.abspath(config_handle["profiles"][profile]["content_dir"] + "/" + file_path)
    abs_filepath_out = os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_path)
    abs_filedir_out = os.path.join(*Path(abs_filepath_out).parts[:-1])

    # Create the directory structure
    if (os.path.exists(abs_filedir_out) == False):
        os.makedirs(abs_filedir_out)

    # Copy the file
    if (os.path.exists(abs_filepath_in)):
        shutil.copy(abs_filepath_in, abs_filepath_out)

    return