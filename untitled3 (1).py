

import numpy as np

# 1. Create sales data for 10 stores and 12 months
np.random.seed(10)

sales = np.random.randint(50000, 150000, (10, 12))

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

print("SALES DATA")
print(sales)


# 2. Calculate sales for each quarter
print("\nQUARTERLY REPORT")

q1 = sales[:, 0:3]
q2 = sales[:, 3:6]
q3 = sales[:, 6:9]
q4 = sales[:, 9:12]

print("Quarter 1 Sales:", np.sum(q1))
print("Quarter 2 Sales:", np.sum(q2))
print("Quarter 3 Sales:", np.sum(q3))
print("Quarter 4 Sales:", np.sum(q4))


# 3. Show monthly total sales
monthly_sales = np.sum(sales, axis=0)

print("\nMONTHLY SALES")
for i in range(12):
    print(months[i], ":", monthly_sales[i])


# 4. Find months with sales above target
target = 1000000

print("\nMONTHS WITH SALES ABOVE TARGET")
for i in range(12):
    if monthly_sales[i] > target:
        print(months[i], ":", monthly_sales[i])


# 5. Find stores with below-average sales
store_sales = np.sum(sales, axis=1)
average_sales = np.mean(store_sales)

print("\nSTORES WITH BELOW-AVERAGE SALES")
for i in range(10):
    if store_sales[i] < average_sales:
        print("Store", i + 1, ":", store_sales[i])


# 6. Select specific stores using fancy indexing
print("\nSALES OF STORES 2, 5 AND 8")
print(sales[[1, 4, 7], :])


# 7. Find the best three months
best_months = np.argsort(monthly_sales)[-3:][::-1]

print("\nTOP 3 MONTHS")
for i in best_months:
    print(months[i], ":", monthly_sales[i])


# 8. Create monthly growth targets
growth_targets = np.linspace(900000, 1200000, 12)

print("\nMONTHLY GROWTH TARGETS")
for i in range(12):
    print(months[i], ":", round(growth_targets[i]))


# 9. Final summary
print("\nFINAL SUMMARY")
print("Total Yearly Sales:", np.sum(sales))
print("Best Month:", months[np.argmax(monthly_sales)])
print("Best Store: Store", np.argmax(store_sales) + 1)
