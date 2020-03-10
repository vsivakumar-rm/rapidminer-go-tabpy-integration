import tabpy
import json
from tabpy_client import Client
import pandas as pd

tabclient = Client('http://localhost:9004/')
go_url = 'https://go.rapidminer.com'
go_username = ''
go_password =  ''


#values to be changed based on data
deployment_ID = '68784ac3-953f-4a9c-beb2-b00d6b065d20'
label = 'Survived'
PREDICTION = 'prediction('+label+')'

def score(test):
    #removing rows with label values
    test = test[pd.isnull(test[label])]
    # dataframe to json
    input_data = json.loads(test.to_json(orient='records'))
    returnResult = tabclient.query('RapidMiner_Score',go_url, go_username , go_password, input_data, label, deployment_ID)
    test[PREDICTION] = returnResult['response']
    return test

#This function defines the output schema
#***Change the schema according to your result***
def get_output_schema():
  return pd.DataFrame({
    'Row No.' : prep_decimal(),
    'Age': prep_decimal(),
    'Passenger': prep_string(),
    'Sex': prep_string(),
    'Siblings' : prep_decimal(),
    'Parents' : prep_decimal(),
    'Fair' : prep_decimal(),
    PREDICTION: prep_string()
  })