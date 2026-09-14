---
title: '"code" --- Interpreter base classes'
source_url: https://docs.python.org/es/3
source_path: library/code.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1970
---

# "code" --- Interpreter base classes

**Código fuente::** Lib/code.py

======================================================================

El módulo de "code" proporciona facilidades para implementar bucles de
lectura-evaluación-impresión en Python. Se incluyen dos clases y
funciones de conveniencia que se pueden usar para crear aplicaciones
que brinden un *prompt* interactivo del intérprete.

class code.InteractiveInterpreter(locals=None)

   This class deals with parsing and interpreter state (the user's
   namespace); it does not deal with input buffering or prompting or
   input file naming (the filename is always passed in explicitly).
   The optional *locals* argument specifies a mapping to use as the
   namespace in which code will be executed; it defaults to a newly
   created dictionary with key "'__name__'" set to "'__console__'" and
   key "'__doc__'" set to "None".

   Note that functions and classes objects created under an
   "InteractiveInterpreter" instance will belong to the namespace
   specified by *locals*. They are only pickleable if *locals* is the
   namespace of an existing module.

class code.InteractiveConsole(locals=None, filename='<console>', local_exit=False)

   Closely emulate the behavior of the interactive Python interpreter.
   This class builds on "InteractiveInterpreter" and adds prompting
   using the familiar "sys.ps1" and "sys.ps2", and input buffering. If
   *local_exit* is true, "exit()" and "quit()" in the console will not
   raise "SystemExit", but instead return to the calling code.

   Distinto en la versión 3.13: Added *local_exit* parameter.

code.interact(banner=None, readfunc=None, local=None, exitmsg=None, local_exit=False)

   Convenience function to run a read-eval-print loop.  This creates a
   new instance of "InteractiveConsole" and sets *readfunc* to be used
   as the "InteractiveConsole.raw_input()" method, if provided.  If
   *local* is provided, it is passed to the "InteractiveConsole"
   constructor for use as the default namespace for the interpreter
   loop.  If *local_exit* is provided, it is passed to the
   "InteractiveConsole" constructor.  The "interact()" method of the
   instance is then run with *banner* and *exitmsg* passed as the
   banner and exit message to use, if provided.  The console object is
   discarded after use.

   Distinto en la versión 3.6: Se agregó el parámetro *exitmsg*.

   Distinto en la versión 3.13: Added *local_exit* parameter.

code.compile_command(source, filename='<input>', symbol='single')

   Esta función es útil para programas que desean emular el bucle
   principal del intérprete de Python (también conocido como bucle
   *read-eval-print*). La parte complicada es determinar cuándo el
   usuario ha ingresado un comando incompleto que se puede completar
   ingresando más texto (en lugar de un comando completo o un error de
   sintaxis). Esta función *casi* siempre toma la misma decisión que
   el bucle principal del intérprete real.

   *source* es la cadena de caracteres fuente; *filename* es el nombre
   de archivo opcional desde el que se leyó la fuente, por defecto es
   "'<input>'"; y *symbol* es el símbolo de inicio gramatical
   opcional, que debería ser "'single'" (el predeterminado), "'eval'"
   o "'exec'".

   Retorna un objeto de código (lo mismo que "compile(source,
   filename, symbol)") si el comando está completo y es válido; "None"
   si el comando está incompleto; lanza "SyntaxError" si el comando
   está completo y contiene un error de sintaxis, o lanza
   "OverflowError" o "ValueError" si el comando contiene un literal no
   válido.

## Objetos de intérprete interactivo

InteractiveInterpreter.runsource(source, filename='<input>', symbol='single')

   Compila y ejecuta alguna fuente en el intérprete. Los argumentos
   son los mismos que para "compile_command()"; el valor
   predeterminado para *filename* es "'<input>'", y para *symbol* es
   "'single'". Puede suceder una de varias cosas:

   * La entrada es incorrecta; "compile_command()" generó una
     excepción ("SyntaxError" o "OverflowError"). Se imprime un
     seguimiento de sintaxis llamando al método "showsyntaxerror()".
     "runsource()" retorna "False".

   * La entrada está incompleta y se requiere más información;
     "compile_command()" retorna "None". "runsource()" retorna "True".

   * La entrada está completa; "compile_command()" retornó un objeto
     de código. El código se ejecuta llamando a "runcode()" (que
     también maneja excepciones en tiempo de ejecución, excepto
     "SystemExit"). "runsource()" retorna "False".

   El valor de retorno se puede usar para decidir si usar "sys.ps1" o
   "sys.ps2" para solicitar la siguiente línea.

