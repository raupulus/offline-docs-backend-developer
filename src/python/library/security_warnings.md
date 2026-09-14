---
title: Consideraciones de seguridad
source_url: https://docs.python.org/es/3
source_path: library/security_warnings.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3730
---

# Consideraciones de seguridad

Los siguientes módulos tienen consideraciones de seguridad
específicas:

* "base64": consideraciones de seguridad de base64 en **RFC 4648**

* "hashlib": todos los constructores toman un argumento de solo
  palabra clave "usedforsecurity" que deshabilita algoritmos inseguros
  y bloqueados conocidos

* "http.server" no se recomienda para producción. Sólo implementa
  controles de seguridad básicos. Consulte las consideraciones de
  seguridad.

* "logging": La configuración de registro usa eval()

* "multiprocessing": Connection.recv() usa pickle

* "pickle": Restricción de globals en pickle

* "random" no debe usarse por motivos de seguridad, usa "secrets" en
  su lugar

* "shelve": el estante se basa en pickle y, por lo tanto, no es
  adecuado para tratar con fuentes no confiables

* "ssl": consideraciones de seguridad SSL/TLS

* "subprocess": Consideraciones sobre seguridad de subprocesos

* "tempfile": mktemp está en desuso debido a la vulnerabilidad a
  condiciones de urgencia

* "xml": XML security

* "zipfile": los archivos de .zip preparados maliciosamente pueden
  causar agotamiento del volumen del disco

La opción de línea de comando "-I" puede usarse para correr Python en
modo aislado. Cuando no puede ser usado, la opción "-P" o la variable
de entorno "PYTHONSAFEPATH" pueden usarse para no anteponer un camino
potencialmente inseguro al "sys.path" como el directorio actual, el
directorio del script o un string vacío.
