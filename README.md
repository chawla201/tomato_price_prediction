# Tomato Price Prediction
## tl;dr
- Scraped Tomato prices in Karnataka from Jan-01-
2015 to Feb-01-2021 from the [Agricultural Marketing website of the Government of India](https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=30-Jun-2020&DateTo=30-Jun-2020&Fr_Date=30-Jun-2020&To_Date=30-Jun-2020&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--)
- Trained a Random Forest Regression model
- Developed a Flask API
- Developed a web app using Flask 
## File System
```
tomato_price_prediction/ #Home Directory
  |-images/
  |-static/
    |-style.css #CSS file for the web app
  |-templates/
    |-home.html #html code for home page
    |-predict.html #html page for predict page
  |-Scrapper.ipynb #Python Notebook for web scraping code
  |-api.py #Flask API
  |-app.py #Flask Web App
  |-code.ipynb #Python notebook with EDA and Model developemnt code
  |-prediction_model.py #functions used in api.py
  ```
  <b>Note:</b> <a href="https://drive.google.com/drive/folders/1p39S_qRTGpUSbVFK65kb75pRQMAtkogR?usp=sharing">Click here</a> to access the pre-trained ML model.
## Technologies Used
* <strong>Python</strong>
* <strong>Pandas</strong>
* <strong>Plotly</strong>
* <strong>Machine Learning</strong>
* <strong>Flask</strong>
* <strong>HTML, CSS</strong>
* <strong>Selenium</strong>
* <strong>Beuatiful Soup</strong>

## Data
Data used in this application was scraped from the [Agricultural Marketing website of the Government of India](https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=30-Jun-2020&DateTo=30-Jun-2020&Fr_Date=30-Jun-2020&To_Date=30-Jun-2020&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--) using Selenium and Beautiful Soup.<br>
The data consists of 35544 enties of Tomato prices in Karnataka from Jan-01-2015 to Feb-01-2021 from different districts and markets within these districts.<br>
First five entries in the data set are:
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>District Name</th>
      <th>Market Name</th>
      <th>Commodity</th>
      <th>Variety</th>
      <th>Grade</th>
      <th>Min Price (Rs./Quintal)</th>
      <th>Max Price (Rs./Quintal)</th>
      <th>Modal Price (Rs./Quintal)</th>
      <th>Price Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Davangere</td>
      <td>Davangere</td>
      <td>Tomato</td>
      <td>Tomato</td>
      <td>FAQ</td>
      <td>400</td>
      <td>600</td>
      <td>500</td>
      <td>2015-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Davangere</td>
      <td>Honnali</td>
      <td>Tomato</td>
      <td>Tomato</td>
      <td>FAQ</td>
      <td>800</td>
      <td>1000</td>
      <td>900</td>
      <td>2015-01-01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kolar</td>
      <td>Srinivasapur</td>
      <td>Tomato</td>
      <td>Tomato</td>
      <td>FAQ</td>
      <td>465</td>
      <td>1335</td>
      <td>935</td>
      <td>2015-01-01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bangalore</td>
      <td>Channapatana</td>
      <td>Tomato</td>
      <td>Tomato</td>
      <td>FAQ</td>
      <td>1000</td>
      <td>1400</td>
      <td>1200</td>
      <td>2015-01-01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Shimoga</td>
      <td>Shimoga</td>
      <td>Tomato</td>
      <td>Tomato</td>
      <td>FAQ</td>
      <td>400</td>
      <td>600</td>
      <td>500</td>
      <td>2015-01-01</td>
    </tr>
  </tbody>
</table>

## Data Analysis
<img src="https://github.com/chawla201/tomato_price_prediction/blob/main/images/download.png">
By looking at the rolling average with a 30 day window, we can observe that tomato prices in Karnatak follows a seasonal trend:
<ul>
<li>There are two major spikes in the prices during a year. First is the sharp rise around the months of June-July. This rise is followed by another but lower spike in the month of december.</li>
<li>The lowest prices are observed in the year 2018.</li>
<li>The highest peaks are observed in the year 2016 and 2017.</li>
 </ul>
Another observable trend is that average modal price of tomatoes per quintal in Bangalore is higher than that in the rest of the state. 

## Model
A Random Forest Regression Model was used in as the prediction model. Presence of categorical variables suits the base estimator (Decision Trees) and Random forest being a bagging algorithm, is robust to varying varaible values.<br>

```
Pipeline(steps=[('column_transformer',
                 ColumnTransformer(remainder='passthrough',
                                   transformers=[('cat',
                                                  OneHotEncoder(drop='first',
                                                                sparse=False),
                                                  ['District Name',
                                                   'Market Name', 'Variety',
                                                   'Grade']),
                                                 ('scale', MinMaxScaler(),
                                                  ['year', 'month',
                                                   'day of the month',
                                                   'day of the week'])])),
                ('rfr', RandomForestRegressor(n_estimators=300))])
```
## Model Performance
Evaluation metric used to check the model performance was Mean Absolute Error.<br>
The Mean Absolute Error value given by the model on the test data was 175.86

## Screenshots
<img src="https://github.com/chawla201/tomato_price_prediction/blob/main/images/Screenshot1.jpg">
<img src="https://github.com/chawla201/tomato_price_prediction/blob/main/images/Screenshot2.jpg">
