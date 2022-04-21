# PulleyLib.Importers.VPK.Other
# Imports misc files from .VPK archives

# Pulley is licensed under GNU GPLv3.

import os
import PulleyLib.Logging as PulleyLog

def import_file(file_path, vpk_handle, depot_path, config_handle, profile):
    # Get the file
    try:
        general_file = vpk_handle.get_file(file_path)
        file_data = general_file.read()
    except KeyError:
        PulleyLog.VPKImport("File does not exist within VPK. Skipping...\n")
        return

    # Save it to the correct location
    OUT_PATH = depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_path

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    
    # Write the data
    file = open(OUT_PATH, "wb")
    file.write(file_data)
    file.close()

    PulleyLog.VPKImport("Successfully imported '" + file_path + "'\n")
    return

def import_file_noLog(file_path, vpk_handle, depot_path, config_handle, profile):
    # Get the file
    try:
        general_file = vpk_handle.get_file(file_path)
        file_data = general_file.read()
    except KeyError:
        return

    # Save it to the correct location
    OUT_PATH = depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_path

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    
    # Write the data
    file = open(OUT_PATH, "wb")
    file.write(file_data)
    file.close()

    return