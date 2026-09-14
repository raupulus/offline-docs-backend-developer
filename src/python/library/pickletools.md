---
title: '"pickletools" --- Tools for pickle developers'
source_url: https://docs.python.org/es/3
source_path: library/pickletools.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3450
---

# "pickletools" --- Tools for pickle developers

**Código fuente:** Lib/pickletools.py

======================================================================

This module contains various constants relating to the intimate
details of the "pickle" module, some lengthy comments about the
implementation, and a few useful functions for analyzing pickled data.
The contents of this module are useful for Python core developers who
are working on the "pickle"; ordinary users of the "pickle" module
probably won't find the "pickletools" module relevant.

## Command-line usage

Added in version 3.2.

Cuando se invoca desde la línea de comandos, "python -m pickletools"
desensamblará el contenido de uno o más archivos pickle.  Tenga en
cuenta que si desea ver el objeto Python almacenado en el pickle en
lugar de los detalles del formato de pickle, es posible que desee
utilizar "-m pickle" en su lugar. Sin embargo, cuando el archivo de
pickle que desea examinar proviene de una fuente que no es de
confianza, "-m pickletools" es una opción más segura porque no ejecuta
el código de bytes de pickle.

Por ejemplo, con una tupla "(1, 2)" pickled en el archivo "x.pickle":

   $ python -m pickle x.pickle
   (1, 2)

   $ python -m pickletools x.pickle
       0: \x80 PROTO      3
       2: K    BININT1    1
       4: K    BININT1    2
       6: \x86 TUPLE2
       7: q    BINPUT     0
       9: .    STOP
   highest protocol among opcodes = 2

### Command-line options

-a, --annotate

   Anote cada línea con una breve descripción del código de operación.

-o, --output=<file>

   Nombre de un archivo donde se debe escribir la salida.

-l, --indentlevel=<num>

   Número de espacios en blanco por los que se aplica una sangría a un
   nuevo nivel de MARK.

-m, --memo

   Cuando se desensamblan varios objetos, conserve la nota entre los
   ensamblajes.

-p, --preamble=<preamble>

   When more than one pickle file is specified, print given preamble
   before each disassembly.

pickle_file

   A pickle file to read, or "-" to indicate reading from standard
   input.

## Programmatic interface

pickletools.dis(pickle, out=None, memo=None, indentlevel=4, annotate=0)

   Produce un desensamblado simbólico del pickle en el objeto similar
   a un archivo *salida*, de forma predeterminada en "sys.stdout".
   *pickle* puede ser una cadena o un objeto similar a un archivo.
   *memo* puede ser un diccionario Python que se utilizará como nota
   del pickle; se puede utilizar para realizar ensamblajes de desuso
   en varios pickles creados por el mismo selector. Los niveles
   sucesivos, indicados por los códigos de operación "MARK" en la
   secuencia, son indentados por espacios *indentlevel*.  Si se da un
   valor distinto de cero a *anotar*, cada código de operación de la
   salida se anota con una breve descripción.  El valor de *anotar* se
   utiliza como sugerencia para la columna donde debe comenzar la
   anotación.

   Distinto en la versión 3.2: Added the *annotate* parameter.

pickletools.genops(pickle)

   Proporciona un *iterator* sobre todos los códigos de operación en
   un pickle, retornando una secuencia de triples "(opcode, arg,
   pos)".  *opcode* es una instancia de una clase "OpcodeInfo"; *arg*
   es el valor descodificado, como un objeto Python, del argumento del
   código de operación; *pos* es la posición en la que se encuentra
   este código de operación. *pickle* puede ser una cadena o un objeto
   similar a un archivo.

pickletools.optimize(picklestring)

   Retorna una nueva cadena pickle equivalente después de eliminar los
   códigos de operación "PUT" no utilizados. El pickle optimizado es
   más corto, toma menos tiempo de transmisión, requiere menos espacio
   de almacenamiento y se restaura de manera más eficiente.
