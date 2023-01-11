## Evaluation of Modeling Techniques for Enrollment Forecasting at Los Medanos College
The goal of this project is to test several different data modeling techniques for their ability
to predict census enrollment at Los Medanos College.

#### -- Project Status: [Active]
### Project Description
The ability of three different modeling techniques to forecaset enrollment numbers were evaluated on three quantitative criteria and also discussed from hoslistic, qualitative standpoint. The modeling techniques employed were:
1. Simple linear regression
2. Multiple linear regression
3. Neural networks
The major challenge in predicting enrollment numbers at LMC is the extreemly small size of the dataset. This fact makes the problem iteresting not only from a business and opperations viewpoint, but also a more theoretical one - i.e. is it possible to apply machine learning effectivly on such a small dataset. The strategy used to overcome the data limiation was bootsrap aggregation. By randomly resampling and splitting the data into training and testing sets, it was possible to estimate the error distribution for predictions on unseen data and construct prediction confidence intervals. This methodology allowed the models to be evaluated on three criteria:
1. Properties of the mean absolute error of bootstrap test set prediction ()
