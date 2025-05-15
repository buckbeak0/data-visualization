# 📊 Data Visualization with Matplotlib

Welcome to the **Data Visualization with Matplotlib** project! This repository provides practical implementations and examples of how to use [Matplotlib](https://www.geeksforgeeks.org/python-introduction-matplotlib/) for creating powerful and insightful data visualizations in Python.

## 📦 What’s Inside

- 📁 `src/` – Contains Python scripts for various types of visualizations using `matplotlib.pyplot`
- 📁 `Datasets/` – Includes CSV datasets used in examples (e.g., the Tips dataset)
- 📄 `README.md` – You’re readin’ it right now!

---

## 🔧 Installation

First, make sure you have Python and pip installed. Then run:

```bash
pip install matplotlib pandas
```

If you’re using Jupyter Notebook, install via:

```bash
!pip install matplotlib pandas
```

---

## 📈 Visualizations Included

### 1. Line Chart

Used to display relationships between two variables across a continuous scale.

```python
plt.plot(x, y)
```

> Example: Plotting X vs Y with labels and title.

---

### 2. Bar Chart

Used for comparing different categories with rectangular bars.

```python
plt.bar(df['day'], df['total_bill'])
```

> Example: Comparing total bills per day using the `tip.csv` dataset.

---

### 3. Histogram

Shows frequency distribution of numerical data.

```python
plt.hist(df['total_bill'])
```

> Example: Frequency of total bill amounts in the Tips dataset.

---

### 4. Scatter Plot

Used to examine relationships between two continuous variables.

```python
plt.scatter(x, y)
```

> Example: Visualizing relationships in dataset columns.

---

## 📂 Dataset

The dataset used (`tip.csv`) can be found in the `Datasets/` folder. It includes:

- `total_bill`
- `tip`
- `sex`
- `smoker`
- `day`
- `time`
- `size`

---

## 📚 References

- [Matplotlib – GeeksforGeeks](https://www.geeksforgeeks.org/python-introduction-matplotlib/)
- [NumPy – GeeksforGeeks](https://www.geeksforgeeks.org/numpy-tutorial/)
- [Pyplot Module](https://www.geeksforgeeks.org/pyplot-in-matplotlib/)

---

## 🧙 Final Words from Hagrid

Don’t be afraid to play around with colors, labels, and styles — data viz is part science, part magic! Add legends, customize tick marks, and make it all shine like a freshly polished hippogriff saddle.

Happy plotting!
