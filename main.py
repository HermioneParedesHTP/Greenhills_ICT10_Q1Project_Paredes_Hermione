from pyscript import document

def generate(e):

    category = document.getElementById("category").value
    product = document.getElementById("product").value
    quantity = document.getElementById("quantity").value

    category = category.strip().upper()
    product = product.strip().upper()

    sku = category[:3] + product[:3] + quantity

    document.getElementById("sku").innerText = sku

    #PLEASE HELP ME
