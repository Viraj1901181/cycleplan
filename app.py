import pandas as pd
import numpy as np
import pickle
import sklearn
import matplotlib.pyplot as plt
import streamlit as st

# Declaring the input variables

variables = ['CycleValueInsured', 'Accessories', 'ReplacementHire', 'RoadsideRecovery', 'IncludeCompetitiveUse', 'IncludeEuropeanCover', 'IncludeWorldwideCover', 'IncludeExcessWaiver', 'IncludeLegalExpenses', 'Age', 'NumberOfCycles', 'BMX', 'City', 'CycloCross', 'ElectricBike', 'Folding', 'Hybrid', 'Mountain', 'Recumbent', 'RoadRacing', 'Touring', 'Trekking', 'Tricycle', 'Unicycle', 'Other', 'ElectricScooter', 'gender','DeathCover', 'Disablement', 'risk','PublicLiability', 'LossOfEarningsCoverage', 'No. Claims']

ReplacementHire = ['0','500', '750', '1000']
RoadsideRecovery = ['1', '0']
IncludeCompetitiveUse = ['1', '0']
IncludeEuropeanCover = ['1', '0'] 
IncludeWorldwideCover = ['1', '0']
IncludeExcessWaiver = ['1', '0'] 
IncludeLegalExpenses = ['1', '0']
BMX = ['1', '0']  
City = ['1', '0']
CycloCross = ['1', '0']
ElectricBike = ['1', '0']
Folding = ['1', '0'] 
Hybrid = ['1', '0'] 
Mountain = ['1', '0'] 
Recumbent = ['1', '0'] 
RoadRacing = ['1', '0'] 
Touring = ['1', '0'] 
Trekking = ['1', '0'] 
Tricycle = ['1', '0'] 
Unicycle = ['1', '0'] 
Other = ['1', '0']
ElectricScooter = ['1', '0'] 
gender = ['1', '0']
DeathCover = ['0','10000','25000','50000']
Disablement = ['0','10000','25000','50000']
risk = ['1','2','3','4','5']
PublicLiability = ['0','1','2','5'] 
LossOfEarningsCoverage = ['0', '250', '500', '750']


pipe = pickle.load(open('model_from_rawdata.pkl', 'rb'))
st.title('Cycle Plan Premium Calculator')

CycleValueInsured = float(st.number_input('Enter the value of cycle you want to insure'))
PublicLiability = float(st.selectbox('Select the desired Public Liability Coverage', sorted(PublicLiability)))
Accessories = float(st.number_input('Enter the value of accessories you want to insure')) 
ReplacementHire = float(st.selectbox('Select the desired ReplacementHire value needed', sorted(ReplacementHire)))
RoadsideRecovery = float(st.selectbox('Want roadside recovery', sorted(RoadsideRecovery)))
DeathCover = float(st.selectbox('Select the desired Death Coverage', sorted(DeathCover)))
Disablement = float(st.selectbox('Select the desired Disablement Coverage', sorted(Disablement)))
IncludeCompetitiveUse = float(st.selectbox('Want to include competitive use?', sorted(IncludeCompetitiveUse)))
IncludeEuropeanCover = float(st.selectbox('Want to include European Cover?', sorted(IncludeEuropeanCover)))
IncludeWorldwideCover = float(st.selectbox('Want to include Worldwide cover?', sorted(IncludeWorldwideCover)))
IncludeExcessWaiver = float(st.selectbox('Want to include Excess Waiver?', sorted(IncludeExcessWaiver)))
IncludeLegalExpenses = float(st.selectbox('Want to include legal expenses coverage?', sorted(IncludeLegalExpenses)))
LossOfEarningsCoverage = float(st.selectbox('Select the desired Loss of Earnings Coverage needed', sorted(LossOfEarningsCoverage)))
Age = float(st.number_input('Enter the age of policy holder'))
NumberOfCycles = float(st.number_input('Enter the total number of cycles to be insured'))
BMX = float(st.selectbox('Whether bike type BMX?', sorted(BMX)))
City = float(st.selectbox('Whether bike type City?', sorted(City)))
CycloCross = float(st.selectbox('Whether bike type CycloCross?', sorted(CycloCross)))
ElectricBike = float(st.selectbox('Whether bike type Electric Bike?', sorted(ElectricBike)))
Folding = float(st.selectbox('Whether bike type Folding?', sorted(Folding)))
Hybrid = float(st.selectbox('Whether bike type Hybrid?', sorted(Hybrid)))
Mountain = float(st.selectbox('Whether bike type Mountain?', sorted(Mountain)))
Recumbent = float(st.selectbox('Whether bike type Recumbent?', sorted(Recumbent)))
RoadRacing = float(st.selectbox('Whether bike type RoadRacing?', sorted(RoadRacing)))
Touring = float(st.selectbox('Whether bike type Touring?', sorted(Touring)))
Trekking = float(st.selectbox('Whether bike type Trekking?', sorted(Trekking)))
Tricycle = float(st.selectbox('Whether bike type Tricycle?', sorted(Tricycle)))
Unicycle = float(st.selectbox('Whether bike type Unicycle?', sorted(Unicycle)))
Other = float(st.selectbox('Whether bike type Other?', sorted(Other)))
ElectricScooter = float(st.selectbox('Whether type Electric Scooter?', sorted(ElectricScooter)))
N_Claims = float(st.number_input('Enter the total number of claims made in the past'))
risk = float(st.selectbox('Select the location risk level of policy holder', sorted(risk)))
gender = float(st.selectbox('Select the gender of policy holder', sorted(gender)))



