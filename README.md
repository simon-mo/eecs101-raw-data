# eecs101-raw-data
This repo provides essential data for those who wants to build a bot for Piazza. 

It has three kinds of data with its accompanying Jupyter Notebook detailing how the data is produced. 

## 0. Real Dataset Warning

Caution: this is a "real" dataset. It's not toy dataset. This dataset is very very very messy but it captures the ground truth. 

## 1. Raw Data

Data: `all_posts.pkl` consists of a list of dictionaries. 

Note: The raw `json` turned `dict` in python for every single post object. This data contains everything you would see on viewing a post on Piazza and even more information. But be data is a bit messy. You are welcome to dig around. You might use `Raw to Dataframe.ipynb` to get some hints on how to understand the dictionary scheme. 

## 2. Processed Data (in pd.Dataframe Format)

Data: `all_content_dataframe.pkl` consists of a pandas dataframe

Note: I roughly processed the raw data and selected certain components and put them into a pandas dataframe. This is still unpolished data. 

## 3. Reference Matrix 

Data: `ref_matrix.npz` is a spicy csr compressed matrix. You can easily 'convert' it into a numpy matrix.

Note: I counted the reference (in @post_number format) from post row `i` to post column `j`. This matrix turns out to to really sparse. The dimension is roughly 5600 times 5600. But there are only about 800 references. 