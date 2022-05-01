# DBS Stockprice Prediction App

The following project is a (very) simple assignment done for the module CET023 for the NTU Fleximasters in Business and Financial Analytics Programme.
The app was deployed using Streamlit Cloud and can be accessed [here](https://share.streamlit.io/ashwinphilipgeorge/credit_card_prediction/main/streamlit.py)


## Project Details
The following project is a deployment of a Linear Regressor model used to predict the share price of DBS Bank with relation to the value of the Singapore Dollar against the US Dollar. The app is deployed on Streamlit cloud, making use of the Streamlit UI python package.

The app uses one feature:
1. Value of the Singapore Dollar against the US Dollar
to predict the stockprice of DBS at that given value.

The app also has features that allow the user to view the raw data, as well as charts that show the movement of the SGD/DBS prices against time.

### Models Used
1) Linear Regressor

### Deployment Technique
The app's front-end was created with the python package `streamlit`, which generates an intuitive and user friendly UI for users. Refer to the documentation [here](https://docs.streamlit.io/) to find out more about how streamlit can be used to create and customised user interfaces and forms.

On top of the python package, Streamlit Cloud is a platform (similar to heroku) that allows users to seamlessly deploy applications that make use of the streamlit package. An app can be deployed very quickly by folowing the deployment documentation [here](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app)

### Dependencies
The app uses `joblib`, `sklearn` and `pandas`. Version numebr not specified as the app is a very simple one using very basic functionalities that should not be affected by package version.








