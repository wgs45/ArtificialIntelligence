# 🤖 Machine Learning Algorithms

---

# 🌌 1. Regression

Regression is a **statistical method** used to model the relationship between variables.

### 🎯 Goal

Find a **continuous function** that best represents the relationship between input and output data.

---

## 📊 Example Dataset — Seniority vs Salary

| Seniority (Years) | Salary |
| ----------------- | ------ |
| 1                 | 30000  |
| 2                 | 25000  |
| 3                 | 35000  |
| 3.5               | 32000  |
| 4                 | 35000  |
| 4.5               | 32000  |
| 6                 | 35000  |
| 6                 | 50000  |
| 7                 | 40000  |

---

### 📈 Concept

Regression attempts to learn a function:

```text
Salary = f(Seniority)
```

Example prediction:

```text
Seniority = 5 years → Salary ≈ predicted value
```

---

### ⚡ Common Regression Models

- 📉 Linear Regression
- 📊 Polynomial Regression
- 📈 Ridge / Lasso Regression

---

### 🧠 Mini Recap

Regression:

- predicts **continuous values**
- models **relationships between variables**

---

# 🌳 2. Decision Tree

A **decision tree** is a supervised learning algorithm that uses a **tree-like structure of decisions**.

Each node asks a **question about features**.

---

## 🐾 Example: Animal Classification

```text
Does it have fur?
├── Yes → Dog
└── No
    ├── Can it fly? → Bird
    └── Does it have legs?
         ├── Yes → Fish
         └── No → Shrimp
```

---

### 🌟 Key Idea

Decision trees work by:

1️⃣ Splitting data based on features
2️⃣ Creating branches for decisions
3️⃣ Producing a final classification

---

### ⚠️ Limitation

Trees can **overfit training data**.

---

### 🧠 Mini Recap

Decision Trees:

- simple and interpretable
- prone to **overfitting**

---

# 🌲 3. Random Forest

A **Random Forest** is an ensemble method that combines **multiple decision trees**.

Instead of relying on a single tree:

```text
Many Trees → Combined Prediction
```

---

## ⚙️ Concept

```text
Original Training Data
       ↓
Random Sampling
       ↓
Tree A   Tree B   Tree C   Tree D
       ↓
Average / Majority Vote
       ↓
Final Prediction
```

---

### 🎯 Advantages

- 🌳 Reduces overfitting
- 🎯 Improves prediction accuracy
- 🔁 Robust against noise

---

### 🧠 Why It Works

Each tree:

- sees **different data samples**
- makes **slightly different errors**

Averaging reduces overall error.

---

### 🧠 Mini Recap

Random Forest:

- ensemble of decision trees
- reduces overfitting
- improves generalization

---

# 📐 4. Support Vector Machine (SVM)

A **Support Vector Machine (SVM)** is a supervised algorithm used for **classification and regression**.

It finds the **optimal hyperplane** separating different classes.

---

## 📊 Concept

Example classification:

```text
Class A ● ● ●
Class B ○ ○ ○
```

SVM finds a boundary:

```text
● ● ● | ○ ○ ○
      ↑
   Optimal Hyperplane
```

---

### 🎯 Key Idea

Maximize the **margin** between classes.

```text
Margin = distance between closest points and boundary
```

Those closest points are called:

```text
Support Vectors
```

---

### ⚡ Advantages

- Works well with **high-dimensional data**
- Effective when **features > samples**

---

### 🧠 Mini Recap

SVM:

- finds **optimal separation boundary**
- uses **support vectors**
- works well in **high-dimensional spaces**

---

# 📊 5. Bayesian Classifier

The **Bayesian classifier** is based on **probability theory**.

It uses **Bayes' Theorem** to estimate class probabilities.

---

## 📐 Bayes Theorem

```text
P(A|B) = (P(B|A) × P(A)) / P(B)
```

| Symbol | Meaning           |                          |
| ------ | ----------------- | ------------------------ |
| P(A    | B)                | Probability of A given B |
| P(B    | A)                | Likelihood               |
| P(A)   | Prior probability |                          |
| P(B)   | Evidence          |                          |

---

### 💡 Naive Bayes Assumption

All features are **conditionally independent**.

Although unrealistic, it works **surprisingly well in practice**.

---

### 📊 Applications

- 📧 Spam detection
- 📰 Text classification
- 📚 Document categorization

---

### 🧠 Mini Recap

Bayesian classifiers:

- probabilistic models
- assume **feature independence**

---

# 📍 6. K-Nearest Neighbors (KNN)

KNN is a **simple supervised learning algorithm**.

It classifies a new data point based on **its nearest neighbors**.

---

## 🧩 Concept

```text
New Point ?
Nearby Points → Class A
Nearby Points → Class B
```

The majority class among neighbors determines the prediction.

