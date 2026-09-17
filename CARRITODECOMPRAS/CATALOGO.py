# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 02:13:11 2026

@author: Usuario
"""

def cargar_catalogo():
    catalogo = {
        "P001": {"nombre": "Café", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Té", "precio": 30.0, "stock": 15},
        "P003": {"nombre": "Galleta", "precio": 15.0, "stock": 50},
        "P004": {"nombre": "Leche", "precio":18.0, "stock": 35 },
        "P005": {"nombre": "Cereal", "precio":35.0, "stock": 40 },
        "P006": {"nombre": "Doritos", "precio":20.0, "stock": 25 },
        "P007": {"nombre": "Agua", "precio":15.0, "stock": 50 },
        "P008": {"nombre": "Dulces", "precio":12.0, "stock": 70 },
        "P009": {"nombre": "Refresco", "precio":20.0, "stock": 15 },
        "P010": {"nombre": "Salsa", "precio":14.0, "stock": 25 }
        
    }
    return catalogo

def mostrar_catalogo(catalogo):
    print("--- CATÁLOGO DE PRODUCTOS ---")
    print(f"{'Código':<8} | {'Nombre':<12} | {'Precio':<8} | {'Stock':<6}")
    print("-" * 45)
    
    # Recorremos cada producto del diccionario
    for codigo, info in catalogo.items():
        print(f"{codigo:<8} | {info['nombre']:<12} | ${info['precio']:<7.2f} | {info['stock']:<6}")

# --- CÓDIGO PRINCIPAL (debe ir pegado al margen izquierdo, sin espacios) ---
mi_catalogo = cargar_catalogo()
mostrar_catalogo(mi_catalogo)