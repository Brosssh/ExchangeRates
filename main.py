import datetime
import time
from Classes.exceptions import MissingColumn
from Managers import rates_api
from Classes.daily_rate import DailyRates
from Managers.excel_manager import ExcelManager
from Managers.file_manager import get_valid_path


try:
    excel_file_path = get_valid_path()
    excel = ExcelManager(excel_file_path)
    process_date = excel.get_last_date()

    while process_date < datetime.datetime.utcnow():
        api_response = DailyRates.from_dict(rates_api.get_daily(process_date))
        excel.append(process_date, api_response)
        process_date += datetime.timedelta(days=1)
        time.sleep(.5)

except MissingColumn as e:
    print(f"ERROR: No column named {e.column_name} was found!")
except PermissionError:
    print(f"ERROR: Permission error! Make sure the Excel file is not being modified by another user.")
except Exception as e:
    print(f"ERROR: something went wrong! {e}")
finally:
    time.sleep(60)