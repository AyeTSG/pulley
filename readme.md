# Pulley
Pulley is a content importing tool for Source Engine that imports content from other Source Engine titles. It runs based off of a `pulley_config.json` configuration file.


## Using Pulley
### Setting up the configuration file
The Pulley configuration file uses the following format:
```json
{
    "config": {
        "paths": {
            "depots": "./pulley_imported/",
            "mdl_compile": "C:/SourceSDK2013/bin/studiomdl.exe",
            "mdl_decompile": "./PulleyLib/studiomdl_decomp.exe"
        },
        "profiles_to_run": [
            "profile_1"
        ]
    },
    "profiles": {
        "profile_1": {
            "uses_vpk": true,
            "depot_to_import_to": "depot_name",
            "content_dir": "path/to/content/directory",
            "content_to_import": [
                "materials/material/to/import.vmt",
                "scripts/or/other/content.txt"
            ]
        }
    }
}
```

- `config`: Holds the primary configuration information.
    - `paths`: Information on where Pulley can find resources and tools.
      - `depots`: A path where depot content resides. Should be a string value.
      - `mdl_compile`: A path to the .MDL compiler exe. Should be a string value.
      - `mdl_decompile`: A path to the .MDL decompiler exe. Generally, this should stay as the default value. Should be a string value.
    - `profiles_to_run`: A list of profiles for Pulley to process and import. Should be string values.
- `profiles`: A list of profile definitions.
  - `<profile_name>`: The name of a Pulley profile. Should be a string value.
    - `uses_vpk`: Does the profile import from .VPK content? Should be either `true` or `false`.
    - `depot_to_import_to`: The name of a content depot to import to. When running this profile, content will be imported to `<config:paths:depots>/<value>`. Should be a string value.
    - `content_dir`: The directory to import content from. Should be a string value. If `uses_vpk` is set to `true`, this should be a path to a directory vpk, otherwise it should be a path to a content directory.
    - `content_to_import`: A list of content to import. Values are relative to the content directory. Should be string values.

### Running a Pulley import
To run Pulley, you should directly run the Python script, or run `py pulley.py` in a command line. Pulley will run through and process each profile listed in the `profiles_to_run` section of the configuration. Once an import is completed, the content should be available within the depot directory.

## Other Notes
- The tool has special import procedures for .MDL model files. Pulley will attempt to decompile models, and then recompile them under the SDK 2013 toolset.
- Pulley is not designed to be used for copyright infringement. Support will not be provided in cases where you use Pulley to infringe on copyright.
- The `pulley_config.json` includes a sample `import_test` profile, to show how the tool operates.
- Pulley makes use of [CrowbarDecompilerCMD](https://github.com/mrglaster/CrowbarDecompilerCMD), a derivitive of [Crowbar](https://github.com/ZeqMacaw/Crowbar) for model decompilation.