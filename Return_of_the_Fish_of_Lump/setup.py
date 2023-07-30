import sys
from cx_Freeze import setup, Executable

# Replace 'game.py' with your main Python game script.
target = "jumper.py"

# Dependencies that cx_Freeze needs to include.
# Add any additional packages/modules your game uses.
# For example, if your game uses Pygame and you want to include it:
build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["./assets/"],
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Create the executable.
executables = [
    Executable(target, base=base)  # Replace with your icon file if desired.
]

setup(
    name="YourGameName",  # Replace with your game's name.
    version="1.0",
    description="Description of your game",
    options={"build_exe": build_exe_options},
    executables=executables
)