---

## 📏 Distance Metrics

### Euclidean Distance

```text
D(X,Y) = √((x1 - x2)² + (y1 - y2)²)
```

---

### Manhattan Distance

```text
D(X,Y) = |x1 - x2| + |y1 - y2|
```

---

### Cosine Distance

Measures **angle similarity between vectors**.

---

### Jaccard Distance

```text
1 - |X ∩ Y| / |X ∪ Y|
```

Used for **set similarity**.

---

### 🧠 Mini Recap

KNN:

- instance-based learning
- classification via **neighbor similarity**

---

# 🔵 7. K-Means Clustering

K-Means is an **unsupervised clustering algorithm**.

It groups data into **K clusters** based on similarity.

---

## ⚙️ Algorithm Steps

1️⃣ Randomly choose **K cluster centers**

2️⃣ Assign each data point to the **nearest cluster**

3️⃣ Recalculate cluster centers

4️⃣ Repeat until centers stop changing

---

## 📊 Example Points

| Point | Coordinates |
| ----- | ----------- |
| A     | (0,0)       |
| B     | (1,1)       |
| C     | (2,1)       |
| D     | (1,3)       |
| E     | (2,4)       |
| F     | (3,3)       |

Clusters gradually stabilize as centers update.

---

### ⚠️ Limitations

- Must **predefine K**
- Sensitive to **initial cluster centers**

---

### 🧠 Mini Recap

K-Means:

- partitions data into K groups
- iterative centroid updates

---

# 🌌 8. DBSCAN Clustering

DBSCAN is a **density-based clustering algorithm**.

Unlike K-Means, it does **not require predefined clusters**.

---

## ⚙️ Concept

Cluster formation:

```text
Dense Region → Cluster
Sparse Region → Noise / Outlier
```

---

### 🎯 Advantages

- finds **clusters of arbitrary shapes**
- identifies **outliers automatically**

---

### 🧠 Mini Recap

DBSCAN:

- density-based clustering
- detects **noise and anomalies**

---

# 🧬 9. Hierarchical Clustering

Hierarchical clustering builds **nested clusters**.

Two main approaches:

| Method        | Description            |
| ------------- | ---------------------- |
| Agglomerative | Merge smaller clusters |
| Divisive      | Split larger clusters  |

---

## Agglomerative Steps

1️⃣ Treat each point as a cluster

2️⃣ Find **closest clusters**

3️⃣ Merge them

4️⃣ Repeat until desired cluster number

---

### 📊 Output

Clusters form a **tree structure** called a **dendrogram**.

---

### 🧠 Mini Recap

Hierarchical clustering:

- builds **cluster hierarchies**
- visualized with **dendrograms**

---

# 🛒 10. Association Rule Learning

Association rules discover **relationships between items in datasets**.

Often used in **market basket analysis**.

---

## 🛍 Example

```text
Customers who buy:
Bread → also buy Butter
```

Rule:

```text
Bread → Butter
```

---

## Key Metrics

### 📊 Support

Probability that **A and B occur together**.

```text
Support(A,B)
```

---

### 🎯 Confidence

Probability that **B occurs given A**.

```text
Confidence = P(B|A)
```

---

### 🚀 Lift

Measures improvement over random chance.

```text
Lift > 1 → strong association
```

---

### 🧠 Mini Recap

Association rules:

- identify **frequent item combinations**
- measure relationships with **support, confidence, lift**

---

# ⚙️ 11. Apriori Algorithm

The **Apriori algorithm** efficiently finds **frequent itemsets**.

---

## 🔑 Core Principle

```text
If an itemset is frequent
→ all of its subsets must also be frequent
```

---

## Algorithm Flow

```text
Start with small itemsets
        ↓
Remove infrequent sets
        ↓
Generate larger candidates
        ↓
Repeat until no new sets
```

---

### 🎯 Benefit

Greatly reduces **computational complexity**.

---

### 🧠 Mini Recap

Apriori:

- finds frequent item combinations
- eliminates impossible candidates early

---

# 🌃 Final Machine Learning Algorithm Map

```text
Machine Learning Algorithms

Supervised
├─ Regression
├─ Decision Tree
├─ Random Forest
├─ Support Vector Machine
├─ Bayesian Classifier
└─ K-Nearest Neighbors

Unsupervised
├─ K-Means
├─ DBSCAN
├─ Hierarchical Clustering
└─ Association Rule Learning
     └─ Apriori Algorithm
```

---

# 🌠 Memory Anchor

```text
Regression → Predict numbers
Decision Tree → Rule-based classification
Random Forest → Many trees together
SVM → Optimal separating hyperplane
KNN → Neighbor similarity
K-Means → Cluster by centroids
DBSCAN → Density clusters
Apriori → Market basket patterns
```
