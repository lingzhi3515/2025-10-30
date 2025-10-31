import csv

def process_data():
    shop_sales = {}
    try:
        with open('sales.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                shop, sales = row[0], float(row[1])
                shop_sales[shop] = shop_sales.get(shop, 0) + sales
    except FileNotFoundError:
        print("sales.csv文件不存在")

    rider_orders = {}
    try:
        with open('rider.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                rider, orders = row[0], int(row[1])
                rider_orders[rider] = rider_orders.get(rider, 0) + orders
    except FileNotFoundError:
        print("rider.csv文件不存在")

    with open('result.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['店铺', '总销售额'])
        for shop, sales in shop_sales.items():
            writer.writerow([shop, sales])
        writer.writerow([])
        writer.writerow(['骑手', '订单总数'])
        for rider, orders in rider_orders.items():
            writer.writerow([rider, orders])
process_data()