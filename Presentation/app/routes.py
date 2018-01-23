from app import app
from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import KMeans
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from functions import *

options = ['AvgLoadFactor', 'StopIdlePercent', 'DistanceAvgvehiclespeed','TopGearMinusOneUsage', 'HardBrakesPr1000miles', \
       'BrakesPr1000miles', 'IdleFuelPercentage', 'EngineBrakePercentage', 'CruisePercentage', 'OverSpeedBPercentage', \
       'OverSpeedAPercentage', 'EngineFanPercentage']
current_sel = 'DistanceAvgvehiclespeed'

cl_options = ['1', '2', '3', '4', '5', '6', '7']
cl_sel = '5'
# Load the Data Set
df = GetData()
# get the adjusted DFE
df['dfe45'] = AdjustDFE(df)


x = df['DistanceAvgvehiclespeed']
sip = df['StopIdlePercent']
y = df['dfe45']
y0 = df['DriveFuelEconomy']

df['DriveFuel45'] = df['TripDistance']/df['dfe45']
dfe_by_vehicle = df[['VehicleId','TripDistance','DriveFuel45','HardBrakeCount']]
dfe_by_vehicle2 = dfe_by_vehicle.groupby('VehicleId').sum()
dfe_by_vehicle2['dfeTotal'] = dfe_by_vehicle2['TripDistance']/dfe_by_vehicle2['DriveFuel45']
dfe_by_vehicle2['HardBrakesTotal'] = 1000*dfe_by_vehicle2['HardBrakeCount']/dfe_by_vehicle2['TripDistance']
colors = ["red", "olive", "darkred", "goldenrod", "skyblue", "orange", "salmon"]

# Create the main plot
def create_figure(x, y, x_label, y_label):
    c = df['labels'].values
    clr = [colors[x] for x in c]
    p = figure()
    p.scatter(x,y,color = clr)
    p.xaxis.axis_label = x_label
    p.yaxis.axis_label = y_label
    p.xaxis.axis_label_text_font_size = "20pt"
    p.yaxis.axis_label_text_font_size = "20pt"
    return p



@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/clusters')
def clusters():
    cl_sel = request.args.get("selection")
    if cl_sel == None:
        cl_sel = '5'

    df['labels'] = getLabels(df, int(cl_sel))
	# Create the plot
	#p1 = create_figure(x,y)
    p1 = create_figure(x,y, 'Avg Vehicle Speed', 'Adjusted DFE')
    p2 = create_figure(sip,y, 'Stop Idle Percent', 'Adjusted DFE')
    #return
    #p2 = create_figure(sip,y, 'Clusters')
    #p2 = create_figure(sip,y,'Clusters')

    # Embed plot into HTML via Flask Render
    script, div = components(p1)
    script2, div2 = components(p2)
    return render_template("clusters.html", script=script, div=div, script2=script2, div2=div2, cl_options = cl_options, cl_sel = cl_sel)


@app.route('/feature_selection')
def feature_selection():
    #df = GetData()
    feat_imp = GetFeatureImportance(df)
    plot = createFeatureImportancePlot(feat_imp)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("features.html", script=script, div=div)

@app.route('/background')
def background():
    return render_template("background.html")

@app.route('/regression')
def regression():
    current_sel = request.args.get("selection")
    if current_sel == None:
        current_sel = 'DistanceAvgvehiclespeed'

    p1 = createRegressionPlot(df[current_sel],y0, current_sel, 'Drive Fuel Economy')
    p2 = createRegressionPlot(df[current_sel],y, current_sel, 'Adjusted Drive Fuel Economy')

    script1, div1 = components(p1)
    script2, div2 = components(p2)

    return render_template("regression.html", script1=script1, div1=div1, script2 = script2, div2 = div2, options = options, current_sel = current_sel)

@app.route('/ranking')
def ranking():
    v1 = dfe_by_vehicle2['dfeTotal']
    v2 = dfe_by_vehicle2['HardBrakesTotal']

    plot = createRankingPlot(v1,v2)
    script, div = components(plot)

    return render_template("ranking.html", script=script, div=div)

@app.route('/improvements')
def improvements():
    return render_template("improvements.html")

@app.route('/summary')
def summary():
    return render_template("summary.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
