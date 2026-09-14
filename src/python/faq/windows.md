---
title: Preguntas frecuentes sobre Python en Windows
source_url: https://docs.python.org/es/3
source_path: faq/windows.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: faq
order: 1120
---

# Preguntas frecuentes sobre Python en Windows

## ¿Cómo ejecutar un programa Python en Windows?

No es necesariamente una pregunta simple. Si ya está familiarizado con
el lanzamiento de programas desde la línea de comandos de Windows,
todo parecerá obvio; de lo contrario, es posible que necesite un poco
más de orientación.

A menos que esté utilizando algún tipo de entorno de desarrollo,
terminará escribiendo comandos de Windows en lo que se denomina "DOS"
o "símbolo del sistema de Windows". En general, puede abrir dicha
ventana desde su barra de búsqueda buscando *cmd*. Debería poder
reconocer cuándo inició dicha ventana porque verá un símbolo del
sistema de Windows, que en general se ve así:

   C:\>

La letra puede ser diferente y puede haber otras cosas seguidas, por
lo que también puede verse así:

   D:\YourName\Projects\Python>

dependiendo de la configuración de su computadora y de lo que haya
hecho recientemente con ella. Una vez que haya abierto esta ventana,
está en camino de iniciar los programas de Python.

Tenga en cuenta que sus scripts de Python deben ser procesados por
otro programa llamado "intérprete" de Python. El intérprete lee su
script, lo compila en *bytecode* y ejecuta el *bytecode* para ejecutar
su programa. Entonces, ¿cómo le das tu código Python al intérprete?

Primero, debe asegurarse de que la ventana del símbolo del sistema
reconoce la palabra "python" como una instrucción para iniciar el
intérprete. Si abrió un símbolo del sistema, escriba el comando "py" y
luego presione la tecla Enter:

   C:\Users\YourName> py

Debería ver algo como esto:

   Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Has comenzado el intérprete en su "modo interactivo". Esto significa
que puede ingresar declaraciones o expresiones de Python de forma
interactiva para ejecutarlas. Esta es una de las características más
poderosas de Python. Puede verificar esto ingresando algunos comandos
de su elección y ver los resultado:

   >>> print("Hello")
   Hello
   >>> "Hello" * 3
   'HelloHelloHello'

Muchas personas usan el modo interactivo como una calculadora práctica
pero altamente programable. Cuando desee finalizar su sesión
interactiva de Python, llame a la función "exit()" o mantenga
presionada la tecla "Ctrl" mientras ingresa una "Z", luego presione la
tecla ""Enter"" para regresar a su símbolo del sistema de Windows.

Es posible que haya notado una nueva entrada en su menú Inicio, como
Inicio ‣ Programas ‣ Python 3.x ‣ Python (línea de comando) que hace
que vea el mensaje ">>>" en una nueva ventana. Si es así, la ventana
desaparecerá cuando llame a la función "exit()" o presione la
combinación "Ctrl"-"Z"; Windows ejecuta un comando "python" en la
ventana y lo cierra cuando cierra el intérprete.

Ahora que sabemos que se reconoce el comando "py", puede darle su
script Python. Debe proporcionar la ruta absoluta o relativa de la
secuencia de comandos de Python. Digamos que su script Python se
encuentra en su escritorio y se llama "hello.py", y su símbolo del
sistema está abierto en su directorio de inicio, por lo que verá algo
como:

   C:\Users\YourName>

Entonces, le pedirá al comando "py" que le dé su script a Python
escribiendo "py" seguido de la ruta de su script:

   C:\Users\YourName> py Desktop\hello.py
   hello

## ¿Cómo hacer que los scripts de Python sean ejecutables?

En Windows, el instalador de Python asocia la extensión *.py* con un
tipo de archivo *(Python.File)* y un comando que inicia el intérprete
("D:\Archivos de programa\Python\python.exe "%1" %*") . Esto es
suficiente para poder ejecutar scripts de Python desde la línea de
comandos ingresando 'foo.py'. Si desea poder ejecutar los scripts
simplemente escribiendo 'foo' sin la extensión, debe agregar .py a la
variable del entorno PATHEXT.

