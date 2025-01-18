import io
import base64
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        init_deposit = int(request.form['initial-deposit'])
        interest     = float(request.form['interest-rate'])
        contribution = float(request.form['contribution'])
        compounding_type = request.form['compound-type']
        time_period_years = int(request.form['time-period'])

        n = 12 if compounding_type == 'monthly' else 1
            
        total_amount = init_deposit * (1 + interest / n) ** (n * time_period_years)
        total_contribution = contribution * (((1 + interest / n) ** (n * time_period_years) -1) / (interest / n))

        final_amount_with_interest = total_amount + total_contribution
        
        total_contribution_without_interest = init_deposit + contribution * time_period_years * n
        
        difference = final_amount_with_interest - total_contribution_without_interest
        
        
        amount_with_interest = []
        amount_without_interest = []
        
        years = list(range(time_period_years + 1))
        
        for year in years:
            year_total_amount = init_deposit * (1 + interest / n) ** (n * year)
            year_total_contribution = contribution * (((1 + interest / n) ** (n * year) - 1) / (interest / n))
            
            year_total_contribution_without_interest = init_deposit + contribution * year * n 
            
            amount_with_interest.append(year_total_amount + year_total_contribution)
            amount_without_interest.append(year_total_contribution_without_interest)
            
        plt.figure(figsize=(10, 5))
        plt.plot(years, amount_with_interest, marker='o', label='With Interest')
        plt.plot(years, amount_without_interest, marker='o', label='Without Interest')
        plt.title('Compound Interest Over Time Comparison')
        plt.xlabel('years')
        plt.ylabel('Amount ($)')
        plt.grid(True)
        plt.legend()
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        
        return render_template('result.html', final_amount=final_amount_with_interest, difference=difference, plot_url=plot_url)
    else:
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True)