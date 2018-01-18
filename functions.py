import pandas as pd

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
