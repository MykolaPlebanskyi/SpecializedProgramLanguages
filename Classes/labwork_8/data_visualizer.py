import os

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from Shared.Save.file_save import FileSaver


class DataVisualizer:
    """
    A class for visualizing data.

    Attributes:
    - data: A pandas DataFrame containing the data to be visualized.
    - columns: A list of column names in the DataFrame.
    - file_save: An instance of the FileSaver class for saving files.

    Methods:
    - explore_data(): Display minimum and maximum values in the DataFrame.
    - save_plots(data, name_file): Save plots as PNG files.
    - visualize_data(user_choice): Visualize data based on user input.
    - scatter_plot(): Create and save a scatter plot of ID and Income.
    - histogram_plot(): Create and save a histogram of Income.
    - bar_plot(): Create and save a bar plot of employee status.
    - multiple_subplots(): Create and save multiple subplots of different visualizations.
    """

    def __init__(self):
        self.data = pd.read_csv("Classes/labwork_8/tax.csv")
        self.columns = self.data.columns.tolist()
        self.file_save = FileSaver("Data/labwork_8")

    def explore_data(self):
        """
        Display minimum and maximum values in the DataFrame.
        """
        min_values = self.data.min()
        max_values = self.data.max()

        print("Min value:")
        print(min_values)

        print("\nMax value:")
        print(max_values)

    def save_plots(self, data, name_file):
        """
        Save plots as PNG files.

        :param data: The plot object to be saved.
        :param name_file: The name of the file to be saved.
        """
        path = "Data/labwork_8"
        full_path = os.path.join(path, name_file)
        data.savefig(full_path)
        print(f"Plot saved at: {full_path}")

    def visualize_data(self, user_choice):
        """
        Visualize data based on user input.

        :param user_choice: User's choice for the type of visualization.
        """
        if user_choice == "1":
            self.scatter_plot()
        elif user_choice == "2":
            self.histogram_plot()
        elif user_choice == "3":
            self.bar_plot()
        elif user_choice == "4":
            self.multiple_subplots()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    def scatter_plot(self):
        """
        Create and save a scatter plot of ID and Income.
        """
        scatter_fig, scatter_ax = plt.subplots()
        scatter_ax.scatter(self.data['ID'], self.data['Income'], alpha=0.5)
        scatter_ax.set_xlabel('ID')
        scatter_ax.set_ylabel('Income')
        scatter_ax.set_title('Scatter Plot of Id and Last Income')
        self.save_plots(scatter_fig, 'scatter_plot')
        plt.show()

    def histogram_plot(self):
        """
        Create and save a histogram of Income.
        """
        histogram_fig, histogram_ax = plt.subplots()
        self.data['Income'].plot(kind='hist', bins=10, color='green', alpha=0.7, ax=histogram_ax)
        histogram_ax.set_title('Histogram')
        histogram_ax.set_xlabel('Value')
        histogram_ax.set_ylabel('Number of people')
        self.save_plots(histogram_fig, 'histogram_plot')
        plt.show()

    def bar_plot(self):
        """
        Create and save a bar plot of employee status.
        """
        bar_fig, bar_ax = plt.subplots(figsize=(8, 7))
        self.data['Status'].value_counts().plot(kind='bar', color='skyblue', ax=bar_ax)
        bar_ax.set_title('Number of employees by status')
        bar_ax.set_xlabel('Status')
        bar_ax.set_ylabel('Number of employees')
        self.save_plots(bar_fig, 'bar_plot')
        plt.show()

    def multiple_subplots(self):
        """
        Create and save multiple subplots of different visualizations.
        """
        # create a figure with two rows and two columns, with a width of 10 and a height of 8 inches
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        # extract the status distribution from the data and plot it as a pie chart
        status_distribution = self.data['Status'].value_counts()
        axes[0, 0].pie(status_distribution, autopct='%1.1f%%', labels=status_distribution.index, startangle=90)
        axes[0, 0].set_title('Status Distribution')

        # plot the scatter plot of ID and Income in the first subplot
        axes[0, 1].scatter(self.data['ID'], self.data['Income'], alpha=0.5)
        axes[0, 1].set_xlabel('ID')
        axes[0, 1].set_ylabel('Income')
        axes[0, 1].set_title('Scatter Plot of ID and Income')

        # plot the bar chart of the refund counts in the second subplot
        refund_counts = self.data['Refund'].value_counts()
        axes[1, 0].bar(refund_counts.index, refund_counts)
        axes[1, 0].set_xlabel('Refund')
        axes[1, 0].set_ylabel('Count')
        axes[1, 0].set_title('Number of Refunds')
        axes[1, 0].tick_params(axis='x', labelrotation=90)

        # plot the line chart of ID and Income in the third subplot
        axes[1, 1].plot(self.data['ID'], self.data['Income'], color='red')
        axes[1, 1].set_xlabel('ID')
        axes[1, 1].set_ylabel('Income')
        axes[1, 1].set_title('Line Chart of ID and Income')

        # show the plot
        plt.show()

        # adjust the spacing between the subplots
        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        # save the plot as a PNG file and output it as an HTML file
        self.save_plots(fig, 'all_plots.png')
        fig = px.scatter(self.data, x='ID', y='Income', color='Status',
                        title='Scatter Plot of ID and Income')
        fig.write_html('Data/labwork_8/output_plot.html')
        plt.show()
