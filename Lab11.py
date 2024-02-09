from pandas import DataFrame

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load the California Housing Dataset
cali = fetch_california_housing()

# Create a Pandas DataFrame from the dataset
caliDataframe = DataFrame(data=cali.data, columns=cali.feature_names)
caliDataframe['Target'] = cali.target  # Adding the target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(caliDataframe.drop('Target', axis = 1), caliDataframe['Target'], test_size = 0.2, random_state = 42)

# Perform multiple linear regression using all features
multiLinearRegression = LinearRegression()
multiLinearRegression.fit(X_train, y_train)
multiYPrediction = multiLinearRegression.predict(X_test)

multiRSquaredValue = r2_score(y_test, multiYPrediction)
multiMSEValue = mean_squared_error(y_test, multiYPrediction)

# Print results for multiple linear regression
print("\nMultiple Linear Regression using All features")
print(f"R2 score: {multiRSquaredValue}")
print(f"MSE score: {multiMSEValue}\n")

# Initialize lists to store results for each feature
RSquaredPerFeature = []
MSEPerFeature = []

# Iterate through each feature and perform simple linear regression
for featureName in cali.feature_names:
    # Extract the feature as a single column
    feature = X_train[featureName].values.reshape(-1, 1)
    feature_test = X_test[featureName].values.reshape(-1, 1)

    # Create and train a simple linear regression model
    simpleLinearRegression = LinearRegression()
    simpleLinearRegression.fit(feature, y_train)
    
    # Make predictions
    yPredictionValue = simpleLinearRegression.predict(feature_test)
    
    # Calculate R2 score and MSE for each feature
    FeatureRSquared = r2_score(y_test, yPredictionValue)
    FeatureMSE = mean_squared_error(y_test, yPredictionValue)
    
    # Append the scores to the lists
    RSquaredPerFeature.append(FeatureRSquared)
    MSEPerFeature.append(FeatureMSE)
    
    # Print results for each feature
    print(f"Feature {cali.feature_names.index(featureName)} has R2 score: {FeatureRSquared}")
    print(f"        has MSE score: {FeatureMSE}\n")