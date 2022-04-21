# PulleyLib.Importers.VPK.MDL
# Imports .MDL files from .VPK archives

# Pulley is licensed under GNU GPLv3.

import os
import subprocess
import shutil

import PulleyLib.Logging as PulleyLog
import PulleyLib.Importers.VPK.Other

from pathlib import Path

MDL_FILE_EXTS = [
    ".dx7_2bone.vtx",
    ".dx80.vtx",
    ".dx90.vtx",
    ".mdl",
    ".sw.vtx",
    ".vvd",
    ".phy"
]

def import_file(file_path, vpk_handle, depot_path, config_handle, profile):
    #PulleyLog.VPKImport("Model importing not yet implementet. Skipping...\n")

    # Strip out the file extension
    file_without_ext = os.path.splitext(file_path)[0]

    # Import all required MDL files
    for file_ext in MDL_FILE_EXTS:
        try:
            PulleyLib.Importers.VPK.Other.import_file_noLog(file_without_ext + file_ext, vpk_handle, depot_path, config_handle, profile)
        except:
            continue

    # Begin model decompile
    PulleyLog.MDLDecompile("Attempting to decompile '" + file_path + "'")

    # Get the absolute file path to the model
    model_path = os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_path)
    out_src_path =  os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/src/" + file_path)

    # Call the model decompilation function
    decompile_model(model_path, out_src_path, config_handle)
    PulleyLog.MDLDecompile("Successfully decompiled '" + file_path + "'")

    # Remove the leftover input files
    for file_ext in MDL_FILE_EXTS:
        if (os.path.exists(os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_without_ext + file_ext))):
            os.remove(os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/" + file_without_ext + file_ext))

    # Begin model compile
    PulleyLog.MDLCompile("Attempting to compile '" + file_path + "'")

    # Get the QC path
    QC_PATH = os.path.abspath(depot_path + config_handle["profiles"][profile]["depot_to_import_to"] + "/src/" + file_path + "/" + Path(file_without_ext).parts[-1] + ".qc")
    COMPILE_DIR = os.path.join(*Path(model_path).parts[:-1])

    # Compile model
    compile_model(QC_PATH, COMPILE_DIR, os.path.splitext(model_path)[0], os.path.splitext(file_path)[0], config_handle)
    PulleyLog.MDLCompile("Successfully compiled '" + file_path + "'")

    PulleyLog.VPKImport("Successfully imported '" + file_path + "'\n")
    return

def decompile_model(file_path, out_folder, content_config):
    DECOMP_EXE = content_config["config"]["paths"]["mdl_decompile"]

    # Run the decomp EXE
    proc = subprocess.call([DECOMP_EXE, file_path, out_folder], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def compile_model(qc_path, out_folder, helper_out_mdl, helper_in_mdl, content_config):
    COMP_EXE = content_config["config"]["paths"]["mdl_compile"]

    # Run the comp EXE
    proc = subprocess.call([COMP_EXE, "-game", os.path.abspath(os.getcwd() + "\\..\\..\\"), qc_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # move files to out folder
    for file_ext in MDL_FILE_EXTS:
        if (os.path.exists(os.path.abspath("..\\..\\" + helper_in_mdl + file_ext))):
            shutil.move(os.path.abspath("..\\..\\" + helper_in_mdl + file_ext), os.path.abspath(out_folder))