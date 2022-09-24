import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/0 (e.g. pd.read_csv) import matplotlib.pyplot as plt
import seaborn as sns


pip install flask-ngrok

     


pip install pyngrok




!ngrok authtoken 2A4f3c62dcjMoEtGqmNdeTekvcN_5uYh5JgubE6qPCLSrD416 Authtoken saved to configuration file: /root/.ngrok2/ngrok.yml

from google.colab import drive drive.mount('drive')




cd /content/drive/MyDrive/Colab Notebooks/data/Flask-deploy-model


 


df=pd.read_csv(”final dataset.csv“)
# y has target data (clases) such as 1 and 0. y = df.target.values
# This means that take target data out from the datasets and assign them to x_data variabl x_data = df.drop([“target“],axis=1)
mn=np.min(x_data) mx=np.max(x_data) print(mn) print(mx)

x	(x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data)).values print(x)

	





from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=42)


# Build Support Vector Machine Model
from sklearn.svm import SVC svm = SVC(random_state = 42) svm.fit(x_train,y_train)
# prediction and accuracy
print(”print accuracy of svm algo: ”,svm.score(x_test,y_test)) print accuracy of svm algo: 0.8852459016393442

import numpy as np
from flask import Flask, request, render_template
 
from flask_ngrok import run_with_ngrok


app = Flask( name ) run_with_ngrok(app)


@app.route('/') def home():
return render_template('demo.html')



@app.route(“/login") def login():
return render_template(“index.html“)



@app.route(“/homepage“) def homepage():
return render_template('demo.html')


@app.route('/predict',methods=['POST']) def predict():
#For rendering results on HTML GUI features=[x for x in request.form.values()] if(features[1]=='Male'):
features[1]=1
elif features[1]=='Female': features[1]=0
else:
return render_template('index.html', prediction_text='Sorry you have given an inva int_features = [int(x) for x in features]
int_features=(int_features-mn)/(mx-mn).values final_features = [int_features]
prediction = svm.predict(final_features) output = round(prediction[0], 2) if(prediction[0]==1):
return render_template('index.html', prediction_text='Our Model predicted :{} so the else:
return render_template('index.html', prediction_text='Our Model predicted :{} so t









if		name	== ” main “: app.run()
