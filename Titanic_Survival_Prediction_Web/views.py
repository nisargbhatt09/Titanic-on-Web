from django.shortcuts import render
from sklearn.preprocessing import MinMaxScaler

def home(request):
    return render(request, 'index.html')

def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    import pickle
    model = pickle.load(open(r"C:\Users\DELL\Titanic_Model_Random.sav", "rb"))
    model1 = pickle.load(open(r"C:\Users\DELL\Titanic_Model_Decision.sav", "rb"))
    model2 = pickle.load(open(r"C:\Users\DELL\Titanic_Model_Logistic.sav", "rb"))
    scaled = pickle.load(open(r"C:\Users\DELL\scaler.sav", "rb"))
    sc = MinMaxScaler(feature_range=(0, 1))
    prediction = model.predict(sc.fit_transform ([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))

    if prediction == 0:
        return "not survived"
    
    elif prediction == 1:
        return "survived"

    else:
        return "Error"

def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'result.html', {'result':result})
