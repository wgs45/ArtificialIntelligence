# 🤖 Chapter 3 — Machine Learning

---

# 🌌 1. The Relationship Between Keras and TensorFlow

Modern machine learning frameworks often work **in layered architectures**.

### 🧠 Core Idea

**Keras** is a **high-level deep learning API** that runs on top of **TensorFlow**.

---

## ⚙️ Architecture Overview

```txt
Keras (High-level API)
        ↓
TensorFlow (Deep Learning Engine)
        ↓
Hardware Acceleration
CPU | GPU | TPU
```

---

### 🔧 Roles of Each Layer

| Layer       | Role                                          |
| ----------- | --------------------------------------------- |
| Keras       | Simple interface for building neural networks |
| TensorFlow  | Handles computation graphs and optimization   |
| CPU/GPU/TPU | Performs the heavy mathematical operations    |

---

### 💡 Why This Design Exists

- 🧑‍💻 **Keras simplifies model building**
- ⚡ **TensorFlow performs efficient computation**
- 🖥 Hardware accelerates training

---

### 🧠 Mini Recap

- **Keras = user-friendly API**
- **TensorFlow = computation engine**
- **Hardware = acceleration layer**

---

# 🧠 2. Introduction to Machine Learning

Machine learning is a method that allows computers to **learn patterns directly from data**.

---

## 📚 Definition

Machine learning is:

> A data analysis technique that enables computers to **learn from experience without explicit programming**.

---

### 👶 Human Learning Analogy

Children learn to recognize cats by:

- seeing many examples
- identifying patterns

Computers do the same.

---

### 🐱 Example: Cat Recognition

**Traditional Programming**

```txt
if (ears == triangular AND whiskers == true AND tail == long)
    then cat
```

⚠️ Problem:

- Impossible to list **every possible cat feature**.

---

**Machine Learning Approach**

```txt
Provide many images of cats
↓
Model learns patterns automatically
↓
Predict if new image contains a cat
```

---

### 🧠 Mini Recap

Machine learning:

- learns **patterns from data**
- avoids **hand-coded rules**
- improves with **experience**

---

# 🧩 3. Machine Learning Classification

Machine learning methods fall into several categories.

---

## 📊 Main Types

| Type                     | Description                               |
| ------------------------ | ----------------------------------------- |
| Supervised Learning      | Uses labeled data                         |
| Unsupervised Learning    | Finds patterns without labels             |
| Semi-supervised Learning | Uses few labeled + many unlabeled samples |
| Reinforcement Learning   | Learns by interacting with environment    |

---

### Visual Overview

```txt
Machine Learning
├── Supervised Learning
│   ├── Regression
│   ├── Classification
│   ├── Decision Tree
│   ├── Random Forest
│   └── Support Vector Machine
│
├── Unsupervised Learning
│   ├── Clustering
│   │   ├── K-Means
│   │   ├── DBSCAN
│   │   └── Hierarchical Clustering
│   ├── Bayes Classifier
│   └── K-Nearest Neighbor
│
├── Semi-Supervised Learning
│
└── Reinforcement Learning
    └── Q-learning
```

---

### 🧠 Mini Recap

Machine learning algorithms fall into **four major learning paradigms**.

---

# 🧑‍🏫 4. Supervised Learning

Supervised learning uses **labeled data**.

---

## 🏷 What is a Label?

A label is the **correct answer** attached to training data.

Example dataset:

| Email               | Label    |
| ------------------- | -------- |
| "Win a free prize!" | Spam     |
| "Meeting tomorrow"  | Not Spam |

---

## 📈 Learning Process

```txt
Training Data (with labels)
        ↓
Model learns relationship
        ↓
Prediction for new data
```

---

### 📊 Applications

- 📧 Spam detection
- 🚗 Predicting car sales from advertising budgets
- 🩺 Medical diagnosis
- 🖼 Image classification

---

### 🧠 Mini Recap

Supervised learning:

- requires **labeled datasets**
- predicts **categories or numerical values**

---

# 🔍 5. Unsupervised Learning

Unsupervised learning works **without labels**.

The algorithm must **discover patterns by itself**.

---

## 📊 Main Tasks

| Task              | Description                          |
| ----------------- | ------------------------------------ |
| Clustering        | Group similar items                  |
| Association Rules | Find relationships between variables |
| Anomaly Detection | Identify unusual data                |

