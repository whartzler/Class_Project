import tabpy_client
from tabpy.tabpy_tools.client import Client
client = tabpy_client.Client('http://localhost:9004/')


def battery_predictor( _arg1, _arg2,_arg3):
    import pandas as pd
    row = {'Manufacture': _arg1,
           'Model': _arg2,
          'Model Year':_arg3}
    #Convert it into a dataframe
    test_data = pd.DataFrame(data = row,index=[0])
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    test_data['Manufacture']  = le.fit_transform(test_data['Manufacture'])
    test_data['Model']  = le.fit_transform(test_data['Model'])
    #Predict 
    from sklearn.ensemble import RandomForestClassifier
    random_forest = RandomForestClassifier(n_estimators=100)
    predprob_battery = random_forest.predict_proba(test_data)
    #Return only the probability
    return [probability[1] for probability in predprob_battery]


n_jobs = 1
#Deploying
client.deploy('battery_predictor', battery_predictor, override = True)
