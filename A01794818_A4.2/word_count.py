"""
This module count the number of words in a text file.
"""
import os
import sys
import time

# pylint: disable=trailing-whitespace
class CountWords:
    """
    Class to count frequency of words of a file containing a list of words.
    """
    def __init__(self, filepath):
        self.data = filepath
    
    def read_data_and_count_words(self) -> dict:
        """
        Count the number of words in the file.
        Save the word count in a dictionary.

        Returns:
            list: _description_
        """
        word_count = {}
        try:
            with open(self.data, 'r', encoding='utf-8') as f:
                for line in f:
                    words = line.split()
                    for word in words:
                        word = word.lower() 
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
        except FileNotFoundError:
            print(f"Error: File {self.data} not found.")
        
        return word_count
        
    def save_results(self, word_count: dict, output_file: str, execution_time) -> None:
        """
        Save the word count to a file.

        Args:
            word_count (dict): Dictionary with the word count.
            output_file (str): Output file path.
        """
        try:
            directory = os.path.dirname(output_file)
            os.makedirs(directory, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as results_file:
                for word, count in word_count.items():
                    results_file.write(f"{word}: {count}\n")
                    print(f"{word}: {count}")
                results_file.write(f"Execution time: {execution_time}s.")
        except OSError as e:
            print(f"Error saving the converted numbers to {output_file}: {e}")
    
def main():
    """
    Main function to count the words.
    """
    start_time = time.time()
    
    file_ = sys.argv[1]
    txt_filename = file_.split('/')[-1].split('.')[0]
    word_count = CountWords(file_)
    words_with_freq = word_count.read_data_and_count_words()
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time}s.")
    word_count.save_results(
        words_with_freq, 
        f"results/P3/{txt_filename}/WordCountResults.txt", 
        execution_time
    )

if __name__ == "__main__":
    main()
