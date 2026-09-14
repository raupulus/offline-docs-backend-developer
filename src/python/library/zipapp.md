---
title: '"zipapp" --- Manage executable Python zip archives'
source_url: https://docs.python.org/es/3
source_path: library/zipapp.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4690
---

# "zipapp" --- Manage executable Python zip archives

Added in version 3.5.

**Código fuente:** Lib/zipapp.py

======================================================================

Este módulo provee herramientas para administrar la creación de
archivos zip que contengan código Python, los que pueden ser
ejecutados directamente por el intérprete de Python. El módulo provee
tanto una Interfaz de línea de comando y una API de Python.

## Ejemplo básico

El siguiente ejemplo muestra cómo la Interfaz de línea de comando
puede utilizarse para crear un archivador ejecutable de un directorio
que contenga código en Python. Al ponerse en funcionamiento, el
archivador ejecutará la función "main" del módulo "myapp" en el
archivador.

   $ python -m zipapp myapp -m "myapp:main"
   $ python myapp.pyz
   <output from myapp>

## Interfaz de línea de comando

En la ejecución como programa desde la línea de comandos, se utiliza
el siguiente formato:

   $ python -m zipapp source [options]

Si *source* es un directorio, se creará un archivador zip para los
contenidos de *source*. Si *source* es un archivo, debería ser un
archivador, y se copiará al archivador de destino (o los contenidos de
su línea *shebang* se mostrarán si se especifica la opción --info).

Se aceptan las siguientes opciones:

-o <output>, --output=<output>

   Escribe la salida a un archivo llamado *output*. Si esta opción no
   está especificada, el nombre del archivo de salida será el mismo
   que la entrada *source*, con la extensión ".pyz" agregada. Si se
   provee de un nombre de archivo explícito, se usa tal como está (por
   lo que una extensión ".pyz" debería incluirse si esto se requiere).

   Un nombre de archivo de salida debe especificarse si *source* es un
   archivador (y en ese caso, *output* no debería ser igual que
   *source*).

-p <interpreter>, --python=<interpreter>

   Agrega una línea "#!" al archivador especificando *interpreter*
   como comando a ejecutar. También en POSIX, convierte al archivador
   en ejecutable. La opción por defecto es no escribir una línea "#!",
   y no hacer que el archivo sea ejecutable.

-m <mainfn>, --main=<mainfn>

   Escribe un archivo "__main__.py" en el archivador que ejecuta
   *mainfn*.  El argumento *mainfn* debería tener la forma
   "pkg.mod:fn", donde "pkg.mod" is un paquete/módulo en el
   archivador, y "fn" es un invocable (*callable*) en ese módulo. El
   archivo "__main__.py" ejecutará ese invocable.

   "--main" no puede especificarse al copiar un archivador.

-c, --compress

   Comprime los archivos con el método *deflate*, lo que reduce el
   tamaño del archivo de salida. Por defecto, los archivos se guardan
   sin comprimir en el archivador.

   "--compress" no surte efecto al copiar un archivador.

   Added in version 3.7.

--info

   Muestra el intérprete incrustado en el archivador, para
   diagnósticos. En este caso cualquier otra opción se ignora, y
   SOURCE debe ser un archivador, no un directorio.

-h, --help

   Muestra un breve mensaje sobre el modo de uso, y sale.

## API de Python

El módulo define dos funciones convenientes:

