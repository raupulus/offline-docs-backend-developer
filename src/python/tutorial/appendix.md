---
title: 16. Apéndice
source_url: https://docs.python.org/es/3
source_path: tutorial/appendix.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4860
---

# 16. Apéndice

## 16.1. Modo interactivo

There are two variants of the interactive *REPL*.  The classic basic
interpreter is supported on all platforms with minimal line control
capabilities.

Since Python 3.13, a new interactive shell is used by default. This
one supports color, multiline editing, history browsing, and paste
mode.  To disable color, see Controlling color for details.  Function
keys provide some additional functionality. "F1" enters the
interactive help browser "pydoc". "F2" allows for browsing command-
line history with neither output nor the *>>>* and *...* prompts. "F3"
enters "paste mode", which makes pasting larger blocks of code easier.
Press "F3" to return to the regular prompt.

When using the new interactive shell, exit the shell by typing "exit"
or "quit". Adding call parentheses after those commands is not
required.

If the new interactive shell is not desired, it can be disabled via
the "PYTHON_BASIC_REPL" environment variable.

### 16.1.1. Manejo de errores

When an error occurs, the interpreter prints an error message and a
stack trace. In interactive mode, it then returns to the primary
prompt; when input came from a file, it exits with a nonzero exit
status after printing the stack trace. (Exceptions handled by an
"except" clause in a "try" statement are not errors in this context.)
Some errors are unconditionally fatal and cause an exit with a nonzero
exit status; this applies to internal inconsistencies and some cases
of running out of memory.  All error messages are written to the
standard error stream; normal output from executed commands is written
to standard output.

Al ingresar el carácter de interrupción (por lo general "Control"-"C"
o "Supr") en el prompt primario o secundario, se cancela la entrada y
retorna al prompt primario.  [1] Tipear una interrupción mientras un
comando se están ejecutando lanza la excepción "KeyboardInterrupt",
que puede ser manejada con una sentencia "try".

### 16.1.2. Programas ejecutables de Python

En los sistemas Unix y tipo BSD, los programas Python pueden
convertirse directamente en ejecutables, como programas del intérprete
de comandos, poniendo la linea:

   #!/usr/bin/env python3

...al principio del script y dándole al archivo permisos de ejecución
(asumiendo que el intérprete están en la variable de entorno "PATH"
del usuario).  "#!" deben ser los primeros dos caracteres del archivo.
En algunas plataformas, la primera línea debe terminar al estilo Unix
("'\n'"), no como en Windows ("'\r\n'").  Notá que el carácter numeral
"'#'" se usa en Python para comenzar un comentario.

Se le puede dar permisos de ejecución al script usando el comando
**chmod**.

   $ chmod +x myscript.py

En sistemas Windows, no existe la noción de "modo ejecutable".  El
instalador de Python asocia automáticamente la extensión ".py" con
"python.exe" para que al hacerle doble clic a un archivo Python se
corra el script.  La extensión también puede ser ".pyw", en este caso
se omite la ventana con la consola que normalmente aparece.

### 16.1.3. El archivo de inicio interactivo

Cuando usas Python en forma interactiva, suele ser útil que algunos
comandos estándar se ejecuten cada vez que el intérprete se inicia.
Puedes hacer esto configurando la variable de entorno "PYTHONSTARTUP"
con el nombre de un archivo que contenga tus comandos de inicio.  Esto
es similar al archivo ".profile" en los intérpretes de comandos de
Unix.

Este archivo es solo leído en las sesiones interactivas del
intérprete, no cuando Python lee comandos de un script ni cuando
"/dev/tty" se explicita como una fuente de comandos (que de otro modo
se comporta como una sesión interactiva).  Se ejecuta en el mismo
espacio de nombres en el que los comandos interactivos se ejecutan,
entonces los objetos que define o importa pueden ser usados sin
cualificaciones en la sesión interactiva.  En este archivo también
puedes cambiar los prompts "sys.ps1" y "sys.ps2".

Si quieres leer un archivo de inicio adicional desde el directorio
actual, puedes programarlo en el archivo de inicio global usando algo
como "if os.path.isfile('.pythonrc.py'):
exec(open('.pythonrc.py').read())".  Si quieres usar el archivo de
inicio en un script, tienes que hacer lo siguiente de forma explícita
en el script:

   import os
   filename = os.environ.get('PYTHONSTARTUP')
   if filename and os.path.isfile(filename):
       with open(filename) as fobj:
           startup_file = fobj.read()
       exec(startup_file)

### 16.1.4. Los módulos de customización

Python provee dos formas para customizarlo: sitecustomize y
usercustomize.  Para ver cómo funciona, necesitas primero encontrar
dónde está tu directorio para tu usuario de paquetes del sistema.
Inicia Python y ejecuta el siguiente código:

   >>> import site
   >>> site.getusersitepackages()
   '/home/user/.local/lib/python3.x/site-packages'

Ahora puedes crear un archivo llamado "usercustomize.py" en ese
directorio y poner lo que quieras en él.  Eso afectará cada ejecución
de Python, a menos que se inicie con la opción "-s" para deshabilitar
esta importación automática.

sitecustomize funciona de la misma manera, pero normalmente lo crea el
administrador de la computadora en el directorio global de paquetes
del sistema, y se importa antes que usercustomize. Para más detalles,
mira la documentación del módulo "site".

-[ Notas al pie ]-

[1] Un problema con el paquete GNU Readline puede prevenir esto.
