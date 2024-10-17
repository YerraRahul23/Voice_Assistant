from cx_Freeze import setup, Executable

# Define the executable
executables = [Executable("index.py")]

# Setup the configuration
setup(
    name="EDITH",
    version="1.0",
    description="Even Dead I am The Hero",
    executables=executables
)
