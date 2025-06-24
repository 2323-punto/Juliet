 


cart =[]

def addToCart (product):
    cart. append (product)
    print (f" (product) agregado al carrito.")

def removeFromCart (product):
     if product in cart:
          cart.remove(product)
          print(f"{product}eliminado del carrito.")
     else:
          print(f"{product}no esta en el carrito.")  
    
def displayCart():
     if cart:
          print("productos en el carro")
          for item in cart:
               print("-", item)
     else:
          print("el carrito esta vacio.")   

#prueba de las funciones 