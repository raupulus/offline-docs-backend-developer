---
title: '"tabnanny" --- Detection of ambiguous indentation'
source_url: https://docs.python.org/es/3
source_path: library/tabnanny.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4050
---

# "tabnanny" --- Detection of ambiguous indentation

**Código fuente:** Lib/tabnanny.py

======================================================================

Por el momento, este módulo está pensado para ser llamado como un
script. Sin embargo, es posible importarlo en un IDE y usar la función
"check()" que se describe a continuación.

Nota:

  Es probable que la API proporcionada por este módulo cambie en
  versiones futuras; dichos cambios pueden no ser compatibles con
  versiones anteriores.

tabnanny.check(file_or_dir)

   Si *file_or_dir* es un directorio y no un enlace simbólico,
   desciende recursivamente en el árbol de directorios nombrado por
   *file_or_dir*, verificando todos los archivos ".py" al mismo
   tiempo. Si *file_or_dir* es un archivo fuente normal de Python, se
   comprueba si hay problemas relacionados con los espacios en blanco.
   Los mensajes de diagnóstico se escriben en la salida estándar
   mediante la función "print()".

tabnanny.verbose

   Marcador que indica si se deben imprimir mensajes detallados. Esto
   se incrementa con la opción "-v" si se llama como un script.

tabnanny.filename_only

   Marcador que indica si se deben imprimir solo los nombres de
   archivo de los archivos que contienen problemas relacionados con
   los espacios en blanco. Esto se establece como verdadero con la
   opción "-q"  si se llama como un script.

exception tabnanny.NannyNag

   Invocada por "process_tokens()" sí detecta una indentación ambigua.
   Capturada y gestionada en "check()".

tabnanny.process_tokens(tokens)

   Esta función es utilizada por "check()" para procesar los tokens
   generados por el módulo "tokenize".

Ver también:

  Módulo "tokenize"
     Escáner léxico para código fuente Python.
