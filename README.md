# Mean-Variance-Standard Deviation Calculator

This is the complete submitted code of my Mean-Variance-Standard Deviation Calculator project for completion of the "Data Analysis with Python" certification. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator


This Python project is a calculator that uses NumPy to compute the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Gnanadeep-Settykara/MVSD-Calculator.git
    cd MVSD-Calculator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The main functionality is implemented in the `mean_var_std.py` file. To use the calculator, you can call the `calculate` function with a list containing 9 digits. For example:

```python
from mean_var_std import calculate

data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(data)

print(result)