if st.button('Calculate Premium'):
     input_dict = {'CycleValueInsured': CycleValueInsured, 'PublicLiability': PublicLiability, 'Accessories' : Accessories, 'ReplacementHire': ReplacementHire, 'RoadsideRecovery': RoadsideRecovery,'DeathCover' : DeathCover , 'Disablement' : Disablement, 'IncludeCompetitiveUse' : IncludeCompetitiveUse, 'IncludeEuropeanCover': IncludeEuropeanCover, 'IncludeWorldwideCover': IncludeWorldwideCover, 'IncludeExcessWaiver': IncludeExcessWaiver, 'IncludeLegalExpenses': IncludeLegalExpenses,'LossOfEarningsCoverage': LossOfEarningsCoverage, 'Age': Age, 'NumberOfCycles': NumberOfCycles, 'BMX': BMX, 'City': City, 'CycloCross': CycloCross, 'ElectricBike': ElectricBike, 'Folding': Folding, 'Hybrid':Hybrid, 'Mountain': Mountain, 'Recumbent': Recumbent, 'RoadRacing': RoadRacing, 'Touring': Touring, 'Trekking': Trekking, 'Tricycle' : Tricycle, 'Unicycle' : Unicycle, 'Other' : Other, 'ElectricScooter': ElectricScooter, 'No. Claims' : N_Claims,'risk': risk, 'gender': gender}
     
     #values = [list for key, list in input_dict.items()]
     values = list(input_dict.values())
     values_array = np.array(values)
     
     #from sklearn.preprocessing import StandardScaler, MinMaxScaler
     X_mean_lst = [[1.54709090e+03, 7.56425299e+05, 1.16952118e+02, 2.10385067e+01,
        1.48653886e-04, 8.33781065e+03, 8.33781065e+03, 6.50997839e-02,
        1.05061134e-01, 2.42836741e-02, 3.22775368e-01, 2.48390025e-01,
        4.22283218e+01, 4.22989907e+01, 1.08391512e+00, 4.20478135e-03,
        2.28449168e-02, 3.16845140e-02, 1.32498394e-01, 1.66970168e-02,
        1.65350903e-01, 2.39231884e-01, 1.25293990e-03, 4.19957846e-01,
        1.58369479e-02, 2.10239067e-03, 1.42813912e-03, 2.91998705e-04,
        3.05324464e-02, 6.02579145e-03, 4.51429997e-02, 3.18995312e+00,
        8.56416273e-01]]
     X_stddev_lst = [[1.82778519e+03, 1.08745029e+06, 2.22087468e+02, 1.20008091e+02,
        1.21914961e-02, 1.60002377e+04, 1.60002377e+04, 2.46702503e-01,
        3.06632991e-01, 1.53928890e-01, 4.67538865e-01, 4.32080330e-01,
        1.48853828e+02, 1.40656996e+01, 7.04472646e-01, 7.25228287e-02,
        1.57504926e-01, 1.82288602e-01, 3.69671991e-01, 1.34363369e-01,
        4.05183831e-01, 5.18105232e-01, 3.53748029e-02, 6.20669475e-01,
        1.30784644e-01, 4.67218075e-02, 3.77638333e-02, 1.73934810e-02,
        1.90916491e-01, 9.09528678e-02, 2.24002351e-01, 1.44618007e+00,
        3.50668067e-01]]
     values_scaled = (values_array - X_mean_lst)/X_stddev_lst   
     premium = pipe.predict(values_scaled.reshape(1,-1))
     
     y_mean = 111.59871714881261
     y_stddev = 106.44860291260697
     premium_final = (premium*y_stddev) + y_mean
     
     st.header("Premium of selected policy =" + str(premium_final))
