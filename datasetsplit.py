import os
import shutil
import pandas as pd


main_dataset_dir="D:/covid-chestxray-dataset-master/images/"

df=pd.read_csv("D:/covid-chestxray-dataset-master/metadata.csv")

def path_check(path):
    if(os.path.exists(path)):
        return
    else:
        os.makedirs(path)
        return
    
dataset_dir="D:/Covid_19_Mark1/Dataset/"

for ind in df.index:
    try:
        if (df["finding"][ind]=="Pneumonia/Viral/COVID-19"):
            if(df["view"][ind]=="PA" or df["view"][ind]=="AP"):
                path_check(dataset_dir+"Covid_19/")
                shutil.copy(main_dataset_dir+df["filename"][ind], dataset_dir+"Covid_19/"+df["filename"][ind])
        else:
            continue
    except:
        pass

path_check(dataset_dir+"Normal/")
normal_dataset_dir="D:/chest_xray/train/NORMAL/"

for file in os.listdir(normal_dataset_dir):
    if(len(os.listdir(dataset_dir+"Normal/"))<len(os.listdir(dataset_dir+"Covid_19/"))):
        shutil.copy(normal_dataset_dir+file,dataset_dir+"Normal/"+file)  
        

    
train_test_split=70
dataset_split_dir="D:/Covid_19_Mark1/Dataset2/"
for folder in os.listdir(dataset_dir):
    path_check(dataset_split_dir+"train/"+folder+"/")
    path_check(dataset_split_dir+"test/"+folder+"/")
    for file in os.listdir(dataset_dir+folder):
        if(len(os.listdir(dataset_split_dir+"train/"+folder+"/"))<((len(os.listdir(dataset_dir+folder+"/"))*train_test_split)/100)):
            shutil.copy(dataset_dir+folder+"/"+file,dataset_split_dir+"train/"+folder+"/"+file)
        else:
            shutil.copy(dataset_dir+folder+"/"+file,dataset_split_dir+"test/"+folder+"/"+file)

