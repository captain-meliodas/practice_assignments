Life Cycle of Data Science Projects
 - Data Preprocessing
    - EDA (Exploratory Data Analysis)
    - Feature Engineering
    - Feature Selection
 - Model Training
    - Model Creation
    - Hyperparameters Model Tuning
    - Model Deployment

Types of Regression
 - You can only predict continuous data using regression technique
 - Feature scaling is used to scaled large values (10 lakhs to 50 lakhs) to small range like -3 to +3
 - Linear Regression
    - y = b0 + b1 * x1
    - contains single independent variable (features)
    - based on signle independe variable predicts the y (label) (dependent variable)
 
 - Multiple Linear Regression
    - contains multiple independent variable (features)
    - y = b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + ... upto n

 - Polynomial Regression
    - y = b0 + b1*x1 + b2*(x1 ^ 2) + b3*(x1 ^ 2) + b4*(x1 ^ 2) + ... upto n
    - when data can't be fitted using a straight line

Support Vector Machine
 - Support Vector Regression
    - Minimizing the error between vectors (points on the plane)
    - Focuses on boundary vectors which called support vectors
    - Margin of error shoudl always be set to minimum as possible
    - for best results use rbf kernel with svr
 - Types of kernels in SVM
    - Gaussian RBF kernel
    - Laplace RBF kernel
    - Gaussian kernel
    - Polynomial kernel
    -  Hyperbolic tangent kernel
    - Sigmoid kernel

Decision Tree Regression
 - Divide the dataset into several parts
 - Creates decisions for new dataset that in which part it belongs
 - Each part contains a output which is resulted out as output when new dataset belongs to that part

Random Forest Regression
 - Pick at random K data points from the training set.
 - Build the decision tree associated to these K data points.
 - Choose the number Ntree of trees you want to build and repeats Steps 1 & 2
 - For a new data point. make each one of your Ntree trees predict the value of Y to for the data point in question. and assign the new data point the average across all of the predicted Y values

Logistic Regression
 - linear regresson + sigmoid function = Logitic Regression
 - type of classifier

KNN- K-nearest neighbour
 - Choose the number of k neighbours
 - take the K-nearest neighbours of the new data point, according to the Euclidean distance
 - Among these K neighbours count the number of data points in each category

Support Vector Classification
 - Choose the kernel linear or non-linear type
 - gaussian rbf kernel gives the best results. It is a non-linear kernel
 - The kernel trick

Naive Bayes
 - t predicts membership probabilities for each class such as the probability that given record or data point belongs to a particular class.
 - Posterior Probability = (Likelihood * Prior Probability) / Marginal Probability
 - Posterior Probability = P(Walks/X) 
 - Likelihood = P(X/Walks) = Number of similar observations Among those who walks / total number of walkers
 - Prior Probability = P(Walks) = Number of Walkers / Total Observations
 - Marginal Probability = P(X) = Number of similar observations / Total Observations

Decision Tree Classification
 - Criterion
    - gini --> the range of Gini Impurity lies in between 0 to 0.5
    - entropy --> The range of Entropy lies in between 0 to 1

Random Forest Classification
 - Based on decision tree
 - Creates n numbers of decision trees and predict new data points using those created n trees.

Clustering Techniques
 - K-Means Clustering.
   - The elbow method to choose optimal number of clusters.
   - Within Cluster Sum Of Squares (WCSS)
      - The within-cluster sum of squares is a measure of the variability of the observations within each cluster. Small Square means compact clusters than larger squares.
   - Random initialization trap
      - is a problem that occurs in the K-means algorithm. In random initialization trap when the centroids of the clusters to be generated are explicitly defined by the User then inconsistency may be created and this may sometimes lead to generating wrong clusters in the dataset.
   - Algorithm
      - Choose the number k of clusters.
      - Select at random K points. the centroids (not neccessarily from your dataset).
      - Assign each data point to the closest centroid --> forms the K clusters.
      - compute and place new centroid of each cluster.
      - Reassign each data point to the new closest centroid. If any reassignment took place. Goto previous step otherwise goto FIN.
 
 - Heirarchical Clustering
    - K-Means performs better than Hierarchical Clustering on large datasets.
    - Dendograms
       - Used to choose optimal number of clusters
       - Memorizes how the clusters are formed
    - Agglomerativeclustering
       - Training the models using heirarchical clustering
       - Predict the new data points to the clusters
 
 - Association Rule Learning
    - Support -> This says how popular an itemset is, as measured by the proportion of transactions in which an itemset appears.
    - Confidence -> This says how likely item Y is purchased when item X is purchased, expressed as {X -> Y}.
    - Lift -> support(X,Y) / (support(X) * support(Y)). For an association rule X ==> Y, if the lift is equal to 1, it means that X and Y are independent. If the lift is higher than 1, it means that X and Y are positively correlated. If the lift is lower than 1, it means that X and Y are negatively correlated.

    - Apriori
       - set minimum support and confidence.
       - Take all the subsets in transactions having higher support than minimum support. 
       - Take all the rules of these subsets having higher confidence than minimum confidence.
       - Sort the rules by decreasing lift. (lift = confidence / support)
    
    - Eclat
       - Set a minimum support.
       - Take all the subsets in transactions having higher support than minimum support.
       - Sort these subsets by decreasing support.
 
 - Multi-Armed bandit Problem
    - Problem related to reinforcement learning.

 - Reinforcement Learning
    - UCB (Upper Confidence Bound)
       - It allows to find which item is going to be used more than other so that we can focus on that item before market demand is increased for that item. For ex- several ads are clicked by the users we have to find most clicked add by the users i.e, which add is going to be clicked most by the users.
    
    - Thompson Sampling
       - It is probalistic approach to multi armed bandit problem
       - It allows us to visualize the outcomes in a distribution. The distribution allows us to find out the best solution to a problem in a probabilistic manner.
       - Beta Distribution --> the beta distribution is a family of continuous probability distributions defined on the interval [0, 1] parameterized by two positive shape parameters.

    - Prior Probability --> represents what is originally believed before new evidence is introduced.
    - Posterior Probability --> Posterior probability = prior probability + new evidence (called likelihood). It's an adjustment to prior probability with new evidence introduced.

