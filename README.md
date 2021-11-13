Final Project: ASHRAE Predicting
Building Energy Consumption
Team Members: Ravi Patel, Jay Pike, Vijay Rajagopal, Samuel Okhuegbe, Chris O’Brien
Class: COSC 522-Machine Learning
Professor: Dr. Hairong Qi
Date: November 13, 2021

Introduction and Background
Building energy consumption accounts for a large portion of a country's total energy
consumption. In OECD (Organization for Economic Co-operation and Development) countries,
commercial buildings account for approximately 32% of final electric energy consumption. In
the United States, buildings account for over 35% of end-use electricity consumption [1].
Predicting the energy consumption of a building can be quite challenging largely due to the fact
that energy consumption is affected by various internal and external factors.
Such examples of variations include weather conditions, occupants’ behavioral patterns
regarding energy consumption, and structural layouts of a given building. Predicting the future
energy consumption of a building is of particular interest to us since it can allow building
managers to better optimize their energy usage and create load-balancing solutions during
periods of peak energy demand. Additionally, energy consumption predictions could be used to
intelligently implement “smart”-building retrofits that reduce the building’s overall energy use.
The end goal of energy consumption reduction is the minimization of the building's carbon
footprint.

ASHRAE Kaggle Competition
Our project is based on the Kaggle competition by the American Society of Heating,
Refrigerating and Air-Conditioning Engineers (ASHRAE). We plan to develop machine learning
models that can regress the energy consumption of a building from the building’s features, such
as meter readings from the chilled water, hot water, electric and steam meters. More specifically,
the hourly meter data obtained from over 1,000 buildings over a three-year timeframe will be
used. In addition to the meter data, the ASHRAE dataset also includes a large sample of
weather-related data that can be used to account for effects of temperature and humidity on the
existing building features. In terms of challenging aspects of the given topic, the ASHRAE
dataset contains many different features and more than ten-thousand samples. This can increase
computation costs as well as decrease the accuracy of a given model. There are some features
which have a clear correlation with the energy consumption but are unpredictable. For example,
extreme weather can cause the energy consumption to increase; however, it is difficult to predict
the weather, making it difficult to predict energy consumption with that important feature. A well
known challenge with multiple features is finding the best combination of features which obtain
the most accurate machine learning model. Finally, the results are evaluated using the root mean
squared logarithmic error (RMSLE). 

[1] B. Yildiz, J. I. Bilbao, and A. B. Sproul, “A review and analysis of regression and
machine learning models on commercial building electricity load forecasting,”
Renew. Sustain. Energy Rev., vol. 73, no. March 2016, pp. 1104–1122, 2017, doi:
10.1016/j.rser.2017.02.023.