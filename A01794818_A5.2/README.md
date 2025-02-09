# Activity 5.2
# Instructions to Execute and Replicate the Exercises

## Requirements
Before running the exercises, make sure you have Python 3 installed. You can install the required dependencies using:

```sh
pip install -r requirements.txt
```

### TC1
To execute the script for computing statistics on test cases TC1, run:

```sh
python3 compute_sales.py data/ProductList.json data/TC1/TC1.Sales.json 
```

Results will be saved in:
```sh
results/TC1/SalesResults.txt
```

### TC2
To execute the script for number conversion on test cases TC2, run:

```sh
python3 compute_sales.py data/ProductList.json data/TC2/TC2.Sales.json 
```

Results will be saved in:
```sh
results/TC2/SalesResults.txt
```

### TC3
To execute the script for word count on test cases TC3, run:

```sh
python3 compute_sales.py data/ProductList.json data/TC3/TC3.Sales.json 
```

Results will be saved in:
```sh
results/TC3/SalesResults.txt
```

# Evidence
Evidence of executions and pylint/flake8 tests was saved in:
```sh
/evidence/pylint_flake8/
```
Evidence of compute sales execution was saved in:
```sh
/evidence/test_cases/
```

# Directory organization

```sh
├── compute_sales.py
├── data # input data provided by the teacher
│   ├── ProductList.csv
│   ├── ProductList.json
│   ├── Results.txt
│   ├── TC1
│   │   ├── TC1.ProductList.json
│   │   └── TC1.Sales.json
│   ├── TC2
│   │   └── TC2.Sales.json
│   └── TC3
│       └── TC3.Sales.json
├── evidence
│   ├── pylint_flake8
│   └── test_cases
├── instructions
│   └── Actividad 5.2_Ejercicios.pdf
├── README.md
├── requirements.txt
└── results
    ├── TC1
    │   └── SalesResults.txt
    ├── TC2
    │   └── SalesResults.txt
    └── TC3
        └── SalesResults.txt

```
