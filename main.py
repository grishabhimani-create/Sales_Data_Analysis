import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self, file_path=None):
        self.data = None
        self.last_fig = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        plt.close("all")

    def load_data(self, file_path):
        try:
            if not os.path.exists(file_path):
                print(f"Error: File '{file_path}' does not exist.")
                return False
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return False

    def explore_data(self):
        if self.data is None:
            print("No data loaded.")
            return
        print("\n1. First 5 rows\n2. Last 5 rows\n3. Columns\n4. Data types")
        choice = input("Choice: ")
        if choice == "1":
            print(self.data.head())
        elif choice == "2":
            print(self.data.tail())
        elif choice == "3":
            print(self.data.columns.tolist())
        elif choice == "4":
            print(self.data.dtypes)

    def clean_data(self):
        if self.data is None:
            print("No data loaded.")
            return
        print(
            "\n1. Show missing\n2. Fill with mean\n3. Drop missing\n4. Replace with value"
        )
        choice = input("Choice: ")
        if choice == "1":
            print(self.data[self.data.isnull().any(axis=1)])
        elif choice == "2":
            num_cols = self.data.select_dtypes(include=[np.number]).columns
            self.data[num_cols] = self.data[num_cols].fillna(
                self.data[num_cols].mean()
            )
            print("Filled missing values with mean.")
        elif choice == "3":
            self.data.dropna(inplace=True)
            print("Dropped missing values.")

    def visualize_data(self):
        if self.data is None:
            print("No data loaded.")
            return
        print("\n1. Bar\n2. Line\n3. Scatter\n4. Pie\n5. Histogram")
        choice = input("Choice: ")
        fig, ax = plt.subplots()

        if choice == "3":
            x_col = input("X axis column (e.g. Sales): ")
            y_col = input("Y axis column (e.g. Year): ")
            ax.scatter(self.data[x_col], self.data[y_col])
            ax.set_title("Scatter Plot")
            self.last_fig = fig
            plt.show()

    def save_visualization(self):
        if self.last_fig is None:
            print("No figure to save.")
            return
        filename = input("Enter file name (e.g., scatter_plot.png): ")
        self.last_fig.savefig(filename)
        print(f"Saved as {filename}!")


def main():
    analyzer = SalesDataAnalyzer()
    while True:
        print(
            "\n========== Main Menu ==========\n1. Load Dataset\n2. Explore Data\n3. Handle Missing Data\n4. Data Visualization\n5. Save Visualization\n6. Exit"
        )
        choice = input("Enter choice: ")

        if choice == "1":
            path = input("Enter CSV path (e.g., sales_data.csv): ")
            analyzer.load_data(path)
        elif choice == "2":
            analyzer.explore_data()
        elif choice == "3":
            analyzer.clean_data()
        elif choice == "4":
            analyzer.visualize_data()
        elif choice == "5":
            analyzer.save_visualization()
        elif choice == "6":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()