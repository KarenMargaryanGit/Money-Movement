# Money Movement Analysis

This project provides a Streamlit application to analyze money movement data. It includes features to display the top 100 losers, top 100 gainers, and client analysis based on the provided dataset.

## Setup Instructions

### 1. Run the Setup Script

To create a virtual environment and install the required dependencies, navigate to the project directory and run the following command:

```bash
python setup.py
```

### 2. Run the Application

To run the Streamlit application, use the following command:

```bash
streamlit run main.py
```

## Application Features

### Top 100 Losers

Displays the top 100 clients with the lowest end balance. It includes a bar chart visualization.

### Top 100 Gainers

Displays the top 100 clients with the highest end balance. It includes a bar chart visualization.

### Client Analysis

Allows filtering by `FCLICODE` to analyze the end balance per client. If no `FCLICODE` is selected, it displays the total end balance per category.

## Data

The application expects a CSV file named `example.csv` in the project directory. The CSV file should contain the following columns:
- `FCLICODE`
- `End Balance`
- `Category`

Make sure your data is properly formatted to ensure the application works correctly.