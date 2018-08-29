# do this now
products = [["phone", 340, False], ["pc", 1420.25, True], ["plant", 24.5, True]]
print(products)
sale_products = [product for product in products if product[2]]  # Will only get the ones with true.
print(sale_products)
print(sum(product[1] for product in products if product[2]))

