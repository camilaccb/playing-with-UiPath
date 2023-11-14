import subprocess
import traceback
import os

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def create_command_run_python_script(
    script: str, function: str, parameters: str
) -> list:
    """
    Create command that is going to execute python script
    """

    function_invoke = f"from {script} import {function}; {function}({parameters});"

    command = [
        "poetry",
        "run",
        "python",
        "-c",
        function_invoke,
    ]

    return command


def main(script_name: str, function_name: str, parameters_str: str):
    """
    Create, activate and execute python script

    """

    try:
        # Virtual environment is going to be created in the same folder where scripts are located
        virtual_env_path = SCRIPT_DIRECTORY

        # Install dependencies listed in pyproject.toml and activate environment
        subprocess.run(["poetry", "install"], cwd=virtual_env_path, shell=True)

        # Create command to run script
        command_run_script = create_command_run_python_script(
            script=script_name, function=function_name, parameters=parameters_str
        )

        # Execute script
        with open("output.txt", "w+") as output_file:
            # subprocess.run(['poetry','run', 'python', script_name], cwd= virtual_env_path, shell=True, stdout=output_file, text=True, check=True)
            result = subprocess.run(
                command_run_script,
                cwd=virtual_env_path,
                shell=True,
                stdout=output_file,
                text=True,
                check=True,
            )

            # Get return in the output.txt file
            output_file.seek(0)
            output = output_file.read()
            return output
    except:
        str_traceback = traceback.format_exc()
        return str_traceback