zipapp.create_archive(source, target=None, interpreter=None, main=None, filter=None, compressed=False)

   Crea un archivador de aplicación a partir de *source*. Este
   *source* (origen), puede ser cualquiera de los siguientes:

   * El nombre de un directorio, o un *path-like object* que se
     refiera a un directorio, en cuyo caso un nuevo archivador de
     aplicación se creará a partir del contenido de dicho directorio.

   * El nombre de un archivador de aplicación existente o un  *path-
     like object* que refiera a dicho archivo, en cuyo caso el archivo
     se copiará al destino (modificándolo para reflejar el valor dado
     por el argumento *interpreter*. El nombre de archivo debería
     incluir la extensión ".pyz", si se requiere.

   * Un objeto archivo abierto para lectura en modo bytes. El
     contenido del archivo debería ser un archivador de aplicación. Se
     infiere que el objeto archivo está posicionado al comienzo del
     archivador.

   El argumento *target* determina dónde quedará escrito el archivador
   resultante:

   * Si es el nombre de un archivo, o un *path-like object*, el
     archivador será escrito a ese archivo.

   * Si es un objeto archivo abierto, el archivador se escribirá en
     ese objeto archivo, el cual debe estar abierto para escritura en
     modo bytes.

   * Si el destino (*target*) se omite (o es "None"), el origen
     (*source*) debe ser un directorio, y el destino será un archivo
     con el mismo nombre que el origen, con la extensión ".pyz"
     añadida.

   El argumento *interpreter* especifica el nombre del intérprete
   Python con el que el archivador será ejecutado. Se escribe como una
   línea *"shebang"* al comienzo del archivador. En POSIX, el Sistema
   Operativo será quien lo interprete, y en Windows será gestionado
   por el lanzador Python. Omitir el *interpreter* tendrá como
   consecuencia que no se escribirá ninguna línea *shebang*. Si se
   especifica un intérprete y el destino (*target*) es un nombre de
   archivo, el bit de ejecución del archivo destino será activado.

   El argumento *main* especifica el nombre de un invocable
   (*callable*) que se utilizará como programa principal para el
   archivador. Solamente se puede especificar si el origen (*source*)
   es un directorio que no contiene un archivo "__main__.py". El
   argumento *main* debería tener la forma "pkg.module:callable", y el
   archivador será ejecutado importando "pkg.module" y ejecutando el
   *callable* sin argumentos. Es un error omitir *main* si el origen
   es un directorio que no contiene un archivo "__main__.py", ya que
   esto resultaría en un archivador no ejecutable.

   El argumento opcional *filter* especifica una función *callback*
   que se pasa como objeto Path, para representar el *path* (ruta) al
   archivo que se está añadiendo (ruta relativa al directorio origen,
   *source*). Debería retornar "True" si el archivo será añadido.

   El argumento opcional *compressed* determina si los archivos están
   comprimidos. Si se define como "True", los archivos en el
   archivador serán comprimidos con el método deflate.

   Si se especifica un objeto archivo  para *source* o *target*, es
   responsabilidad de quien invoca cerrarlo luego de invocar a
   create_archive.

   Al copiar un archivador existente, los objetos archivo provistos,
   solamente necesitan los métodos "read" y "readline", o bien
   "write". Al crear un archivador a partir de un directorio, si el
   destino (*target*) es un objeto archivo, éste se pasará a la clase
   "zipfile.ZipFile", y debe proveer los métodos que esa clase
   necesita.

   Distinto en la versión 3.7: Added the *filter* and *compressed*
   parameters.

zipapp.get_interpreter(archive)

   Retorna el intérprete especificado en la línea "#!" al comienzo del
   archivador. Si no hay línea "#!", retorna "None". El argumento
   *archive* (archivador), puede ser un nombre de archivo o un objeto
   tipo archivo abierto para lectura en modo bytes. Se supone que está
   al principio del archivador.

## Ejemplos

Empaqueta un directorio en un archivador, y lo ejecuta.

   $ python -m zipapp myapp
   $ python myapp.pyz
   <output from myapp>

Lo mismo puede lograrse utilizando la función "create_archive()":

   >>> import zipapp
   >>> zipapp.create_archive('myapp', 'myapp.pyz')

Para que la aplicación sea ejecutable directamente en POSIX,
especifica un intérprete.

   $ python -m zipapp myapp -p "/usr/bin/env python"
   $ ./myapp.pyz
   <output from myapp>

Para reemplazar la línea *shebang* en un archivador existente, cree un
archivador modificado, utilizando la función "create_archive()":

   >>> import zipapp
   >>> zipapp.create_archive('old_archive.pyz', 'new_archive.pyz', '/usr/bin/python3')

Para actualizar el archivo en el lugar, reemplaza en memoria
utilizando un objeto "BytesIO", y luego sobreescribe el origen
(*source*). Nótese que hay un riesgo al sobreescribir un archivo en el
lugar, ya que un error resultará en la pérdida del archivo original.
Este código no ofrece protección contra este tipo de errores, pero los
códigos de producción deberían hacerlo. Además, este método solamente
funcionará si el archivador cabe en la memoria:

   >>> import zipapp
   >>> import io
   >>> temp = io.BytesIO()
   >>> zipapp.create_archive('myapp.pyz', temp, '/usr/bin/python2')
   >>> with open('myapp.pyz', 'wb') as f:
   >>>     f.write(temp.getvalue())

## Especificar el intérprete

Nótese que si se especifica el intérprete y luego se distribuye el
archivador de aplicación, es necesario asegurarse de que el intérprete
utilizado es portable. El lanzador Python para Windows soporta las
formas más comunes de líneas "#!" POSIX, pero hay otras cuestiones a
considerar:

* Si se utiliza "/usr/bin/env python" (u otras formas del comando
  "python", como "/usr/bin/python"), es necesario considerar que los
  usuarios quizá tengan tanto Python2 como Python3 como versión por
  defecto, y el código debe escribirse bajo ambas versiones.

* Si se utiliza una versión específica, por ejemplo "/usr/bin/env
  python3", la aplicación no funcionará para los usuarios que no
  tengan esa versión.  (Esta puede ser la opción deseada si no se
  hecho el código compatible con Python 2).

* No hay manera de decir "python X.Y o posterior", así que se debe ser
  cuidadoso al utilizar una versión exacta, tal como "/usr/bin/env
  python3.4", ya que será necesario cambiar la línea *shebang* para
  usuarios de Python 3.5, por ejemplo.

Normalmente, se debería utilizar  "/usr/bin/env python2" o
"/usr/bin/env python3", según si el código está escrito para Python 2
ó 3.

## Creando aplicaciones independientes con zipapp

Using the "zipapp" module, it is possible to create self-contained
Python programs, which can be distributed to end users who only need
to have a suitable version of Python installed on their system.  The
key to doing this is to bundle all of the application's dependencies
into the archive, along with the application code.

Los pasos para crear un archivador independiente son los siguientes:

1. Crea tu aplicación en un directorio normalmente, tal que tengas una
   directorio "myapp" que contenga un archivo "__main__.py", y
   cualquier código extra de la aplicación.

2. Instala todas las dependencias de la aplicación en el directorio
   "myapp", usando pip:

      $ python -m pip install -r requirements.txt --target myapp

   (se supone que tienes los requisitos de tu proyecto en un archivo
   "requirements.txt", de lo contrario, puedes listar manualmente las
   dependencias en la línea de comandos de pip).

3. Empaqueta la aplicación utilizando:

      $ python -m zipapp -p "interpreter" myapp

Esto producirá un ejecutable independiente, que puede ser ejecutado en
cualquier máquina que disponga del intérprete apropiado. Véase
Especificar el intérprete para más detalles. Puede enviarse a los
usuarios como un solo archivo.

En Unix, el archivo "myapp.pyz" será ejecutable tal como está. Puede
ser renombrado, para quitar la extensión ".pyz" si se prefiere un
nombre de comando "simple". En Windows, el archivo "myapp.pyz[w]" es
ejecutable, ya que el intérprete Python registra las extensiones
".pyz" y "pyzw" al ser instalado.

### Advertencias

Si la aplicación depende de un paquete que incluye una extensión C,
ese paquete no puede ser ejecutado desde un archivo zip (esta es una
limitación del sistema operativo, dado que el código ejecutable debe
estar presente en el sistema de archivos para que el *loader* del SO
lo pueda cargar). En este caso, se puede excluir la dependencia del
archivo zip, y requerir que los usuarios la tengan instalada, o bien
distribuirla conjuntamente con el archivo zip, y agregar código al
"__main__.py" para que incluya el directorio que contiene el módulo
descomprimido en "sys.path". En este caso, será necesario asegurarse
de distribuir los binarios adecuados para la/s arquitectura/s a las
que esté destinada la aplicación (y potencialmente elegir la versión
correcta para agregar a "sys.path" en tiempo de ejecución, basándose
en la máquina del usuario).

## El formato de archivado Zip de aplicaciones Python

Python puede ejecutar archivadores zip que contengan un archivo
"__main__.py" desde la versión 2.6. Para que sea ejecutada por Python,
basta con que una aplicación de archivador sea un archivo zip estándar
que contenga un archivo "__main__.py", el cual será ejecutado como
punto de entrada para la aplicación. Como es usual para cualquier
script Python, el elemento padre del script (en este caso, el archivo
zip), será ubicado en "sys.path", por lo que pueden importarse otros
módulos desde el archivo zip.

El formato de archivo zip, permite que se antepongan al archivo datos
arbitrarios. El formato de aplicación zip utiliza esta capacidad para
anteponer una línea "*shebang*" POSIX estándar al archivo
("#!/ruta/al/interprete").

Formalmente, el Formato de archivado Zip de aplicaciones Python es:

1. An optional shebang line, containing the characters "b'#!'"
   followed by an interpreter name, and then a newline ("b'\n'")
   character.  The interpreter name can be anything acceptable to the
   OS "shebang" processing, or the Python launcher on Windows.  The
   interpreter should be encoded in UTF-8 on Windows, and in
   "sys.getfilesystemencoding()" on POSIX.

2. Los datos estándares de archivo zip, tal como se generan en el
   módulo "zipfile". El contenido del archivo zip *debe* incluir un
   archivo llamado "__main__.py" (que debe estar en la "raíz" del
   archivo zip, es decir, no puede estar en un subdirectorio). El los
   datos del archivo zip pueden estar comprimidos o no.

Si un archivador de aplicación tiene una línea de shebang, puede tener
el bit de ejecución activado en los sistemas POSIX, para permitir que
sea ejecutado directamente.

No se requiere que las herramientas de este módulo sean las que se
utilicen para crear archivadores de aplicación. El módulo es útil,
pero cualquier archivo que esté en el formato descripto anteriormente
es aceptable para Python, no importa cómo haya sido creado.
