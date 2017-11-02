from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import csv

date_list =[]
price_list = []

print("Welcome to Stock exchange predictor using Linear Regression\n ")
def collect_data(filename):  #Function to read and save collected csv data from file 'Japan_stock.csv' to lists
    rawdata = open(filename , 'r')
    data = csv.reader(rawdata)
    next(data)
    for row in data:
        date_list.append(int(row[0]))
        price_list.append(float(row[1]))

def plot_predict_model(date_list, price_list, x):  #Function to plot our model and precit the stock open price on Sep. 29th
    model = linear_model.LinearRegression()
    dates = np.reshape(date_list,(len(date_list),1))
    prices = np.reshape(price_list,(len(price_list),1))
    model.fit(dates,prices)
    plt.scatter(dates, prices, color='yellow')  #Plot of the collected data on the coordinates
    plt.plot(dates, model.predict(dates), color='orange', linewidth=5)  # Plot of the line (model fit) formed by Linear Regreesion
    plt.show()
    predicted_price = model.predict(x)  #Predicting the stock open price on Sep. 29th
    coef = model.coef_[0][0]  #Coefficient(m) of the model formed (Y = m*X + c)
    intercept = model.intercept_[0]  #Intercept(c) of the model formed (Y = m*X + c)
    print("Predicted price for stock open on September 28th is: ",predicted_price[0][0])
    print("The coefficient and intercept of the formed model by Linear Regression are: ", coef , intercept )

collect_data('Japan_stock.csv')
plot_predict_model(date_list,price_list,1)

