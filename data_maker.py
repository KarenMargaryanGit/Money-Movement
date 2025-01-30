import pandas as pd
import numpy as np

def calculate_data(path):
    startDate = path.split('-')[1]
    endDate = path.split('-')[2]
    # Define parameters
    num_fclicodes = 150  # Number of unique FCLICODES
    currencies = ["AMD", "USD", "EUR", "Other"]
    columns = [
        "FCLICODE", "Start Balance", "New Client", "Closed Clients",
        "From other", "Own Resources", "End Balance", "Category"
    ]

    data = []

    for i in range(1, num_fclicodes + 1):
        for currency in currencies:
            fclicode = f"0400000{i}"
            start_balance = np.round(np.random.uniform(0, 5000), 2) if np.random.rand() > 0.5 else 0.0
            new_clients = np.random.randint(0, 10)
            closed_clients = np.random.randint(0, 5)
            from_other = np.round(np.random.uniform(100, 1000), 2)
            own_resources = np.round(np.random.uniform(-1000, 1000), 2)
            end_balance = start_balance + from_other + own_resources - (closed_clients * 100)
            end_balance = np.round(end_balance, 2)
            
            data.append([fclicode, start_balance, new_clients, closed_clients, from_other, own_resources, end_balance, currency])

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    df.to_csv(path, index=False)

