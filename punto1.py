"""
PUNTO 1 – Análisis de Complejidad de Código
Materia: Análisis de Algoritmos

Descripción:
Una empresa tecnológica analiza interacciones de usuarios en una red social.
El siguiente código calcula la publicación con más "me gusta" por usuario.

Preguntas:
a) Determinar la complejidad temporal total (Big-O)
b) Proponer una optimización que mantenga el mismo resultado, pero reduzca el tiempo.

---------------------------------------------------------------
RESPUESTAS:

a) Complejidad temporal del código original:
   El algoritmo recorre tres niveles:
     - Usuarios (U)
     - Posts por usuario (P)
     - Likes por post (L)
   → Complejidad total = O(U · P · L)
   → Está en la zona de complejidad alta (similar a O(n³)).

b) Optimización propuesta:
   En lugar de contar los likes con un bucle, usar len(post["likes"]),
   que es O(1) en Python. 
   Así, la complejidad mejora a O(U · P).

   También puede mantenerse un contador de likes actualizado al agregar o eliminar likes,
   para no recorrer listas innecesariamente.
---------------------------------------------------------------
"""

# Código original (no optimizado)
def post_mas_popular_original(usuarios):
    resultado = {}
    for usuario in usuarios:
        max_likes = 0
        for post in usuario["posts"]:
            total = 0
            for like in post["likes"]:
                total += 1
            if total > max_likes:
                max_likes = total
        resultado[usuario["nombre"]] = max_likes
    return resultado


# Código optimizado (uso de len())
def post_mas_popular(usuarios):
    resultado = {}
    for usuario in usuarios:
        max_likes = 0
        for post in usuario["posts"]:
            total = len(post["likes"])  # cuenta en O(1)
            if total > max_likes:
                max_likes = total
        resultado[usuario["nombre"]] = max_likes
    return resultado


# Ejemplo de uso (opcional para pruebas)
if __name__ == "__main__":
    usuarios = [
        {
            "nombre": "Ana",
            "posts": [
                {"likes": ["u1", "u2", "u3"]},
                {"likes": ["u4", "u5"]}
            ]
        },
        {
            "nombre": "Luis",
            "posts": [
                {"likes": ["x1", "x2"]},
                {"likes": ["x3"]}
            ]
        }
    ]
    print(post_mas_popular(usuarios))
    # Salida esperada: {'Ana': 3, 'Luis': 2}
