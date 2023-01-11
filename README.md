## Evaluation of Modeling Techniques for Enrollment Forecasting at Los Medanos College
The goal of this project is to test several different data modeling techniques for their ability
to predict census enrollment at Los Medanos College.

#### -- Project Status: [Active]
### Project Description
The ability of three different modeling techniques to forecast enrollment numbers were evaluated on three quantitative criteria and also discussed from holistic, qualitative standpoint. The modeling techniques employed were:
1. Simple linear regression
2. Multiple linear regression
3. Neural networks

The major challenge in predicting enrollment numbers at LMC is the extremely small size of the dataset. This fact makes the problem interesting not only from a business and operations viewpoint, but also a more theoretical one - i.e. is it possible to apply machine learning effectively on such a small dataset. The strategy used to overcome the data limitation was bootstrap aggregation. By randomly resampling and splitting the data into training and testing sets, it was possible to estimate the error distribution for predictions on unseen data and construct prediction confidence intervals.