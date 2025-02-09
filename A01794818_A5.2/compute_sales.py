"""
Module to compute the total cost of sales given a price catalogue and
a sales record.
"""
import json
import os
import time
import sys


class ComputeSales:
    """
    Class to compute the total cost of sales given a price catalogue
    and a sales record.
    """
    def __init__(self, price_file: json, sales_file: json) -> None:
        self.price_file = price_file
        self.sales_file = sales_file
        self.products = {}
        self.sales = []
        self.total_cost = 0.0

    def load_data(self) -> None:
        """
        Load the price catalogue and sales record from the JSON files.
        """
        try:
            with open(self.price_file, 'r', encoding='utf-8') as f:
                self.products = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading the file {self.price_file}: {e}")

        try:
            with open(self.sales_file, 'r', encoding='utf-8') as f:
                self.sales = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading the file {self.sales_file}: {e}")

    def compute_total_cost(self) -> None:
        """
        Compute the total cost of sales.
        """
        for sale in self.sales:
            product_name_sale = sale.get("Product")
            product_quantity_sale = sale.get("Quantity", 0)
            for product in self.products:
                product_name = product.get("title")
                product_price = product.get("price")
                if (product_name_sale == product_name and
                        isinstance(product_quantity_sale, (int, float))):
                    self.total_cost += product_price * product_quantity_sale

    def save_results(self, filename: str, execution_time: float) -> None:
        """
        Save and print the results of the computation.

        Args:
            filename (str): Filename path to save the results.
            execution_time (float): _description_
        """
        if filename:
            # create the directory if it does not exist
            directory = os.path.dirname(filename)
            os.makedirs(directory, exist_ok=True)
        total_sales = f"Total sales: ${self.total_cost:.2f}"
        execution_time = f"Execution time: {execution_time:.6f}s."
        result_text = f"{total_sales}\n{execution_time}\n"
        print(result_text)
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result_text)
        except FileNotFoundError as e:
            print(f"Error writing the file {filename}: {e}")


def main():
    """
    Main function to compute the total cost of sales.
    """
    if len(sys.argv) != 3:  # Check the number of arguments
        print("Error: Invalid quantity of arguments. Please check.")
    else:
        start_time = time.time()
        compute_sales = ComputeSales(sys.argv[1], sys.argv[2])
        file_ = sys.argv[2]
        txt_filename = file_.split('/')[-1].split('.')[0]
        compute_sales.load_data()
        compute_sales.compute_total_cost()
        execution_time = time.time() - start_time
        compute_sales.save_results(f"results/{txt_filename}/SalesResults.txt",
                                   execution_time)


if __name__ == "__main__":
    main()
