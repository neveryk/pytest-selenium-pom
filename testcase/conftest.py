import pytest
from selenium import  webdriver
import os
from common.read_yaml import yaml_data


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')

def get_data(file):
    data_file=os.path.join(BASE_PATH,"data",file)
    data_yaml=yaml_data.load_yaml(data_file)
    return data_yaml

data=get_data("data.yaml")