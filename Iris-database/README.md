# Iris-database

## How to Run

```shell
python main.py
```

**Expected output:**
```shell
name of flowers in the Iris dataset:
['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
```

---

## Folder Structure

```
Iris-database/
├── main.py
└── utils/
    ├── __init__.py
    └── iris_utils.py
```

> **Note:**  
> An empty `__init__.py` file is needed to tell Python that a directory should be treated as a package.  
> Without `__init__.py`, Python may not recognize the folder as a package, especially in older Python versions or some tools.  
> Even though it's optional in Python 3.3+, it's still good practice for compatibility and clarity.