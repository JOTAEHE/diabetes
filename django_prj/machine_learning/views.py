import os.path
import pickle
import numpy as np

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'machine_learning/index.html')

def result(request):
    current_path = os.path.abspath(__file__)
    file_path_model = os.path.join(os.path.dirname(current_path), 'classifier.pkl')
    model = pickle.load(open(file_path_model, 'rb'))            #피클파일 읽어오기

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n1'])
    val3 = float(request.GET['n1'])
    val4 = float(request.GET['n1'])
    val5 = float(request.GET['n1'])
    val6 = float(request.GET['n1'])
    val7 = float(request.GET['n1'])
    val8 = float(request.GET['n1'])

    input_features = np.array([val1,val2,val3,val4,val5,val6,val7,val8])
    pred = model.predict(input_features.reshape(1,-1))
    # pred = 1 이면

    if pred == [1]:
        result_pred = '당뇨병이 의심됩니다. 의사선생님께 문의하세요'
    else :
        result_pred = '건강합니다'

    return render(request, 'machine_learning/result.html', {"result_pred" : result_pred})