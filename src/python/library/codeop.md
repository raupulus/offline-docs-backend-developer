---
title: '"codeop" --- Compile Python code'
source_url: https://docs.python.org/es/3
source_path: library/codeop.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1990
---

# "codeop" --- Compile Python code

**Código fuente:** Lib/codeop.py

======================================================================

The "codeop" module provides utilities upon which the Python read-
eval-print loop can be emulated, as is done in the "code" module.  As
a result, you probably don't want to use the module directly; if you
want to include such a loop in your program you probably want to use
the "code" module instead.

Esta actividad consta de dos partes:

1. Ser capaz de identificar si una línea de entrada completa una
   sentencia de Python: en resumen, decir si se debe imprimir a
   continuación '">>>"' o '"..."'.

2. Recordar qué declaraciones futuras ha ingresado el usuario, para
   que la entrada posterior puedan ser compiladas con estas en efecto.

The "codeop" module provides a way of doing each of these things, and
a way of doing them both.

Para hacer lo anterior:

codeop.compile_command(source, filename='<input>', symbol='single')

   Intenta compilar *source*, que debe ser una cadena de caracteres de
   código Python y retorna un objeto si *source* es código Python
   válido. En este caso, el atributo del nombre del archivo del objeto
   va a ser *filename*, el cuál por defecto es "'<input>'". Retorna
   "None" si *source* no es código Python válido, pero es un prefijo
   de código Python válido.

   Si hay un problema con *source*, se lanzará una excepción.
   "SyntaxError" se lanza si hay una sintaxis de Python no válida, y
   "OverflowError" o "ValueError" si hay un literal no válido.

   El argumento *symbol* determina si *source* se compila como una
   declaración ("'single'", el valor predeterminado), como una
   secuencia de *statement* ("'exec'") o como un *expression*
   ("'eval'"). Cualquier otro valor hará que se lance "ValueError".

   Nota:

     Es posible (pero no probable) que el analizador deje de analizar
     con un resultado exitoso antes de llegar al final de la fuente;
     en este caso, los símbolos finales pueden ignorarse en lugar de
     provocar un error. Por ejemplo, una barra invertida seguida de
     dos nuevas líneas puede ir seguida de basura arbitraria. Esto se
     solucionará una vez que la API para el analizador sea mejor.

class codeop.Compile

   Las instancias de esta clase tienen métodos "__call__()" idénticos
   en firma a la función incorporada "compile()", pero con la
   diferencia de que si la instancia compila el texto del programa que
   contiene una instrucción "__future__", la instancia 'recuerda' y
   compila todos los textos de programa posteriores con la declaración
   en vigor.

class codeop.CommandCompiler

   Las instancias de esta clase tienen métodos "__call__()" idénticos
   en firma a "compile_command()"; la diferencia es que si la
   instancia compila un texto de programa que contiene una declaración
   "__future__", la instancia 'recuerda' y compila todos los textos de
   programa posteriores con la declaración en vigor.
