import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def download_grid_info():
    grid_info_url = "https://github.com/leap-stc/ClimSim/raw/main/grid_info/ClimSim_low-res_grid-info.nc"
    grid_info_folder = "../grid_info/"

    if os.path.exists(grid_info_folder + os.path.basename(grid_info_url)):
        print(f"File already exists in {grid_info_folder}. Skipping download.")
    else:
        if not os.path.exists(grid_info_folder):
            os.makedirs(grid_info_folder)

        file_name = os.path.join(grid_info_folder, os.path.basename(grid_info_url))
        response = requests.get(grid_info_url)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"File downloaded and saved to {file_name}")
        else:
            print("Failed to download the file.")


def download_normalizations():
    normalizations_url = "https://github.com/leap-stc/ClimSim/raw/main/preprocessing/normalizations/"
    normalizations_folder = "../preprocessing/normalizations/"

    normalizations_files = ['inputs/input_mean.nc', 'inputs/input_max.nc', 'inputs/input_min.nc', 'outputs/output_scale.nc']

    if not os.path.exists(normalizations_folder):
        os.makedirs(normalizations_folder + 'inputs/')
        os.makedirs(normalizations_folder + 'outputs/')

    for norm_file in normalizations_files:
        file_name = os.path.join(normalizations_folder, norm_file)
        if os.path.exists(file_name):
            print(f"File already exists in {normalizations_folder}. Skipping download.")
        else:           
            url = normalizations_url + norm_file
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"File downloaded and saved to {file_name}")
            else:
                print("Failed to download the file.")



def download_subsampled_data():
    data_base_url = "https://huggingface.co/datasets/LEAP/subsampled_low_res/resolve/main/"
    data_folder = "../data/e3sm_train_npy/"

    data_files = ['train_input.npy', 'train_target.npy', 'val_input.npy', 'val_target.npy', 'scoring_input.npy', 'scoring_target.npy']

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    for data_file in data_files:
        file_name = os.path.join(data_folder, data_file)
        if os.path.exists(file_name):
            print(f"File already exists in {data_folder}. Skipping download.")
        else:   
            url = data_base_url + data_file
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"File downloaded and saved to {file_name}")
            else:
                print("Failed to download the file.")


def download_train_data(url):
    data_folder = "../data/e3sm_train/"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    file_name = os.path.join(data_folder, url.split("/")[-1])
    if os.path.exists(file_name):
            print(f"File already exists in {data_folder}. Skipping download.")
    else:
        response = requests.get(url)
        
        if response.status_code == 200:
            # file_name = url.split("/")[-1]
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"File downloaded and saved to {file_name}")

def fetch_train_data():
    x1 = [f'{i:04d}-{j:02d}' for i in range(1, 10) for j in range(1,13)]
    x21 = '/E3SM-MMF.mli.'
    x22 = '/E3SM-MMF.mlo.'
    x3 = [f'-{i:02d}-{j:05}.nc' for i in range(1, 31) for j in range(0,85200, 1200)]

    data_base_url = "https://huggingface.co/datasets/LEAP/ClimSim_low-res/resolve/main/train/"

    for folder in x1[1:]:
        for day in x3:
            full_mli_url = data_base_url + folder + x21 + folder + day
            full_mlo_url = data_base_url + folder + x22 + folder + day

            response_mli = requests.get(full_mli_url)
            response_mlo = requests.get(full_mlo_url)
            
            if response_mli.status_code == 200:
                download_train_data(full_mli_url)
            if response_mlo.status_code == 200:
                download_train_data(full_mlo_url)
        