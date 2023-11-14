import os
import sys
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
        project_folder, "Python-scripts", f"EvidencePython_{date_time_str}.log"
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


def main(parameters: dict):
    """
    Receive 2 numbers and write in a sheet
    """

    try:
        # Set log file
        set_log_file()
        logging.info("Log file created")

        # Include execution information
        include_info_execution()

        # Accessing parameters
        num1 = parameters["num1"]
        num2 = parameters["num2"]

        # Logging datatype of parameters just to double check
        logging.info(f"float 1: {num1}, type: {type(num1)}")
        logging.info(f"float 2: {num2}, type: {type(num2)}")

        data = {"Number 1": [num1], "Number 2": [num2]}
        df = pd.DataFrame(data)

        # Number of columns to insert
        qty_numb = len(df.columns)
        qty_numb_str = str(qty_numb)

        # Define excel file path
        excel_file_name = "numbers.xlsx"

        # Write dataframe in excel
        df.to_excel(excel_file_name, index=False)
        logging.info("Received data was inlcuded in excel")
        print(qty_numb_str)

    except Exception:
        trackback_str = traceback.format_exc()
        logging.error(trackback_str)
        sys.exit(1)
