---
title: La inicialización de la ruta de búsqueda de módulo de "sys.path"
source_url: https://docs.python.org/es/3
source_path: library/sys_path_init.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4020
---

# La inicialización de la ruta de búsqueda de módulo de "sys.path"

Una ruta de búsqueda de módulo se inicializa cuando se inicia Python.
Se puede acceder a esta ruta de búsqueda de módulo en "sys.path".

La primera entrada en la ruta de búsqueda de módulo es el directorio
que contiene el script de entrada, si lo hay. De lo contrario, la
primera entrada es el directorio actual, que es el caso cuando se
ejecuta el shell interactivo, un comando "-c" o un módulo "-m".

La variable de entorno "PYTHONPATH" se utiliza a menudo para añadir
directorios a la ruta de búsqueda. Si se encuentra esta variable de
entorno, su contenido se añade a la ruta de búsqueda del módulo.

Nota:

  "PYTHONPATH" afectará a todas las versiones/entornos de Python
  instalados. Tenga cuidado al establecer esto en su perfil de shell o
  en las variables de entorno globales. El módulo "site" ofrece
  técnicas más suavizadas como se menciona a continuación.

Los siguientes elementos que se añaden son los directorios que
contienen los módulos estándar de Python, así como los *extension
module* de los que dependen estos módulos. Los módulos de extensión
son archivos ".pyd" en Windows y archivos ".so" en otras plataformas.
El directorio con los módulos Python independientes de la plataforma
se llama "prefix". El directorio con los módulos de extensión se llama
"exec_prefix".

La variable de entorno "PYTHONHOME" puede utilizarse para establecer
las ubicaciones "prefix" y "exec_prefix". De lo contrario, estos
directorios se encuentran utilizando el ejecutable de Python como
punto de partida y luego buscando varios archivos y directorios "de
referencia". Tenga en cuenta que cualquier enlace simbólico se sigue,
por lo que la ubicación real del ejecutable de Python se utiliza como
punto de partida de la búsqueda. La ubicación del ejecutable de Python
se llama "home".

Una vez determinado "home", el directorio "prefix" se encuentra
buscando primero "python*majorversion**minorversion*.zip"
("python311.zip"). En Windows el archivo zip se busca en "home" y en
Unix se espera que el archivo esté en "lib". Tenga en cuenta que la
ubicación esperada del archivo zip se añade a la ruta de búsqueda del
módulo incluso si el archivo no existe. Si no se encuentra ningún
archivo, Python en Windows continuará la búsqueda de "prefix" buscando
en "Lib\os.py". Python en Unix buscará
"lib/python*majorversion*.*minorversion*/os.py"
("lib/python3.11/os.py"). En Windows "prefix" y "prefix_exec" son los
mismos, sin embargo en otras plataformas se busca
"lib/python*majorversion*.*minorversion*/lib-dynload" ("lib/python3.11
/lib-dynload") y se utiliza como ancla para "prefix_exec". En algunas
plataformas "lib" puede ser "lib64" u otro valor, ver "sys.platlibdir"
y "PYTHONPLATLIBDIR".

Once found, "prefix" and "exec_prefix" are available at
"sys.base_prefix" and "sys.base_exec_prefix" respectively.

If "PYTHONHOME" is not set, and a "pyvenv.cfg" file is found alongside
the main executable, or in its parent directory, "sys.prefix" and
"sys.exec_prefix" get set to the directory containing "pyvenv.cfg",
otherwise they are set to the same value as "sys.base_prefix" and
"sys.base_exec_prefix", respectively. This is used by Virtual
Environments.

Finalmente, el módulo "site" se procesa y los directorios "site-
packages" se añaden a la ruta de búsqueda de módulo. Una forma común
de personalizar la ruta de búsqueda es crear módulos "sitecustomize" o
"usercustomize" como se describe en la documentación del módulo
"site".

Nota:

  Ciertas opciones de la línea de comandos pueden afectar aún más los
  cálculos de ruta. Vea "-E", "-I", "-s" y "-S" para más detalles.

Distinto en la versión 3.14: "sys.prefix" and "sys.exec_prefix" are
now set to the "pyvenv.cfg" directory during the path initialization.
This was previously done by "site", therefore affected by "-S".

## Virtual Environments

Virtual environments place a "pyvenv.cfg" file in their prefix, which
causes "sys.prefix" and "sys.exec_prefix" to point to them, instead of
the base installation.

The "prefix" and "exec_prefix" values of the base installation are
available at "sys.base_prefix" and "sys.base_exec_prefix".

As well as being used as a marker to identify virtual environments,
"pyvenv.cfg" may also be used to configure the "site" initialization.
Please refer to "site"'s virtual environments documentation.

Nota:

  "PYTHONHOME" overrides the "pyvenv.cfg" detection.

Nota:

  There are other ways how "virtual environments" could be
  implemented, this documentation refers implementations based on the
  "pyvenv.cfg" mechanism, such as "venv". Most virtual environment
  implementations follow the model set by "venv", but there may be
  exotic implementations that diverge from it.

## Archivos _pth

Para anular completamente "sys.path" cree un archivo "._pth" con el
mismo nombre que la biblioteca compartida o el ejecutable
("python._pth" o "python311._pth"). La ruta de la biblioteca
compartida se conoce siempre en Windows, pero puede no estar
disponible en otras plataformas. En el archivo "._pth" especifique una
línea por cada ruta a añadir a "sys.path`". El archivo basado en el
nombre de la biblioteca compartida anula el basado en el ejecutable,
lo que permite restringir las rutas para cualquier programa en tiempo
de ejecución si se desea.

Cuando el archivo existe, se ignoran todas las variables de registro y
de entorno, se habilita el modo aislado y no se importa "site" a menos
que una línea del archivo especifique "import site". Las rutas en
blanco y las líneas que comienzan con "#" son ignoradas. Cada ruta
puede ser absoluta o relativa a la ubicación del fichero. No se
permiten declaraciones de importación distintas de "site", y no se
puede especificar código arbitrario.

Tenga en cuenta que los archivos ".pth" (sin guión bajo inicial) serán
procesados normalmente por el módulo "site" cuando se haya
especificado "import site".

## Python embebido

If Python is embedded within another application
"Py_InitializeFromConfig()" and the "PyConfig" structure can be used
to initialize Python. The path specific details are described at
Configuración de la ruta de Python.

Ver también:

  * Encontrar módulos para las notas detalladas de Windows.

  * Uso de Python en plataformas Unix para los detalles de Unix.
