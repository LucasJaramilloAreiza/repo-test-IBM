# Criterios de Aceptación para Feature: Checkout Update

**Issue**: Implementar el endpoint de checkout para procesar órdenes.

**Criterios de Aceptación**:
1. El usuario debe poder enviar una lista de IDs de productos y un porcentaje de descuento.
2. El descuento máximo aplicable es del 20%.
3. El stock de cada producto comprado debe decrementarse tras la compra exitosa.
4. El endpoint debe devolver el total a pagar y el estado de la orden.
