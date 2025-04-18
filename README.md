# 💻 Programación 1  🧮 Matematica

**Tecnicatura Universitaria en Programación**  
📍 *Universidad Tecnológica Nacional*  

- Este ejercicio integrador de las areas de matematica y programación fue realizador por... {nombres}

📌 **mcpython.py**  

Se ingresa al menú se selecciona el pedido requerido y se ingresa si tiene promociones de descuento
una vez que elije todas las opciones y las promo, le informa el total del pedido

## Explicación del Código

Este código está diseñado para simular un sistema simple de pedido en un restaurante de comida rápida, permitiendo gestionar productos, precios y promociones.

**1. Variables principales :**
Se declaran varias variables para manejar el estado del pedido y los precios de los productos:

- Variables de productos: hamb, papas, bebida, queso (inician en 0 para indicar que no están seleccionados).
- Promociones: promo_galicia y promo_otra para manejar descuentos disponibles.
- Precios: Los precios de los productos están definidos en variables como precio_hamburguesa, precio_coca, etc.

---

**2. Función mostrar_menu :**
Esta función inicializa un pedido con ciertos valores predeterminados:

- Activa una hamburguesa (hamb = 1).
- Activa una promoción específica (promo_galicia = 1).
- Otros productos y promociones inician en 0.

---

**3. Cálculo del total del pedido :**
El total se calcula sumando los precios de los productos seleccionados:

- Si una hamburguesa está incluida (hamb == 1), se suma su precio.
- Se hace lo mismo para las papas, la bebida y el queso.

---

**4. Validación de pago :**
El código valida que el pedido sea permitido antes de proceder con el pago:

- Restricción del queso: Si se selecciona queso adicional pero no hay hamburguesa, el sistema solicita agregar una hamburguesa o elimina el queso del pedido.
- Si hay al menos un producto válido en el pedido, se permite el pago.

---

**5. Aplicación de promociones :**
Si el pago es permitido:

- Se valida si una promoción es aplicable (promo_galicia o promo_otra, pero no ambas al mismo tiempo):
- Promo Galicia: Aplica un 10% de descuento.
- Otra Promo: Aplica un 5% de descuento.
- El total se actualiza en función de la promoción aplicada.

---

**6. Salida final :**

- Finalmente, el programa muestra el total con o sin descuento y agradece al cliente por su pedido.

## Aspectos destacados

- Uso de variables globales: Para simplificar el manejo del estado del pedido.
- Condiciones con lógica booleana: Se utilizan operadores como ^ (XOR) para garantizar que solo una promoción pueda aplicarse.

## Mejoras posibles

- Modularizar más el código dividiendo responsabilidades en funciones adicionales.
- Agregar más validaciones para entradas de usuario.
- Usar estructuras de datos como listas o diccionarios para manejar productos de forma más dinámica.
