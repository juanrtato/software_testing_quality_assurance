"""
This module converts a list of numbers to binary and hexadecimal.
"""
import os
import sys
import time


# pylint: disable=trailing-whitespace
class ConvertNumbers:
    """
    Class to compute the statistics of a file containing a list of numbers.
    """
    def __init__(self, filepath):
        self.data = filepath
    
    def read_data(self) -> list:
        """
        Read the numbers from the file and return the list of numbers.

        Returns:
            list: List of numbers.
        """
        numbers = []
        try:
            with open(self.data, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"Invalid value: '{line}'. Skipping...")

        except FileNotFoundError:
            print(f"Error: File {self.data} not found.")
            return None
        return numbers
    
    def number_to_binary(self, number: int, bits: int = 10) -> str | None:
        """
        Convierte un número a su representación binaria usando complemento a dos si es negativo.

        Args:
            number (int): Número a convertir.
            bits (int): Número de bits para la representación binaria.

        Returns:
            str | None: Representación binaria en complemento a dos o None si hay error.
        """
        binary = None
        if not isinstance(number, int):
            raise ValueError("Number must be an integer.")

        if number >= 0:
            binary = format(number, f'{bits}b')  # Binary representation
        else:
            binary = format((1 << bits) + number, f'0{bits}b')  # Complement to two

        return binary


    def number_to_hexadecimal(self, number: int) -> str | None:
        """
        Convert a number to hexadecimal.

        Args:
            number (int): Number.

        Returns:
            str | None: Hexadecimal number or None if the conversion fails.
        """
        
        hex_value = None

        if number >= 0:
            hex_value = hex(number)[2:].upper()  # Direct conversion to hexadecimal
        else:
            hex_value = format(number & 0xFFFFFFFF, '08X')  # Complement to two

        return hex_value

    
    def save_converted_numbers(
            self, 
            filename: str, 
            converted_numbers: 
            dict, 
            execution_time: float) -> None:
        """
        Save the converted numbers to a file.

        Args:
            filename (str): Filename.
            converted_numbers (dict): Dictionary with the numbers converted to 
            binary and hexadecimal.
            execution_time (float): Execution time.
        """
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("ITEM\tNUM\tBIN\tHEX\n")
                for idx, (number, conversions) in enumerate(converted_numbers.items(), start=1):
                    f.write(f"{idx}\t{number}\t{conversions['bin']}\t{conversions['hex']}\n")
                f.write(f"\nExecution time: {execution_time}s.")
        except OSError as e:
            print(f"Error saving the converted numbers to {filename}: {e}")


def main():
    """
    Main function to compute the convert the numbers.
    """
    start_time = time.time()
    file_ = sys.argv[1]
    txt_filename = file_.split('/')[-1].split('.')[0]
    convert_numbers = ConvertNumbers(file_)
    numbers = convert_numbers.read_data()
    converted_numbers = {}
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print(f"Invalid number: {number}. Skipping...")
            continue
        binary = convert_numbers.number_to_binary(number)
        hexadecimal = convert_numbers.number_to_hexadecimal(number)
        converted_numbers[number] = {
            'bin': binary,
            'hex': hexadecimal
        }
        print(f"Number: {number} -> Binary: {binary} -> Hexadecimal: {hexadecimal}")
    
    execution_time = time.time() - start_time
    convert_numbers.save_converted_numbers(
        f"results/P2/{txt_filename}/ConvertionResults.txt", 
        converted_numbers, 
        execution_time
    )

if __name__ == "__main__":
    main()
