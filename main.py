from pyscript import display, document

def make_receipt(e):
    iced_mocha = document.getElementById('iced mocha')
    hot_mocha = document.getElementById('hot mocha')
    hot_chocolate = document.getElementById('hot chocolate')
    iced_vanilla = document.getElementById('iced vanilla')
    hot_vanilla = document.getElementById('hot vanilla')
    # gets the values of the products

    subtotal = float(iced_mocha.value) * iced_mocha.checked + float(hot_mocha.value) * hot_mocha.checked + float(hot_chocolate.value) * hot_chocolate.checked + float(iced_vanilla.value) * iced_vanilla.checked + float(hot_vanilla.value) * hot_vanilla.checked
    # calculates the subtotal
    vAT = subtotal * 0.12
    # calculates the VAT
    total_cost = subtotal + vAT
    # calculates the total cost

    display(f'Your subtotal is ₱{subtotal:.2f}', target='receipt')
    display(f'Your VAT is ₱{vAT:.2f}', target='receipt')
    display(f'Your order costs ₱{total_cost:.2f} in total', target='receipt')
    # displays the information that was calculated above

def generate_sku(e):
    category = document.getElementById("category")
    product = document.getElementById("product_name")
    stock = document.getElementById("stock_quantity")
    # gets the values of the category, product, and stock quantity

    sku = category.value + "-" + product.value[:3].upper() + "-" + stock.value
    # calculates for the sku

    document.getElementById("sku-product").innerText = sku
    # displays the sku