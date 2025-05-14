# Ejercicio practico

# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Paso 1: creacion de lista
lista = [5, 8, 2, 10, 3]

# Paso 2: media y desviación estándar de la lista
# Media:
media = sum(lista) / len(lista)
print(f"   Media: {media}")

# Desviación estándar:
desviacion_estandar = np.std(lista)
print(f"   Desviación estándar: {desviacion_estandar}")

# Paso 3: convertir la lista en un DataFrame y mostrar contenido
dataframe = pd.DataFrame(lista, columns=['Valores'])
print("\n3. DataFrame creado:")
print(dataframe)

# Paso 5: simular "ventas" y agregar columna "alta/baja"
# Creacion de nuevo dataframe
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
datos_ventas = pd.DataFrame({
    'Día': dias,
    'Ventas': lista
})

# Agregar la columna "alta/baja, si el valor es mayor que 6: "alta", si es menor o igual: "baja"
datos_ventas['Categoria'] = datos_ventas['Ventas'].apply(lambda x: 'alta' if x > 6 else 'baja')
print(datos_ventas)

# Paso 4: uso de matplotlib para graficar los valores
plt.figure(figsize=(8, 6))
plt.plot(datos_ventas['Día'], datos_ventas['Ventas'], marker='o', linestyle='-', color ='blue', label='Ventas')
plt.title('Gráfico de Ventas')
plt.xlabel('días')
plt.ylabel('Ventas')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

