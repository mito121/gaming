import sys
from cx_Freeze import setup, Executable

## Run command to build: python setup.py build

target = "klumpfisk.py"

build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["./assets/"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(target, base=base, icon="assets/graphics/mola/klumpfisk.png")
]

setup(
    name="RunescapeCraft: Return of the Fisk of Klump",
    version="1.0",
    description="En klumpfisk er mere slimet end man skulle tro.",
    options={"build_exe": build_exe_options},
    executables=executables
)