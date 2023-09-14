import logging
import datetime

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
log_file_name = f"logs/log_{current_date}.log"
file_handler = logging.FileHandler(log_file_name)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.addHandler(console_handler)
