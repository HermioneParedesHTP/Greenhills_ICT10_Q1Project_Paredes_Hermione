from pyscript import document

def generate(e):

    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    quantity = document.querySelector("#quantity").value

    category = category.strip().upper()
    product = product.strip().upper()

    sku = category[:3] + product[:3] + quantity

    document.querySelector("#sku").innerText = sku

    #PLEASE HELP ME