## ¿Por qué Python tarda en comenzar?

Normalmente en Windows, Python se inicia muy rápidamente, pero a veces
los informes de error indican que Python de repente comienza a tardar
mucho tiempo en iniciarse. Es aún más desconcertante porque Python
funcionará correctamente con otros Windows configurados de manera
idéntica.

El problema puede provenir de un antivirus mal configurado. Se sabe
que algunos antivirus duplican el tiempo de arranque cuando se
configuran para verificar todas las lecturas del sistema de archivos.
Intente verificar si los antivirus de las dos máquinas están
configurados correctamente de manera idéntica. *McAfee* es
especialmente problemático cuando se configura para verificar todas
las lecturas del sistema de archivos.

## ¿Cómo hacer un ejecutable a partir de un script de Python?

Vea ¿Cómo puedo crear un binario independiente a partir de un programa
Python? para una lista de herramientas que pueden ser usadas para
crear ejecutables.

## ¿Es un archivo "*.pyd" lo mismo que una DLL?

Sí, los archivos *.pyd* son archivos dll, pero hay algunas
diferencias. Si tiene una DLL llamada "foo.pyd", debe tener una
función "PyInit_foo()". Luego puede escribir en Python "import foo" y
Python buscará el archivo *foo.pyd* (así como *foo.py* y *foo.pyc*);
si lo encuentra, intentará llamar a "PyInit_foo()" para inicializarlo.
No vincules tu .exe con *foo.lib* porque en este caso Windows
necesitará la DLL.

Tenga en cuenta que la ruta de búsqueda para *foo.pyd* es PYTHONPATH,
es diferente de la que usa Windows para buscar *foo.dll*. Además,
*foo.pyd* no necesita estar presente para que su programa se ejecute,
mientras que si ha vinculado su programa con una dll, esto es
necesario. Por supuesto, *foo.pyd* es necesario si escribes "import
foo". En una DLL, el enlace se declara en el código fuente con
"__declspec(dllexport)". En un *.pyd*, la conexión se define en una
lista de funciones disponibles.

## ¿Cómo puedo integrar Python en una aplicación de Windows?

La integración del intérprete de Python en una aplicación de Windows
se puede resumir de la siguiente manera:

1. Do **not** build Python into your .exe file directly.  On Windows,
   Python must be a DLL to handle importing modules that are
   themselves DLL's.  (This is the first key undocumented fact.)
   Instead, link to "python*NN*.dll"; it is typically installed in
   "C:\Windows\System".  *NN* is the Python version, a number such as
   "33" for Python 3.3.

   Puede vincular a Python de dos maneras diferentes. Un enlace en
   tiempo de carga significa apuntar al archivo "python*NN*.lib",
   mientras que un enlace en tiempo de ejecución significa apuntar al
   archivo "python*NN*.dll". (Nota general: el archivo
   "python*NN*.lib" es la llamada "lib de importación" correspondiente
   para el archivo "python*NN*.dll". Simplemente define enlaces
   simbólicos para el enlazador).

   El enlace en tiempo real simplifica enormemente las opciones de
   enlace; Todo sucede en el momento de la ejecución. Su código debe
   cargar el archivo "python*NN*.dll" utilizando la rutina de Windows
   "LoadLibraryEx()". El código también debe usar rutinas de acceso y
   datos en el archivo "python*NN*.dll" (es decir, las API C de
   Python) usando punteros obtenidos por la rutina de Windows
   "GetProcAddress()". Las macros pueden hacer que el uso de estos
   punteros sea transparente para cualquier código C que llame a
   rutinas en la API C de Python.

2. If you use SWIG, it is easy to create a Python "extension module"
   that will make the app's data and methods available to Python.
   SWIG will handle just about all the grungy details for you.  The
   result is C code that you link *into* your .exe file (!)  You do
   **not** have to create a DLL file, and this also simplifies
   linking.

