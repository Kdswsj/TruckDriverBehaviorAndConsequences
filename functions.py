import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from bokeh.plotting import figure

def GetData():
    # read in the data
    df = pd.read_csv('data/ECMData.csv')

    # add colums
    df['AvgLoadFactor'] = 0.45
    df['HardBrakesPr1000miles'] = 1000*df['HardBrakeCount']/df['TripDistance']
    df['BrakesPr1000miles'] = 1000*df['BrakeCount']/df['TripDistance']
    df['TopGearMinusOneUsage'] = df['TopGearMinusOneDistance']/(df['TopGearMinusOneDistance'] + df['TopGearDistance'])
    df['IdleFuelPercentage'] = df['StopIdleFuel']/df['DriveFuel']
    df['EngineBrakePercentage'] = df['EngineBraketime']/df['Drivetime']
    df['CruisePercentage'] = df['CruiseTime']/df['Drivetime']
    df['OverSpeedAPercentage'] = df['OverSpeedAtime']/df['Drivetime']
    df['OverSpeedBPercentage'] = df['OverSpeedBtime']/df['Drivetime']
    df['EngineFanPercentage'] = df['EngineFantime']/df['Drivetime']

    # remove a few outliers
    df = df[df['DriveFuelEconomy'] > 2]
    df = df[df['DriveFuelEconomy'] < 9]

    #return dataset for analysis
    return df

def AdjustDFE(df):
    #select the features
    X = df[['DistanceAvgLoadFactor', 'StopIdlePercent', 'DistanceAvgvehiclespeed','TopGearMinusOneUsage', 'HardBrakesPr1000miles', \
           'BrakesPr1000miles', 'IdleFuelPercentage', 'EngineBrakePercentage', 'CruisePercentage', 'OverSpeedBPercentage', \
           'OverSpeedAPercentage', 'EngineFanPercentage']]
    y = df['DriveFuelEconomy']

    lm = LinearRegression(normalize=True)
    lm.fit(X,y)

    # replace DistanceAvgLoadFactor with AvgLoadFactor (45%)
    X = df[['AvgLoadFactor', 'StopIdlePercent', 'DistanceAvgvehiclespeed','TopGearMinusOneUsage', 'HardBrakesPr1000miles', \
           'BrakesPr1000miles', 'IdleFuelPercentage', 'EngineBrakePercentage', 'CruisePercentage', 'OverSpeedBPercentage', \
           'OverSpeedAPercentage', 'EngineFanPercentage']]

    # calculate dfe45
    dfe45 = lm.predict(X)

    return dfe45


def GetFeatureImportance(df):
    #select the features
    X = df[['DistanceAvgLoadFactor', 'StopIdlePercent', 'DistanceAvgvehiclespeed','TopGearMinusOneUsage', 'HardBrakesPr1000miles', \
           'BrakesPr1000miles', 'IdleFuelPercentage', 'EngineBrakePercentage', 'CruisePercentage', 'OverSpeedBPercentage', \
           'OverSpeedAPercentage', 'EngineFanPercentage']]
    y = df['DriveFuelEconomy']

    regr = RandomForestRegressor(max_depth=10, random_state=0)
    regr.fit(X, y)

    return regr.feature_importances_

def createFeatureImportancePlot(feat_imp):
    p = figure(plot_width = 400, plot_height=400)
    y1 = [x for x in range(len(feat_imp.columns))]

    p.hbar(y = y1,right=feat_imp,height=0.5,left=0)

    return p
