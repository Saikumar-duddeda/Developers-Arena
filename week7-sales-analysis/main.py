from sales_analyzer.analyzer import SalesAnalyzer

analyzer = SalesAnalyzer("data/raw/sales_data.csv")

print("BASIC STATS")
stats = analyzer.basic_stats()
for k,v in stats.items():
    print(k,":",v)

analyzer.plot_sales("data/reports")
print("Report generated in data/reports folder")