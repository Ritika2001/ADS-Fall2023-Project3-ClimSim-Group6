# Project: ClimSim - Machine Learning for Climate Modeling


### [Full Project Description](doc/project3_desc.md)

<img src="https://leap-stc.github.io/ClimSim/_images/fig_1.png" alt="climsim" width="300"/>

Term: Fall 2023

+ Team #6
+ Team members:
	+ Jingxuan Wang (jw4311)
	+ Ritika Nandi (rn2578)
	+ Heze Ma (hm2938)
	+ Daniel Luce (dtl2129)
	+ Feiyu Guo (fg2545)
  	+ Lia Cho (lc3683)

+ Project summary: In this project, we attempted to replicate the quickstart notebook from the ClimSim to a Google Colab notebook for a simpler access to the ClimSim data, but due to file issues were not able to succeed. Using a data loader, we utilized the Huggingface Hub to assist in reading the data files and loading it onto the Colab notebook. Note that we created two different functions (download_nc_file and one under climsim_geo_temporal_data_finder_function_definition) to retrieve data from hugging face, and user can implement any of them to retrieve data. We also added visualizations extending what is within the ClimSim files to provide users more visual representations of the ClimSim data. 
	

**Contribution statement**: All team members contributed equally in all stages of this project. All team members approve our work presented in this GitHub repository including this contributions statement. 

DL and RN worked on creating a function to pull the data, JW and HM worked on reproducing preprocessing/create_npy_data_splits.ipynb notebook to take in the pulled data and revised DL and RN's functions, and FG and RN assisted with the preprocessing notebook issues. FG worked on adapting the quickstart notebook and LC worked on adding visualizations of the data. LC, FG, DL, RN, and JW worked on the presentation slides. RN and LC wrote and edited the github pages. 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
