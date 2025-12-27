import pandas as pd
import matplotlib.pyplot as plt

class SalesAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])

    def basic_stats(self):
        return {
            "Total Sales": self.df['total_amount'].sum(),
            "Average Order Value": self.df['total_amount'].mean(),
            "Total Orders": len(self.df)
        }

    def monthly_sales(self):
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        return self.df.groupby('month')['total_amount'].sum()

    def plot_sales(self, out_dir):
        sales = self.monthly_sales()
        sales.plot(kind='line', title='Monthly Sales Trend')
        plt.tight_layout()
        plt.savefig(f"{out_dir}/monthly_sales.png")
        plt.close()