---

## 🧩 Clustering Example

Original Data

```txt
Machine 1
Machine 2
Machine 3
Machine A
Machine B
Machine C
```

Possible clustering strategies:

- 🔤 First letter grouping
- 🎨 Color grouping
- 🔢 Serial number grouping

The algorithm automatically decides **which grouping makes sense**.

---

### 🧠 Mini Recap

Unsupervised learning:

- requires **no labels**
- discovers **hidden structure in data**

---

# 🧬 6. Semi-Supervised Learning

Semi-supervised learning combines:

```txt
Small labeled dataset
+
Large unlabeled dataset
```

---

## ⚠️ Why It Exists

Labeling data manually is **expensive and slow**.

Examples:

- medical images
- satellite imagery
- speech datasets

---

### 💡 Solution

Use:

- a **small labeled dataset**
- many **unlabeled samples**

The model improves by leveraging **both sources**.

---

### 🧠 Mini Recap

Semi-supervised learning:

- reduces labeling cost
- improves accuracy using unlabeled data

---

# 🎮 7. Reinforcement Learning

Reinforcement learning trains agents through **trial and error**.

---

## 🎯 Learning Process

```txt
Agent interacts with environment
        ↓
Performs action
        ↓
Receives reward or penalty
        ↓
Learns optimal strategy
```

---

### Famous Example

**AlphaGo** by **DeepMind**

- trained using millions of Go games
- played against itself
- defeated **Lee Sedol** in **2016**

---

### 🧠 Mini Recap

Reinforcement learning:

- learns through **rewards**
- improves by **interacting with environment**

---

# 🧭 8. Q-Learning Example — Maze Navigation

Imagine an agent (like Mario) exploring a maze.

He does **not know the map initially**.

---

## 🧩 Components

| Element | Meaning              |
| ------- | -------------------- |
| State   | Current position     |
| Action  | Move direction       |
| Reward  | Score received       |
| Policy  | Best action strategy |

---

## 🧮 Reward Matrix R

Rewards define the **benefit of moving between states**.

Example:

- `100` → goal reached
- `0` → neutral step
- `-1` → invalid or bad move

---

# ⚙️ Q-Learning Formula

The update rule is:

```txt
Q(state, action) =
R(state, action) +
γ * max[Q(next_state, all_actions)]
```

Where:

| Symbol | Meaning                |
| ------ | ---------------------- |
| R      | reward                 |
| γ      | discount factor        |
| Q      | expected future reward |

---

### Initial Q Matrix

At the start:

```txt
Q =
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

The agent **knows nothing yet**.

---

# 📊 Example Calculations

## Step 1

```
Q(2,6) = R(2,6) + 0.8 * max[Q(6,2), Q(6,5), Q(6,6)]
```

```
= 100 + 0.8 * 0
= 100
```

Updated matrix:

```
Q =
0 0 0 0 0
0 0 0 0 100
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

---

## Step 2

```
Q(4,2) = R(4,2) + 0.8 * max[Q(2,4), Q(2,6)]
```

```
= 0 + 0.8 * 100
= 80
```

Updated matrix:

```
Q =
0 0 0 0 0
0 0 0 0 100
0 0 0 0 0
0 80 0 0 0
0 0 0 0 0
```

---

Eventually the matrix converges into:

```
Q =
0   0   0   400   0
0   0   320 0     500
0   0   320 0     0
400 256 0   400   0
320 0   320 0     500
400 0   0   400   500
```

---

### 🎯 Meaning

Higher Q-values represent **better actions**.

The agent eventually learns the **optimal path to the exit**.

---

### 🧠 Mini Recap

Q-learning:

- learns **optimal policies**
- updates rewards iteratively
- balances **current reward + future reward**

---

# 🌃 Final Neon Summary

### Machine Learning Landscape

| Paradigm        | Key Idea                    |
| --------------- | --------------------------- |
| Supervised      | learn from labeled data     |
| Unsupervised    | discover hidden patterns    |
| Semi-supervised | combine labeled + unlabeled |
| Reinforcement   | learn via rewards           |

---

### Reinforcement Learning Core

```txt
Action → Reward → Update Q-value → Improve Policy
```

---

# 🌠 Memory Anchor

```txt
Supervised      → Labels
Unsupervised    → Patterns
Semi-supervised → Few labels + many data
Reinforcement   → Trial and reward
```
