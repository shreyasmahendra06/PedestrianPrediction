# Pedestrian intention Prediction : A Smart way to analyse Pedestrian Perspective


## _Absract_:
Pedestrian trajectory prediction is one of the main concerns of computer vision problems in the automotive industry, especially in the field of advanced driver assistance systems. The ability to anticipate the next movements of pedestrians on the street is a key task in many areas, e.g., self-driving auto vehicles or advanced surveillance systems, and they still represent a technological challenge. In this project we develop an application which helps in to predict the pedestrian intentions while crossing or not crossing the road for the safety of both pedestrian and autonomous car driver. It refers to the back-end machine learning model's predictions which is based on the LSTM neural network to prompt the autonomous vehicle to take appropriate decision based on the predicted pedestrian behavior. Pedestrian Intention Prediction solve the problem by predicting the intention and visual states of pedestrians. With the predictions made we can find out the intention of a person and then, based on that, decides when to stop and when to pass. Our method yields better results than previous works, it stills needs to be improved in longer period prediction. In this project we demonstrated that predicting the velocity of bounding boxes instead of the positions, taking advantage of the observed positions and speed of bounding boxes, as well as using multi-task learning architecture, could improve the accuracy of pedestrian intention prediction.

## Introduction:
As the industry of automotive vehicles growing rapidly, the ability of those vehicles to predict trajectories of pedestrians becomes more crucial than ever. Pedestrian trajectory prediction is a complex task because humans may change directions suddenly depending on objects, vehicles, human interaction, etc.  Each pedestrian is characterized by a particular pattern of motion, which depends on their gaits, acceleration, and velocities. An autonomous vehicle in such a situation should be able to anticipate the positions of pedestrians and adjust its path accordingly to avoid collision. The problem can be viewed as a sequence problem, in this project we anticipate the future positions of the pedestrians based on their past positions which is known as bounding box. In this project, we compare the performance of different machine learning models. An arbitrary number of people previous positions in x-y coordinates and the output is the next future positions of the pedestrian. The methods been applied are Long Short-Term Memory (LSTM) combined with linear regression. 

## Contents
------------
  * [Repository Structure](#repository-structure)
  * [Proposed Method](#proposed-method)
  * [Results](#results)
  * [Installation](#installation)
  * [Dataset](#dataset)
  * [Training/Testing](#training-testing)
  * [Tested Environments](#tested-environments)
  
## Repository structure:
------------
    ├── Pedestrian intention Prediction : Project repository
            ├── prepare_data.py         : Script for processing raw JAAD data.
            ├── train.py                : Script for training PV-LSTM.  
            ├── test.py                 : Script for testing PV-LSTM.  
            ├── DataLoader.py           : Script for data pre-processing and loader. 
            ├── networks.py             : Script containing the implementation of the network.
            ├── utils.py                : Script containing necessary math and transformation functions.
            
## Proposed method
-------------
![Network architecture](/Netwrok.png)


## Results
--------------
![Example of outputs](/visualizations.png)

## Installation:
------------
Start by cloning this repositiory:
```
git clone https://github.com/vita-epfl/bounding-box-prediction.git
cd bounding-box-prediction
```
Create a new conda environment (Python 3.7):
```
conda create -n pv-lstm python=3.7
conda activate pv-lstm
```
And install the dependencies:
```
pip install -r requirements.txt
```

## Dataset:
  
  * Clone the dataset's [repository](https://github.com/ykotseruba/JAAD).
  ```
  git clone https://github.com/ykotseruba/JAAD
  ```
  * Run the `prepare_data.py` script, make sure you provide the path to the JAAD repository and the train/val/test ratios (ratios must be in [0,1] and their sum should equal 1.
  ```
  python3 prepare_data.py |path/to/JAAD/repo| |train_ratio| |val_ratio| |test_ratio|
  ```
  * Download the [JAAD clips](http://data.nvision2.eecs.yorku.ca/JAAD_dataset/) (UNRESIZED) and unzip them in the `videos` folder.
  * Run the script `split_clips_to_frames.sh` to convert the JAAD videos into frames. Each frame will be placed in a folder under the `scene` folder. Note that this takes 169G of space.
  
  
## Training/Testing:
Open `train.py` and `test.py` and change the parameters in the args class depending on the paths of your files.
Start training the network by running the command:
```
python3 train.py
```
Test the trained network by running the command:
```
python3 test.py
```

## Tested Environments:
------------
  * Windows 11, CUDA 11.2

```
