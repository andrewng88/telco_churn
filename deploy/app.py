# Core Pkg
import streamlit as st
import pandas as pd 
import numpy as np

import pickle # loading model 
import base64 # enable file download

#function to load and cache(faster) the dataset and set mutation to True
@st.cache(allow_output_mutation=True)
def load_data(dataset):
     df = pd.read_csv(dataset)
     return df

# load model from pickle after ML
def load_prediction_models(model_file):
	loaded_model = pickle.load(open(model_file,"rb"))
	return loaded_model

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="file.csv">Download csv file</a>'

# the main or header function
# visitors can select Prediction and About
def main():
    
    st.title('Telco Churn Binary Classification ')
    st.image("data/churn.png")

    # load all the 3 models
    logreg = load_prediction_models('data/logreg_model.pkl')
    rf = load_prediction_models('data/rf_model.pkl')
    svc = load_prediction_models('data/svc_model.pkl')

    st.sidebar.subheader('Project by:')
    st.sidebar.markdown('**Andrew Ng**  [![LinkedIn](https://cdn3.iconfinder.com/data/icons/socialnetworking/32/linkedin.png)](https://www.linkedin.com/in/sc-ng-andrew/)')
    st.sidebar.markdown('He is passionate :heart: about Data Science and helps businesses :moneybag: uncover insights from their data :computer:.\
        He is currently pursuing his :books: Masters in Analytics at GeorgiaTech')
    
    # Menu
    menu = ['Prediction','Batch Prediction']
    choices = st.sidebar.selectbox('Select Menu',menu)

    if choices == 'Prediction':
        st.header('Supervised Machine Learning')
        st.subheader('Select all the options below and it will predict') 
        st.subheader('whether the customer will churn or not .')

        # convert Yes/No to 1/0 and vice-versa
        binary_mapper = { 'Yes' : 1 , 'No' : 0}
        binary_mapper_inv = { 1 : ':ballot_box_with_check:' , 0 : ':negative_squared_cross_mark:'}

        # Obtain inputs from user
        gender = st.radio("Gender : ", ("Male", "Female"))
        gender_results = f"Gender is **{gender}**."

        SeniorCitizen_temp = st.radio("Senior Citizen : ", ("Yes", "No"))
        SeniorCitizen = binary_mapper[SeniorCitizen_temp]
        SeniorCitizen_results = f"Senior Citizen : **{SeniorCitizen_temp}**."

        Partner = st.radio("Partner : ", ("Yes", "No"))
        Partner_results = f"Partner : **{Partner}**."

        Dependents = st.radio("Dependents : ", ("Yes", "No"))
        Dependents_results = f"Dependents : **{Dependents}**."

        tenure = st.text_input("Tenure( months ) : ", 1 )
        tenure_results = f"Tenure : **{tenure}** months."

        PhoneService = st.radio("PhoneService : ", ("Yes", "No"))
        PhoneService_results = f"PhoneService : **{PhoneService}**."

        MultipleLines = st.radio("MultipleLines : ", ('No', 'Yes','No phone service'))
        MultipleLines_results = f"MultipleLines : **{MultipleLines}**."

        InternetService = st.radio("InternetService : ", ('DSL', 'Fiber optic', 'No'))
        InternetService_results = f"InternetService : **{InternetService}**."

        OnlineSecurity= st.radio("OnlineSecurity : ", ('Yes', 'No', 'No internet service'))
        OnlineSecurity_results = f"OnlineSecurity : **{OnlineSecurity}**."

        OnlineBackup = st.radio("OnlineBackup  : ", ('Yes', 'No', 'No internet service'))
        OnlineBackup_results = f"OnlineBackup  : **{OnlineBackup }**."

        DeviceProtection = st.radio("DeviceProtection : ", ('Yes', 'No', 'No internet service'))
        DeviceProtection_results = f"DeviceProtection : **{DeviceProtection}**."
        
        TechSupport = st.radio("TechSupport: ", ('Yes', 'No', 'No internet service'))
        TechSupport_results = f"TechSupport : **{TechSupport}**."

        StreamingTV = st.radio("StreamingTV : ", ('Yes', 'No', 'No internet service'))
        StreamingTV_results = f"OnlineSecurity : **{StreamingTV}**." 

        StreamingMovies = st.radio("StreamingMovies : ", ('Yes', 'No', 'No internet service'))
        StreamingMovies_results = f"OnlineSecurity : **{StreamingMovies}**."

        Contract = st.radio("Contract : ", ('Month-to-month', 'One year', 'Two year'))
        Contract_results = f"Contract : **{Contract}**."

        PaperlessBilling = st.radio("PaperlessBilling : ", ('Yes', 'No'))
        PaperlessBilling_results = f"OnlineSecurity : **{PaperlessBilling}**."

        PaymentMethod = st.radio("PaymentMethod : ", ('Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'))
        PaymentMethod_results = f"PaymentMethod : **{PaymentMethod}**."

        MonthlyCharges = st.text_input("MonthlyCharges $ : ", 12 )
        MonthlyCharges_results = f"MonthlyCharges : **${MonthlyCharges}**."
  
        TotalCharges = st.text_input("TotalCharges $ : ", 123 )
        TotalCharges_results = f"TotalCharges : **${TotalCharges}**."

        # display data input
        # if st.checkbox('Verbose ON/OFF:'):
        #     st.markdown(gender_results)
        #     st.markdown(SeniorCitizen_results)
        #     st.markdown(Partner_results)
        #     st.markdown(Dependents_results)
        #     st.markdown(tenure_results)
        #     st.markdown(PhoneService_results)
        #     st.markdown(MultipleLines_results)
        #     st.markdown(InternetService_results)
        #     st.markdown(OnlineSecurity_results)
        #     st.markdown(OnlineBackup_results)
        #     st.markdown(DeviceProtection_results)
        #     st.markdown(TechSupport_results)
        #     st.markdown(StreamingTV_results)
        #     st.markdown(StreamingMovies_results)
        #     st.markdown(Contract_results)
        #     st.markdown(PaperlessBilling_results)
        #     st.markdown(PaymentMethod_results)
        #     st.markdown(MonthlyCharges_results)
        #     st.markdown(TotalCharges_results)

        # condolidate all data for prediction
        sample_data = [[gender, SeniorCitizen, Partner, Dependents,
        tenure, PhoneService, MultipleLines, InternetService,
        OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
        StreamingTV, StreamingMovies, Contract, PaperlessBilling,
        PaymentMethod, MonthlyCharges, TotalCharges]]

        # columns to attach to DataFrame
        list_columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
        'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

        # create sample data as DF for prediction
        sample_data = pd.DataFrame(sample_data, columns = list_columns) 

        #predict sample_data using LogReg and convert from binary to Yes/No in emoji!!

        if st.button("Predict"):
            logreg_pred = logreg.predict(sample_data)
            st.subheader('Prediction whether it will Churn or Not ?:')
            logreg_pred = "{} {}".format('**MAIN Prediction by Logistic Regression** : ', binary_mapper_inv[logreg_pred[0]])
            st.markdown(logreg_pred)

        # additional predictions using RF and SVC
        #if st.checkbox('Display predictions from Random Forest and SVC:'):
            rf_pred = rf.predict(sample_data)
            rf_pred = "{} {}".format('Prediction by Random Forest : ', binary_mapper_inv[rf_pred[0]])
            st.markdown(rf_pred)
            
            svc_pred = svc.predict(sample_data)
            svc_pred = "{} {}".format('Prediction by SVC : ', binary_mapper_inv[svc_pred[0]])
            st.markdown(svc_pred)

        #display data input
        if st.checkbox('Display input Data:'):

            st.write('Data collated for prediction:')
            st.write(sample_data)  

        #display odds
        if st.checkbox('Display Logistic Regression Odds - Higher odds will contribute to Churn:'):
            odds  = load_data('data/odds.csv')
            st.dataframe(odds)

    # Batch Predictions
    if choices == 'Batch Prediction':
         st.header('Batch Prediction')
         st.write('Template csv can be downloaded here')
         
         # prepare template df for demo purposes
         template = load_data('data/template.csv')
         columns = template.columns
         st.markdown(get_table_download_link(template), unsafe_allow_html=True)

         # upload template file for batch predictions
         file_upload = st.file_uploader("Upload template csv file for predictions", type=["csv"])
         
         if file_upload is not None:
            df_file_upload = pd.read_csv(file_upload)
            batch_predictions = logreg.predict(df_file_upload)
            df_batch_predictions = pd.concat([pd.DataFrame({'churn' : batch_predictions}),df_file_upload], axis=1)
            
            # output text
            st.write(df_batch_predictions)

            # choice to download csv
            if st.checkbox('Download batch prediction in csv format'):
                st.markdown(get_table_download_link(df_batch_predictions), unsafe_allow_html=True)
    
if __name__=='__main__':
    main()
