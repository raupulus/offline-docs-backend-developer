---
title: Depuración y perfilado
source_url: https://docs.python.org/es/3
source_path: library/debug.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2280
---

# Depuración y perfilado

Estas bibliotecas le ayudan con el desarrollo de Python: el depurador
le permite recorrer paso a paso el código, analizar marcos de pila y
establecer puntos de interrupción, etc., y los perfiladores ejecutan
código y le proporcionan un desglose detallado de los tiempos de
ejecución, lo que le permite identificar cuellos de botella en sus
programas. Los eventos de auditoría proporcionan visibilidad de los
comportamientos en tiempo de ejecución que, de lo contrario,
requerirían depuración o parches intrusivos.

* Tabla de auditoría de eventos

* "bdb" --- Debugger framework

* "faulthandler" --- Dump the Python traceback

  * Volcar el rastreo

  * Dumping the C stack

    * C Stack Compatibility

  * Estado del gestor de fallos

  * Volcar los rastreos después de un tiempo de espera

  * Volcar el rastreo en una señal del usuario

  * Problema con descriptores de archivo

  * Ejemplo

* "pdb" --- The Python Debugger

  * Command-line interface

  * Debugger commands

* Los perfiladores de Python

  * Introducción a los perfiladores

  * Manual instantáneo de usuario

  * "profile" and "cProfile" Module Reference

  * La clase "Stats"

  * ¿Qué es el perfil determinista?

  * Limitaciones

  * Calibración

  * Usando un temporizador personalizado

* "timeit" --- Measure execution time of small code snippets

  * Ejemplos básicos

  * Interfaz de Python

  * Interfaz de línea de comandos

  * Ejemplos

* "trace" --- Trace or track Python statement execution

  * Uso de la línea de comandos

    * Opciones principales

    * Modificadores

    * Filtros

  * Interfaz programática

* "tracemalloc" --- Trace memory allocations

  * Ejemplos

    * Mostrar los 10 principales

    * Calcula las diferencias

    * Consigue el seguimiento del bloque de memoria

    * "Los 10 más bonitos"

      * Graba los tamaños actual y máximo de todos los bloques de
        memoria rastreados

  * API

    * Funciones

    * Filtro de dominio

    * Filtro

    * Cuadro

    * Captura instantánea

    * Estadística

    * StatisticDiff

    * Rastro

    * Seguimiento
