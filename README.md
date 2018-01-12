# Truck Driver Behavior And Consequences

Galvanize Data Science Immersive Capstone Project

Kim D. Sorensen, 12/17/2017

Final Proposal:

This project is presented in collaboration with Predictive Fleet Technologies, Michigan (www.engineangel.com). The data for this project will come from Engine Angel which is an application software and a database that captures and analyzes data from fleet vehicles. Engine Angel provides predictions and risk analysis to obtain a more efficient and safe operation of vehicles. 
The objective of this project is to classify truck driver behavior into groups and identify relative costs per mile for each group. The purpose is to improve the hiring process and to recommend training/termination decisions to improve safety and profitability.
The primary data will be based on 'trip data' from the engine ECM (Engine Control Module) that records and summarizes various sensor data as the vehicle makes a trip. Relevant data that mainly depend on the driver behavior include average speed, idle fuel used etc.

The analysis steps are outlined below:
The ECM computers provide an estimate of an average load on the engine over the course of the trip. This factor affects the Drive Fuel Economy (DFE) and is not a factor of the driver's behavior. First step is to estimate DFE from the given data and then re-calculate the DFE for a 'normal' average load.

Next step is to compile a list of the factors that are mainly dependent on the driver, such as the adjusted DFE (from step 1), idle fuel used, average speed, percentage of time with speed above speed limit, braking, cruise control usage, top gear usage etc. The trips can then be clustered using k-means clustering and all trips can be assigned a cluster id.

Third step is to generate a driver score based on the each driver's trips. An overall score should be weighed by the total distance of the trips. It is the expectation that at this point it should be possible to recommend a best driver profile.

With many features available in the dataset, feature importance will be evaluated by use of random forest techniques. If time allows, Principal Component Analysis will be used to see which features have the greatest variation and how they relate to each other.
