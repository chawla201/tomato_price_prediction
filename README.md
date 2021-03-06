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
## Screenshots
<img src="https://github.com/chawla201/tomato_price_prediction/blob/main/images/Screenshot1.jpg">
<img src="https://github.com/chawla201/tomato_price_prediction/blob/main/images/Screenshot2.jpg">
