import configparser
import logging
import os
from pathlib import Path
import sys

path_to_config = Path(__file__).parent.parent.joinpath('config.ini')
CONFIG = configparser.ConfigParser()
CONFIG.read(path_to_config)

log_filename = os.path.join(CONFIG.get(section='LOGGING', option='log_folder'), CONFIG.get(section='LOGGING', option='log_name'))

logging.basicConfig(
    filename= log_filename,
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

logging.info(f'Reading config file {path_to_config}')
#logging.getLogger().addHandler(logging.StreamHandler())

# also write on console
#logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
