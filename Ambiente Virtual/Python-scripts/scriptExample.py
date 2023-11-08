import sys
import os
import logging
import datetime
import pandas as pd
import traceback

SCRIPT_DIRETORIO = os.path.dirname(os.path.abspath(__file__))


def include_info_execution():
    """Includes execution information in a log file"""

    # Path to libs used
    logging.info(f"Import path pandas: {pd.__file__}")

    # Path to Python execution
    python_execution = sys.executable
    logging.info(f"Python execution file: {python_execution}")

    # List of directories where Python searches dependencies
    directories_list = sys.path
    diretory_str = "\n".join(directories_list)
    logging.info(
        f"List of directories where Python searches dependencies: \n{diretory_str}"
    )


def set_log_file():
    """Sets path for log file and its"""

    # Gets current date and hour
    current_datetime = datetime.datetime.now()

    # Format date and hour
    date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # Define log file path
    project_folder = os.path.dirname(SCRIPT_DIRETORIO)
    log_file_path = os.path.join(
        project_folder, f"EvidencePython_{date_time_str}.log"
    )

    # handle no writing in log file
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Sets log format
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
    )


def main(num1_str: str,num2_str: str):
    """
    Receive 2 numbers and write in a sheet
    """

    try:
        # Set log file
        set_log_file()
        logging.info("Log file created")

        # Include execution information
        include_info_execution()

        # Transform string to integer
        num1_int = int(num1_str)
        num2_int = int(num2_str)

        # Create dataframe
        data = {'Number 1': [num1_int], 'Number 2': [num2_int]}
        df = pd.DataFrame(data)

        # Define excel file path
        excel_file_name = 'numbers.xlsx'

        # Write dataframe in excel
        df.to_excel(excel_file_name, index=False)
        logging.info("Received data was inlcuded in excel")

        output = "sucesso"

        return output

    except Exception:
        trackback_str = traceback.format_exc()
        logging.info(trackback_str)
        return trackback_str
    
main("1","2")
  