import matplotlib.pyplot as plt

# monthly sales data(in dollara)

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sales=[5000,6000,7000,8000,9000,5098,7889,6798,5980,6987,4098,9876]

# create bar chart
plt.figure(figsize=(10,6))
plt.bar(months,sales,color='skyblue')

# add labels and titles
plt.xlabel('Month')
plt.ylabel('Sales($)')
plt.title('Monthly Sales Performance')

# display the chart
plt.grid(True)
plt.tight_layout()
plt.show()

