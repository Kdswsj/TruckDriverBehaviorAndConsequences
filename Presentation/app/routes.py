from app import app
from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import KMeans
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from functions import *

# Load the Data Set
df = GetData()
# get the adjusted DFE
df['dfe45'] = AdjustDFE(df)
km = KMeans(n_clusters=6)
X = df[['StopIdlePercent', 'DistanceAvgvehiclespeed','TopGearMinusOneUsage','HardBrakesPr1000miles', 'dfe45','CruisePercentage']]
clf = km.fit(X)
df['labels'] = clf.labels_
x = df['DistanceAvgvehiclespeed']
y = df['dfe45']
labels = df['labels']

# Create the main plot
def create_figure(x,y,labels):
    p = figure(title = 'Clusters')
    p.scatter(x,y)
    return p



@app.route('/')
@app.route('/index')
def index():
    user = {'username':'kim'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/clusters')
def clusters():
    # Determine the selected feature
	#current_feature_name = request.args.get("feature_name")
	#if current_feature_name == None:
	#	current_feature_name = "Sepal Length"

	# Create the plot
	plot = create_figure(x,y,labels)

	# Embed plot into HTML via Flask Render
	script, div = components(plot)
	return render_template("iris_index1.html", script=script, div=div)

@app.route('/feature_selection')
def feature_selection():
    df = GetData()
    feat_imp = GetFeatureImportance(df)
    plot = createFeatureImportancePlot(feat_imp)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("iris_index1.html", script=script, div=div)
