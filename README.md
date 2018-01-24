# Truck Driver Behavior And Consequences

### Galvanize Data Science Immersive Capstone Project, January 2018

# Introduction

This project is presented in collaboration with Predictive Fleet Technologies, Michigan (www.engineangel.com). The data for this project comes from Engine Angel which is an application software and a database that captures and analyzes data from fleet vehicles. Engine Angel provides predictions and risk analysis to obtain a more efficient and safe operation of vehicles. 

The objective of this project is to classify truck driver behavior into groups and identify relative costs per mile for each group. The purpose is to improve the hiring process and to recommend training/termination decisions to improve safety and profitability.

The primary data will be based on 'trip data' from the engine ECM (Engine Control Module) that records and summarizes various sensor data as the vehicle makes a trip. Relevant data that mainly depend on the driver behavior include average speed, idle fuel used, top gear usage etc.

All analysis was performed using Python including packages NumPy, Pandas and scikit-learn

# Analysis

The analysis steps are outlined below:

## Load Normalizing Using Regression

The ECM computers provide an estimate of an average load on the engine over the course of the trip. This factor affects the Drive Fuel Economy (DFE) and is not a factor of the driver's behavior. First step is to estimate DFE from the given data and then re-calculate the DFE for a 'normal' average load. The figure below shows the Drive Fuel Economy as a function of average vehicle speed before and after load normalizing.

![regression](https://github.com/Kdswsj/TruckDriverBehaviorAndConsequences/blob/master/images/regression.png)


## Feature Importance

Next step is to compile a list of the factors that are mainly dependent on the driver, such as the adjusted DFE (from step 1), idle fuel used, average speed, percentage of time with speed above speed limit, braking, cruise control usage, top gear usage etc. The trips can then be clustered using k-means clustering and all trips can be assigned a cluster id. Feature importance was evaluated using a random forest regressor.

![features](https://github.com/Kdswsj/TruckDriverBehaviorAndConsequences/blob/master/images/features.png)

## Clustering

Clustering of trips is performed using K means clustering. The most optimal number of clusters in this case turned out to be five, with 3 larger clusters and two smaller. The initial assumption was that any given driver would have most of his trips in one cluster, and in this case the conclusion was that the assumption is quite accurate.

![clustering](https://github.com/Kdswsj/TruckDriverBehaviorAndConsequences/blob/master/images/clustering.png)

## Ranking

Final step is to generate a driver score based on the each driver's trips. An overall score should be weighed by the total distance of the trips. 

In this case, the fleet owner would like to be able to rank drivers based on a combination of drive fuel economy and safety. In other words, a driver is not a better driver just by having better fuel economy. Since there is not enough data available to build an accurate model, it is assumed here that the number of hard brakes is an indicator for unsafe driving. For example, one driver has a large number of hard brakes, and based on the intuition and experience of the fleet owner, this driver might be considered the worst driver, where as the best driver is at the bottom right. After ranking the drivers from best to worst, a decision tree was trained in order to be able to quickly assign a score to new trips.

![ranking](https://github.com/Kdswsj/TruckDriverBehaviorAndConsequences/blob/master/images/ranking.png)


# Acknowledgements

I would like to thank James Mentele, Predictive Fleet Technologies, for his assistance on this project.