3. *SWIG* creará una función de inicialización (función en C) cuyo
   nombre depende del nombre del complemento. Por ejemplo, si el
   nombre del módulo es leo, la función *init* se llamará *initleo()*.
   Si está utilizando clases *shadow SWIG*, como debería, la función
   *init* se llamará *initleoc()*. Esto inicializa una clase auxiliar
   invisible utilizada por la clase *shadow*.

   ¡La razón por la que puede vincular el código C en el paso 2 en su
   archivo .exe es que llamar a la función de inicialización es
   equivalente a importar el módulo a Python! (Este es el segundo
   hecho clave indocumentado).

4. En resumen, puede usar el siguiente código para inicializar el
   intérprete de Python con su complemento.

      #include <Python.h>
      ...
      Py_Initialize();  // Initialize Python.
      initmyAppc();  // Initialize (import) the helper class.
      PyRun_SimpleString("import myApp");  // Import the shadow class.

5. Hay dos problemas con la API de Python C que aparecerán si utiliza
   un compilador que no sea *MSVC*, el compilador utilizado para
   construir *pythonNN.dll*.

   Problem 1: The so-called "Very High Level" functions that take
   "FILE *" arguments will not work in a multi-compiler environment
   because each compiler's notion of a "struct FILE" will be
   different.  From an implementation standpoint these are very low
   level functions.

   Problema 2: *SWIG* genera el siguiente código al generar
   contenedores para cancelar las funciones:

      Py_INCREF(Py_None);
      _resultobj = Py_None;
      return _resultobj;

   Por desgracia, *Py_None* es una macro que se desarrolla con
   referencia a una estructura de datos compleja llamada
   *_Py_NoneStruct* dentro de *pythonNN.dll*. Nuevamente, este código
   fallará en un entorno de múltiples compiladores. Reemplace este
   código con:

      return Py_BuildValue("");

   Es posible utilizar el comando *SWIG* "%typemap" para realizar el
   cambio automáticamente, aunque no he logrado que funcione (soy un
   principiante con *SWIG*).

6. Usar una secuencia de comandos de shell Python para crear una
   ventana de intérprete de Python desde su aplicación de Windows no
   es una buena idea; la ventana resultante será independiente del
   sistema de ventanas de su aplicación. Usted (o la clase
   *wxPythonWindow*) debería crear una ventana de intérprete "nativa".
   Es fácil conectar esta ventana al intérprete de Python. Puede
   redirigir la entrada/salida de Python a cualquier objeto que admita
   lectura y escritura, por lo que todo lo que necesita es un objeto
   de Python (definido en su complemento) que contenga los métodos de
   *read()* y *write()*.

## ¿Cómo puedo evitar que mi editor inserte pestañas en mi archivo fuente de Python?

Las preguntas frecuentes no recomiendan el uso de pestañas y la guía
de estilo de Python, **PEP 8**, recomienda el uso de 4 espacios para
distribuir el código de Python. Este es también el modo predeterminado
de Emacs con Python.

Sea cual sea su editor, mezclar pestañas y espacios es una mala idea.
*MSVC* no es diferente en este aspecto, y se puede configurar
fácilmente para usar espacios: vaya a Tools ‣ Options ‣ Tabs, y para
el tipo de archivo "Default", debe establecer "Tab size" and "Indent
size" en 4, luego seleccione Insertar espacios.

Python lanzará los errores "IndentationError" o "TabError" si una
combinación de tabulación y sangría es problemática al comienzo de la
línea. También puede usar el módulo "tabnanny" para detectar estos
errores.

## ¿Cómo verifico una pulsación de tecla sin bloquearla?

Use el módulo "msvcrt". Es una extensión estándar específica de
Windows, que define una función "kbhit()" que verifica si se ha
presionado una tecla, y "getch()" que recupera el carácter sin
mostrarlo.

## ¿Cómo resuelvo el error de api-ms-win-crt-runtime-l1-1-0.dll no encontrado?

Esto puede ocurrir en Python 3.5 y posteriores usando Windows 8.1 o
anteriores sin que todas las actualizaciones hayan sido instaladas.
Primero asegúrese que su sistema operativo sea compatible y esté
actualizado, y si eso no resuelve el problema, visite la Página de
soporte de Microsoft para obtener orientación sobre como instalar
manualmente la actualización de C Runtime.
