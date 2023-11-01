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
    try:
        data_base_url = "https://huggingface.co/datasets/LEAP/ClimSim_low-res/tree/main/train"

        response = requests.get(data_base_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            folder_links = soup.find_all('a', class_="col-span-8 flex items-center hover:underline md:col-span-4 lg:col-span-3")

            for link in folder_links:
                href = link.get('href')
                if href.startswith('/datasets/LEAP/ClimSim_low-res/tree/main/train/') and re.match(r'/datasets/LEAP/ClimSim_low-res/tree/main/train/\d{4}-\d{2}', href):
                    subfolder_url = urljoin(data_base_url, href)
                    response_sub = requests.get(subfolder_url)
                    if response_sub.status_code == 200:
                            soup_sub = BeautifulSoup(response_sub.text, 'html.parser')
                            file_links = soup_sub.find_all('a', {'title' : 'Download file'})
                            for file_link in file_links:
                                href_sub = file_link.get('href')
                                if re.match(r'/datasets/LEAP/ClimSim_low-res/resolve/main/train/(\d{4}-\d{2}/[^\s]+)', href_sub):
                                    subfile_url = urljoin(subfolder_url, href_sub)
                                    download_train_data(subfile_url)
    except:
        print("")
