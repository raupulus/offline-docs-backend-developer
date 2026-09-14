---
title: Servicios genéricos del sistema operativo
source_url: https://docs.python.org/es/3
source_path: library/allos.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1510
---

# Servicios genéricos del sistema operativo

Los módulos descritos en este capítulo proporcionan interfaces a las
características del sistema operativo que están disponibles en (casi)
todos los sistemas operativos, como archivos y un reloj. Las
interfaces se modelan, por norma general, según las interfaces Unix o
C, pero también están disponibles en la mayoría de los otros sistemas.
Esta es una visión general:

* "os" --- Interfaces misceláneas del sistema operativo

  * Nombres de archivos, argumentos de la línea de comandos y
    variables de entorno

  * Modo Python UTF-8

  * Parámetros de proceso

  * Creación de objetos de tipo archivo

  * Operaciones de descriptores de archivos

    * Consultando las dimensiones de una terminal

    * Herencia de los descriptores de archivos

  * Archivos y directorios

    * Descriptores de archivos del temporizador

    * Atributos extendidos de Linux

  * Gestión de proceso

  * Interfaz al planificador

  * Información miscelánea del sistema

  * Números al azar

* "io" --- Core tools for working with streams

  * Resumen

    * E/S Texto

    * E/S Binaria

    * E/S sin formato

  * Codificación de texto

    * EncodingWarning opcional

  * Interfaz de módulo de alto nivel

  * Jerarquía de clases

    * Clases base E/S

    * Archivo sin formato E/S

    * *Streams* almacenados (búfer)

    * E/S Texto

  * Static Typing

  * Rendimiento

    * E/S Binaria

    * E/S Texto

    * Multihilo

    * Reentrada

* "time" --- Time access and conversions

  * Las Funciones

  * Constantes de ID de reloj

  * Constantes de zona horaria

* "logging" --- Logging facility for Python

  * Objetos logger

  * Niveles de logging

  * Gestor de objetos

  * Objetos formateadores

  * Filtro de Objetos

  * Objetos LogRecord

  * Atributos LogRecord

  * Objetos LoggerAdapter

  * Seguridad del hilo

  * Funciones a nivel de módulo

  * Atributos a nivel de módulo

  * Integración con el módulo de advertencias

* "logging.config" --- Logging configuration

  * Funciones de configuración

  * Consideraciones de seguridad

  * Esquema del diccionario de configuración

    * Detalles del esquema del diccionario

    * Configuración incremental

    * Conexiones de objeto

    * Objetos definidos por el usuario

    * Handler configuration order

    * Acceso a objetos externos

    * Acceso a objetos internos

    * Resolución de importación e importadores personalizados

    * Configuring QueueHandler and QueueListener

  * Formato de archivo de configuración

* "logging.handlers" --- Logging handlers

  * StreamHandler

  * FileHandler

  * NullHandler

  * WatchedFileHandler

  * BaseRotatingHandler

  * RotatingFileHandler

  * TimedRotatingFileHandler

  * SocketHandler

  * DatagramHandler

  * Gestor *SysLog* (*SysLogHandler*)

  * Gestor de eventos *NTELog* (NTEventLogHandler)

  * SMTPHandler

  * MemoryHandler

  * HTTPHandler

  * QueueHandler

  * QueueListener

* "platform" ---  Access to underlying platform's identifying data

  * Cross platform

  * Java platform

  * Windows platform

  * macOS platform

  * iOS platform

  * Unix platforms

  * Linux platforms

  * Android platform

  * Command-line usage

* "errno" --- Standard errno system symbols

* "ctypes" --- A foreign function library for Python

  * tutorial de ctypes

    * Carga de bibliotecas de enlaces dinámicos

    * Acceder a las funciones de los dll cargados

    * Funciones de llamada

    * Tipos de datos fundamentales

    * Funciones de llamada, continuación

    * Calling variadic functions

    * Funciones de llamada con sus propios tipos de datos
      personalizados

    * Especificar los tipos de argumentos requeridos (prototipos de
      funciones)

    * Tipos de retorno

    * Pasar los punteros (o: pasar los parámetros por referencia)

    * Estructuras y uniones

    * Structure/union layout, alignment and byte order

    * Campos de bits en estructuras y uniones

    * Arreglos

    * Punteros

    * Thread safety without the GIL

    * Conversiones de tipos

    * Tipos incompletos

    * Funciones de retrollamadas (*callback*)

    * Acceder a los valores exportados de los dlls

    * Sorpresas

    * Tipos de datos de tamaño variable

  * referencia ctypes

    * Encontrar bibliotecas compartidas

    * Listing loaded shared libraries

    * Cargando bibliotecas compartidas

    * Funciones foráneas

    * Prototipos de funciones

    * Funciones de utilidad

    * Tipos de datos

    * Tipos de datos fundamentales

    * Tipos de datos estructurados

    * Arreglos y punteros

    * Exceptions
