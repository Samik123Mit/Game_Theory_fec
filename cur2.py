import pandas as pd
import numpy as np

# Define the data structure for our experiment
data = {
    "Student Name": [],
    "Effort Level (Dream Company)": [],
    "Effort Level (Multiple Companies)": [],
    "Probability of Selection (Dream Company)": [],
    "Probability of Selection (Multiple Companies)": [],
    "Payoff (Dream Company)": [],
    "Payoff (Multiple Companies)": [],
    "Outcome (Optimal Strategy)": []
}

# Sample Data for 10 students
students = ["Student A", "Student B", "Student C", "Student D", "Student E", 
            "Student F", "Student G", "Student H", "Student I", "Student J"]

# Generate random effort levels using numpy's random generator
np.random.seed(0)  # For reproducibility
effort_levels_dream = np.random.randint(30, 100, size=10)  # Random efforts for dream company (30 to 100)
effort_levels_multiple = 100 - effort_levels_dream  # Remaining effort for multiple companies

competition_level_dream = 0.7  # Assume a competition level for dream company
num_companies = 5  # Number of multiple companies

# Functions to calculate probabilities
def calculate_probability_dream(effort, competition):
    return min(1.0, effort / (100 * competition))

def calculate_probability_multiple(effort, num_companies):
    if num_companies == 0:
        return 0
    return min(1.0, effort / (20 * num_companies))  # Adjusted divisor to 20 for a reasonable probability range

# Functions to calculate payoffs
def calculate_payoff(probability, value, effort):
    cost = effort * 0.1  # Example cost function
    return probability * value - cost

# Assign values to our data
for i, student in enumerate(students):
    data["Student Name"].append(student)
    data["Effort Level (Dream Company)"].append(effort_levels_dream[i])
    data["Effort Level (Multiple Companies)"].append(effort_levels_multiple[i])
    
    # Calculate probabilities
    P_d = calculate_probability_dream(effort_levels_dream[i], competition_level_dream)
    P_m = calculate_probability_multiple(effort_levels_multiple[i], num_companies)
    
    data["Probability of Selection (Dream Company)"].append(P_d)
    data["Probability of Selection (Multiple Companies)"].append(P_m)
    
    # Calculate payoffs
    V_dream = 100  # Example value for getting into dream company
    V_multiple = 50  # Example average value for getting into any of the multiple companies
    payoff_dream = calculate_payoff(P_d, V_dream, effort_levels_dream[i])
    payoff_multiple = calculate_payoff(P_m, V_multiple, effort_levels_multiple[i])
    
    data["Payoff (Dream Company)"].append(payoff_dream)
    data["Payoff (Multiple Companies)"].append(payoff_multiple)
    
    # Determine optimal strategy
    optimal_strategy = "Dream" if payoff_dream >= payoff_multiple else "Multiple"
    data["Outcome (Optimal Strategy)"].append(optimal_strategy)

# Create DataFrame
df = pd.DataFrame(data)

# Corrected path to save the Excel file
file_path = "24_Placement_Strategy_Anaysis.csv"
df.to_csv(file_path, index=False)

file_path