Natural Language Processing
    - Natural Language Processing (or NLP) is applying Machine Learning models to text and language.
    - Classification. Good ones for NLP include:
       - CART
       - C5.0
       - Maximum Entropy

Deep Learning
    - Deep Learning is the most exciting and powerful branch of Machine Learning. Deep Learning models can be used for a variety of complex tasks:
       - Artificial Neural Networks for Regression and Classification.
       - Convolutional Neural Networks for Computer Vision.
       - Recurrent Neural Networks for Time Series Analysis
       - Self Organizing Maps for Feature Extraction.
       - Deep Boltzmann Machines for Recommendation Systems.
       - Auto Encoders for Recommendation Systems.
   
    - Artificail Neural Network (ANN)
       - Activation Function
          - Sigmoid, Tanh
       - Gradient Descent
       - Stochastic Gradient Descent
       - Backpropagation

       - Training the ANN with stochastic Gradient Descent.
          - Randomly inititalise the weights to small numbers close to 0 (but not 0).
          - Input the first observation of your dataset in the input layer, each feature in one input node.
          - Forward-Propagation: from left to right, the neurons are activated in a way that the impact of each neuron's activation is limited by the weights. Propagate the activations untill getting the predicted result y.
          - Compare the predicted result to the actual result Measure the generated error.
          - Back-Propagation: from right to left the error is back-propagated. Update the weights according to how much they are responsible for the error. The learning rate decides by how much we update the weights.
          - Repeat Steps 1 to 5 and update the weights after each observation (Reinforcement Learning). Or: Repeat steps 1 to 5 but update the weights only after a batch of observations (Batch Learning).
          - When the whole training set passed through the ANN, that makes an epoch. Redo more epochs.
    
    - Convolutional Neural Networks:
       - We use feature map to map the given matrix to which class it belongs.
       - ReLu Layer --> Rectified Linear Unit activation function will output the input directly if it is positive, otherwise, it will output zero.
       - Max Pooling --> if we are using different images at different angles of same thing neural network should able to classify it as same. where we use pooling layer to extract weighted important features only.
       - Flattening --> flattening the pooled matrix to fed to the neural network.
       - SoftMax and Cross Entropy --> Softmax is an activation function that outputs the probability for each class and these probabilities will sum up to one. Cross Entropy loss is just the sum of the negative logarithm of the probabilities. They are both commonly used together in classifications.The cross-entropy function, through its logarithm, allows the network to asses such small errors and work to eliminate them

    - Dimensionality Reduction
       - Feature Selection
          - Backward Elimination, Forward Selection, Bidirectional Elimination, Score Comparision and more.
       - Feature Extraction
          - Pricipal Component Analysis (PCA) --> Component axes that maximize the variance.
          - Linear Discriminant Analysis (LDA) --> maximizing the component axes for class-separation.
          - Kernel PCA.
          - Quadratic Discriminant Analysis (QDA).

    - Model Selection Techniques
       - Evaluating models, optimal values for the hyperparameters and finding appropriate model for problems.
       - Techniques
          - k-Fold Cross Validation.
          - Grid Search.
   
    - XGBoost (XGBoostClassifier and XGBRegressor)
       - This approach supports both regression and classification predictive modeling problems.
       - XGBoost is an implementation of gradient boosted decision trees designed for speed and performance.
       - Gradient boosting is a machine learning technique used in regression and classification tasks, among others. It gives a prediction model in the form of an ensemble of weak prediction models, which are typically decision trees.
   
    - More Model Boosters like XGboost
       - CatBoost

---
Machine Learning Terms
 - Confusion Matrix
    - A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known
    - Error rate = total wrong / total observations
    - Accuracy Rate = total correct / total observations
    - Accuracy Paradox- when lots of observations falls into one classification, 2nd classification was neglected this increases the accuracy but removing a classification class will result in failure of model predictions.

    - Cumlative Accuracy Profile -> A cumulative accuracy profile can be used to evaluate a model by comparing the current curve to both the 'perfect' and a randomized curve.A good model will have a CAP between the perfect and random curves; the closer a model is to the perfect CAP, the better is.

 - In data preprocessing Fit calulates the value and transform apply those values to cells in each features. It will convert our feature vector f to f' after fit_transform.
 - In model creation fit mehtod on regressor or classifier tries to learn the (y=mx+c in case of linear regression) values of slope m and coefficient c using the f' or f features which is provided.
 - Fit and transform are apllied to training data only.
 - Only transform is applied for testing data. This help us to overcome overfitting of data as original computed values in fit and transform is also used for test data transform.
 - Mapping data to higher dimension. This method is compute intensive as we have to project the plane to higher dimension for computation and revert the changes back to a 2d plane.
 - Hyperparameters -> The hyperparameters are the parameters that are not learnt and that are fixed values inside the model equations