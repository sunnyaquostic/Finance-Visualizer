init_deposit = 10000
interest     = 0.05
contribution = 100
compounding_type = 'monthly'
time_period_years = 5

if compounding_type == 'annual':
    n = 1
elif compounding_type == 'monthly':
    n = 12
    
total_amount = init_deposit * (1 + interest / n) ** (n * time_period_years)

total_contribution = contribution * (((1 + interest / n) ** (n * time_period_years) -1) / (interest / n))

final_amount = total_amount + total_contribution

print(final_amount)