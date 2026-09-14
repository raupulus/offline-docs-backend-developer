---
title: Importando módulos
source_url: https://docs.python.org/es/3
source_path: library/modules.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3250
---

# Importando módulos

Los módulos descritos en este capítulo proporcionan nuevas formas de
importar otros módulos de Python y ganchos para personalizar los
procesos de importación.

La lista completa de módulos descritos en este capítulo es:

* "zipimport" --- Import modules from Zip archives

  * Objetos zipimporter

  * Ejemplos

* "pkgutil" --- Package extension utility

* "modulefinder" --- Find modules used by a script

  * Ejemplo de uso de "ModuleFinder"

* "runpy" --- Localización y ejecución de módulos Python

* "importlib" --- La implementación de "import"

  * Introducción

  * Funciones

  * "importlib.abc" -- Abstract base classes related to import

  * "importlib.machinery" -- Importers and path hooks

  * "importlib.util" -- Utility code for importers

  * Ejemplos

    * Importar programáticamente

    * Comprobando si se puede importar un módulo

    * Importar un archivo fuente directamente

    * Implementar importaciones diferidas

    * Configurar un importador

    * Aproximando "importlib.import_module()"

* "importlib.resources" -- Package resource reading, opening and
  access

  * Functional API

* "importlib.resources.abc" -- Abstract base classes for resources

* "importlib.metadata" -- Acceso a los metadatos de los paquetes

  * Descripción general

  * API funcional

    * Puntos de entrada

    * Metadatos de distribución

    * Versiones de distribución

    * Archivos de distribución

    * Requerimientos de la distribución

    * Mapeo de paquetes de importación a distribución

  * Distribuciones

  * Distribution Discovery

  * Implementing Custom Providers

    * Example

* La inicialización de la ruta de búsqueda de módulo de "sys.path"

  * Virtual Environments

  * Archivos _pth

  * Python embebido
