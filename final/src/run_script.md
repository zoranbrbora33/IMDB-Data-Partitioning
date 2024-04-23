This batch script, `run_script.bat`, is designed to execute a series of commands related to activating a virtual environment and running a Python script. Below is a breakdown of each command:

1. **Change Directory (cd)**:

   - `cd C:\Users\iOLAPAcademy2023\Envs\iolap-academy\Scripts\activate`: Changes the current directory to the virtual environment's `Scripts` directory in order to activate the virtual environment.

2. **Activate Virtual Environment**:

   - `C:\Users\iOLAPAcademy2023\Envs\iolap-academy\Scripts\activate`: Activates the virtual environment named `iolap-academy`.

3. **Change Directory (cd)**:

   - `cd C:\Users\iOLAPAcademy2023\Projects\zbrbora-academy-python\Final\src`: Changes the current directory to the project's source code directory.

4. **Run Python Script**:

   - `C:\Users\iOLAPAcademy2023\Envs\iolap-academy\Scripts\python main.py`: Executes the Python script named `main.py` using the Python interpreter from the activated virtual environment.

5. **Pause**:
   - `pause`: Pauses the script execution, allowing the user to review any output or error messages before the terminal window closes.

#### Additional Notes:

- This batch script automates the process of activating a virtual environment and running a Python script.
- It assumes that the virtual environment has already been created and contains the necessary dependencies for running the `main.py` script.
- The script provides a convenient way to run the Python script without manually activating the virtual environment each time.