InteractiveInterpreter.runcode(code)

   Ejecuta un objeto de código. Cuando ocurre una excepción, se llama
   a "showtraceback()" para mostrar un seguimiento del código. Se
   capturan todas las excepciones excepto "SystemExit", que puede
   propagarse.

   Una nota sobre "KeyboardInterrupt": esta excepción puede ocurrir en
   otra parte de este código y no siempre se detecta. Quien llama la
   función debe estar preparado para manejar esto.

InteractiveInterpreter.showsyntaxerror(filename=None)

   Muestra el error de sintaxis que acaba de ocurrir. Esto no muestra
   la traza de seguimiento porque no la hay para errores de sintaxis.
   Si se proporciona *filename*, se incluirá en la excepción en lugar
   del nombre de archivo predeterminado proporcionado por el
   analizador de Python, ya que siempre usa "'<string>'" cuando lee de
   una cadena de caracteres. La salida se escribe mediante el método
   "write()".

InteractiveInterpreter.showtraceback()

   Muestra la excepción que acaba de ocurrir. Eliminamos el primer
   elemento de la pila porque está dentro de la implementación del
   intérprete. La salida se escribe mediante el método "write()".

   Distinto en la versión 3.5: Se muestra la traza de seguimiento
   encadenada completa en lugar de solo la traza primaria de pila.

InteractiveInterpreter.write(data)

   Escribe una cadena de caracteres en el flujo de error estándar
   ("sys.stderr"). Las clases derivadas deben reemplazar esto para
   proporcionar el manejo de salida apropiado según sea necesario.

## Objetos de consola interactiva

La clase "InteractiveConsole" es una subclase de
"InteractiveInterpreter", por lo que ofrece todos los métodos de los
objetos del intérprete, así como las siguientes adiciones.

InteractiveConsole.interact(banner=None, exitmsg=None)

   Emula estrictamente la consola interactiva de Python. El argumento
   opcional *banner* especifica la bandera a imprimir antes de la
   primera interacción; de forma predeterminada, imprime una bandera
   similar al impreso por el intérprete estándar de Python, seguido
   del nombre de clase del objeto de la consola entre paréntesis (para
   no confundir esto con el intérprete real, ¡ya que está muy cerca!)

   El argumento opcional *exitmsg* especifica un mensaje de salida que
   se imprime al salir. Pase la cadena de caracteres vacía para
   suprimir el mensaje de salida. Si no se proporciona *exitmsg* o es
   "None", se imprime el mensaje predeterminado.

   Distinto en la versión 3.4: Para suprimir la impresión de cualquier
   bandera, pase una cadena de caracteres vacía.

   Distinto en la versión 3.6: Imprime un mensaje de salida al salir.

InteractiveConsole.push(line)

   Envía una línea de texto fuente al intérprete. La línea no debe
   tener un salto de línea al final; puede tener nuevas líneas
   internas. La línea se agrega a un búfer y se llama al método
   "runsource()" del intérprete con el contenido concatenado del búfer
   y la nueva fuente. Si indica que el comando se ejecutó o no es
   válido, el búfer se restablece; de lo contrario, el comando está
   incompleto y el búfer se deja como estaba después de agregar la
   línea. Si se requieren más entradas el valor de retorno es "True",
   "False" si la línea se procesó de alguna manera (esto es lo mismo
   que "runsource()").

InteractiveConsole.resetbuffer()

   Elimina cualquier texto fuente no gestionado del búfer de entrada.

InteractiveConsole.raw_input(prompt='')

   Escribe un *prompt* y lee una línea. La línea retornada no incluye
   el salto de línea final. Cuando el usuario ingresa la secuencia de
   teclas EOF, se lanza "OFError". La implementación base lee de
   "sys.stdin"; una subclase puede reemplazar esto con una
   implementación diferente.
