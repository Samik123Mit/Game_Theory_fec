import numpy as np
import pandas as pd

# Define constants
price_range = (10, 50)
iterations = 100
num_experiments = 10

def profit(price, marginal_cost, quantity=100):
    """ Calculate profit for a firm based on its price """
    return (price - marginal_cost) * quantity

def best_response(other_price, marginal_cost, price_range):
    """ Determine the best response price for a firm given the other firm's price """
    best_price = price_range[0]
    best_profit = -np.inf
    for price in np.linspace(price_range[0], price_range[1], 100):
        if price < other_price + 5:  # Avoid aggressive undercutting
            current_profit = profit(price, marginal_cost)
            if current_profit > best_profit:
                best_price = price
                best_profit = current_profit
    return best_price

def bertrand_game(marginal_costs, price_range, iterations):
    """ Simulate the Bertrand game with varying marginal costs and demand curves """
    price_lohit = np.random.uniform(*price_range)
    price_disang = np.random.uniform(*price_range)
    
    for _ in range(iterations):
        new_price_lohit = best_response(price_disang, marginal_costs[0], price_range)
        new_price_disang = best_response(price_lohit, marginal_costs[1], price_range)
        
        if abs(new_price_lohit - price_lohit) < 0.01 and abs(new_price_disang - price_disang) < 0.01:
            break
        
        price_lohit = new_price_lohit
        price_disang = new_price_disang

    return price_lohit, price_disang

def run_experiments(num_experiments, price_range, iterations):
    """ Run multiple experiments with variable marginal costs and demand curves """
    data = []
    for experiment in range(num_experiments):
        # Random marginal costs for each experiment
        marginal_costs = [np.random.uniform(5, 20), np.random.uniform(5, 20)]
        
        # Run the Bertrand game with variable costs
        price_lohit, price_disang = bertrand_game(marginal_costs, price_range, iterations)
        
        # Calculate profits based on final prices and marginal costs
        profit_lohit = profit(price_lohit, marginal_costs[0])
        profit_disang = profit(price_disang, marginal_costs[1])
        
        data.append({
            'Experiment': experiment + 1,
            'Initial Price Lohit': np.random.uniform(*price_range),
            'Initial Price Disang': np.random.uniform(*price_range),
            'Final Price Lohit': price_lohit,
            'Final Price Disang': price_disang,
            'Profit Lohit': profit_lohit,
            'Profit Disang': profit_disang
        })
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    return df

# Run experiments and save to spreadsheet
df = run_experiments(num_experiments, price_range, iterations)
print("Experiment Results:")
print(df)
df.to_csv('variable_bertrand_competition_data.csv', index=False)
print("\nData has been saved to 'variable_bertrand_competition_data.xlsx'")
