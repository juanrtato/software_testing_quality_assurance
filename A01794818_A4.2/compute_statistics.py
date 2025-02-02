"""
This module computes several statistics from a list of numbers.
"""
import math
import os
import sys
import time
from typing import Counter

# pylint: disable=trailing-whitespace
class ComputeStatistics:
    """
    Class to compute the statistics of a file containing a list of numbers.
    """
    def __init__(self, file):
        self.data = file

    def read_data(self) -> list:
        """
        Read the numbers from the file and return the list of numbers.

        Returns:
            list: List of numbers.
        """
        numbers = []
        with open(self.data, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                line = line.replace(',', '.') # Replace comma with dot
                line = line.replace(';', '.') # Replace semicolon with dot
                try:
                    numbers.append(float(line))
                except ValueError:
                    # Remove non-numeric characters
                    print(f"Invalid value: '{line}'. Trying to extract number...")
                    cleaned_number = ''.join(filter(str.isdigit, line)) 
                    # Check if the line contains a number
                    if cleaned_number != '': 
                        print(f"Extracted number of '{line}': {cleaned_number}")
                        numbers.append(float(cleaned_number))
                    else:
                        print(f"Invalid value: '{line}'. Skipping...")
        return numbers
    
    def compute_mean(self, numbers: list) -> float:
        """
        Compute the mean of the numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            float: Mean of the numbers.
        """
        if len(numbers) == 0:
            return 0.0
        return sum(numbers) / len(numbers)
    
    def compute_median(self, numbers: list) -> float:
        """
        Compute the median of the numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            float: Median of the numbers.
        """
        if len(numbers) == 0:
            return 0.0
        numbers.sort()
        n = len(numbers)
        mid = n // 2
        if n % 2 == 0:
            return (numbers[mid - 1] + numbers[mid]) / 2
        return numbers[mid]
    
    def compute_mode(self, numbers: list) -> float | None:
        """
        Compute the mode of the numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            float: Mode of the numbers.
        """
        if len(numbers) == 0:
            return 0.0
        freq = Counter(numbers)
        max_freq = max(freq.values())
        mode = [num for num, count in freq.items() if count == max_freq]
        if len(mode) > 1:
            return mode[-1]
        return None
    
    def compute_variance(self, numbers: list) -> float:
        """
        Compute the variance of the numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            float: Variance of the numbers.
        """
        if len(numbers) == 0:
            return 0.0
        mean = self.compute_mean(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return variance
    
    def compute_standard_deviation(self, variance: float) -> float:
        """
        Compute the standard deviation from the variance.

        Args:
            variance (float): Variance of the numbers.

        Returns:
            float: Standard deviation of the numbers.
        """
        return math.sqrt(variance)
    
    def save_stats(self, filename: str, stats: dict, execution_time: float):
        """
        Save the statistics to a file.

        Args:
            stats (dict): Dictionary containing the statistics.
        """
        if filename:
            # create the directory if it does not exist
            directory = os.path.dirname(filename)
            os.makedirs(directory, exist_ok=True)
            
        with open(filename, 'w', encoding='utf-8') as f:
            for stat, value in stats.items():
                f.write(f"{stat}: {value}\n")
            f.write(f"Execution time: {execution_time}s.")

    
def main():
    """
    Main function to compute the statistics.
    """
    start_time = time.time()
    file_ = sys.argv[1]
    txt_filename = file_.split('/')[-1].split('.')[0]
    compute_statistics = ComputeStatistics(file_)
    numbers = compute_statistics.read_data()
    stats = {
        'count': len(numbers),
        'mean': compute_statistics.compute_mean(numbers),
        'median': compute_statistics.compute_median(numbers),
        'mode': compute_statistics.compute_mode(numbers),
        'variance': compute_statistics.compute_variance(numbers),
        'standard_deviation': compute_statistics.compute_standard_deviation(
            compute_statistics.compute_variance(numbers)
        )
    }
    execution_time = time.time() - start_time

    for stat, value in stats.items():
        print(f"{stat}: {value}")
    print(f"Excecution time: {execution_time}s.")
    
    compute_statistics.save_stats(
        f"results/P1/{txt_filename}/StatisticsResults.txt", 
        stats, 
        execution_time
    )

if __name__ == "__main__":
    main()
