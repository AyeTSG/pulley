# Pulley
# A tool to import content from Source Engine games into other Source Engine games

# Pulley is licensed under GNU GPLv3.

import json
import pathlib
import os
import vpk

import PulleyLib.Logging as PulleyLog
import PulleyLib.Importers.VPK.MDL as PulleyVPK_MDLImport
import PulleyLib.Importers.VPK.Other as PulleyVPK_OtherImport
import PulleyLib.Importers.FS.MDL as PulleyFS_MDLImport
import PulleyLib.Importers.FS.Other as PulleyFS_OtherImport

print("== Pulley v1.0 ==\n=== By AyeTSG ===\n")

# PulleyLog.General("Using profile " + PROFILE)

# Read the content config JSON
with open("pulley_config.json", "r") as file:
    content_config = json.load(file)

DEPOT_PATH = content_config["config"]["paths"]["depots"]

# Function: Import a file from a VPK archive
def import_vpk_file(import_path, profile_name):
    # Print some debug info
    PulleyLog.VPKImport("Attempting to import '" + import_path + "'")

    # Get the file extension
    file_ext = pathlib.Path(import_path).suffix
    
    # Open the VPK for reading
    vpk_file = vpk.open(content_config["profiles"][profile_name]["content_dir"])

    # Special cases
    if (file_ext == ".mdl"):
        PulleyVPK_MDLImport.import_file(import_path, vpk_file, DEPOT_PATH, content_config, profile_name)
        return

    # If it didn't match the above cases, use general importing
    PulleyVPK_OtherImport.import_file(import_path, vpk_file, DEPOT_PATH, content_config, profile_name)
    return

# Function: Import a file from FS
def import_fs_file(import_path, profile_name):
    # Print some debug info
    PulleyLog.FSImport("Attempting to import '" + import_path + "'")

    # Get the file extension
    file_ext = pathlib.Path(import_path).suffix

    # Special cases
    if (file_ext == ".mdl"):
        PulleyFS_MDLImport.import_file(import_path, DEPOT_PATH, content_config, profile_name)
        return
    
    # General import the file
    PulleyFS_OtherImport.import_file(import_path, DEPOT_PATH, content_config, profile_name)
    return


# Function: Process a pulley profile
def process_profile(profile_name):
    # Check if we use VPK's in this profile
    if (content_config["profiles"][profile_name]["uses_vpk"] == True):
        # Print some debug info
        PulleyLog.General("Importing content into the '" + content_config["profiles"][profile_name]["depot_to_import_to"] + "' depot\n")

        # Check if the depot exists
        if (os.path.exists(DEPOT_PATH + content_config["profiles"][profile_name]["depot_to_import_to"]) == False):
            print("DepotCheck: Creating depot '" + content_config["profiles"][profile_name]["depot_to_import_to"] + "'... Don't forget to add it to gameinfo.txt\n")
            os.mkdir(DEPOT_PATH + content_config["profiles"][profile_name]["depot_to_import_to"])

        # Loop over each importing file
        for import_file in content_config["profiles"][profile_name]["content_to_import"]:
            import_vpk_file(import_file, profile_name)
    else:
        #print("ERROR: Non-VPK importing not yet implemented!")
        #exit()

        # Print some debug info
        PulleyLog.General("Importing content into the '" + content_config["profiles"][profile_name]["depot_to_import_to"] + "' depot\n")

        # Check if the depot exists
        if (os.path.exists(DEPOT_PATH + content_config["profiles"][profile_name]["depot_to_import_to"]) == False):
            print("DepotCheck: Creating depot '" + content_config["profiles"][profile_name]["depot_to_import_to"] + "'... Don't forget to add it to gameinfo.txt\n")
            os.mkdir(DEPOT_PATH + content_config["profiles"][profile_name]["depot_to_import_to"])

        # Loop over each importing file
        for import_file in content_config["profiles"][profile_name]["content_to_import"]:
            import_fs_file(import_file, profile_name)

# For each profile
for profile in content_config["config"]["profiles_to_run"]:
    # Process the profile
    process_profile(profile)