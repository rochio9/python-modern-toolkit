"""
Day 01 — Two Sum.

Plataforma: LeetCode (Easy)
URL: https://leetcode.com/problems/two-sum/

Enunciado:
    Dado un array de enteros `nums` y un entero `target`, devolver los
    índices de los dos números cuya suma sea igual a `target`.
    Se asume que existe exactamente una solución y no se puede usar el
    mismo elemento dos veces.

Complejidad de la solución implementada:
    Tiempo:  O(n)  — single pass con hash map.
    Espacio: O(n)  — el hash map almacena hasta n-1 elementos.

Decisiones:
    - Usamos dict en lugar de doble loop O(n²) porque target lookup en
      hash map es O(1) amortizado.
    - Iteramos con enumerate para tener (índice, valor) sin lookup extra.
"""


