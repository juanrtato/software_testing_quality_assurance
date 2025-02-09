# Instructions to Execute and Replicate the Exercises

## Requirements
Before running the exercises, make sure you have Python 3 installed. You can install the required dependencies using:

```sh
pip install -r requirements.txt
```

### Problem 1: Compute Statistics
To execute the script for computing statistics on test cases from Problem 1, run the following command:

```sh
python3 compute_statistics.py data/P1/TCX.txt
```
Replace TCX.txt with the desired test case file from the data/P1 directory.

Example:
```sh
python3 compute_statistics.py data/P1/TC5.txt
```
Results will be saved in:
```sh
results/P1/TCX/StatisticsResults.txt
```

### Problem 2: Convert Numbers
To execute the script for number conversion on test cases from Problem 2, run:

```sh
python3 convert_numbers.py data/P2/TCX.txt
```
Replace TCX.txt with the desired test case file from the data/P2 directory.

Example:
```sh
python3 convert_numbers.py data/P2/TC3.txt
```
Results will be saved in:
```sh
results/P2/TCX/ConvertionResults.txt
```

### Problem 3: Word Count
To execute the script for word count on test cases from Problem 3, run:

```sh
python3 word_count.py data/P3/TCX.txt
```
Replace TCX.txt with the desired test case file from the data/P3 directory.

Example:
```sh
python3 word_count.py data/P3/TC5.txt
```
Results will be saved in:
```sh
results/P3/TCX/WordCountResults.txt
```


# Directory organization
```sh
├── compute_statistics.py
├── convert_numbers.py
├── word_count.py
├── data 
│   ├── P1
│   │   ├── A4.2.P1.Results-errata.txt
│   │   ├── TC1.txt
│   │   ├── TC2.txt
│   │   ├── TC3.txt
│   │   ├── TC4.txt
│   │   ├── TC5.txt
│   │   ├── TC6.txt
│   │   └── TC7.txt
│   ├── P2
│   │   ├── A4.2.P2.Results.txt
│   │   ├── TC1.txt
│   │   ├── TC2.txt
│   │   ├── TC3.txt
│   │   └── TC4.txt
│   └── P3
│       ├── TC1.Results.txt
│       ├── TC1.txt
│       ├── TC2.Results.txt
│       ├── TC2.txt
│       ├── TC3.Results.txt
│       ├── TC3.txt
│       ├── TC4.Results.txt
│       ├── TC4.txt
│       ├── TC5.Results.txt
│       └── TC5.txt
├── excecutions_evidence
│   ├── P1
│   │   ├── pylint.png
│   │   └── tests.png
│   ├── P2
│   │   ├── pylint.png
│   │   ├── tc1.png
│   │   ├── tc2.png
│   │   ├── tc3.png
│   │   └── tc4.png
│   └── P3
│       ├── pylint.png
│       ├── tc1.png
│       ├── tc2.png
│       ├── tc3.png
│       └── tc4.png
├── instructions
│   └── Actividad 4.2_Ejercicios.pdf
├── requirements.txt
├── results
│   ├── P1
│   │   ├── TC1
│   │   │   └── StatisticsResults.txt
│   │   ├── TC2
│   │   │   └── StatisticsResults.txt
│   │   ├── TC3
│   │   │   └── StatisticsResults.txt
│   │   ├── TC4
│   │   │   └── StatisticsResults.txt
│   │   ├── TC5
│   │   │   └── StatisticsResults.txt
│   │   ├── TC6
│   │   │   └── StatisticsResults.txt
│   │   └── TC7
│   │       └── StatisticsResults.txt
│   ├── P2
│   │   ├── TC1
│   │   │   └── ConvertionResults.txt
│   │   ├── TC2
│   │   │   └── ConvertionResults.txt
│   │   ├── TC3
│   │   │   └── ConvertionResults.txt
│   │   └── TC4
│   │       └── ConvertionResults.txt
│   └── P3
│       ├── TC1
│       │   └── WordCountResults.txt
│       ├── TC2
│       │   └── WordCountResults.txt
│       ├── TC3
│       │   └── WordCountResults.txt
│       ├── TC4
│       │   └── WordCountResults.txt
│       └── TC5
│           └── WordCountResults.txt
└── word_count.py
```
