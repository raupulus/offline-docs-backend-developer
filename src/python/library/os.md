---
title: '"os" --- Interfaces misceláneas del sistema operativo'
source_url: https://docs.python.org/es/3
source_path: library/os.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3390
---

# "os" --- Interfaces misceláneas del sistema operativo

**Código fuente:** Lib/os.py

======================================================================

Este módulo provee una manera versátil de usar funcionalidades
dependientes del sistema operativo. Si quieres leer o escribir un
archivo mira "open()", si quieres manipular rutas, mira el módulo
"os.path", y si quieres leer todas las líneas en todos los archivos en
la línea de comandos mira el módulo "fileinput". Para crear archivos
temporales y directorios mira el módulo "tempfile", y para el manejo
de alto nivel de archivos y directorios puedes ver el módulo "shutil".

Notas sobre la disponibilidad de estas funciones:

* El diseño de todos los módulos incorporados de Python dependientes
  del sistema operativo es tal que, mientras funcionalidad esté
  disponible, usará la misma interfaz; por ejemplo, la función
  "os.stat(path)" retorna estadísticas sobre la ruta (*path*) en el
  mismo formato (lo que sucede originalmente con la interfaz POSIX).

* Extensions peculiar to a particular operating system are also
  available through the "os" module, but using them is of course a
  threat to portability.

* Todas las funciones que aceptan rutas o nombres de archivos aceptan
  *bytes* o cadenas de texto, y el resultado es un objeto del mismo
  tipo, siempre que se retorna una ruta o un archivo.

* En VxWorks, os.popen, os.fork, os.execv y os.spawn*p* no son
  compatibles.

* On WebAssembly platforms, Android and iOS, large parts of the "os"
  module are not available or behave differently. APIs related to
  processes (e.g. "fork()", "execve()") and resources (e.g. "nice()")
  are not available. Others like "getuid()" and "getpid()" are
  emulated or stubs. WebAssembly platforms also lack support for
  signals (e.g. "kill()", "wait()").

Nota:

  Todas las funciones en este módulo lanzan "OSError" (o subclases),
  en el caso de archivos o rutas inaccesibles o inválidas, u otros
  argumentos que tienen el tipo correcto, pero que no son aceptados
  por el sistema operativo.

exception os.error

   Un alias de la excepción incorporada "OSError".

os.name

   El nombre del módulo dependiente del sistema operativo importado.
   Los siguientes nombres están registrados: "'posix'", "'nt'",
   "'java'".

   Ver también:

     "sys.platform" tiene una granularidad más fina. "os.uname()"
     proporciona información de versión dependiente del sistema.

     El módulo "platform" proporciona verificaciones detalladas de la
     identidad del sistema.

## Nombres de archivos, argumentos de la línea de comandos y variables de entorno

En Python, los nombres de archivo, los argumentos de la línea de
comandos y las variables de entorno se representan mediante el tipo de
cadena de caracteres. En algunos sistemas, es necesario decodificar
estas cadenas desde y hacia bytes antes de pasarlas al sistema
operativo. Python usa la *codificación del sistema de archivos y
manejador de errores* para realizar esta conversión (consulte
"sys.getfilesystemencoding()").

La *codificación del sistema de archivos y manejador de errores* se
configuran al inicio de Python mediante la función "PyConfig_Read()":
consulte los miembros "filesystem_encoding" y "filesystem_errors" de
"PyConfig".

Distinto en la versión 3.1: En algunos sistemas, la conversión
mediante la codificación del sistema de archivos puede fallar. En este
caso, Python utiliza surrogateescape encoding error handler, lo que
significa que los bytes no decodificables se reemplazan por un
carácter Unicode U+DC*xx* durante la decodificación y estos se
traducen nuevamente al byte original durante la codificación.

La *codificación del sistema de archivos y manejador de errores* debe
garantizar la decodificación exitosa de todos los bytes por debajo de
128. Si la codificación del sistema de archivos no proporciona esta
garantía, las funciones de API pueden generar "UnicodeError".

Consulte también la *codificación de la configuración regional*.

## Modo Python UTF-8

Added in version 3.7: Consulte **PEP 540** para obtener más detalles.

El modo Python UTF-8 ignora la *codificación de la configuración
regional* y fuerza el uso de la codificación UTF-8:

* Utilice UTF-8 como *codificación del sistema de archivos y manejador
  de errores*.

* "sys.getfilesystemencoding()" retorna "'utf-8'".

* "locale.getpreferredencoding()" retorna "'utf-8'" (el argumento
  *do_setlocale* no tiene ningún efecto).

* "sys.stdin", "sys.stdout" y "sys.stderr" usan UTF-8 como su
  codificación de texto, con "surrogateescape" error handler
  habilitado para "sys.stdin" y "sys.stdout" ("sys.stderr" continúa
  usando "backslashreplace" como lo hace en el modo predeterminado de
  reconocimiento de configuración regional)

* En Unix, "os.device_encoding()" retorna "'utf-8'". en lugar de la
  codificación del dispositivo.

Tenga en cuenta que "PYTHONIOENCODING" puede anular la configuración
de transmisión estándar en el modo UTF-8 (al igual que en el modo
predeterminado con reconocimiento de configuración regional).

Como consecuencia de los cambios en esas API de nivel inferior, otras
API de nivel superior también exhiben diferentes comportamientos
predeterminados:

* Los argumentos de la línea de comandos, las variables de entorno y
  los nombres de archivo se decodifican en texto utilizando la
  codificación UTF-8.

* "os.fsdecode()" y "os.fsencode()" utilizan la codificación UTF-8.

* "open()", "io.open()" y "codecs.open()" utilizan la codificación
  UTF-8 de forma predeterminada. Sin embargo, todavía usan el
  controlador de errores estricto de forma predeterminada, por lo que
  es probable que intentar abrir un archivo binario en modo texto
  genere una excepción en lugar de producir datos sin sentido.

El Modo Python UTF-8 se habilita si la configuración regional LC_CTYPE
es "C" o "POSIX" al iniciar Python (consulte la función
"PyConfig_Read()").

Se puede habilitar o deshabilitar usando la opción de línea de comando
"-X utf8" y la variable de entorno "PYTHONUTF8".

Si la variable de entorno "PYTHONUTF8" no está configurada en
absoluto, entonces el intérprete utiliza de forma predeterminada la
configuración regional actual, *a no ser que* la configuración
regional actual se identifica como una configuración regional heredada
basada en ASCII (como se describe para "PYTHONCOERCECLOCALE") y la
coerción de la configuración regional está deshabilitada o falla . En
tales configuraciones regionales heredadas, el intérprete habilitará
de forma predeterminada el modo UTF-8 a menos que se le indique
explícitamente que no lo haga.

El modo Python UTF-8 solo se puede habilitar al inicio de Python. Su
valor se puede leer en "sys.flags.utf8_mode".

Consulte también modo UTF-8 en Windows y *codificación del sistema de
archivos y manejador de errores*.

Ver también:

  **PEP 686**
     Python 3.15 hará que Modo Python UTF-8 sea el predeterminado.

## Parámetros de proceso

Estas funciones y elementos de datos proporcionan información y operan
en el proceso y con el usuario actuales.

os.ctermid()

   Retorna el nombre del archivo correspondiente al terminal que
   controla el proceso.

   Availability: Unix, not WASI.

os.environ

   Un objeto *mapping* donde las claves y los valores son cadenas que
   representan el entorno del proceso. Por ejemplo, "environ['HOME']"
   es el nombre de ruta de su directorio de inicio (en algunas
   plataformas) y es equivalente a "getenv("HOME")" en C.

   This mapping is captured the first time the "os" module is
   imported, typically during Python startup as part of processing
   "site.py".  Changes to the environment made after this time are not
   reflected in "os.environ", except for changes made by modifying
   "os.environ" directly.

   Este mapeo puede ser usado para modificar el entorno y también para
   consultarlo. "putenv()" será llamado automáticamente cuando el
   mapeo sea modificado.

   En Unix, claves y valores usan la función
   "sys.getfilesystemencoding()" y  el controlador de errores
   "'surrogateescape'". Hay que utilizar "environb" si se quiere usar
   una codificación diferente.

   En Windows, las claves se convierten a mayúsculas. Esto también se
   aplica al obtener, configurar o eliminar un elemento. Por ejemplo,
   "environ['monty'] = 'python'" asigna a la clave "'MONTY'" el valor
   "'python'".

   Nota:

     Llamar a "putenv()" directamente no cambia "os.environ", por lo
     que es mejor modificar "os.environ".

   Nota:

     En algunas plataformas, incluidas FreeBSD y macOS, configurar
     "environ" puede provocar pérdidas de memoria. Consulte la
     documentación del sistema para "putenv()".

   Puede eliminar elementos en esta asignación para desactivar las
   variables de entorno. "unsetenv()" se llamará automáticamente
   cuando se elimine un elemento de "os.environ" y cuando se llame a
   uno de los métodos "pop()" o "clear()".

   Ver también: The "os.reload_environ()" function.

   Distinto en la versión 3.9: Actualizado para soportar los
   operadores merge ("|") y update ("|=") de **PEP 584**'s.

os.environb

   Versión de bytes de "environ": un objeto *mapping* donde tanto las
   claves como los valores son objetos "bytes" que representan el
   entorno del proceso. "environ" y "environb" están sincronizados
   (modificando "environb" actualiza "environ", y viceversa).

   "environb" está disponible sólo si "supports_bytes_environ" está
   establecido en "True".

   Added in version 3.2.

   Distinto en la versión 3.9: Actualizado para soportar los
   operadores merge ("|") y update ("|=") de **PEP 584**'s.

os.reload_environ()

   The "os.environ" and "os.environb" mappings are a cache of
   environment variables at the time that Python started. As such,
   changes to the current process environment are not reflected if
   made outside Python, or by "os.putenv()" or "os.unsetenv()". Use
   "os.reload_environ()" to update "os.environ" and "os.environb" with
   any such changes to the current process environment.

   Advertencia:

     This function is not thread-safe. Calling it while the
     environment is being modified in another thread is an undefined
     behavior. Reading from "os.environ" or "os.environb", or calling
     "os.getenv()" while reloading, may return an empty result.

   Added in version 3.14.

os.chdir(path)
os.fchdir(fd)
os.getcwd()

   Estas funciones están detalladas en Archivos y directorios.

os.fsencode(filename)

   Codifique *path-like* *filename* en *filesystem encoding and error
   handler*; retorna "bytes" sin cambios.

   "fsdecode()" es la función inversa.

   Added in version 3.2.

   Distinto en la versión 3.6: Soporte agregado para aceptar objetos
   que implementan una interfaz "os.PathLike".

os.fsdecode(filename)

   Decodifica el *path-like* *filename* del *filesystem encoding and
   error handler*; retorna "str" sin cambios.

   "fsencode()" es la función inversa.

   Added in version 3.2.

   Distinto en la versión 3.6: Soporte agregado para aceptar objetos
   que implementan una interfaz "os.PathLike".

os.fspath(path)

   Retorna la representación en el sistema de archivos de la ruta.

   Si se le pasa "str" o "bytes", retorna sin alterar. De lo contrario
   se llama a "__fspath__()" y se retorna su valor siempre que sea un
   objeto "str" o "bytes". En los demás casos se lanza una excepción
   del tipo "TypeError".

   Added in version 3.6.

class os.PathLike

   Una *clase base abstracta* para objetos que representan una ruta
   del sistema de archivos, i.e. "pathlib.PurePath".

   Added in version 3.6.

   abstractmethod __fspath__()

      Retorna la representación de la ruta del sistema de archivos del
      objeto.

      Este método sólo retornará objetos "str" or "bytes",
      preferentemente "str".

os.getenv(key, default=None)

   Devuelve el valor de la variable de entorno *key* como una cadena
   si existe, o *default* si no existe. *key* es una cadena. Tenga en
   cuenta que dado que "getenv()" usa "os.environ", la asignación de
   "getenv()" también se captura de manera similar en la importación,
   y es posible que la función no refleje futuros cambios en el
   entorno.

   En Unix, claves y valores se decodifican con la función
   "sys.getfilesystemencoding()" y con el controlador de errores
   "'surrogateescape'". Usar "os.getenvb()" si se quiere usar una
   codificación diferente.

   Availability: Unix, Windows.

os.getenvb(key, default=None)

   Devuelve el valor de la variable de entorno *key* como bytes si
   existe, o *default* si no existe. *key* debe ser bytes. Tenga en
   cuenta que dado que "getenvb()" usa "os.environb", la asignación de
   "getenvb()" también se captura de manera similar en la importación,
   y es posible que la función no refleje futuros cambios en el
   entorno.

   "getenvb()" está disponible sólo si "supports_bytes_environ" está
   establecido en "True".

   Availability: Unix.

   Added in version 3.2.

os.get_exec_path(env=None)

   Retorna una lista de directorios en la que se buscará un
   ejecutable, similar a una *shell*, cuando se ejecuta un proceso.
   *env*, cuando se especifica, tienen que ser un diccionario de
   variables de entorno donde buscar el *PATH*. Por defecto cuando
   *env* es "None", se usa "environ".

   Added in version 3.2.

os.getegid()

   Retorna el *id* del grupo (*gid*) efectivo correspondiente al
   proceso que se está ejecutando. Esto corresponde al bit de *"set
   id"* en el archivo que se está ejecutando en el proceso actual.

   Availability: Unix, not WASI.

os.geteuid()

   Retorna el id el usuario correspondiente al proceso que se está
   ejecutando actualmente.

   Availability: Unix, not WASI.

os.getgid()

   Retorna el id del grupo real correspondiente al proceso que se está
   ejecutando actualmente.

   Availability: Unix.

   La función es un "stub" de WASI, consulte Plataformas WebAssembly
   para obtener más información.

os.getgrouplist(user, group, /)

   Devuelve la lista de ID de grupo a los que pertenece *user*. Si
   *group* no está en la lista, se incluye; normalmente, *group* se
   especifica como el campo de ID de grupo del registro de contraseña
   para *user*, porque de lo contrario, esa ID de grupo podría
   omitirse.

   Availability: Unix, not WASI.

   Added in version 3.3.

os.getgroups()

   Retorna la lista de *ids* de grupos secundarios asociados con el
   proceso actual.

   Availability: Unix, not WASI.

   Nota:

     En macOS, el comportamiento de "getgroups()" difiere un poco del
     de otras plataformas Unix. Si el intérprete de Python se creó con
     un objetivo de implementación "10.5" o anterior, "getgroups()"
     devuelve la lista de identificadores de grupo efectivos asociados
     con el proceso de usuario actual; esta lista está limitada a una
     cantidad de entradas definida por el sistema, normalmente 16, y
     puede modificarse mediante llamadas a "setgroups()" si se cuenta
     con los privilegios adecuados. Si se creó con un objetivo de
     implementación mayor que "10.5", "getgroups()" devuelve la lista
     de acceso de grupo actual para el usuario asociado con el
     identificador de usuario efectivo del proceso; la lista de acceso
     de grupo puede cambiar durante la vida útil del proceso, no se ve
     afectada por las llamadas a "setgroups()" y su longitud no está
     limitada a 16. El valor del objetivo de implementación,
     "MACOSX_DEPLOYMENT_TARGET", se puede obtener con
     "sysconfig.get_config_var()".

os.getlogin()

   Retorna el nombre del usuario que inició sesión en el terminal que
   controla el proceso. Para la mayoría de los casos, es más útil usar
   "getpass.getuser()" ya que este último verifica las variables de
   entorno "LOGNAME" o "USERNAME" para averiguar quién es el usuario y
   recurre a "pwd.getpwuid(os.getuid())[0]" para obtener el nombre de
   inicio de sesión del ID de usuario real actual.

   Availability: Unix, Windows, not WASI.

os.getpgid(pid)

   Retorna el id del grupo de procesos del proceso con la
   identificación del proceso *pid*. Si *pid* es 0, se retorna la
   identificación del grupo de proceso del proceso actual.

   Availability: Unix, not WASI.

os.getpgrp()

   Retorna el *id* del grupo de proceso actual.

   Availability: Unix, not WASI.

os.getpid()

   Retorna el *id* del proceso actual.

   La función es un "stub" de WASI, consulte Plataformas WebAssembly
   para obtener más información.

os.getppid()

   Retorna el *id* del proceso del padre. Cuando el proceso padre ha
   terminado, en Unix la identificación que retorna es la del proceso
   *init* (1), en Windows sigue siendo la misma identificación, que ya
   puede ser reutilizada por otro proceso.

   Availability: Unix, Windows, not WASI.

   Distinto en la versión 3.2: Se agregó soporte para Windows.

os.getpriority(which, who)

   Obtenga la prioridad del programa. El valor *which* es uno de
   "PRIO_PROCESS", "PRIO_PGRP", o "PRIO_USER", y *who* se interpreta
   en relación a *which* (un identificador de proceso para
   "PRIO_PROCESS", un identificador de grupo de proceso para
   "PRIO_PGRP", y un ID de usuario para "PRIO_USER"). Un valor cero
   para *who* denota (respectivamente) el proceso llamado, el grupo de
   proceso del proceso llamado o el ID de usuario real del proceso
   llamado.

   Availability: Unix, not WASI.

   Added in version 3.3.

os.PRIO_PROCESS
os.PRIO_PGRP
os.PRIO_USER

   Parámetros para las funciones "getpriority()" y "setpriority()".

   Availability: Unix, not WASI.

   Added in version 3.3.

os.PRIO_DARWIN_THREAD
os.PRIO_DARWIN_PROCESS
os.PRIO_DARWIN_BG
os.PRIO_DARWIN_NONUI

   Parámetros para las funciones "getpriority()" y "setpriority()".

   Availability: macOS

   Added in version 3.12.

os.getresuid()

   Retorna una tupla (ruid, euid, suid) que denota los ID de usuario
   reales, efectivos y guardados del proceso actual.

   Availability: Unix, not WASI, not macOS, not iOS.

   Added in version 3.2.

os.getresgid()

   Retorna una tupla (rgid, egid, sgid) que denota los ID de grupo
   reales, efectivos y guardados del proceso actual.

   Availability: Unix, not WASI, not macOS, not iOS.

   Added in version 3.2.

os.getuid()

   Retorna el *id* del usuario real del proceso actual.

   Availability: Unix.

   La función es un "stub" de WASI, consulte Plataformas WebAssembly
   para obtener más información.

os.initgroups(username, gid, /)

   Call the system "initgroups()" to initialize the group access list
   with all of the groups of which the specified username is a member,
   plus the specified group id.

   Availability: Unix, not WASI, not Android.

   Added in version 3.2.

os.putenv(key, value, /)

   Establece la variable de entorno llamada *key* con el valor de la
   cadena *value*. Dichos cambios en el entorno impactan a los
   subprocesos iniciados con "os.system()", "popen()" o "fork()" y
   "execv()".

   Las asignaciones a elementos en "os.environ" se traducen
   automáticamente en llamadas correspondientes a "putenv()"; sin
   embargo, las llamadas a "putenv()" no actualizan "os.environ", por
   lo que en realidad es preferible asignar elementos de "os.environ".
   Esto también se aplica a "getenv()" y "getenvb()", que utilizan
   respectivamente "os.environ" y "os.environb" en sus
   implementaciones.

   See also the "os.reload_environ()" function.

   Nota:

     En algunas plataformas, incluidas FreeBSD y macOS, la
     configuración de "environ" puede provocar pérdidas de memoria.
     Consulta la documentación del sistema para obtener información
     sobre "putenv()".

   Lanza un evento de auditoría "os.putenv" con argumentos "key",
   "value".

   Distinto en la versión 3.9: Esta función actualmente siempre esta
   disponible.

os.setegid(egid, /)

   Establece el *id* de grupo efectivo del proceso actual.

   Availability: Unix, not WASI, not Android.

os.seteuid(euid, /)

   Establece el *id* de usuario efectivo del proceso actual.

   Availability: Unix, not WASI, not Android.

os.setgid(gid, /)

   Establece el *id* de grupo del proceso actual.

   Availability: Unix, not WASI, not Android.

os.setgroups(groups, /)

   Establece la lista de *ids* de grupos secundarios asociados con el
   proceso actual en *groups*. *groups* debe ser una secuencia y cada
   elemento debe ser un número entero que identifique un grupo. Esta
   operación generalmente está disponible sólo para el superusuario.

   Availability: Unix, not WASI.

   Nota:

     En macOS, la longitud de *groups* no puede exceder el número
     máximo definido por el sistema de ID de grupo efectivos, por lo
     general 16. Consulte la documentación de "getgroups()" para ver
     los casos en los que puede no retornar la misma lista de grupos
     establecida llamando a setgroups().

os.setns(fd, nstype=0)

   Reasociar el hilo actual con un espacio de nombres de Linux.
   Consulta las páginas del manual *setns(2)* y *namespaces(7)* para
   obtener más detalles.

   Si *fd* hace referencia a un enlace "/proc/*pid*/ns/", "setns()"
   reasocia el hilo que llama con el espacio de nombres asociado con
   ese enlace, y *nstype* puede configurarse en uno de los CLONE_NEW*
   constants para imponer restricciones a la operación ("0" significa
   sin restricciones).

   Desde Linux 5.8, *fd* puede hacer referencia a un descriptor de
   archivo PID obtenido de "pidfd_open()". En este caso, "setns()"
   reasocia el subproceso que realiza la llamada en uno o más de los
   mismos espacios de nombres que el subproceso al que hace referencia
   *fd*. Esto está sujeto a las restricciones impuestas por *nstype*,
   que es una máscara de bits que combina uno o más de los CLONE_NEW*
   constants, por ejemplo, "setns(fd, os.CLONE_NEWUTS |
   os.CLONE_NEWPID)". Las pertenencias del autor de la llamada a
   espacios de nombres no especificados no se modifican.

   *fd* puede ser cualquier objeto con un método "fileno()" o un
   descriptor de archivo sin formato.

   Este ejemplo reasocia el hilo con el espacio de nombres de red del
   proceso "init":

      fd = os.open("/proc/1/ns/net", os.O_RDONLY)
      os.setns(fd, os.CLONE_NEWNET)
      os.close(fd)

   Availability: Linux >= 3.0 with glibc >= 2.14.

   Added in version 3.12.

   Ver también: La función "unshare()".

os.setpgrp()

   Llama a la llamada del sistema "setpgrp()" o "setpgrp(0, 0)" según
   la versión implementada (si hay alguna). Consulte el manual de Unix
   para conocer la semántica.

   Availability: Unix, not WASI.

os.setpgid(pid, pgrp, /)

   Llama a la llamada del sistema "setpgid()" para establecer el ID
   del grupo de procesos del proceso con el ID *pid* en el grupo de
   procesos con el ID *pgrp*. Consulte el manual de Unix para conocer
   la semántica.

   Availability: Unix, not WASI.

os.setpriority(which, who, priority)

   Establecer la prioridad del programa. El valor *which* es uno de
   "PRIO_PROCESS", "PRIO_PGRP", o "PRIO_USER", y *who* se interpreta
   en relación con *which* (un identificador de proceso para
   "PRIO_PROCESS", un identificador de grupo de proceso para
   "PRIO_PGRP", y un ID de usuario para "PRIO_USER"). Un valor cero
   para *who* denota (respectivamente) el proceso llamado, el grupo de
   procesos del proceso llamado o el ID del usuario real del proceso
   llamado. *priority* es un valor en el rango de -20 a 19. La
   prioridad predeterminada es 0; las prioridades más bajas causan una
   programación más favorable.

   Availability: Unix, not WASI.

   Added in version 3.3.

os.setregid(rgid, egid, /)

   Establece los *ids* de grupos reales y efectivos del proceso
   actual.

   Availability: Unix, not WASI, not Android.

os.setresgid(rgid, egid, sgid, /)

   Establece los *ids* de grupo reales, efectivos y guardados del
   proceso actual.

   Availability: Unix, not WASI, not Android, not macOS, not iOS.

   Added in version 3.2.

os.setresuid(ruid, euid, suid, /)

   Establece los *ids* de usuario reales, efectivos y guardados del
   proceso actual.

   Availability: Unix, not WASI, not Android, not macOS, not iOS.

   Added in version 3.2.

os.setreuid(ruid, euid, /)

   Establece los *ids* de usuario reales y efectivos del proceso
   actual.

   Availability: Unix, not WASI, not Android.

os.getsid(pid, /)

   Llamar a la llamada del sistema "getsid()". Consultar el manual de
   Unix para conocer la semántica.

   Availability: Unix, not WASI.

os.setsid()

   Llamar a la llamada del sistema "setsid()". Consultar el manual de
   Unix para conocer la semántica.

   Availability: Unix, not WASI.

os.setuid(uid, /)

   Establece *id* del usuario del proceso actual.

   Availability: Unix, not WASI, not Android.

os.strerror(code, /)

   Devuelve el mensaje de error correspondiente al código de error en
   *code*. En las plataformas donde "strerror()" devuelve "NULL"
   cuando se le asigna un número de error desconocido, se genera
   "ValueError".

os.supports_bytes_environ

   "True" si el tipo de entorno nativo del sistema operativo es bytes
   (por ejemplo, "False" en Windows).

   Added in version 3.2.

os.umask(mask, /)

   Establece la *umask* numérica actual y retorna la *umask* anterior.

   La función es un "stub" de WASI, consulte Plataformas WebAssembly
   para obtener más información.

os.uname()

   Returns information identifying the current operating system. The
   return value is a "uname_result".

   On macOS, iOS and Android, this returns the *kernel* name and
   release (i.e., "'Darwin'" on macOS and iOS; "'Linux'" on Android).
   "platform.uname()" can be used to get the user-facing operating
   system name and release on iOS and Android.

   Ver también:

     "sys.platform" which has finer granularity.

     El módulo "platform" proporciona verificaciones detalladas de la
     identidad del sistema.

   Availability: Unix.

   Distinto en la versión 3.3: El tipo de objeto retornado cambió de
   una tupla a un objeto tipo tupla con atributos con nombre.

class os.uname_result

   Name and information about the system returned by "os.uname()".
   These attributes correspond to the members described in *uname(2)*.

   For backwards compatibility, this object is also iterable, behaving
   like a five-tuple containing "sysname", "nodename", "release",
   "version", and "machine" in that order.

   sysname

      Operating system name.

   nodename

      Name of machine on network. Some systems truncate "nodename" to
      8 characters or to the leading component; a better way to get
      the hostname is "socket.gethostname()" or even
      "socket.gethostbyaddr(socket.gethostname())".

   release

      Operating system release.

   version

      Operating system version.

   machine

      Hardware identifier.

os.unsetenv(key, /)

   Desestablece (elimine) la variable de entorno llamada *key*. Dichos
   cambios en el entorno afectan a los subprocesos iniciados con
   "os.system()", "popen()" o "fork()" y "execv()".

   La eliminación de elementos en "os.environ" se traduce
   automáticamente en una llamada correspondiente a "unsetenv()"; sin
   embargo, las llamadas a "unsetenv()" no actualizan "os.environ",
   por lo que en realidad es preferible eliminar elementos de
   "os.environ".

   See also the "os.reload_environ()" function.

   Lanza un evento de auditoría "os.unsetenv" con argumento "key".

   Distinto en la versión 3.9: Estas funciones se encuentra ahora
   siempre disponible y también esta disponible en Windows.

os.unshare(flags)

   Desasociar partes del contexto de ejecución del proceso y moverlas
   a un nuevo espacio de nombres creado. Consulte la página del manual
   *unshare(2)* para obtener más detalles. El argumento *flags* es una
   máscara de bits que combina cero o más de los CLONE_* constants y
   que especifica qué partes del contexto de ejecución deben dejar de
   compartirse de sus asociaciones existentes y moverse a un nuevo
   espacio de nombres. Si el argumento *flags* es "0", no se realizan
   cambios en el contexto de ejecución del proceso que realiza la
   llamada.

   Availability: Linux >= 2.6.16.

   Added in version 3.12.

   Ver también: La función "setns()".

Indicadores de la función "unshare()", si la implementación los
admite. Consulte *unshare(2)* en el manual de Linux para conocer su
efecto exacto y su disponibilidad.

os.CLONE_FILES
os.CLONE_FS
os.CLONE_NEWCGROUP
os.CLONE_NEWIPC
os.CLONE_NEWNET
os.CLONE_NEWNS
os.CLONE_NEWPID
os.CLONE_NEWTIME
os.CLONE_NEWUSER
os.CLONE_NEWUTS
os.CLONE_SIGHAND
os.CLONE_SYSVSEM
os.CLONE_THREAD
os.CLONE_VM

## Creación de objetos de tipo archivo

Estas funciones crean nuevos *objetos de archivo*. (Consulte también
"open()" para abrir los descriptores de archivos).

os.fdopen(fd, *args, **kwargs)

   Retorna un objeto de archivo abierto conectado al descriptor de
   archivo *fd*. Este es un alias de la función incorporada "open()" y
   acepta los mismos argumentos. La única diferencia es que el primer
   argumento de "fdopen()" siempre debe ser un número entero.

## Operaciones de descriptores de archivos

Estas funciones operan en flujos de E/S a los que se hace referencia
mediante descriptores de archivo.

Los descriptores de archivo son enteros pequeños que corresponden a un
archivo que ha sido abierto por el proceso actual. Por ejemplo, la
entrada estándar suele ser el descriptor de archivo 0, la salida
estándar es el 1 y el error estándar es el 2. A los archivos abiertos
por un proceso se les asignará 3, 4, 5, y así sucesivamente. El nombre
"descriptor de archivo" es ligeramente engañoso; en las plataformas
Unix, los descriptores de archivo también hacen referencia a *sockets*
y tuberías.

El método "fileno()" se puede utilizar para obtener el descriptor de
archivo asociado con un *file object* cuando sea necesario. Tenga en
cuenta que el uso del descriptor de archivo directamente omitirá los
métodos de objeto de archivo, ignorando aspectos como el
almacenamiento interno interno de datos.

os.close(fd)

   Cierra el descriptor de archivo *fd*.

   Nota:

     Esta función está diseñada para E/S de bajo nivel y debe
     aplicarse a un descriptor de archivo tal como lo retorna
     "os.open()" o "pipe()". Para cerrar un "objeto de archivo"
     retornado por la función incorporada "open()" o por "popen()" o
     "fdopen()", use el método "close()".

os.closerange(fd_low, fd_high, /)

   Cierra todos los descriptores de archivo desde *fd_low* (inclusive)
   hasta *fd_high* (exclusivo), ignorando los errores. Equivalente a
   (pero mucho más rápido que):

      for fd in range(fd_low, fd_high):
          try:
              os.close(fd)
          except OSError:
              pass

os.copy_file_range(src, dst, count, offset_src=None, offset_dst=None)

   Copiar bytes *count* desde el descriptor de archivo *src*,
   comenzando desde el desplazamiento *offset_src*, al descriptor de
   archivo *dst*, comenzando desde el desplazamiento *offset_dst*. Si
   *offset_src* es "None", entonces *src* se lee desde la posición
   actual; respectivamente para *offset_dst*.

   En un kernel de Linux anterior a 5.3, los archivos a los que
   apuntan *src* y *dst* deben residir en el mismo sistema de
   archivos; de lo contrario, se genera un "OSError" con "errno"
   establecido en "errno.EXDEV".

   Esta copia se realiza sin el costo adicional de transferir datos
   desde el núcleo al espacio de usuario y luego de vuelta al núcleo.
   Además, algunos sistemas de archivos podrían implementar
   optimizaciones adicionales, como el uso de enlaces de referencia
   (es decir, dos o más inodos que comparten punteros a los mismos
   bloques de disco de copia en escritura; los sistemas de archivos
   compatibles incluyen btrfs y XFS) y copia del lado del servidor (en
   el caso de NFS).

   La función copia bytes entre dos descriptores de archivo. Las
   opciones de texto, como la codificación y el final de línea, se
   ignoran.

   El valor de retorno es la cantidad de bytes copiados. Esto podría
   ser menor que la cantidad solicitada.

   Nota:

     En Linux, no se debe utilizar "os.copy_file_range()" para copiar
     un rango de un pseudoarchivo desde un sistema de archivos
     especial como procfs y sysfs. Siempre no copiará ningún byte y
     devolverá 0 como si el archivo estuviera vacío debido a un
     problema conocido del kernel de Linux.

   Availability: Linux >= 4.5 with glibc >= 2.27.

   Added in version 3.8.

os.device_encoding(fd)

   Retorna una cadena que describe la codificación del dispositivo
   asociado con *fd* si está conectado a una terminal; sino retorna
   "None".

   En Unix, si el Modo Python UTF-8 está habilitado, retorna "'UTF-8'"
   en lugar de la codificación del dispositivo.

   Distinto en la versión 3.10: En Unix, la función ahora implementa
   el modo Python UTF-8.

os.dup(fd, /)

   Retorna un duplicado del descriptor de archivo *fd*. El nuevo
   descriptor de archivo es no heredable.

   En Windows, al duplicar un flujo estándar (0: stdin, 1: stdout, 2:
   stderr), el nuevo descriptor de archivo es heredable.

   Availability: not WASI.

   Distinto en la versión 3.4: El nuevo descriptor de archivo ahora es
   no heredable.

os.dup2(fd, fd2, inheritable=True)

   Duplicar el descriptor de archivo *fd* a *fd2*, cerrando el
   anterior si es necesario. Retorna *fd2*. El nuevo descriptor de
   archivo es heredable por defecto o no heredable si *inheritable* es
   "False".

   Availability: not WASI.

   Distinto en la versión 3.4: Agrega el parámetro opcional
   *inheritable*.

   Distinto en la versión 3.7: Retorna *fd2* en caso de éxito.
   Anteriormente se retornaba siempre "None".

os.fchmod(fd, mode)

   Cambia el modo del archivo dado por *fd* al modo numérico *mode*.
   Consulte los documentos para "chmod()" para conocer los posibles
   valores de *mode*. A partir de Python 3.3, esto es equivalente a
   "os.chmod(fd, mode)".

   Lanza un evento de auditoría "os.chmod" con argumentos "path",
   "mode", "dir_fd".

   Availability: Unix, Windows.

   La función está limitada en WASI, consulte Plataformas WebAssembly
   para obtener más información.

   Distinto en la versión 3.13: Se agregó soporte en Windows.

os.fchown(fd, uid, gid)

   Cambia el propietario y el *id* del grupo del archivo proporcionado
   por *fd* a los numéricos dados por *uid* y *gid*. Para dejar uno de
   los identificadores sin cambios, configúrelo en -1. Ver "chown()".
   A partir de Python 3.3, esto es equivalente a "os.chown(fd, uid,
   gid)".

   Lanza un evento de auditoría "os.chown" con argumentos "path",
   "uid", "gid", "dir_fd".

   Availability: Unix.

   La función está limitada en WASI, consulte Plataformas WebAssembly
   para obtener más información.

os.fdatasync(fd)

   Fuerza la escritura del archivo con el descriptor de archivo *fd*
   en el disco. No fuerza la actualización de metadatos.

   Availability: Unix, not macOS, not iOS.

os.fpathconf(fd, name, /)

   Retorna la información de configuración del sistema relevante para
   un archivo abierto. *name* especifica el valor de configuración
   para recuperar; puede ser una cadena que es el nombre de un valor
   de sistema definido; estos nombres se especifican en varios
   estándares (POSIX.1, Unix 95, Unix 98 y otros). Algunas plataformas
   también definen nombres adicionales. Los nombres conocidos por el
   sistema operativo anfitrión se dan en el diccionario
   "pathconf_names". Para las variables de configuración no incluidas
   en esa asignación, también se acepta pasar un número entero para
   *name*.

   Si *name* es una cadena y no se conoce, se lanza un "ValueError".
   Si el sistema anfitrión no admite un valor específico para *name*,
   incluso si está incluido en "pathconf_names", se genera un
   "OSError" con "errno.EINVAL" para el número de error.

   A partir de Python 3.3, esto es equivalente a "os.pathconf(fd,
   name)".

   Availability: Unix.

os.fstat(fd)

   Obtiene el estado del descriptor de archivo *fd*. Retorna un objeto
   "stat_result".

   A partir de Python 3.3, esto es equivalente a "os.stat(fd)".

   Ver también: La función "stat()".

os.fstatvfs(fd, /)

   Return information about the filesystem containing the file
   associated with file descriptor *fd* in a "statvfs_result", like
   "statvfs()". As of Python 3.3, this is equivalent to
   "os.statvfs(fd)".

   Availability: Unix.

os.fsync(fd)

   Fuerza la escritura de un archivo con el descriptor de archivo *fd*
   en el disco. En Unix, esto llama a la función "fsync()" nativa; en
   Windows, a la función "_commit()" de MS.

   Si está comenzando con un Python almacenado en búfer *file object*
   *f*, primero haga "f.flush()", y luego haga "os.fsync(f.fileno())",
   para garantizar que todas las memorias intermedias internas
   asociadas con *f* se escriban en disco.

   Availability: Unix, Windows.

os.ftruncate(fd, length, /)

   Trunca el archivo correspondiente al descriptor de archivo *fd*,
   para que tenga como máximo *length* bytes de tamaño. A partir de
   Python 3.3, esto es equivalente a "os.truncate(fd, length)".

   Lanza un evento de auditoría "os.truncate" con argumentos "fd",
   "length".

   Availability: Unix, Windows.

   Distinto en la versión 3.5: Se agregó soporte para Windows

os.get_blocking(fd, /)

   Obtiene el modo de bloqueo del descriptor de archivo: "False" si se
   establece el indicador "O_NONBLOCK", "True" si el indicador se
   borra.

   Consulte también "set_blocking()" y "socket.socket.setblocking()".

   Availability: Unix, Windows.

   La función está limitada en WASI, consulte Plataformas WebAssembly
   para obtener más información.

   En Windows, esta función está limitada a las tuberías.

   Added in version 3.5.

   Distinto en la versión 3.12: Se agregó soporte para pipes en
   Windows.

os.grantpt(fd, /)

   Otorgar acceso al dispositivo pseudoterminal esclavo asociado con
   el dispositivo pseudoterminal maestro al que hace referencia el
   descriptor de archivo *fd*. El descriptor de archivo *fd* no se
   cierra en caso de falla.

   Llama a la función de la biblioteca estándar C "grantpt()".

   Availability: Unix, not WASI.

   Added in version 3.13.

os.isatty(fd, /)

   Retorna "True" si el descriptor de archivo *fd* está abierto y
   conectado a un dispositivo tipo tty, de lo contrario, "False".

os.lockf(fd, cmd, len, /)

   Aplique, pruebe o elimine un bloqueo POSIX en un descriptor de
   archivo abierto. *fd* es un descriptor de archivo abierto. *cmd*
   especifica el comando a usar - uno de "F_LOCK", "F_TLOCK",
   "F_ULOCK" o "F_TEST". *len* especifica la sección del archivo a
   bloquear.

   Lanza un evento de auditoría "os.lockf" con argumentos "fd", "cmd",
   "len".

   Availability: Unix.

   Added in version 3.3.

os.F_LOCK
os.F_TLOCK
os.F_ULOCK
os.F_TEST

   Indicadores que especifican qué acción tomará "lockf()".

   Availability: Unix.

   Added in version 3.3.

os.login_tty(fd, /)

   Prepare el tty del cual fd es un descriptor de archivo para una
   nueva sesión de inicio de sesión. Convierta el proceso de
   convocatoria en un líder de sesión; hacer que el tty sea el tty
   controlador, el stdin, el stdout y el stderr del proceso de
   llamada; cerrar fd.

   Availability: Unix, not WASI.

   Added in version 3.11.

os.lseek(fd, pos, whence, /)

   Establece la posición actual del descriptor de archivo *fd* en la
   posición *pos*, modificada por *whence*, y devuelve la nueva
   posición en bytes con respecto al inicio del archivo. Los valores
   válidos para *whence* son:

   * "SEEK_SET" o "0": establece *pos* en relación con el comienzo del
     archivo

   * "SEEK_CUR" o "1": establece *pos* en relación con la posición
     actual del archivo

   * "SEEK_END" o "2": establece *pos* en relación con el final del
     archivo

   * "SEEK_HOLE": establece *pos* en la siguiente ubicación de datos,
     relativa a *pos*

   * "SEEK_DATA": establece *pos* en el siguiente agujero de datos,
     relativo a *pos*

   Distinto en la versión 3.3: Añadir soporte para "SEEK_HOLE" y
   "SEEK_DATA".

os.SEEK_SET
os.SEEK_CUR
os.SEEK_END

   Parámetros de la función "lseek()" y del método "seek()" en *file-
   like objects*, para desde donde ajustar el indicador de posición
   del archivo.

   "SEEK_SET"
      Ajuste la posición del archivo en relación con el comienzo del
      archivo.

   "SEEK_CUR"
      Ajuste la posición del archivo en relación con la posición del
      archivo actual.

   "SEEK_END"
      Ajuste la posición del archivo en relación con el final del
      archivo.

   Sus valores son 0, 1 y 2, respectivamente.

os.SEEK_HOLE
os.SEEK_DATA

   Parámetros de la función "lseek()" y del método "seek()" en *file-
   like objects*, para buscar datos de archivos y agujeros en archivos
   escasamente asignados.

   "SEEK_DATA"
      Ajuste el desplazamiento del archivo a la siguiente ubicación
      que contenga datos, en relación con la posición de búsqueda.

   "SEEK_HOLE"
      Ajuste el desplazamiento del archivo a la siguiente ubicación
      que contenga un agujero, en relación con la posición de
      búsqueda. Un agujero se define como una secuencia de ceros.

   Nota:

     Estas operaciones sólo tienen sentido para los sistemas de
     archivos que las admiten.

   Availability: Linux >= 3.1, macOS, Unix

   Added in version 3.3.

os.open(path, flags, mode=0o777, *, dir_fd=None)

   Abre el archivo *path* y configura varios indicadores según *flags*
   y su modo según *mode*. Al calcular el modo el valor actual de
   *umask* se enmascara primero. Retorna el descriptor de archivo para
   el archivo recién abierto. El nuevo descriptor de archivo es no
   heredable.

   For a description of the flag and mode values, see the C run-time
   documentation; flag constants (like "O_RDONLY" and "O_WRONLY") are
   defined in the "os" module.  In particular, on Windows adding
   "O_BINARY" is needed to open files in binary mode.

   Esta función puede admitir rutas relativas a descriptores de
   directorio con el parámetro *dir_fd*.

   Lanza un evento de auditoría "open" con argumentos "path", "mode",
   "flags".

   Distinto en la versión 3.4: El nuevo descriptor de archivo ahora es
   no heredable.

   Nota:

     This function is intended for low-level I/O.  For normal usage,
     use the built-in function "open()", which returns a *file object*
     with "read()" and "write()" methods. To wrap a file descriptor in
     a file object, use "fdopen()".

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.5: Si la llamada al sistema se interrumpe
   y el controlador de señal no genera una excepción, la función
   vuelve a intentar la llamada del sistema en lugar de generar una
   excepción "InterruptedError" (ver **PEP 475** para la
   justificación).

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

Las siguientes constantes son opciones para el parámetro *flags* de la
función "open()". Se pueden combinar con el operador OR a nivel de bit
"|". Algunos de ellas no están disponibles en todas las plataformas.
Para obtener descripciones de su disponibilidad y uso, consulte la
página de manual *open(2)* en Unix o la MSDN en Windows.

os.O_RDONLY
os.O_WRONLY
os.O_RDWR
os.O_APPEND
os.O_CREAT
os.O_EXCL
os.O_TRUNC

   Las constantes anteriores están disponibles en Unix y Windows.

os.O_DSYNC
os.O_RSYNC
os.O_SYNC
os.O_NDELAY
os.O_NONBLOCK
os.O_NOCTTY
os.O_CLOEXEC

   Las constantes anteriores sólo están disponibles en Unix.

   Distinto en la versión 3.3: Se agregó la constante "O_CLOEXEC".

os.O_BINARY
os.O_NOINHERIT
os.O_SHORT_LIVED
os.O_TEMPORARY
os.O_RANDOM
os.O_SEQUENTIAL
os.O_TEXT

   Las constantes anteriores sólo están disponibles en Windows.

os.O_EVTONLY
os.O_FSYNC
os.O_SYMLINK
os.O_NOFOLLOW_ANY

   Las constantes anteriores solo están disponibles en macOS.

   Distinto en la versión 3.10: Agregue las constantes "O_EVTONLY",
   "O_FSYNC", "O_SYMLINK" y "O_NOFOLLOW_ANY".

os.O_ASYNC
os.O_DIRECT
os.O_DIRECTORY
os.O_NOFOLLOW
os.O_NOATIME
os.O_PATH
os.O_TMPFILE
os.O_SHLOCK
os.O_EXLOCK

   Las constantes anteriores son extensiones y no están presentes si
   no están definidas por la biblioteca de C.

   Distinto en la versión 3.4: Se agrega la constante "O_PATH" en los
   sistemas que lo admiten. Se agrega "O_TMPFILE", sólo disponible en
   Linux para el Kernel 3.11 o posterior.

os.openpty()

   Abre un nuevo par de pseudo-terminal. Retorna un par de
   descriptores de archivo "(master, slave)"; para pty y tty,
   respectivamente. Los nuevos descriptores de archivo son no
   heredable. Para un enfoque (ligeramente) más portátil, use el
   módulo "pty".

   Availability: Unix, not WASI.

   Distinto en la versión 3.4: Los nuevos descriptores de archivo
   ahora son no heredables.

os.pipe()

   Crea una tubería. Retorna un par de descriptores de archivo "(r,
   w)" que se pueden usar para leer y escribir, respectivamente. El
   nuevo descriptor de archivo es no heredable.

   Availability: Unix, Windows.

   Distinto en la versión 3.4: Los nuevos descriptores de archivo
   ahora son no heredables.

os.pipe2(flags, /)

   Crea una tubería con *flags* establecidas atómicamente. *flags*
   pueden construirse juntando uno o más de estos valores:
   "O_NONBLOCK", "O_CLOEXEC" con el operador OR. Retorna un par de
   descriptores de archivo "(r, w)" que se pueden usar para leer y
   escribir, respectivamente.

   Availability: Unix, not WASI, not macOS, not iOS.

   Added in version 3.3.

os.posix_fallocate(fd, offset, len, /)

   Asegura que se asigne suficiente espacio en disco para el archivo
   especificado por *fd* a partir de *offset* y se extiende por *len*
   bytes.

   Availability: Unix, not macOS, not iOS.

   Added in version 3.3.

os.posix_fadvise(fd, offset, len, advice, /)

   Avisa una intención de acceder a los datos en un patrón específico,
   permitiendo así que el núcleo haga optimizaciones. El consejo se
   aplica a la región del archivo especificada por *fd* que comienza
   en *offset* y se extiende para *len* bytes. *advice* es uno de
   "POSIX_FADV_NORMAL", "POSIX_FADV_SEQUENTIAL", "POSIX_FADV_RANDOM",
   "POSIX_FADV_NOREUSE", "POSIX_FADV_WILLNEED" o
   "POSIX_FADV_DONTNEED".

   Availability: Unix, not macOS, not iOS.

   Added in version 3.3.

os.POSIX_FADV_NORMAL
os.POSIX_FADV_SEQUENTIAL
os.POSIX_FADV_RANDOM
os.POSIX_FADV_NOREUSE
os.POSIX_FADV_WILLNEED
os.POSIX_FADV_DONTNEED

   Indicadores que se pueden usar en *advice* en "posix_fadvise()" que
   especifican el patrón de acceso que es probable que se use.

   Availability: Unix.

   Added in version 3.3.

os.pread(fd, n, offset, /)

   Lee como máximo *n* bytes del descriptor de archivo *fd* en una
   posición de *offset*, sin modificar el desplazamiento (*offset*)
   del archivo.

   Retorna una cadena de bytes que contiene los bytes leídos. Si se
   alcanza el final del archivo al que hace referencia *fd*, se
   retorna un objeto de bytes vacío.

   Availability: Unix.

   Added in version 3.3.

os.posix_openpt(oflag, /)

   Abrir y devolver un descriptor de archivo para un dispositivo
   pseudo-terminal maestro.

   Llama a la función de la biblioteca estándar de C "posix_openpt()".
   El argumento *oflag* se utiliza para establecer indicadores de
   estado de archivo y modos de acceso a archivos, tal como se
   especifica en la página del manual de "posix_openpt()" de su
   sistema.

   El descriptor de archivo devuelto es non-inheritable. Si el valor
   "O_CLOEXEC" está disponible en el sistema, se agrega a *oflag*.

   Availability: Unix, not WASI.

   Added in version 3.13.

os.preadv(fd, buffers, offset, flags=0, /)

   Lee de un descriptor de archivo *fd* en una posición de *offset* en
   mutable *objetos de tipo bytes* *buffers*, dejando el
   desplazamiento del archivo sin cambios. Transfiere datos a cada
   búfer hasta que esté lleno y luego pase al siguiente búfer en la
   secuencia para contener el resto de los datos.

   El argumento flags contiene un operador de bit a bit OR de cero o
   más de las siguientes flags:

   * "RWF_HIPRI"

   * "RWF_NOWAIT"

   Retorna el número total de bytes realmente leídos que puede ser
   menor que la capacidad total de todos los objetos.

   El sistema operativo puede establecer un límite ("sysconf()" valor
   "'SC_IOV_MAX'") en el número de búferes que se pueden usar.

   Combina la funcionalidad de "os.readv()" y "os.pread()".

   Availability: Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX
   >= 7.1.

   El uso de banderas requiere Linux >= 4.6.

   Added in version 3.7.

os.RWF_NOWAIT

   No espere datos que no estén disponibles de inmediato. Si se
   especifica este indicador, la llamada al sistema regresará
   instantáneamente si tuviera que leer datos del almacenamiento de
   respaldo o esperar por un bloqueo.

   Si se leyeron correctamente algunos datos, devolverá la cantidad de
   bytes leídos. Si no se leyeron bytes, devolverá "-1" y establecerá
   errno en "errno.EAGAIN".

   Availability: Linux >= 4.14.

   Added in version 3.7.

os.RWF_HIPRI

   Alta prioridad de lectura/escritura. Permite que los sistemas de
   archivos basados en bloques utilicen el sondeo del dispositivo, lo
   que proporciona una latencia más baja, pero puede usar recursos
   adicionales.

   Actualmente, en Linux, esta función sólo se puede usar en un
   descriptor de archivo abierto con el indicador "O_DIRECT".

   Availability: Linux >= 4.6.

   Added in version 3.7.

os.ptsname(fd, /)

   Devuelve el nombre del dispositivo pseudoterminal esclavo asociado
   con el dispositivo pseudoterminal maestro al que hace referencia el
   descriptor de archivo *fd*. El descriptor de archivo *fd* no se
   cierra en caso de error.

   Llama a la función de biblioteca estándar reentrante C
   "ptsname_r()" si está disponible; de ​​lo contrario, se llama a la
   función de biblioteca estándar C "ptsname()", que no se garantiza
   que sea segura para subprocesos.

   Availability: Unix, not WASI.

   Added in version 3.13.

os.pwrite(fd, str, offset, /)

   Escribe la cadena de bytes en *str* en el descriptor de archivo
   *fd* en la posición *offset*, sin modificar el desplazamiento del
   archivo.

   Retorna el número de bytes realmente escritos.

   Availability: Unix.

   Added in version 3.3.

os.pwritev(fd, buffers, offset, flags=0, /)

   Escribe el contenido de *buffers* en el descriptor de archivo *fd*
   en un desplazamiento *offset*, sin modificar el desplazamiento del
   archivo. *buffers* debe ser una secuencia de *bytes-like objects*.
   Los búferes se procesan en orden de matriz. Se escribe todo el
   contenido del primer búfer antes de pasar al segundo, y así
   sucesivamente.

   El argumento flags contiene un operador de bit a bit OR de cero o
   más de las siguientes flags:

   * "RWF_DSYNC"

   * "RWF_SYNC"

   * "RWF_APPEND"

   Retorna el número total de bytes realmente escritos.

   El sistema operativo puede establecer un límite ("sysconf()" valor
   "'SC_IOV_MAX'") en el número de búferes que se pueden usar.

   Combina la funcionalidad de "os.writev()" y "os.pwrite()".

   Availability: Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX
   >= 7.1.

   El uso de banderas requiere Linux >= 4.6.

   Added in version 3.7.

os.RWF_DSYNC

   Proporcione un equivalente por escritura del indicador "O_DSYNC"
   "os.open()". Este efecto de bandera se aplica solo al rango de
   datos escrito por la llamada al sistema.

   Availability: Linux >= 4.7.

   Added in version 3.7.

os.RWF_SYNC

   Proporcione un equivalente por escritura del indicador "O_SYNC"
   "os.open()". Este efecto de bandera se aplica solo al rango de
   datos escrito por la llamada al sistema.

   Availability: Linux >= 4.7.

   Added in version 3.7.

os.RWF_APPEND

   Proporcione un equivalente por escritura del indicador "O_APPEND"
   "os.open()". Esta bandera es significativa solo para "os.pwritev()"
   y su efecto se aplica solo al rango de datos escrito por la llamada
   al sistema. El argumento *offset* no afecta la operación de
   escritura; los datos siempre se añaden al final del archivo. Sin
   embargo, si el argumento *offset* es "-1", se actualiza el *offset*
   actual del archivo.

   Availability: Linux >= 4.16.

   Added in version 3.10.

os.read(fd, n, /)

   Lee como máximo *n* bytes del descriptor de archivo *fd*.

   Retorna una cadena de bytes que contiene los bytes leídos. Si se
   alcanza el final del archivo al que hace referencia *fd*, se
   retorna un objeto de bytes vacío.

   Nota:

     This function is intended for low-level I/O and must be applied
     to a file descriptor as returned by "os.open()" or "pipe()".  To
     read a "file object" returned by the built-in function "open()"
     or by "popen()" or "fdopen()", or "sys.stdin", use its "read()"
     or "readline()" methods.

   Distinto en la versión 3.5: Si la llamada al sistema se interrumpe
   y el controlador de señal no genera una excepción, la función
   vuelve a intentar la llamada del sistema en lugar de generar una
   excepción "InterruptedError" (ver **PEP 475** para la
   justificación).

os.readinto(fd, buffer, /)

   Read from a file descriptor *fd* into a mutable buffer object
   *buffer*.

   The *buffer* should be mutable and *bytes-like*. On success,
   returns the number of bytes read. Less bytes may be read than the
   size of the buffer. The underlying system call will be retried when
   interrupted by a signal, unless the signal handler raises an
   exception. Other errors will not be retried and an error will be
   raised.

   Returns 0 if *fd* is at end of file or if the provided *buffer* has
   length 0 (which can be used to check for errors without reading
   data). Never returns negative.

   Nota:

     This function is intended for low-level I/O and must be applied
     to a file descriptor as returned by "os.open()" or "os.pipe()".
     To read a "file object" returned by the built-in function
     "open()", or "sys.stdin", use its member functions, for example
     "io.BufferedIOBase.readinto()", "io.BufferedIOBase.read()", or
     "io.TextIOBase.read()"

   Added in version 3.14.

os.sendfile(out_fd, in_fd, offset, count)
os.sendfile(out_fd, in_fd, offset, count, headers=(), trailers=(), flags=0)

   Copia *count* bytes del descriptor de archivo *in_fd* al descriptor
   de archivo *out_fd* comenzando en *offset*. Retorna el número de
   bytes enviados. Cuando se alcanza EOF, retorna "0".

   La primera notación de la función es compatible con todas las
   plataformas que definen "sendfile()".

   En Linux, si *offset* se entrega como "None", los bytes se leen
   desde la posición actual de *in_fd* y la posición de *in_fd* se
   actualiza.

   El segundo caso se puede usar en macOS y FreeBSD donde *headers* y
   *trailers* son secuencias arbitrarias de búferes que se escriben
   antes y después de que se escriban los datos de *in_fd*. Retorna lo
   mismo que el primer caso.

   En macOS y FreeBSD, un valor de "0" para *count* especifica enviar
   hasta que se alcanza el final de *in_fd*.

   Todas las plataformas admiten sockets como descriptor de archivo
   *out_fd*, y algunas plataformas también permiten otros tipos (por
   ejemplo, archivo regular, tuberías).

   Las aplicaciones multiplataforma no deben usar los argumentos
   *headers*, *trailers* y *flags*.

   Availability: Unix, not WASI.

   Nota:

     Para un contenedor de alto nivel de "sendfile()", vea
     "socket.socket.sendfile()".

   Added in version 3.3.

   Distinto en la versión 3.9: Parámetros *out* e *in* han sido
   renombrados a *out_fd* e *in_fd*.

os.SF_NODISKIO
os.SF_MNOWAIT
os.SF_SYNC

   Parámetros para la función "sendfile()", si la implementación los
   admite.

   Availability: Unix, not WASI.

   Added in version 3.3.

os.SF_NOCACHE

   Parámetro a la función "sendfile()", si la implementación lo
   admite. Los datos no se almacenarán en caché en la memoria virtual
   y se liberarán después.

   Availability: Unix, not WASI.

   Added in version 3.11.

os.set_blocking(fd, blocking, /)

   Establece el modo de bloqueo del descriptor de archivo
   especificado. Establece la flag "O_NONBLOCK" si se quiere que el
   bloqueo sea "False", borre la flag de lo contrario.

   Consulte también "get_blocking()" y "socket.socket.setblocking()".

   Availability: Unix, Windows.

   La función está limitada en WASI, consulte Plataformas WebAssembly
   para obtener más información.

   En Windows, esta función está limitada a las tuberías.

   Added in version 3.5.

   Distinto en la versión 3.12: Se agregó soporte para pipes en
   Windows.

os.splice(src, dst, count, offset_src=None, offset_dst=None, flags=0)

   Transfer *count* bytes from file descriptor *src*, starting from
   offset *offset_src*, to file descriptor *dst*, starting from offset
   *offset_dst*.

   The splicing behaviour can be modified by specifying a *flags*
   value. Any of the following variables may used, combined using
   bitwise OR (the "|" operator):

   * If "SPLICE_F_MOVE" is specified, the kernel is asked to move
     pages instead of copying, but pages may still be copied if the
     kernel cannot move the pages from the pipe.

   * If "SPLICE_F_NONBLOCK" is specified, the kernel is asked to not
     block on I/O. This makes the splice pipe operations nonblocking,
     but splice may nevertheless block because the spliced file
     descriptors may block.

   * If "SPLICE_F_MORE" is specified, it hints to the kernel that more
     data will be coming in a subsequent splice.

   At least one of the file descriptors must refer to a pipe. If
   *offset_src* is "None", then *src* is read from the current
   position; respectively for *offset_dst*. The offset associated to
   the file descriptor that refers to a pipe must be "None". The files
   pointed to by *src* and *dst* must reside in the same filesystem,
   otherwise an "OSError" is raised with "errno" set to "errno.EXDEV".

   Esta copia se realiza sin el costo adicional de transferir datos
   desde el kernel al espacio del usuario y luego nuevamente al
   kernel. También, algunos sistemas de archivos podrían implementar
   optimizaciones adicionales. La copia se realiza como si ambos
   archivos se abrieran como binarios.

   Una vez completado con éxito, retorna el número de bytes empalmados
   hacia o desde la tubería. Un valor de retorno de 0 significa el
   final de la entrada. Si *src* se refiere a una tubería, esto
   significa que no hay datos para transferir y no tendría sentido
   bloquear porque no hay escritores conectados al extremo de
   escritura de la tubería.

   Ver también: The *splice(2)* man page.

   Availability: Linux >= 2.6.17 with glibc >= 2.5

   Added in version 3.10.

os.SPLICE_F_MOVE
os.SPLICE_F_NONBLOCK
os.SPLICE_F_MORE

   Added in version 3.10.

os.readv(fd, buffers, /)

   Leer desde un descriptor de archivo *fd* en una cantidad de mutable
   *objetos tipo bytes* *buffers*. Transfiere datos a cada búfer hasta
   que esté lleno y luego pase al siguiente búfer en la secuencia para
   contener el resto de los datos.

   Retorna el número total de bytes realmente leídos que puede ser
   menor que la capacidad total de todos los objetos.

   El sistema operativo puede establecer un límite ("sysconf()" valor
   "'SC_IOV_MAX'") en el número de búferes que se pueden usar.

   Availability: Unix.

   Added in version 3.3.

os.tcgetpgrp(fd, /)

   Retorna el grupo del proceso asociado con la terminal proporcionada
   por *fd* (un descriptor de archivo abierto como lo retorna
   "os.open()").

   Availability: Unix, not WASI.

os.tcsetpgrp(fd, pg, /)

   Establece el grupo del proceso asociado con la terminal dada por
   *fd* (un descriptor de archivo abierto como lo retorna "os.open()")
   a *pg*.

   Availability: Unix, not WASI.

os.ttyname(fd, /)

   Retorna una cadena que especifica el dispositivo de terminal
   asociado con el descriptor de archivo *fd*. Si *fd* no está
   asociado con un dispositivo de terminal, se genera una excepción.

   Availability: Unix.

os.unlockpt(fd, /)

   Desbloquee el dispositivo pseudoterminal esclavo asociado con el
   dispositivo pseudoterminal maestro al que hace referencia el
   descriptor de archivo *fd*. El descriptor de archivo *fd* no se
   cierra en caso de falla.

   Llama a la función de la biblioteca estándar C "unlockpt()".

   Availability: Unix, not WASI.

   Added in version 3.13.

os.write(fd, str, /)

   Escribe la cadena de bytes en *str* en el descriptor de archivo
   *fd*.

   Retorna el número de bytes realmente escritos.

   Nota:

     This function is intended for low-level I/O and must be applied
     to a file descriptor as returned by "os.open()" or "pipe()".  To
     write a "file object" returned by the built-in function "open()"
     or by "popen()" or "fdopen()", or "sys.stdout" or "sys.stderr",
     use its "write()" method.

   Distinto en la versión 3.5: Si la llamada al sistema se interrumpe
   y el controlador de señal no genera una excepción, la función
   vuelve a intentar la llamada del sistema en lugar de generar una
   excepción "InterruptedError" (ver **PEP 475** para la
   justificación).

os.writev(fd, buffers, /)

   Escribe el contenido de *buffers* en el descriptor de archivo *fd*.
   *buffers* debe ser una secuencia de *objetos tipo bytes*. Los
   búferes se procesan en orden secuencial. Se escribe todo el
   contenido del primer búfer antes de pasar al segundo, y así
   sucesivamente.

   Retorna el número total de bytes realmente escritos.

   El sistema operativo puede establecer un límite ("sysconf()" valor
   "'SC_IOV_MAX'") en el número de búferes que se pueden usar.

   Availability: Unix.

   Added in version 3.3.

### Consultando las dimensiones de una terminal

Added in version 3.3.

os.get_terminal_size(fd=STDOUT_FILENO, /)

   Retorna el tamaño de la ventana de la terminal como "(columns,
   lines)", una tupla del tipo "terminal_size".

   El argumento opcional "fd" (por defecto es "STDOUT_FILENO", o la
   salida estándar) especifica qué descriptor de archivo debe
   consultarse.

   Si el descriptor de archivo no está conectado a una terminal, se
   genera un "OSError".

   "shutil.get_terminal_size()" es la función de alto nivel que
   normalmente debería usarse, "os.get_terminal_size" es la
   implementación de bajo nivel.

   Availability: Unix, Windows.

class os.terminal_size

   Una subclase de tupla, que contiene "(columns, lines)"
   representando el tamaño de la ventana de la terminal.

   columns

      Ancho de la ventana de la terminal en caracteres.

   lines

      Alto de la ventana de la terminal en caracteres.

### Herencia de los descriptores de archivos

Added in version 3.4.

Un descriptor de archivo tiene un indicador heredable (*inheritable*)
que indica si el descriptor de archivo puede ser heredado por procesos
secundarios. Desde Python 3.4, los descriptores de archivo creados por
Python son no heredables por defecto.

On UNIX, non-inheritable file descriptors are closed in child
processes at the execution of a new program, other file descriptors
are inherited. Note that non-inheritable file descriptors are still
*inherited* by child processes on "os.fork()".

En Windows, los descriptores de archivo y los identificadores no
heredables se cierran en los procesos hijos, a excepción de los flujos
estándar (descriptores de archivo 0, 1 y 2: stdin, stdout y stderr),
que siempre se heredan. Usando las funciones "spawn*", todos los
identificadores heredables y todos los descriptores de archivos
heredables se heredan. Usando el módulo "subprocess", todos los
descriptores de archivo, excepto los flujos estándar, están cerrados,
y los identificadores heredables sólo se heredan si el parámetro
*close_fds* es "False".

En las plataformas WebAssembly, el descriptor de archivo no se puede
modificar.

os.get_inheritable(fd, /)

   Obtiene el indicador heredable (*inheritable*) del descriptor de
   archivo especificado (un valor booleano).

os.set_inheritable(fd, inheritable, /)

   Establece el indicador heredable (*inheritable*) del descriptor de
   archivo especificado.

os.get_handle_inheritable(handle, /)

   Obtiene el indicador heredable (*inheritable*) del identificador
   especificado (un valor booleano).

   Availability: Windows.

os.set_handle_inheritable(handle, inheritable, /)

   Establece el indicador heredable (*inheritable*) del identificador
   especificado.

   Availability: Windows.

## Archivos y directorios

En algunas plataformas Unix, muchas de estas funciones admiten una o
más de estas características:

* **specifying a file descriptor:** Normally the *path* argument
  provided to functions in the "os" module must be a string specifying
  a file path.  However, some functions now alternatively accept an
  open file descriptor for their *path* argument. The function will
  then operate on the file referred to by the descriptor. For POSIX
  systems, Python will call the variant of the function prefixed with
  "f" (e.g. call "fchdir" instead of "chdir").

  Puede verificar si *path* se puede especificar o no como un
  descriptor de archivo para una función particular en su plataforma
  usando "os.supports_fd". Si esta funcionalidad no está disponible,
  su uso lanzará un "NotImplementedError".

  Si la función también admite argumentos *dir_fd* o
  *follow_symlinks*, es un error especificar uno de esos al
  suministrar *path* como descriptor de archivo.

* **paths relative to directory descriptors:** If *dir_fd* is not
  "None", it should be a file descriptor referring to a directory, and
  the path to operate on should be relative; path will then be
  relative to that directory.  If the path is absolute, *dir_fd* is
  ignored.  For POSIX systems, Python will call the variant of the
  function with an "at" suffix and possibly prefixed with "f" (e.g.
  call "faccessat" instead of "access").

  Puede verificar si *dir_fd* es compatible o no para una función
  particular en su plataforma usando "os.supports_dir_fd". Si no está
  disponible, usarlo lanzará un "NotImplementedError".

* **not following symlinks:** If *follow_symlinks* is "False", and the
  last element of the path to operate on is a symbolic link, the
  function will operate on the symbolic link itself rather than the
  file pointed to by the link.  For POSIX systems, Python will call
  the "l..." variant of the function.

  Puede verificar si *follow_symlinks* es compatible o no para una
  función particular en su plataforma usando
  "os.supports_follow_symlinks". Si no está disponible, usarlo lanzará
  un "NotImplementedError".

os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)

   Use el uid/gid real para probar el acceso a *path*. Tenga en cuenta
   que la mayoría de las operaciones utilizarán el uid/gid efectivo,
   por lo tanto, esta rutina se puede usar en un entorno suid/sgid
   para probar si el usuario que invoca tiene el acceso especificado a
   *path*. *mode* debería ser "F_OK" para probar la existencia de
   *path*, o puede ser el OR inclusivo de uno o más de "R_OK", "W_OK",
   y "X_OK" para probar los permisos. Retorna "True" si el acceso está
   permitido, "False" si no. Consulte la página de manual de Unix
   *access (2)* para obtener más información.

   Esta función puede admitir la especificación rutas relativas a
   descriptores de directorio y no seguir los enlaces simbólicos.

   Si *effective_ids* es "True", "access()" realizará sus
   comprobaciones de acceso utilizando el uid/gid efectivo en lugar
   del uid/gid real. *effective_ids* puede no ser compatible con su
   plataforma; puede verificar si está disponible o no usando
   "os.supports_effective_ids". Si no está disponible, usarlo lanzará
   un "NotImplementedError".

   Nota:

     Usando "access()" para verificar si un usuario está autorizado
     para, por ejemplo, abrir un archivo antes de hacerlo usando
     "open()" crea un agujero de seguridad, porque el usuario podría
     explotar el breve intervalo de tiempo entre verificar y abrir el
     archivo para manipularlo es preferible utilizar técnicas *EAFP*.
     Por ejemplo:

        if os.access("myfile", os.R_OK):
            with open("myfile") as fp:
                return fp.read()
        return "some default data"

     está mejor escrito como:

        try:
            fp = open("myfile")
        except PermissionError:
            return "some default data"
        else:
            with fp:
                return fp.read()

   Nota:

     Las operaciones de E/S pueden fallar incluso cuando "access()"
     indica que tendrán éxito, particularmente para operaciones en
     sistemas de archivos de red que pueden tener una semántica de
     permisos más allá del modelo habitual de bits de permiso POSIX.

   Distinto en la versión 3.3: Se agregaron los parámetros *dir_fd*,
   *effective_ids* y *follow_symlinks*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.F_OK
os.R_OK
os.W_OK
os.X_OK

   Valores para pasar como parámetro *mode* de "access()" para probar
   la existencia, legibilidad, escritura y ejecutabilidad de *path*,
   respectivamente.

os.chdir(path)

   Cambia el directorio de trabajo actual a *path*.

   Esta función puede soportar especificando un descriptor de archivo.
   El descriptor debe hacer referencia a un directorio abierto, no a
   un archivo abierto.

   Esta función puede generar "OSError" y subclases como
   "FileNotFoundError", "PermissionError", y "NotADirectoryError".

   Lanza un evento de auditoría "os.chdir" con argumento "path".

   Ver también:

     The "contextlib.chdir()" context manager, which changes the
     current working directory on entering and restores the previous
     one on exit.

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como descriptor de archivo en algunas plataformas.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.chflags(path, flags, *, follow_symlinks=True)

   Establece las flags del *path* a las *flags* numéricas. *flags*
   puede tomar una combinación (OR bit a bit) de los siguientes
   valores (como se define en el módulo "stat"):

   * "stat.UF_NODUMP"

   * "stat.UF_IMMUTABLE"

   * "stat.UF_APPEND"

   * "stat.UF_OPAQUE"

   * "stat.UF_NOUNLINK"

   * "stat.UF_COMPRESSED"

   * "stat.UF_HIDDEN"

   * "stat.SF_ARCHIVED"

   * "stat.SF_IMMUTABLE"

   * "stat.SF_APPEND"

   * "stat.SF_NOUNLINK"

   * "stat.SF_SNAPSHOT"

   Esta función puede soportar no seguir enlaces simbólicos.

   Lanza un evento de auditoría "os.chflags" con argumentos "path",
   "flags".

   Availability: Unix, not WASI.

   Distinto en la versión 3.3: Se agregó el argumento
   *follow_symlinks*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)

   Cambia el modo de *path* al modo numérico *mode*. *mode* puede
   tomar uno de los siguientes valores (como se define en el módulo
   "stat") o combinaciones OR de bit a bit de ellos:

   * "stat.S_ISUID"

   * "stat.S_ISGID"

   * "stat.S_ENFMT"

   * "stat.S_ISVTX"

   * "stat.S_IREAD"

   * "stat.S_IWRITE"

   * "stat.S_IEXEC"

   * "stat.S_IRWXU"

   * "stat.S_IRUSR"

   * "stat.S_IWUSR"

   * "stat.S_IXUSR"

   * "stat.S_IRWXG"

   * "stat.S_IRGRP"

   * "stat.S_IWGRP"

   * "stat.S_IXGRP"

   * "stat.S_IRWXO"

   * "stat.S_IROTH"

   * "stat.S_IWOTH"

   * "stat.S_IXOTH"

   Esta función puede soportar especificando un descriptor de archivo,
   rutas relativas a los descriptores de directorio y no seguir
   enlaces simbólicos.

   Nota:

     Aunque Windows admite "chmod()", solo se puede configurar el
     indicador de solo lectura del archivo con él (a través de las
     constantes "stat.S_IWRITE" y "stat.S_IREAD" o un valor entero
     correspondiente). Se ignoran todos los demás bits. El valor
     predeterminado de *follow_symlinks* es "False" en Windows.La
     función está limitada en WASI, consulte Plataformas WebAssembly
     para obtener más información.

   Lanza un evento de auditoría "os.chmod" con argumentos "path",
   "mode", "dir_fd".

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como un descriptor de archivo abierto, y los argumentos
   *dir_fd* y *follow_symlinks*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.13: Se agregó soporte para un descriptor
   de archivo y el argumento *follow_symlinks* en Windows.

os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)

   Cambia el propietario y el *id* del grupo de *path* a los numéricos
   *uid* y *gid*. Para dejar uno de los identificadores sin cambios,
   configúrelo en -1.

   Esta función puede soportar especificando un descriptor de archivo,
   rutas relativas a los descriptores de directorio y no seguir
   enlaces simbólicos.

   Ver "shutil.chown()" para una función de nivel superior que acepta
   nombres además de identificadores numéricos.

   Lanza un evento de auditoría "os.chown" con argumentos "path",
   "uid", "gid", "dir_fd".

   Availability: Unix.

   La función está limitada en WASI, consulte Plataformas WebAssembly
   para obtener más información.

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como un descriptor de archivo abierto, y los argumentos
   *dir_fd* y *follow_symlinks*.

   Distinto en la versión 3.6: Admite un *objeto tipo ruta*.

os.chroot(path)

   Cambia el directorio raíz del proceso actual a *path*.

   Availability: Unix, not WASI, not Android.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.fchdir(fd)

   Cambia el directorio de trabajo actual al directorio representado
   por el descriptor de archivo *fd*. El descriptor debe hacer
   referencia a un directorio abierto, no a un archivo abierto. A
   partir de Python 3.3, esto es equivalente a "os.chdir(fd)".

   Lanza un evento de auditoría "os.chdir" con argumento "path".

   Availability: Unix.

os.getcwd()

   Retorna una cadena que representa el directorio de trabajo actual.

os.getcwdb()

   Retorna una cadena de bytes que representa el directorio de trabajo
   actual.

   Distinto en la versión 3.8: La función ahora usa la codificación
   UTF-8 en Windows, en lugar de los códigos ANSI: consulte **PEP
   529** para ver la justificación. La función ya no está en desuso en
   Windows.

os.lchflags(path, flags)

   Establece las flags de *path* a las *flags* numéricas, como
   "chflags()", pero no siga los enlaces simbólicos. A partir de
   Python 3.3, esto es equivalente a "os.chflags(path, flags,
   follow_symlinks=False)".

   Lanza un evento de auditoría "os.chflags" con argumentos "path",
   "flags".

   Availability: Unix, not WASI.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.lchmod(path, mode)

   Cambia el modo de *path* al *mode* numérico. Si la ruta es un
   enlace simbólico, esto afecta al enlace simbólico en lugar del
   objetivo. Consulte los documentos para "chmod()" para conocer los
   posibles valores de *mode*. A partir de Python 3.3, esto es
   equivalente a "os.chmod(path, mode, follow_symlinks=False)".

   "lchmod()" no es parte de POSIX, pero las implementaciones de Unix
   pueden tenerlo si se admite el cambio del modo de enlaces
   simbólicos.

   Lanza un evento de auditoría "os.chmod" con argumentos "path",
   "mode", "dir_fd".

   Availability: Unix, Windows, not Linux, FreeBSD >= 1.3, NetBSD >=
   1.3, not OpenBSD

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.13: Se agregó soporte en Windows.

os.lchown(path, uid, gid)

   Cambia el propietario y la identificación del grupo de *path* a los
   numéricos *uid* y *gid*. Esta función no seguirá enlaces
   simbólicos. A partir de Python 3.3, esto es equivalente a
   "os.chown(path, uid, gid, follow_symlinks=False)".

   Lanza un evento de auditoría "os.chown" con argumentos "path",
   "uid", "gid", "dir_fd".

   Availability: Unix.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)

   Cree un enlace rígido que apunte a *src* llamado *dst*.

   This function can support specifying *src_dir_fd* and/or
   *dst_dir_fd* to supply paths relative to directory descriptors, and
   not following symlinks. The default value of *follow_symlinks* is
   "False" on Windows.

   Lanza un evento de auditoría "os.link" con argumentos "src", "dst",
   "src_dir_fd", "dst_dir_fd".

   Availability: Unix, Windows.

   Distinto en la versión 3.2: Se agregó soporte para Windows.

   Distinto en la versión 3.3: Se agregaron los parámetros
   *src_dir_fd*, *dst_dir_fd* y *follow_symlinks*.

   Distinto en la versión 3.6: Acepta un *path-like object* para *src*
   y *dst*.

os.listdir(path='.')

   Retorna una lista que contiene los nombres de las entradas en el
   directorio dado por *path*. La lista está en un orden arbitrario y
   no incluye las entradas especiales "'.'" Y "'..'" incluso si están
   presentes en el directorio. Si un archivo es removido de o añadido
   al directorio mientras se llama a esta función, no se especifica si
   el nombre para el archivo será incluido.

   *path* puede ser un *path-like object*. Si *path* es de tipo
   "bytes" (directa o indirectamente a través de la interfaz
   "PathLike"), los nombres de archivo retornados también serán de
   tipo "bytes"; en todas las demás circunstancias, serán del tipo
   "str".

   Esta función también puede admitir especificando un descriptor de
   archivo; el descriptor de archivo debe hacer referencia a un
   directorio.

   Lanza un evento de auditoría "os.listdir" con el argumento "ruta".

   Nota:

     Para codificar los nombres de archivo "str" en "bytes", use
     "fsencode()".

   Ver también:

     La función "scandir()" retorna entradas de directorio junto con
     información de atributos de archivo, lo que proporciona un mejor
     rendimiento para muchos casos de uso comunes.

   Distinto en la versión 3.2: El parámetro *path* se convirtió en
   opcional.

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como un descriptor de archivo abierto.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.listdrives()

   Devuelve una lista que contiene los nombres de las unidades en un
   sistema Windows.

   El nombre de una unidad suele ser "'C:\\'". No todos los nombres de
   unidades se asociarán a un volumen y es posible que algunas sean
   inaccesibles por diversos motivos, incluidos permisos, conectividad
   de red o medios faltantes. Esta función no prueba el acceso.

   Puede generar "OSError" si ocurre un error al recopilar los nombres
   de las unidades.

   Genera un auditing event "os.listdrives" sin argumentos.

   Availability: Windows

   Added in version 3.12.

os.listmounts(volume)

   Devuelve una lista que contiene los puntos de montaje de un volumen
   en un sistema Windows.

   *volume* debe representarse como una ruta GUID, como las que
   devuelve "os.listvolumes()". Los volúmenes pueden montarse en
   varias ubicaciones o no montarse en ninguna. En este último caso,
   la lista estará vacía. Esta función no devolverá los puntos de
   montaje que no estén asociados a un volumen.

   Los puntos de montaje devueltos por esta función serán rutas
   absolutas y pueden ser más largos que el nombre de la unidad.

   Genera "OSError" si no se reconoce el volumen o si se produce un
   error al recopilar las rutas.

   Genera un auditing event "os.listmounts" con el argumento "volume".

   Availability: Windows

   Added in version 3.12.

os.listvolumes()

   Devuelve una lista que contiene los volúmenes del sistema.

   Los volúmenes se representan normalmente como una ruta GUID similar
   a "\\?\Volume{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\". Normalmente,
   se puede acceder a los archivos a través de una ruta GUID, si los
   permisos lo permiten. Sin embargo, los usuarios no suelen estar
   familiarizados con ellos, por lo que el uso recomendado de esta
   función es recuperar los puntos de montaje mediante
   "os.listmounts()".

   Puede generar "OSError" si ocurre un error al recopilar los
   volúmenes.

   Genera un auditing event "os.listvolumes" sin argumentos.

   Availability: Windows

   Added in version 3.12.

os.lstat(path, *, dir_fd=None)

   Realiza el equivalente de una llamada al sistema "lstat()" en la
   ruta indicada. Similar a "stat()", pero no sigue enlaces
   simbólicos. Devuelve un objeto "stat_result".

   En plataformas que no admiten enlaces simbólicos, este es un alias
   para "stat()".

   A partir de Python 3.3, esto es equivalente a "os.stat(path,
   dir_fd=dir_fd, follow_symlinks=False)".

   Esta función también puede admitir rutas relativas a descriptores
   de directorio.

   Ver también: La función "stat()".

   Distinto en la versión 3.2: Se agregó soporte para enlaces
   simbólicos de Windows 6.0 (Vista).

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.8: En Windows, ahora abre puntos de
   análisis que representan otra ruta (nombres sustitutos), incluidos
   enlaces simbólicos y uniones de directorio. El sistema operativo
   resuelve otros tipos de puntos de análisis como "stat()".

os.mkdir(path, mode=0o777, *, dir_fd=None)

   Cree un directorio llamado *path* con modo numérico *mode*.

   Si el directorio ya existe, se genera "FileExistsError". Si no
   existe un directorio principal en la ruta, se genera
   "FileNotFoundError".

   En algunos sistemas, *mode* se ignora. Donde se usa, el valor
   actual de umask se enmascara primero. Si se establecen bits
   distintos de los últimos 9 (es decir, los últimos 3 dígitos de la
   representación octal del *mode*), su significado depende de la
   plataforma. En algunas plataformas, se ignoran y debe llamar a
   "chmod()" explícitamente para configurarlos.

   En Windows, se maneja específicamente un *mode* o "0o700" para
   aplicar el control de acceso al nuevo directorio de modo que solo
   el usuario actual y los administradores tengan acceso. Se ignoran
   otros valores de *mode*.

   Esta función también puede admitir rutas relativas a descriptores
   de directorio.

   También es posible crear directorios temporales; vea la función
   "tempfile" del módulo "tempfile.mkdtemp()".

   Lanza un evento de auditoría "os.mkdir" con argumentos "ruta",
   "modo", "dir_fd".

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.13: Windows ahora maneja un *mode* o
   "0o700".

os.makedirs(name, mode=0o777, exist_ok=False)

   Función de creación de directorio recursiva. Como "mkdir()", pero
   hace que todos los directorios de nivel intermedio sean necesarios
   para contener el directorio hoja.

   El parámetro *mode* se pasa a "mkdir()" para crear el directorio
   hoja; consulte the mkdir() description para saber cómo se
   interpreta. Para configurar los bits de permiso de archivo de
   cualquier directorio principal recién creado, puede configurar
   umask antes de invocar "makedirs()". Los bits de permiso de archivo
   de los directorios principales existentes no se modifican.

   Si *exist_ok* es "False" (el valor predeterminado), se genera un
   "FileExistsError" si el directorio de destino ya existe.

   Nota:

     "makedirs()" se confundirá si los elementos de ruta a crear
     incluyen "pardir" (por ejemplo, ".." en sistemas UNIX).

   Esta función maneja las rutas UNC correctamente.

   Lanza un evento de auditoría "os.mkdir" con argumentos "ruta",
   "modo", "dir_fd".

   Distinto en la versión 3.2: Se agregó el parámetro *exist_ok*.

   Distinto en la versión 3.4.1: Antes de Python 3.4.1, si *exist_ok*
   era "True" y el directorio existía, "makedirs()" aún generaría un
   error si *mode* no coincidía con el modo del directorio existente.
   Como este comportamiento era imposible de implementar de forma
   segura, se eliminó en Python 3.4.1. Ver bpo-21082.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.7: El argumento *mode* ya no afecta los
   bits de permiso de archivo de los directorios de nivel intermedio
   recién creados.

os.mkfifo(path, mode=0o666, *, dir_fd=None)

   Cree una FIFO (una tubería con nombre) llamada *path* con modo
   numérico *modo*. El valor actual de umask se enmascara primero del
   modo.

   Esta función también puede admitir rutas relativas a descriptores
   de directorio.

   Los FIFO son tuberías a las que se puede acceder como archivos
   normales. Los FIFO existen hasta que se eliminan (por ejemplo con
   "os.unlink()"). En general, los FIFO se utilizan como punto de
   encuentro entre los procesos de tipo "cliente" y "servidor": el
   servidor abre el FIFO para leer y el cliente lo abre para escribir.
   Tenga en cuenta que "mkfifo()" no abre el FIFO --- solo crea el
   punto de encuentro.

   Availability: Unix, not WASI.

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.mknod(path, mode=0o600, device=0, *, dir_fd=None)

   Cree un nodo del sistema de archivos (archivo, archivo especial del
   dispositivo o canalización con nombre) llamado *path*. *mode*
   especifica tanto los permisos para usar como el tipo de nodo que se
   creará, combinándose (OR bit a bit) con uno de "stat.S_IFREG",
   "stat.S_IFCHR", "stat.S_IFBLK" , y "stat.S_IFIFO" (esas constantes
   están disponibles en "stat"). Para "stat.S_IFCHR" y "stat.S_IFBLK",
   *device* define el archivo especial del dispositivo recién creado
   (probablemente usando "os.makedev()"), de lo contrario se ignora.

   Esta función también puede admitir rutas relativas a descriptores
   de directorio.

   Availability: Unix, not WASI.

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.major(device, /)

   Extrae el número principal del dispositivo de un número de
   dispositivo sin procesar (generalmente el campo "st_dev" o
   "st_rdev" de "stat").

os.minor(device, /)

   Extrae el número menor del dispositivo de un número de dispositivo
   sin procesar (generalmente el campo "st_dev" o "st_rdev" de
   "stat").

os.makedev(major, minor, /)

   Compone un número de dispositivo sin procesar a partir de los
   números de dispositivo mayor y menor.

os.pathconf(path, name)

   Retorna información de configuración del sistema relevante para un
   archivo con nombre. *name* especifica el valor de configuración
   para recuperar; puede ser una cadena que es el nombre de un valor
   de sistema definido; Estos nombres se especifican en varios
   estándares (POSIX.1, Unix 95, Unix 98 y otros). Algunas plataformas
   también definen nombres adicionales. Los nombres conocidos por el
   sistema operativo host se dan en el diccionario "pathconf_names".
   Para las variables de configuración no incluidas en esa asignación,
   también se acepta pasar un número entero para *name*.

   Si *name* es una cadena y no se conoce, se lanza un "ValueError".
   Si el sistema anfitrión no admite un valor específico para *name*,
   incluso si está incluido en "pathconf_names", se genera un
   "OSError" con "errno.EINVAL" para el número de error.

   Esta función puede soportar especificando un descriptor de archivo.

   Availability: Unix.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.pathconf_names

   Nombres de mapeo de diccionario aceptados por "pathconf()" y
   "fpathconf()" a los valores enteros definidos para esos nombres por
   el sistema operativo host. Esto se puede usar para determinar el
   conjunto de nombres conocidos por el sistema.

   Availability: Unix.

os.readlink(path, *, dir_fd=None)

   Retorna una cadena que representa la ruta a la que apunta el enlace
   simbólico. El resultado puede ser un nombre de ruta absoluto o
   relativo; si es relativo, se puede convertir a un nombre de ruta
   absoluto usando "os.path.join(os.path.dirname(path), result)".

   Si la *path* es un objeto de cadena (directa o indirectamente a
   través de una interfaz "PathLike"), el resultado también será un
   objeto de cadena y la llamada puede generar un UnicodeDecodeError.
   Si la *path* es un objeto de bytes (directa o indirectamente), el
   resultado será un objeto de bytes.

   Esta función también puede admitir rutas relativas a descriptores
   de directorio.

   Cuando intente resolver una ruta que puede contener enlaces, use
   "realpath()" para manejar adecuadamente la recurrencia y las
   diferencias de plataforma.

   Availability: Unix, Windows.

   Distinto en la versión 3.2: Se agregó soporte para enlaces
   simbólicos de Windows 6.0 (Vista).

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *path-like object* en Unix.

   Distinto en la versión 3.8: Acepta un *path-like object* y un
   objeto de bytes en Windows.Se agregó soporte para uniones de
   directorio y se modificó para retornar la ruta de sustitución (que
   generalmente incluye el prefijo "\\?\") En lugar del campo opcional
   "nombre de impresión" que se retornó anteriormente.

os.remove(path, *, dir_fd=None)

   Eliminar (borrar) el archivo *path*. Si *path* es un directorio, se
   genera un error "OSError". Utilice "rmdir()" para eliminar
   directorios. Si el archivo no existe, se genera un error
   "FileNotFoundError".

   Esta función puede admitir rutas relativas a descriptores de
   directorio.

   En Windows, intentar eliminar un archivo que está en uso provoca
   una excepción; en Unix, la entrada del directorio se elimina pero
   el almacenamiento asignado al archivo no está disponible hasta que
   el archivo original ya no esté en uso.

   Esta función es semánticamente idéntica a "unlink()".

   Lanza un evento de auditoría "os.remove" con argumentos "ruta",
   "dir_fd".

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.removedirs(name)

   Eliminar directorios de forma recursiva. Funciona como "rmdir()"
   excepto que, si el directorio hoja se elimina con éxito,
   "removeirs()" intenta eliminar sucesivamente cada directorio
   principal mencionado en *path* hasta que se genere un error (que se
   ignora, porque generalmente significa que un directorio padre no
   está vacío). Por ejemplo, "os.removedirs('foo/bar/baz')" primero
   eliminará el directorio "'foo/bar/baz'", y luego eliminará
   "'foo/bar'" y "'foo'" si están vacíos. Genera "OSError" si el
   directorio hoja no se pudo eliminar con éxito.

   Lanza un evento de auditoría "os.remove" con argumentos "ruta",
   "dir_fd".

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

   Cambia el nombre del archivo o directorio *src* a *dst*. Si *dst*
   existe, la operación fallará con una subclase "OSError" en varios
   casos:

   En Windows, si existe *dst*, siempre se genera un
   "FileExistsError". La operación puede fallar si *src* y *dst* están
   en sistemas de archivos diferentes. Utilice "shutil.move()" para
   admitir movimientos a un sistema de archivos diferente.

   En Unix, si *src* es un archivo y *dst* es un directorio o
   viceversa, se generará un "IsADirectoryError" o un
   "NotADirectoryError" respectivamente. Si ambos son directorios y
   *dst* está vacío, *dst* se reemplazará silenciosamente. Si *dst* no
   es un directorio vacío, se genera un "OSError". Si ambos son
   archivos, *dst* se reemplazará silenciosamente si el usuario tiene
   permiso. La operación puede fallar en algunos tipos de Unix si
   *src* y *dst* están en sistemas de archivos diferentes. Si tiene
   éxito, el cambio de nombre será una operación atómica (este es un
   requisito POSIX).

   Esta función puede admitir la especificación de *src_dir_fd* o
   *dst_dir_fd* para proporcionar rutas relativas a los descriptores
   de directorio.

   Si desea sobrescribir multiplataforma del destino, use "replace()".

   Lanza un evento de auditoría "os.rename" con argumentos "src",
   "dst", "src_dir_fd", "dst_dir_fd".

   Distinto en la versión 3.3: Se agregaron los parámetros
   *src_dir_fd* y *dst_dir_fd*.

   Distinto en la versión 3.6: Acepta un *path-like object* para *src*
   y *dst*.

os.renames(old, new)

   Directorio recursivo o función de cambio de nombre de archivo.
   Funciona como "rename()", excepto que primero se intenta crear
   cualquier directorio intermedio necesario para que el nuevo nombre
   de ruta sea bueno. Después del cambio de nombre, los directorios
   correspondientes a los segmentos de ruta más a la derecha del
   nombre anterior se eliminarán usando "removeirs()".

   Nota:

     Esta función puede fallar con la nueva estructura de directorios
     realizada si carece de los permisos necesarios para eliminar el
     directorio o archivo hoja.

   Lanza un evento de auditoría "os.rename" con argumentos "src",
   "dst", "src_dir_fd", "dst_dir_fd".

   Distinto en la versión 3.6: Acepta un *path-like object* para *old*
   y *new*.

os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

   Cambie el nombre del archivo o directorio *src* a *dst*. Si *dst*
   no es un directorio vacío, se generará "OSError". Si *dst* existe y
   es un archivo, se reemplazará de forma silenciosa si el usuario
   tiene permiso. La operación puede fallar si *src* y *dst* están en
   sistemas de archivos diferentes. Si tiene éxito, el cambio de
   nombre será una operación atómica (este es un requisito POSIX).

   Esta función puede admitir la especificación de *src_dir_fd* o
   *dst_dir_fd* para proporcionar rutas relativas a los descriptores
   de directorio.

   Lanza un evento de auditoría "os.rename" con argumentos "src",
   "dst", "src_dir_fd", "dst_dir_fd".

   Added in version 3.3.

   Distinto en la versión 3.6: Acepta un *path-like object* para *src*
   y *dst*.

os.rmdir(path, *, dir_fd=None)

   Suprime (elimina) el directorio *path*. Si el directorio no existe
   o no está vacío, se genera un "FileNotFoundError" o un "OSError"
   respectivamente. Para eliminar árboles de directorios completos, se
   puede utilizar "shutil.rmtree()".

   Esta función puede admitir rutas relativas a descriptores de
   directorio.

   Lanza un evento de auditoría "os.rmdir" con argumentos "ruta",
   "dir_fd".

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.scandir(path='.')

   Retorna un iterador de objetos "os.DirEntry" correspondientes a las
   entradas en el directorio dado por *path*. Las entradas se entregan
   en orden arbitrario, y las entradas especiales "'.'" Y "'..'" no
   están incluidas. Si un archivo es removido de o añadido al
   directorio después de crear el iterador, no se especifica si una
   entrada para el archivo será incluido.

   El uso de "scandir()" en lugar de "listdir()" puede aumentar
   significativamente el rendimiento del código que también necesita
   información de tipo de archivo o atributo de archivo, porque: los
   objetos "os.DirEntry" exponen esta información si el sistema
   operativo proporciona cuando escanea un directorio. Todos los
   métodos "os.DirEntry" pueden realizar una llamada al sistema, pero
   "is_dir()" y "is_file()" generalmente solo requieren una llamada al
   sistema para enlaces simbólicos; "os.DirEntry.stat()" siempre
   requiere una llamada al sistema en Unix, pero solo requiere una
   para enlaces simbólicos en Windows.

   *path* puede ser un *path-like object*. Si *path* es de tipo
   "bytes" (directa o indirectamente a través de la interfaz
   "PathLike"), el tipo de "name" y los atributos "path" de cada
   "os.DirEntry" serán "bytes"; en todas las demás circunstancias,
   serán del tipo "str".

   Esta función también puede admitir especificando un descriptor de
   archivo; el descriptor de archivo debe hacer referencia a un
   directorio.

   Lanza un evento de auditoría "os.scandir" con argumento "ruta".

   El iterador "scandir()" admite el protocolo *context manager* y
   tiene el siguiente método:

   scandir.close()

      Cierre el iterador y libere los recursos adquiridos.

      Esto se llama automáticamente cuando el iterador se agota o se
      recolecta basura, o cuando ocurre un error durante la iteración.
      Sin embargo, es aconsejable llamarlo explícitamente o utilizar
      la palabra clave "with".

      Added in version 3.6.

   El siguiente ejemplo muestra un uso simple de "scandir()" para
   mostrar todos los archivos (excepto los directorios) en la *path*
   dada que no comienzan con "'.'". La llamada "entry.is_file()"
   generalmente no realizará una llamada adicional al sistema:

      with os.scandir(path) as it:
          for entry in it:
              if not entry.name.startswith('.') and entry.is_file():
                  print(entry.name)

   Nota:

     En los sistemas basados ​​en Unix, "scandir()" usa las funciones
     opendir() y readdir() del sistema. En Windows, utiliza las
     funciones Win32 FindFirstFileW y FindNextFileW.

   Added in version 3.5.

   Distinto en la versión 3.6: Se agregó compatibilidad con el
   protocolo *context manager* y el método "close()". Si un iterador
   "scandir()" no se agota ni se cierra explícitamente, se emitirá un
   "ResourceWarning" en su destructor.La función acepta un *path-like
   object*.

   Distinto en la versión 3.7: Soporte agregado para descriptores de
   archivo en Unix.

class os.DirEntry

   Objeto generado por "scandir()" para exponer la ruta del archivo y
   otros atributos de archivo de una entrada de directorio.

   "scandir()" proporcionará tanta información como sea posible sin
   hacer llamadas adicionales al sistema. Cuando se realiza una
   llamada al sistema "stat()" o "lstat()", el objeto "os.DirEntry"
   almacenará en caché el resultado.

   Las instancias "os.DirEntry" no están destinadas a ser almacenadas
   en estructuras de datos de larga duración; si sabe que los
   metadatos del archivo han cambiado o si ha transcurrido mucho
   tiempo desde la llamada "scandir()", llame a "os.stat(entry.path)"
   para obtener información actualizada.

   Debido a que los métodos "os.DirEntry" pueden hacer llamadas al
   sistema operativo, también pueden generar "OSError". Si necesita un
   control muy preciso sobre los errores, puede detectar "OSError"
   cuando llame a uno de los métodos "os.DirEntry" y maneje según
   corresponda.

   Para ser directamente utilizable como *path-like object*,
   "os.DirEntry" implementa la interfaz "PathLike".

   "DirEntry" objects are generic over the type of the path ("str" or
   "bytes").

   Los atributos y métodos en una instancia de "os.DirEntry" son los
   siguientes:

   name

      El nombre de archivo base de la entrada, relativo al argumento
      "scandir()" *path*.

      El atributo "name" será "bytes" si el argumento "scandir()"
      *path* es de tipo "bytes" y "str" de lo contrario. Utilice
      "fsdecode()" para decodificar los nombres de archivo de bytes.

   path

      The entry's path name: equivalent to "os.path.join(scandir_path,
      entry.name)" where *scandir_path* is the original "scandir()"
      *path* argument.  Apart from the filename, the path preserves
      the original "scandir()" argument.  If the "scandir()" *path*
      argument was relative, the "path" attribute is also relative.
      Changing the current working directory after creating the
      "scandir()" iterator may cause later uses of "path" to resolve
      differently.  On some platforms, the constructed path may not be
      valid if the original "scandir()" argument was usable for
      enumeration but not for joining with the entry name.  If the
      "scandir()" *path* argument was a file descriptor, the "path"
      attribute is the same as the "name" attribute.

      El atributo "path" será "bytes" si el argumento "scandir()"
      *path* es de tipo "bytes" y "str" de lo contrario. Utilice
      "fsdecode()" para decodificar los nombres de archivo de bytes.

   inode()

      Retorna el número de inodo de la entrada.

      El resultado se almacena en caché en el objeto "os.DirEntry".
      Use "os.stat(entry.path, follow_symlinks=False).st_ino" para
      obtener información actualizada.

      En la primera llamada no almacenada en caché, se requiere una
      llamada del sistema en Windows pero no en Unix.

   is_dir(*, follow_symlinks=True)

      Retorna "True" si esta entrada es un directorio o un enlace
      simbólico que apunta a un directorio; retorna "False" si la
      entrada es o apunta a cualquier otro tipo de archivo, o si ya no
      existe.

      Si *follow_symlinks* es "False", retorna "True" solo si esta
      entrada es un directorio (sin seguir los enlaces simbólicos);
      retorna "False" si la entrada es cualquier otro tipo de archivo
      o si ya no existe.

      El resultado se almacena en caché en el objeto "os.DirEntry",
      con un caché separado para *follow_symlinks* "True" y "False".
      Llame a "os.stat()" junto con "stat.S_ISDIR()" para obtener
      información actualizada.

      En la primera llamada no almacenada en caché, no se requiere
      ninguna llamada al sistema en la mayoría de los casos.
      Específicamente, para los enlaces no simbólicos, ni Windows ni
      Unix requieren una llamada al sistema, excepto en ciertos
      sistemas de archivos Unix, como los sistemas de archivos de red,
      que retornan "dirent.d_type == DT_UNKNOWN". Si la entrada es un
      enlace simbólico, se requerirá una llamada al sistema para
      seguir el enlace simbólico a menos que *follow_symlinks* sea
      "False".

      Este método puede generar "OSError", como "PermissionError",
      pero "FileNotFoundError" se captura y no se genera.

   is_file(*, follow_symlinks=True)

      Retorna "True" si esta entrada es un archivo o un enlace
      simbólico que apunta a un archivo; retorna "False" si la entrada
      es o apunta a un directorio u otra entrada que no sea de
      archivo, o si ya no existe.

      Si *follow_symlinks* es "False", retorna "True" solo si esta
      entrada es un archivo (sin los siguientes enlaces simbólicos);
      retorna "False" si la entrada es un directorio u otra entrada
      que no sea de archivo, o si ya no existe.

      El resultado se almacena en caché en el objeto "os.DirEntry". El
      almacenamiento en caché, las llamadas realizadas al sistema y
      las excepciones generadas son las siguientes "is_dir()".

   is_symlink()

      Retorna "True" si esta entrada es un enlace simbólico (incluso
      si está roto); retorna "False" si la entrada apunta a un
      directorio o cualquier tipo de archivo, o si ya no existe.

      El resultado se almacena en caché en el objeto "os.DirEntry".
      Llame a "os.path.islink()" para obtener información actualizada.

      En la primera llamada no almacenada en caché, no se requiere
      ninguna llamada al sistema en la mayoría de los casos.
      Específicamente, ni Windows ni Unix requieren una llamada al
      sistema, excepto en ciertos sistemas de archivos Unix, como los
      sistemas de archivos de red, que retornan "dirent.d_type ==
      DT_UNKNOWN".

      Este método puede generar "OSError", como "PermissionError",
      pero "FileNotFoundError" se captura y no se genera.

   is_junction()

      Devuelve "True" si esta entrada es una unión (incluso si está
      rota); devuelve "False" si la entrada apunta a un directorio
      normal, cualquier tipo de archivo, un enlace simbólico o si ya
      no existe.

      El resultado se almacena en caché en el objeto "os.DirEntry".
      Llame a "os.path.isjunction()" para obtener información
      actualizada.

      Added in version 3.12.

   stat(*, follow_symlinks=True)

      Retorna un objeto a "stat_result" para esta entrada. Este método
      sigue enlaces simbólicos por defecto; para crear un enlace
      simbólico agregue el argumento "follow_symlinks=False".

      En Unix, este método siempre requiere una llamada al sistema. En
      Windows, solo requiere una llamada al sistema si
      *follow_symlinks* es "True" y la entrada es un punto de análisis
      (por ejemplo, un enlace simbólico o una unión de directorio).

      En Windows, los atributos "st_ino", "st_dev" y "st_nlink" de
      "stat_result" siempre se establecen en cero. Llame a "os.stat()"
      para obtener estos atributos.

      El resultado se almacena en caché en el objeto "os.DirEntry",
      con un caché separado para *follow_symlinks* "True" y "False".
      Llame a "os.stat()" para obtener información actualizada.

   Tenga en cuenta que existe una buena correspondencia entre varios
   atributos y métodos de "os.DirEntry" y "pathlib.Path". En
   particular, el atributo "name" tiene el mismo significado, al igual
   que los métodos "is_dir()", "is_file()", "is_symlink()",
   "is_junction()" y "stat()".

   Added in version 3.5.

   Distinto en la versión 3.6: Se agregó soporte para la interfaz
   "PathLike". Se agregó soporte para rutas de "bytes" en Windows.

   Distinto en la versión 3.12: El atributo "st_ctime" de un resultado
   estadístico está obsoleto en Windows. La hora de creación del
   archivo está disponible correctamente como "st_birthtime" y, en el
   futuro, "st_ctime" puede cambiarse para que devuelva cero o la hora
   de cambio de metadatos, si está disponible.

os.stat(path, *, dir_fd=None, follow_symlinks=True)

   Obtener el estado de un archivo o un descriptor de archivo. Realice
   el equivalente de a llamada del sistema "stat()" en la ruta dada.
   *path* puede especificarse como una cadena o bytes, directa o
   indirectamente a través de la interfaz "PathLike", o como un
   descriptor de archivo abierto. Retorna un objeto "stat_result".

   Esta función normalmente sigue enlaces simbólicos; para crear un
   enlace simbólico agregue el argumento "follow_symlinks=False", o
   use "lstat()".

   Esta función puede soportar especificando un descriptor de archivo
   y no siguen enlaces simbólicos.

   En Windows, pasar "follow_symlinks=False" deshabilitará el
   seguimiento de todos los puntos de análisis sustitutos de nombre,
   que incluyen enlaces simbólicos y uniones de directorio. Se abrirán
   directamente otros tipos de puntos de análisis que no se parecen a
   los enlaces o que el sistema operativo no puede seguir. Al seguir
   una cadena de enlaces múltiples, esto puede dar como resultado que
   se retorna el enlace original en lugar del no enlace que impidió el
   recorrido completo. Para obtener resultados estadísticos para la
   ruta final en este caso, use la función "os.path.realpath()" para
   resolver el nombre de la ruta lo más posible y llame a "lstat()" en
   el resultado. Esto no se aplica a enlaces simbólicos o puntos de
   unión colgantes, lo que lanzará las excepciones habituales.

   Ejemplo:

      >>> import os
      >>> statinfo = os.stat('somefile.txt')
      >>> statinfo
      os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
      st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
      st_mtime=1297230027, st_ctime=1297230027)
      >>> statinfo.st_size
      264

   Ver también: "fstat()" y funciones "lstat()".

   Distinto en la versión 3.3: Se agregaron los parámetros *dir_fd* y
   *follow_symlinks*, especificando un descriptor de archivo en lugar
   de una ruta.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.8: En Windows, ahora se siguen todos los
   puntos de análisis que el sistema operativo puede resolver, y pasar
   "follow_symlinks=False" desactiva los siguientes puntos de análisis
   sustitutos de nombre. Si el sistema operativo alcanza un punto de
   análisis que no puede seguir, *stat* ahora retorna la información
   de la ruta original como si se hubiera especificado
   "follow_symlinks=False" en lugar de generar un error.

class os.stat_result

   Objeto cuyos atributos corresponden aproximadamente a los miembros
   de la estructura "stat". Se utiliza para el resultado de
   "os.stat()", "os.fstat()" y "os.lstat()".

   Atributos:

   st_mode

      Modo de archivo: tipo de archivo y bits de modo de archivo
      (permisos).

   st_ino

      Dependiendo de la plataforma, pero si no es cero, identifica de
      forma exclusiva el archivo para un valor dado de "st_dev".
      Típicamente:

      * el número de inodo en Unix,

      * el índice del archivo en Windows

   st_dev

      Identificador del dispositivo en el que reside este archivo.

   st_nlink

      Número de enlaces duros.

   st_uid

      Identificador de usuario del propietario del archivo.

   st_gid

      Identificador de grupo del propietario del archivo.

   st_size

      Tamaño del archivo en bytes, si es un archivo normal o un enlace
      simbólico. El tamaño de un enlace simbólico es la longitud del
      nombre de ruta que contiene, sin un byte nulo de terminación.

   Marcas de tiempo:

   st_atime

      Tiempo de acceso más reciente expresado en segundos.

   st_mtime

      Tiempo de modificación de contenido más reciente expresado en
      segundos.

   st_ctime

      Hora del cambio de metadatos más reciente expresado en segundos.

      Distinto en la versión 3.12: "st_ctime" está obsoleto en
      Windows. Utilice "st_birthtime" para indicar la hora de creación
      del archivo. En el futuro, "st_ctime" contendrá la hora del
      cambio de metadatos más reciente, como en otras plataformas.

   st_atime_ns

      Tiempo de acceso más reciente expresado en nanosegundos como un
      entero.

      Added in version 3.3.

   st_mtime_ns

      Hora de la modificación de contenido más reciente expresada en
      nanosegundos como un entero.

      Added in version 3.3.

   st_ctime_ns

      Hora del cambio de metadatos más reciente expresado en
      nanosegundos como un número entero.

      Added in version 3.3.

      Distinto en la versión 3.12: "st_ctime_ns" está obsoleto en
      Windows. Utilice "st_birthtime_ns" para indicar la hora de
      creación del archivo. En el futuro, "st_ctime" contendrá la hora
      del cambio de metadatos más reciente, como en otras plataformas.

   st_birthtime

      Hora de creación del archivo expresada en segundos. Este
      atributo no siempre está disponible y puede generar el error
      "AttributeError".

      Distinto en la versión 3.12: "st_birthtime" ahora está
      disponible en Windows.

   st_birthtime_ns

      Hora de creación del archivo expresada en nanosegundos como un
      número entero. Este atributo no siempre está disponible y puede
      generar el error "AttributeError".

      Added in version 3.12.

   Nota:

     El significado y la resolución exactos de los atributos
     "st_atime", "st_mtime", "st_ctime" y "st_birthtime" dependen del
     sistema operativo y del sistema de archivos. Por ejemplo, en los
     sistemas Windows que utilizan sistemas de archivos FAT32,
     "st_mtime" tiene una resolución de 2 segundos y "st_atime" tiene
     una resolución de solo 1 día. Consulte la documentación de su
     sistema operativo para obtener más detalles.De manera similar,
     aunque "st_atime_ns", "st_mtime_ns", "st_ctime_ns" y
     "st_birthtime_ns" siempre se expresan en nanosegundos, muchos
     sistemas no proporcionan precisión en nanosegundos. En los
     sistemas que sí proporcionan precisión en nanosegundos, el objeto
     de punto flotante utilizado para almacenar "st_atime",
     "st_mtime", "st_ctime" y "st_birthtime" no puede conservarlo todo
     y, por lo tanto, será ligeramente inexacto. Si necesita las
     marcas de tiempo exactas, siempre debe utilizar "st_atime_ns",
     "st_mtime_ns", "st_ctime_ns" y "st_birthtime_ns".

   En algunos sistemas Unix (como Linux), los siguientes atributos
   también pueden estar disponibles:

   st_blocks

      Número de bloques de 512 bytes asignados para el archivo. Esto
      puede ser más pequeño que "st_size" / 512 cuando el archivo
      tiene agujeros.

   st_blksize

      Tamaño de bloque "preferido" para una eficiente E / S del
      sistema de archivos. Escribir en un archivo en fragmentos más
      pequeños puede causar una lectura-modificación-reescritura
      ineficiente.

   st_rdev

      Tipo de dispositivo si es un dispositivo inodo.

   st_flags

      Indicadores definidos por el usuario para el archivo.

   En otros sistemas Unix (como FreeBSD), los siguientes atributos
   pueden estar disponibles (pero solo se pueden completar si la raíz
   intenta usarlos):

   st_gen

      Número de generación de archivos.

   En Solaris y derivados, los siguientes atributos también pueden
   estar disponibles:

   st_fstype

      Cadena que identifica de forma exclusiva el tipo de sistema de
      archivos que contiene el archivo.

   En los sistemas macOS, los siguientes atributos también pueden
   estar disponibles:

   st_rsize

      Tamaño real del archivo.

   st_creator

      Creador del archivo.

   st_type

      Tipo de archivo.

   En los sistemas Windows, los siguientes atributos también están
   disponibles:

   st_file_attributes

      Atributos de archivo de Windows: "dwFileAttributes" miembro de
      la estructura "BY_HANDLE_FILE_INFORMATION" devuelta por
      "GetFileInformationByHandle()". Consulte las constantes
      "FILE_ATTRIBUTE_* <stat.FILE_ATTRIBUTE_ARCHIVE>" en el módulo
      "stat".

      Added in version 3.5.

   st_reparse_tag

      Cuando "st_file_attributes" tiene "FILE_ATTRIBUTE_REPARSE_POINT"
      configurado, este campo contiene la etiqueta que identifica el
      tipo de punto de análisis. Consulte las constantes
      "IO_REPARSE_TAG_*" en el módulo "stat".

   El módulo estándar "stat" define funciones y constantes que son
   útiles para extraer información de una estructura "stat". (En
   Windows, algunos elementos se rellenan con valores ficticios).

   Para compatibilidad con versiones anteriores, también se puede
   acceder a una instancia "stat_result" como una tupla de al menos 10
   números enteros que den los miembros más importantes (y portables)
   de la estructura "stat", en el orden "st_mode", "st_ino", "st_dev",
   "st_nlink", "st_uid", "st_gid", "st_size", "st_atime", "st_mtime",
   "st_ctime". Algunas implementaciones pueden agregar más elementos
   al final. Para compatibilidad con versiones anteriores de Python,
   acceder a "stat_result" como una tupla siempre devuelve números
   enteros.

   Distinto en la versión 3.5: Windows ahora retorna el índice del
   archivo como "st_ino" cuando está disponible.

   Distinto en la versión 3.7: Se agregó el miembro "st_fstype" a
   Solaris/derivados.

   Distinto en la versión 3.8: Se agregó el miembro "st_reparse_tag"
   en Windows.

   Distinto en la versión 3.8: En Windows, el miembro "st_mode" ahora
   identifica archivos especiales como "S_IFCHR", "S_IFIFO" o
   "S_IFBLK" según corresponda.

   Distinto en la versión 3.12: En Windows, "st_ctime" está obsoleto.
   Con el tiempo, contendrá la última hora de cambio de metadatos,
   para mantener la coherencia con otras plataformas, pero por ahora
   aún contiene la hora de creación. Utilice "st_birthtime" para la
   hora de creación.En Windows, "st_ino" puede tener hasta 128 bits,
   según el sistema de archivos. Antes no superaba los 64 bits y los
   identificadores de archivos más grandes se empaquetaban de forma
   arbitraria.En Windows, "st_rdev" ya no devuelve un valor. Antes
   contenía el mismo valor que "st_dev", lo cual era incorrecto.Se
   agregó el miembro "st_birthtime" en Windows.

os.statvfs(path)

   Perform a *statvfs(3)* system call on the given path.  The return
   value is a "statvfs_result" whose attributes describe the
   filesystem on the given path and correspond to the members of the
   "statvfs" structure.

   Esta función puede soportar especificando un descriptor de archivo.

   Availability: Unix.

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como un descriptor de archivo abierto.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

class os.statvfs_result

   Filesystem statistics returned by "os.statvfs()" and
   "os.fstatvfs()". See *statvfs(3)* for more details.

   f_bsize

      Block size.

   f_frsize

      Fragment size.

   f_blocks

      Number of "f_frsize" sized blocks the filesystem can contain.

   f_bfree

      Number of free blocks.

   f_bavail

      Number of free blocks for unprivileged users.

   f_files

      Number of file entries, inodes, the filesystem can contain.

   f_ffree

      Number of free files entries.

   f_favail

      Number of free file entries for unprivileged users.

   f_flag

      Bit-mask of mount flags.  The following flags are defined:
      "ST_RDONLY", "ST_NOSUID", "ST_NODEV", "ST_NOEXEC",
      "ST_SYNCHRONOUS", "ST_MANDLOCK", "ST_WRITE", "ST_APPEND",
      "ST_IMMUTABLE", "ST_NOATIME", "ST_NODIRATIME", and
      "ST_RELATIME".

   f_namemax

      Filesystem max filename length. OS specific limitations such as
      Windows MAX_PATH and those described in Linux *pathname(7)* may
      exist.

   f_fsid

      Filesystem ID.

      Added in version 3.7.

The following flags are used in "statvfs_result.f_flag".

os.ST_RDONLY

   Read-only filesystem.

   Added in version 3.2.

os.ST_NOSUID

   Setuid/setgid bits are disabled or not supported.

   Added in version 3.2.

os.ST_NODEV

   Disallow access to device special files.

   Availability: Linux.

   Added in version 3.4.

os.ST_NOEXEC

   Disallow program execution.

   Availability: Linux.

   Added in version 3.4.

os.ST_SYNCHRONOUS

   Writes are synced at once.

   Availability: Linux.

   Added in version 3.4.

os.ST_MANDLOCK

   Allow mandatory locks on an FS.

   Availability: Linux.

   Added in version 3.4.

os.ST_WRITE

   Write on file/directory/symlink.

   Availability: Linux.

   Added in version 3.4.

os.ST_APPEND

   Append-only file.

   Availability: Linux.

   Added in version 3.4.

os.ST_IMMUTABLE

   Immutable file.

   Availability: Linux.

   Added in version 3.4.

os.ST_NOATIME

   Do not update access times.

   Availability: Linux.

   Added in version 3.4.

os.ST_NODIRATIME

   Do not update directory access times.

   Availability: Linux.

   Added in version 3.4.

os.ST_RELATIME

   Update atime relative to mtime/ctime.

   Availability: Linux.

   Added in version 3.4.

os.supports_dir_fd

   A "set" object indicating which functions in the "os" module accept
   an open file descriptor for their *dir_fd* parameter. Different
   platforms provide different features, and the underlying
   functionality Python uses to implement the *dir_fd* parameter is
   not available on all platforms Python supports.  For consistency's
   sake, functions that may support *dir_fd* always allow specifying
   the parameter, but will throw an exception if the functionality is
   used when it's not locally available. (Specifying "None" for
   *dir_fd* is always supported on all platforms.)

   Para verificar si una función particular acepta un descriptor de
   archivo abierto para su parámetro *dir_fd*, use el operador "in" en
   "supports_dir_fd". Como ejemplo, esta expresión se evalúa como
   "True" si "os.stat()" acepta descriptores de archivos abiertos para
   *dir_fd* en la plataforma local:

      os.stat en os.supports_dir_fd

   Actualmente, los parámetros *dir_fd* solo funcionan en plataformas
   Unix; ninguno de ellos funciona en Windows.

   Added in version 3.3.

os.supports_effective_ids

   Un objeto "set" que indica si "os.access()" permite especificar
   "True" para su parámetro *fective_ids* en la plataforma local.
   (Especificar "False" para *effective_id* siempre es compatible con
   todas las plataformas). Si la plataforma local lo admite, la
   colección contendrá "os.access()"; de lo contrario estará vacío.

   Esta expresión se evalúa como "True" si "os.access()" admite
   "effective_id=True" en la plataforma local:

      os.access en os.supports_effective_ids

   Actualmente, *effective_ids* solo es compatible con plataformas
   Unix; No funciona en Windows.

   Added in version 3.3.

os.supports_fd

   A "set" object indicating which functions in the "os" module permit
   specifying their *path* parameter as an open file descriptor on the
   local platform.  Different platforms provide different features,
   and the underlying functionality Python uses to accept open file
   descriptors as *path* arguments is not available on all platforms
   Python supports.

   Para determinar si una función en particular permite especificar un
   descriptor de archivo abierto para su parámetro *path*, use el
   operador "in" en "supports_fd". Como ejemplo, esta expresión se
   evalúa como "True" si "os.chdir()" acepta descriptores de archivo
   abiertos para *path* en su plataforma local:

      os.chdir en os.supports_fd

   Added in version 3.3.

os.supports_follow_symlinks

   A "set" object indicating which functions in the "os" module accept
   "False" for their *follow_symlinks* parameter on the local
   platform. Different platforms provide different features, and the
   underlying functionality Python uses to implement *follow_symlinks*
   is not available on all platforms Python supports.  For
   consistency's sake, functions that may support *follow_symlinks*
   always allow specifying the parameter, but will throw an exception
   if the functionality is used when it's not locally available.
   (Specifying "True" for *follow_symlinks* is always supported on all
   platforms.)

   Para verificar si una función particular acepta "False" para su
   parámetro *follow_symlinks*, use el operador "in" en
   "supports_follow_symlinks". Como ejemplo, esta expresión se evalúa
   como "True" si puede especificar "follow_symlinks=False" al llamar
   a "os.stat()" en la plataforma local:

      os.stat en os.supports_follow_symlinks

   Added in version 3.3.

os.symlink(src, dst, target_is_directory=False, *, dir_fd=None)

   Cree un enlace simbólico que apunte a *src* llamado *dst*.

   The *src* parameter refers to the target of the link (the file or
   directory being linked to), and *dst* is the name of the link being
   created.

   En Windows, un enlace simbólico representa un archivo o un
   directorio, y no se transforma dinámicamente en el destino. Si el
   objetivo está presente, el tipo de enlace simbólico se creará para
   que coincida. De lo contrario, el enlace simbólico se creará como
   un directorio si *target_is_directory* es "True" o un enlace
   simbólico de archivo (el valor predeterminado) de lo contrario. En
   plataformas que no son de Windows, *target_is_directory* se ignora.

   Esta función puede admitir rutas relativas a descriptores de
   directorio.

   Nota:

     En las versiones más recientes de Windows 10, las cuentas sin
     privilegios pueden crear enlaces simbólicos si el Modo
     desarrollador está habilitado. Cuando el Modo desarrollador no
     está disponible / habilitado, se requiere el privilegio
     *SeCreateSymbolicLinkPrivilege*, o el proceso debe ejecutarse
     como administrador."OSError" se lanza cuando un usuario sin
     privilegios llama a la función.

   Lanza un evento de auditoría "os.symlink" con argumentos "src",
   "dst", "dir_fd".

   Availability: Unix, Windows.

   La función está limitada en WASI, consulte Plataformas WebAssembly
   para obtener más información.

   Distinto en la versión 3.2: Se agregó soporte para enlaces
   simbólicos de Windows 6.0 (Vista).

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd* y ahora
   se permite *target_is_directory* en plataformas que no sean
   Windows.

   Distinto en la versión 3.6: Acepta un *path-like object* para *src*
   y *dst*.

   Distinto en la versión 3.8: Se agregó soporte para enlaces
   simbólicos sin elevar en Windows con el modo de desarrollador.

os.sync()

   Forzar la escritura de todo en el disco.

   Availability: Unix.

   Added in version 3.3.

os.truncate(path, length)

   Trunca el archivo correspondiente a *path*, para que tenga como
   máximo *length* bytes de tamaño.

   Esta función puede soportar especificando un descriptor de archivo.

   Lanza un evento de auditoría "os.truncate" con argumentos "path",
   "length".

   Availability: Unix, Windows.

   Added in version 3.3.

   Distinto en la versión 3.5: Se agregó soporte para Windows

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.unlink(path, *, dir_fd=None)

   Elimina (elimine) el archivo *path*. Esta función es semánticamente
   idéntica a "remove()"; El nombre "unlink" es su nombre tradicional
   de Unix. Consulte la documentación de "remove()" para obtener más
   información.

   Lanza un evento de auditoría "os.remove" con argumentos "ruta",
   "dir_fd".

   Distinto en la versión 3.3: Se agregó el parámetro *dir_fd*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)

   Establece el acceso y los tiempos modificados del archivo
   especificado por *path*.

   "utime()" toma dos parámetros opcionales, *times* y *ns*. Estos
   especifican los tiempos establecidos en *path* y se utilizan de la
   siguiente manera:

   * Si se especifica *ns*, debe ser una tupla de 2 de la forma
     "(atime_ns, mtime_ns)" donde cada miembro es un int que expresa
     nanosegundos.

   * Si *times* no es "None", debe ser una 2-tupla de la forma
     "(atime, mtime)" donde cada miembro es un int o flotante que
     expresa segundos.

   * Si *times* es "None" y *ns* no está especificado, esto es
     equivalente a especificar "ns=(atime_ns, mtime_ns)" donde ambas
     horas son la hora actual.

   Es un error especificar tuplas para *times* y *ns*.

   Tenga en cuenta que es posible que las horas exactas que establezca
   aquí no se devuelvan en una llamada "stat()" posterior, dependiendo
   de la resolución con la que su sistema operativo registre las horas
   de acceso y modificación; ver "stat()". La mejor manera de
   conservar las horas exactas es usar los campos *st_atime_ns* y
   *st_mtime_ns* del objeto de resultado "os.stat()" con el parámetro
   *ns* a "utime()".

   Esta función puede soportar especificando un descriptor de archivo,
   rutas relativas a los descriptores de directorio y no seguir
   enlaces simbólicos.

   Lanza un evento de auditoría "os.utime" con argumentos "path",
   "times", "ns", "dir_fd".

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como un descriptor de archivo abierto, y los parámetros
   *dir_fd*, *follow_symlinks* y *ns*.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.walk(top, topdown=True, onerror=None, followlinks=False)

   Genere los nombres de archivo en un árbol de directorios
   recorriendo el árbol de arriba hacia abajo o de abajo hacia arriba.
   Para cada directorio en el árbol enraizado en el directorio *top*
   (incluido *top*), produce una tupla de 3 tuplas "(dirpath,
   dirnames, filenames)".

   *dirpath* es una cadena, la ruta al directorio. *dirnames* es una
   lista de los nombres de los subdirectorios en *dirpath* (incluidos
   los enlaces simbólicos a los directorios y excluyendo "'.'" y
   "'..'"). *filenames* es una lista de los nombres de los archivos
   que no son de directorio en *dirpath*. Tenga en cuenta que los
   nombres de las listas no contienen componentes de ruta. Para
   obtener una ruta completa (que comienza con *top*) a un archivo o
   directorio en *dirpath*, ejecute "os.path.join(dirpath, name)". Que
   las listas estén ordenadas o no depende del sistema de archivos. Si
   un archivo se elimina o se agrega al directorio *dirpath* durante
   la generación de las listas, no se especifica si se incluirá un
   nombre para ese archivo.

   Si el argumento opcional *topdown* es "True" o no se especifica, el
   triple para un directorio se genera antes de triplicarse para
   cualquiera de sus subdirectorios (los directorios se generan de
   arriba hacia abajo). Si *topdown* es "False", el triple para un
   directorio se genera después de los triples para todos sus
   subdirectorios (los directorios se generan de abajo hacia arriba).
   No importa el valor de *topdown*, la lista de subdirectorios se
   recupera antes de que se generen las tuplas para el directorio y
   sus subdirectorios.

   Cuando *topdown* es "True", la persona que llama puede modificar la
   lista *dirnames* en su lugar (quizás usando "del" o asignación de
   corte) y "walk()" solo se repetirá en los subdirectorios cuyos
   nombres permanecen en *dirnames*; Esto se puede utilizar para podar
   la búsqueda, imponer un orden específico de visitas o incluso para
   informar "walk()" sobre los directorios que la persona que llama
   crea o renombra antes de que se reanude "walk()" nuevamente. La
   modificación de *dirnames* cuando *topdown* es "False" no tiene
   ningún efecto en el comportamiento de la caminata, porque en el
   modo ascendente los directorios en *dirnames* se generan antes de
   que se genere *dirpath*.

   Por defecto, los errores de la llamada "scandir()" se ignoran. Si
   se especifica el argumento opcional *onerror*, debería ser una
   función; se llamará con un argumento, una instancia "OSError".
   Puede informar el error para continuar con la caminata, o generar
   la excepción para abortar la caminata. Tenga en cuenta que el
   nombre de archivo está disponible como el atributo "filename" del
   objeto de excepción.

   Por defecto, "walk()" no entrará en enlaces simbólicos que se
   resuelven en directorios. Establece *followlinks* en "True" para
   visitar los directorios señalados por los enlaces simbólicos, en
   los sistemas que los admiten.

   Nota:

     Tenga en cuenta que establecer *followlinks* en "True" puede
     conducir a una recursión infinita si un enlace apunta a un
     directorio padre de sí mismo. "walk()" no realiza un seguimiento
     de los directorios que ya visitó.

   Nota:

     Si pasa un nombre de ruta relativo, no cambie el directorio de
     trabajo actual entre las reanudaciones de "walk()". "walk()"
     nunca cambia el directorio actual, y supone que la persona que
     llama tampoco.

   This example displays the number of bytes taken by non-directory
   files in each directory under the starting directory, except that
   it doesn't look under any "__pycache__" subdirectory:

      import os
      from os.path import join, getsize
      for root, dirs, files in os.walk('python/Lib/xml'):
          print(root, "consumes", end=" ")
          print(sum(getsize(join(root, name)) for name in files), end=" ")
          print("bytes in", len(files), "non-directory files")
          if '__pycache__' in dirs:
              dirs.remove('__pycache__')  # don't visit __pycache__ directories

   En el siguiente ejemplo (implementación simple de
   "shutil.rmtree()"), recorrer el árbol de abajo hacia arriba es
   esencial, "rmdir()" no permite eliminar un directorio antes de que
   el directorio esté vacío:

      # Delete everything reachable from the directory named in "top",
      # assuming there are no symbolic links.
      # CAUTION:  This is dangerous!  For example, if top == '/', it
      # could delete all your disk files.
      import os
      for root, dirs, files in os.walk(top, topdown=False):
          for name in files:
              os.remove(os.path.join(root, name))
          for name in dirs:
              os.rmdir(os.path.join(root, name))
      os.rmdir(top)

   Lanza un evento de auditoría "os.spawn" con argumentos "top",
   "topdown", "onerror", "followlinks".

   Distinto en la versión 3.5: Esta función ahora llama "os.scandir()"
   en lugar de "os.listdir()", lo que lo hace más rápido al reducir el
   número de llamadas a "os.stat()".

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.fwalk(top='.', topdown=True, onerror=None, *, follow_symlinks=False, dir_fd=None)

   Esto se comporta exactamente como "walk()", excepto que produce 4
   tuplas "(dirpath, dirnames, filenames, dirfd)", y admite "dir_fd".

   *dirpath*, *dirnames* y *filenames* son idénticos a "walk()"
   output, y *dirfd* es un descriptor de archivo que se refiere al
   directorio *dirpath*.

   Esta función siempre admite rutas relativas a descriptores de
   directorio y no siguen enlaces simbólicos. Sin embargo, tenga en
   cuenta que, a diferencia de otras funciones, el valor
   predeterminado "fwalk()" para *follow_symlinks* es "False".

   Nota:

     Dado que "fwalk()" produce descriptores de archivo, estos solo
     son válidos hasta el siguiente paso de iteración, por lo que debe
     duplicarlos (por ejemplo, con "dup()") si desea mantenerlos más
     tiempo.

   This example displays the number of bytes taken by non-directory
   files in each directory under the starting directory, except that
   it doesn't look under any "__pycache__" subdirectory:

      import os
      for root, dirs, files, rootfd in os.fwalk('python/Lib/xml'):
          print(root, "consumes", end=" ")
          print(sum([os.stat(name, dir_fd=rootfd).st_size for name in files]),
                end=" ")
          print("bytes in", len(files), "non-directory files")
          if '__pycache__' in dirs:
              dirs.remove('__pycache__')  # don't visit __pycache__ directories

   En el siguiente ejemplo, recorrer el árbol de abajo hacia arriba es
   esencial: "rmdir()" no permite eliminar un directorio antes de que
   el directorio esté vacío:

      # Borre todo lo que sea accesible desde el directorio nombrado en "top",
      # asumiendo que no hay enlaces simbólicos.
      # PRECAUCIÓN: ¡Esto es peligroso! Por ejemplo, si top == '/',
      # podría borrar todos los archivos de su disco.
      import os
      for root, dirs, files, rootfd in os.fwalk(top, topdown=False):
      for name in files:
      os.unlink(name, dir_fd=rootfd)
      for name in dirs:
      os.rmdir(name, dir_fd=rootfd)

   Lanza un evento de auditoría "os.chown" con argumentos "top",
   "topdown", "onerror", "follow_symlinks", "dir_fd".

   Availability: Unix.

   Added in version 3.3.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Distinto en la versión 3.7: Se agregó soporte para rutas de acceso
   "bytes".

os.memfd_create(name[, flags=os.MFD_CLOEXEC])

   Cree un archivo anónimo y retorna un descriptor de archivo que se
   refiera a él. *flags* debe ser una de las constantes "os.MFD_*"
   disponibles en el sistema (o una combinación ORed bit a bit de
   ellas). Por defecto, el nuevo descriptor de archivo es no
   heredable.

   El nombre proporcionado en *name* se utiliza como nombre de archivo
   y se mostrará como el destino del enlace simbólico correspondiente
   en el directorio "/proc/self/fd/". El nombre que se muestra siempre
   tiene el prefijo "memfd:" y solo sirve para fines de depuración.
   Los nombres no afectan el comportamiento del descriptor de archivo
   y, como tal, varios archivos pueden tener el mismo nombre sin
   efectos secundarios.

   Availability: Linux >= 3.17 with glibc >= 2.27.

   Added in version 3.8.

os.MFD_CLOEXEC
os.MFD_ALLOW_SEALING
os.MFD_HUGETLB
os.MFD_HUGE_SHIFT
os.MFD_HUGE_MASK
os.MFD_HUGE_64KB
os.MFD_HUGE_512KB
os.MFD_HUGE_1MB
os.MFD_HUGE_2MB
os.MFD_HUGE_8MB
os.MFD_HUGE_16MB
os.MFD_HUGE_32MB
os.MFD_HUGE_256MB
os.MFD_HUGE_512MB
os.MFD_HUGE_1GB
os.MFD_HUGE_2GB
os.MFD_HUGE_16GB

   Estas flags se pueden pasar a "memfd_create()".

   Availability: Linux >= 3.17 with glibc >= 2.27

   Las banderas "MFD_HUGE*" solo están disponibles desde Linux 4.14.

   Added in version 3.8.

os.eventfd(initval[, flags=os.EFD_CLOEXEC])

   Crea y retorna un descriptor de archivo de eventos. Los
   descriptores de archivo admiten "read()" y "write()" sin procesar
   con un tamaño de búfer de 8, "select()", "poll()" y similares.
   Consulte la página de manual *eventfd(2)* para obtener más
   información. De forma predeterminada, el nuevo descriptor de
   archivo no es heredable.

   *initval* es el valor inicial del contador de eventos. El valor
   inicial debe ser un entero sin signo de 32 bits. Tenga en cuenta
   que el valor inicial está limitado a un entero sin signo de 32
   bits, aunque el contador de eventos es un entero sin signo de 64
   bits con un valor máximo de 2^64-2.

   *flags* se puede construir a partir de "EFD_CLOEXEC",
   "EFD_NONBLOCK" y "EFD_SEMAPHORE".

   Si se especifica "EFD_SEMAPHORE" y el contador de eventos no es
   cero, "eventfd_read()" retorna 1 y reduce el contador en uno.

   Si no se especifica "EFD_SEMAPHORE" y el contador de eventos no es
   cero, "eventfd_read()" retorna el valor actual del contador de
   eventos y restablece el contador a cero.

   Si el contador de eventos es cero y no se especifica
   "EFD_NONBLOCK", "eventfd_read()" se bloquea.

   "eventfd_write()" incrementa el contador de eventos. Escribe
   bloques si la operación de escritura incrementaría el contador a un
   valor mayor que ^64-2.

   Ejemplo:

      import os

      # semaphore with start value '1'
      fd = os.eventfd(1, os.EFD_SEMAPHORE | os.EFD_CLOEXEC)
      try:
          # acquire semaphore
          v = os.eventfd_read(fd)
          try:
              do_work()
          finally:
              # release semaphore
              os.eventfd_write(fd, v)
      finally:
          os.close(fd)

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.10.

os.eventfd_read(fd)

   Lee el valor de un descriptor de archivo "eventfd()" y retorna un
   int sin signo de 64 bits. La función no verifica que *fd* sea un
   "eventfd()".

   Availability: Linux >= 2.6.27

   Added in version 3.10.

os.eventfd_write(fd, value)

   Agregue valor a un descriptor de archivo "eventfd()". *value* debe
   ser un int sin signo de 64 bits. La función no verifica que *fd*
   sea un "eventfd()".

   Availability: Linux >= 2.6.27

   Added in version 3.10.

os.EFD_CLOEXEC

   Establezca el indicador close-on-exec para el nuevo descriptor de
   archivo "eventfd()".

   Availability: Linux >= 2.6.27

   Added in version 3.10.

os.EFD_NONBLOCK

   Establezca el indicador de estado "O_NONBLOCK" para el nuevo
   descriptor de archivo "eventfd()".

   Availability: Linux >= 2.6.27

   Added in version 3.10.

os.EFD_SEMAPHORE

   Proporcionar semántica similar a la de un semáforo para las
   lecturas desde un descriptor de archivo "eventfd()". Al leer, el
   contador interno se reduce en uno.

   Availability: Linux >= 2.6.30

   Added in version 3.10.

### Descriptores de archivos del temporizador

Added in version 3.13.

Estas funciones brindan soporte para la API *timer file descriptor* de
Linux. Naturalmente, todas ellas solo están disponibles en Linux.

os.timerfd_create(clockid, /, *, flags=0)

   Crea y devuelve un descriptor de archivo de temporizador
   (*timerfd*).

   El descriptor de archivo devuelto por "timerfd_create()" admite:

   * "read()"

   * "select()"

   * "poll()"

   El método "read()" del descriptor de archivo se puede llamar con un
   tamaño de búfer de 8. Si el temporizador ya ha expirado una o más
   veces, "read()" devuelve la cantidad de expiraciones con el orden
   de bytes del host, que se puede convertir a "int" mediante
   "int.from_bytes(x, byteorder=sys.byteorder)".

   Se pueden usar "select()" y "poll()" para esperar hasta que el
   temporizador expire y el descriptor de archivo sea legible.

   *clockid* debe ser un clock ID válido, como se define en el módulo
   "time":

   * "time.CLOCK_REALTIME"

   * "time.CLOCK_MONOTONIC"

   * "time.CLOCK_BOOTTIME" (desde Linux 3.15 para timerfd_create)

   Si *clockid* es "time.CLOCK_REALTIME", se utiliza un reloj de
   tiempo real configurable para todo el sistema. Si se modifica el
   reloj del sistema, es necesario actualizar la configuración del
   temporizador. Para cancelar el temporizador cuando se modifica el
   reloj del sistema, consulte "TFD_TIMER_CANCEL_ON_SET".

   Si *clockid* es "time.CLOCK_MONOTONIC", se utiliza un reloj que
   aumenta de forma monótona y no se puede configurar. Incluso si se
   cambia el reloj del sistema, la configuración del temporizador no
   se verá afectada.

   Si *clockid* es "time.CLOCK_BOOTTIME", igual que
   "time.CLOCK_MONOTONIC" excepto que incluye cualquier momento en que
   el sistema esté suspendido.

   The file descriptor's behaviour can be modified by specifying a
   *flags* value. Any of the following variables may be used, combined
   using bitwise OR (the "|" operator):

   * "TFD_NONBLOCK"

   * "TFD_CLOEXEC"

   Si "TFD_NONBLOCK" no está configurado como indicador, "read()" se
   bloquea hasta que el temporizador expire. Si está configurado como
   indicador, "read()" no se bloquea, pero si no ha habido una
   expiración desde la última llamada para leer, "read()" genera
   "OSError" y "errno" se configura como "errno.EAGAIN".

   Python siempre establece "TFD_CLOEXEC" automáticamente.

   El descriptor de archivo debe cerrarse con "os.close()" cuando ya
   no sea necesario, de lo contrario se filtrará.

   Ver también: La página del manual *timerfd_create(2)*.

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.timerfd_settime(fd, /, *, flags=flags, initial=0.0, interval=0.0)

   Modificar el temporizador interno de un descriptor de archivo de
   temporizador. Esta función opera con el mismo temporizador de
   intervalos que "timerfd_settime_ns()".

   *fd* debe ser un descriptor de archivo de temporizador válido.

   The timer's behaviour can be modified by specifying a *flags*
   value. Any of the following variables may be used, combined using
   bitwise OR (the "|" operator):

   * "TFD_TIMER_ABSTIME"

   * "TFD_TIMER_CANCEL_ON_SET"

   El temporizador se desactiva al configurar *initial* en cero ("0").
   Si *initial* es igual o mayor que cero, el temporizador se activa.
   Si *initial* es menor que cero, genera una excepción "OSError" con
   "errno" configurado en "errno.EINVAL"

   De forma predeterminada, el temporizador se activará cuando
   transcurran *initial* segundos. (Si *initial* es cero, el
   temporizador se activará inmediatamente).

   Sin embargo, si se establece el indicador "TFD_TIMER_ABSTIME", el
   temporizador se activará cuando el reloj del temporizador
   (establecido por *clockid* en "timerfd_create()") alcance los
   *initial* segundos.

   El intervalo del temporizador se establece mediante *interval*
   "float". Si *interval* es cero, el temporizador solo se activa una
   vez, en la expiración inicial. Si *interval* es mayor que cero, el
   temporizador se activa cada vez que transcurren *interval* segundos
   desde la expiración anterior. Si *interval* es menor que cero,
   genera "OSError" con "errno" establecido en "errno.EINVAL"

   Si el indicador "TFD_TIMER_CANCEL_ON_SET" se configura junto con
   "TFD_TIMER_ABSTIME" y el reloj de este temporizador es
   "time.CLOCK_REALTIME", el temporizador se marca como cancelable si
   el reloj de tiempo real se modifica de manera discontinua. La
   lectura del descriptor se cancela con el error ECANCELED.

   Linux administra el reloj del sistema como UTC. La transición al
   horario de verano se realiza modificando únicamente la diferencia
   horaria y no provoca cambios discontinuos en el reloj del sistema.

   El cambio discontinuo del reloj del sistema será causado por los
   siguientes eventos:

   * "settimeofday"

   * "clock_settime"

   * Establezca la fecha y la hora del sistema mediante el comando
     "date"

   Devuelve una tupla de dos elementos de ("next_expiration",
   "interval") del estado del temporizador anterior, antes de que se
   ejecutara esta función.

   Ver también:

     *timerfd_create(2)*, *timerfd_settime(2)*, *settimeofday(2)*,
     *clock_settime(2)*, y *date(1)*.

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.timerfd_settime_ns(fd, /, *, flags=0, initial=0, interval=0)

   Similar a "timerfd_settime()", pero utiliza el tiempo en
   nanosegundos. Esta función opera con el mismo temporizador de
   intervalos que "timerfd_settime()".

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.timerfd_gettime(fd, /)

   Devuelve una tupla de dos elementos de flotantes
   ("next_expiration", "interval").

   "next_expiration" denotes the relative time until the timer next
   fires, regardless of if the "TFD_TIMER_ABSTIME" flag is set.

   "interval" indica el intervalo del temporizador. Si es cero, el
   temporizador se activará solo una vez, después de que transcurran
   "next_expiration" segundos.

   Ver también: *timerfd_gettime(2)*

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.timerfd_gettime_ns(fd, /)

   Similar a "timerfd_gettime()", pero devuelve el tiempo en
   nanosegundos.

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.TFD_NONBLOCK

   Un indicador para la función "timerfd_create()", que establece el
   indicador de estado "O_NONBLOCK" para el nuevo descriptor de
   archivo del temporizador. Si "TFD_NONBLOCK" no está establecido
   como indicador, "read()" se bloquea.

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.TFD_CLOEXEC

   Una bandera para la función "timerfd_create()". Si "TFD_CLOEXEC"
   está configurado como bandera, establece la bandera de cierre al
   ejecutar para el nuevo descriptor de archivo.

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.TFD_TIMER_ABSTIME

   Indicador para las funciones "timerfd_settime()" y
   "timerfd_settime_ns()". Si se establece este indicador, *initial*
   se interpreta como un valor absoluto en el reloj del temporizador
   (en segundos UTC o nanosegundos desde la época Unix).

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

os.TFD_TIMER_CANCEL_ON_SET

   Una bandera para las funciones "timerfd_settime()" y
   "timerfd_settime_ns()" junto con "TFD_TIMER_ABSTIME". El
   temporizador se cancela cuando la hora del reloj subyacente cambia
   de manera discontinua.

   Availability: Linux >= 2.6.27 with glibc >= 2.8

   Added in version 3.13.

### Atributos extendidos de Linux

Added in version 3.3.

Estas funciones están disponibles solo en Linux.

os.getxattr(path, attribute, *, follow_symlinks=True)

   Retorna el valor del atributo del sistema de archivos extendido
   *atrribute* para *path*. *attribute* puede ser bytes o str (directa
   o indirectamente a través de la interfaz "PathLike"). Si es str, se
   codifica con la codificación del sistema de archivos.

   Esta función puede soportar especificando un descriptor de archivo
   y no siguen enlaces simbólicos.

   Lanza un evento de auditoría "os.getxattr" con argumentos "path",
   "atributo".

   Distinto en la versión 3.6: Acepta un *path-like object* para
   *path*y *attribute*.

os.listxattr(path=None, *, follow_symlinks=True)

   Retorna una lista de los atributos del sistema de archivos
   extendido en *path*. Los atributos en la lista se representan como
   cadenas decodificadas con la codificación del sistema de archivos.
   Si *path* es "None", "listxattr()" examinará el directorio actual.

   Esta función puede soportar especificando un descriptor de archivo
   y no siguen enlaces simbólicos.

   Lanza un evento de auditoría "os.listxattr" con el argumento
   "path".

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os.removexattr(path, attribute, *, follow_symlinks=True)

   Elimina el atributo extendido del sistema de archivos *attribute*
   de *path*. *attribute* debe ser bytes o str (directa o
   indirectamente a través de la interfaz "PathLike"). Si es una
   cadena, está codificada con *filesystem encoding and error
   handler*.

   Esta función puede soportar especificando un descriptor de archivo
   y no siguen enlaces simbólicos.

   Lanza un evento de auditoría "os.removexattr" con argumentos
   "path", "attribute".

   Distinto en la versión 3.6: Acepta un *path-like object* para
   *path*y *attribute*.

os.setxattr(path, attribute, value, flags=0, *, follow_symlinks=True)

   Establece el atributo del sistema de archivos extendido *attribute*
   en *path* en *value*. *attribute* debe ser un bytes o una cadena
   sin NUL incrustados (directa o indirectamente a través de la
   interfaz "PathLike"). Si es una cadena, está codificado con
   *filesystem encoding and error handler*. *flags* puede ser
   "XATTR_REPLACE" o "XATTR_CREATE". Si se proporciona "XATTR_REPLACE"
   y el atributo no existe, se lanzará "ENODATA". Si se proporciona
   "XATTR_CREATE" y el atributo ya existe, no se creará el atributo y
   se lanza "EEXISTS".

   Esta función puede soportar especificando un descriptor de archivo
   y no siguen enlaces simbólicos.

   Nota:

     Un error en las versiones de kernel de Linux anteriores a 2.6.39
     hizo que el argumento de las flags se ignorara en algunos
     sistemas de archivos.

   Lanza un evento de auditoría "os.setxattr" con argumentos "path",
   "attribute", "value", "flags".

   Distinto en la versión 3.6: Acepta un *path-like object* para
   *path*y *attribute*.

os.XATTR_SIZE_MAX

   El tamaño máximo que puede tener el valor de un atributo extendido.
   Actualmente, esto es 64 KiB en Linux.

os.XATTR_CREATE

   Este es un valor posible para el argumento flags en "setxattr()".
   Indica que la operación debe crear un atributo.

os.XATTR_REPLACE

   Este es un valor posible para el argumento flags en "setxattr()".
   Indica que la operación debe reemplazar un atributo existente.

## Gestión de proceso

Estas funciones pueden usarse para crear y administrar procesos.

Las varias funciones "exec *" toman una lista de argumentos para el
nuevo programa cargado en el proceso. En cada caso, el primero de
estos argumentos se pasa al nuevo programa como su propio nombre en
lugar de como un argumento que un usuario puede haber escrito en una
línea de comando. Para el programador C, este es el "argv[0]" pasado a
un programa "main()". Por ejemplo, "os.execv('/bin/echo', ['foo',
'bar'])" solo imprimirá "bar" en la salida estándar; "foo" parecerá
ignorado.

os.abort()

   Genere una señal "SIGABRT" para el proceso actual. En Unix, el
   comportamiento predeterminado es producir un volcado de núcleo; en
   Windows, el proceso retorna inmediatamente un código de salida de
   "3". Tenga en cuenta que llamar a esta función no llamará al
   controlador de señal Python registrado para "SIGABRT" con
   "signal.signal()".

os.add_dll_directory(path)

   Agregue una ruta a la ruta de búsqueda de DLL.

   Esta ruta de búsqueda se utiliza al resolver dependencias para
   módulos de extensión importados (el propio módulo se resuelve
   mediante "sys.path") y también mediante "ctypes".

   Elimina el directorio llamando a **close()** en el objeto retornado
   o utilizándolo en una "with" instrucción.

   Consulte la documentación de Microsoft para obtener más información
   sobre cómo se cargan las DLL.

   Lanza un evento de auditoría "os.add_dll_directory" con el
   argumento "path".

   Availability: Windows.

   Added in version 3.8: Las versiones anteriores de CPython
   resolverían las DLL utilizando el comportamiento predeterminado
   para el proceso actual. Esto condujo a inconsistencias, como solo a
   veces buscar "PATH" o el directorio de trabajo actual, y las
   funciones del sistema operativo como "AddDllDirectory" no tienen
   ningún efecto.En 3.8, las dos formas principales en que se cargan
   las DLL ahora anulan explícitamente el comportamiento de todo el
   proceso para garantizar la coherencia. Ver el notas de portabilidad
   para obtener información sobre la actualización de bibliotecas.

os.execl(path, arg0, arg1, ...)
os.execle(path, arg0, arg1, ..., env)
os.execlp(file, arg0, arg1, ...)
os.execlpe(file, arg0, arg1, ..., env)
os.execv(path, args)
os.execve(path, args, env)
os.execvp(file, args)
os.execvpe(file, args, env)

   Todas estas funciones ejecutan un nuevo programa, reemplazando el
   proceso actual; No vuelven. En Unix, el nuevo ejecutable se carga
   en el proceso actual y tendrá la misma identificación de proceso
   que la persona que llama. Los errores se informarán como
   excepciones "OSError".

   The current process is replaced immediately. Open file objects and
   descriptors are not flushed, so if there may be data buffered on
   these open files, you should flush them using "flush()" or
   "os.fsync()" before calling an "exec*" function.

   Las variantes "l" y "v" de las funciones "exec*" difieren en la
   forma en que se pasan los argumentos de la línea de comandos. Las
   variantes "l" son quizás las más fáciles de usar si el número de
   parámetros es fijo cuando se escribe el código; los parámetros
   individuales simplemente se convierten en parámetros adicionales
   para las funciones "execl*()". Las variantes "v" son buenas cuando
   el número de parámetros es variable, y los argumentos se pasan en
   una lista o tupla como el parámetro *args*. En cualquier caso, los
   argumentos del proceso secundario deben comenzar con el nombre del
   comando que se está ejecutando, pero esto no se aplica.

   Las variantes que incluyen una "p" cerca del final ("execlp()",
   "execlpe()", "execvp()" y "execvpe()") utilizarán la variable de
   entorno "PATH" para localizar el programa *file*. Cuando se
   reemplaza el entorno (utilizando una de las variantes "exec*e", que
   se analizan en el párrafo siguiente), el nuevo entorno se utiliza
   como fuente de la variable "PATH". Las otras variantes, "execl()",
   "execle()", "execv()" y "execve()", no utilizarán la variable
   "PATH" para localizar el ejecutable; *path* debe contener una ruta
   absoluta o relativa adecuada. Las rutas relativas deben incluir al
   menos una barra, incluso en Windows, ya que los nombres simples no
   se resolverán.

   Para "execle()", "execlpe()", "execve()" y "execvpe()" (tenga en
   cuenta que todo esto termina en "e"), el parámetro *env* debe ser
   un mapeo que se utiliza para definir las variables de entorno para
   el nuevo proceso (se utilizan en lugar del entorno del proceso
   actual); las funciones "execl()", "execlp()", "execv()" y
   "execvp()" hacen que el nuevo proceso herede el entorno del proceso
   actual.

   Para "execve()" en algunas plataformas, *path* también puede
   especificarse como un descriptor de archivo abierto. Es posible que
   esta funcionalidad no sea compatible con su plataforma; puede
   verificar si está disponible o no usando "os.supports_fd". Si no
   está disponible, su uso lanzará un "NotImplementedError".

   Lanza un evento de auditoría "os.exec" con argumentos "ruta",
   "args", "env".

   Availability: Unix, Windows, not WASI, not Android, not iOS.

   Distinto en la versión 3.3: Se agregó soporte para especificar
   *path* como un descriptor de archivo abierto para "execve()".

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

os._exit(n)

   Salga del proceso con el estado *n*, sin llamar a los controladores
   de limpieza, vaciar los buffers stdio, etc.

   Nota:

     La forma estándar de salir es "sys.exit(n)". Normalmente,
     "_exit()" solo se debe utilizar en el proceso secundario después
     de "fork()".

Los siguientes códigos de salida están definidos y se pueden usar con
"_exit()", aunque no son obligatorios. Por lo general, se usan para
programas del sistema escritos en Python, como el programa de entrega
de comandos externos de un servidor de correo.

Nota:

  Es posible que algunos de estos no estén disponibles en todas las
  plataformas Unix, ya que hay alguna variación. Estas constantes se
  definen donde están definidas por la plataforma subyacente.

os.EX_OK

   Código de salida que significa que no ocurrió ningún error. Puede
   tomarse del valor definido de "EXIT_SUCCESS" en algunas
   plataformas. Generalmente tiene un valor de cero.

   Availability: Unix, Windows.

os.EX_USAGE

   Código de salida que significa que el comando se usó
   incorrectamente, como cuando se da un número incorrecto de
   argumentos.

   Availability: Unix, not WASI.

os.EX_DATAERR

   Código de salida que significa que los datos de entrada eran
   incorrectos.

   Availability: Unix, not WASI.

os.EX_NOINPUT

   Código de salida que significa que no existía un archivo de entrada
   o que no era legible.

   Availability: Unix, not WASI.

os.EX_NOUSER

   Código de salida que significa que un usuario especificado no
   existía.

   Availability: Unix, not WASI.

os.EX_NOHOST

   Código de salida que significa que no existía un host especificado.

   Availability: Unix, not WASI.

os.EX_UNAVAILABLE

   Código de salida que significa que un servicio requerido no está
   disponible.

   Availability: Unix, not WASI.

os.EX_SOFTWARE

   Código de salida que significa que se detectó un error interno de
   software.

   Availability: Unix, not WASI.

os.EX_OSERR

   Código de salida que significa que se detectó un error del sistema
   operativo, como la imposibilidad de bifurcar o crear una tubería.

   Availability: Unix, not WASI.

os.EX_OSFILE

   Código de salida que significa que algunos archivos del sistema no
   existían, no podían abrirse o tenían algún otro tipo de error.

   Availability: Unix, not WASI.

os.EX_CANTCREAT

   Código de salida que significa que no se pudo crear un archivo de
   salida especificado por el usuario.

   Availability: Unix, not WASI.

os.EX_IOERR

   Código de salida que significa que se produjo un error al realizar
   E / S en algún archivo.

   Availability: Unix, not WASI.

os.EX_TEMPFAIL

   Código de salida que significa que ocurrió una falla temporal. Esto
   indica algo que puede no ser realmente un error, como una conexión
   de red que no se pudo realizar durante una operación recuperable.

   Availability: Unix, not WASI.

os.EX_PROTOCOL

   Código de salida que significa que un intercambio de protocolo fue
   ilegal, inválido o no se entendió.

   Availability: Unix, not WASI.

os.EX_NOPERM

   Código de salida que significa que no había permisos suficientes
   para realizar la operación (pero no para problemas del sistema de
   archivos).

   Availability: Unix, not WASI.

os.EX_CONFIG

   Código de salida que significa que se produjo algún tipo de error
   de configuración.

   Availability: Unix, not WASI.

os.EX_NOTFOUND

   Código de salida que significa algo así como "no se encontró una
   entrada".

   Availability: Unix, not WASI.

os.fork()

   Bifurcar un proceso hijo. Retorna "0" en el niño y la
   identificación del proceso del niño en el padre. Si se produce un
   error se genera "OSError".

   Tenga en cuenta que algunas plataformas que incluyen FreeBSD &lt;=
   6.3 y Cygwin tienen problemas conocidos al usar "fork()" desde un
   hilo.

   Lanza un evento de auditoría "os.fork" sin argumentos.

   Advertencia:

     Si utiliza sockets TLS en una aplicación que llama a "fork()",
     consulte la advertencia en la documentación de "ssl".

   Advertencia:

     En macOS, el uso de esta función no es seguro cuando se combina
     con el uso de API de sistema de nivel superior, incluido el uso
     de "urllib.request".

   Distinto en la versión 3.8: Llamar a "fork()" en un
   subinterpretador ya no es compatible ("RuntimeError" está
   activado).

   Distinto en la versión 3.12: Si Python puede detectar que su
   proceso tiene varios subprocesos, "os.fork()" ahora genera un
   "DeprecationWarning".Elegimos mostrar esto como una advertencia,
   cuando sea detectable, para informar mejor a los desarrolladores
   sobre un problema de diseño que la plataforma POSIX señala
   específicamente como no compatible. Incluso en el código en el que
   *appears* funciona, nunca ha sido seguro mezclar subprocesos con
   "os.fork()" en plataformas POSIX. El entorno de ejecución de
   CPython en sí siempre ha realizado llamadas a la API que no son
   seguras para su uso en el proceso secundario cuando existían
   subprocesos en el primario (como "malloc" y "free").Los usuarios de
   macOS o los usuarios de implementaciones de libc o malloc distintas
   de las que se encuentran habitualmente en glibc hasta la fecha se
   encuentran entre los que tienen más probabilidades de experimentar
   bloqueos al ejecutar dicho código.Consulte this discussion on fork
   being incompatible with threads para obtener detalles técnicos
   sobre el motivo por el cual estamos informando a los
   desarrolladores de este problema de compatibilidad de plataformas
   de larga data.

   Availability: POSIX, not WASI, not Android, not iOS.

os.forkpty()

   Bifurca un proceso hijo, usando un nuevo pseudo-terminal como
   terminal de control del niño. Retorna un par de "(pid, fd)", donde
   *pid* es "0" en el elemento secundario, la identificación del
   proceso del elemento secundario nuevo en el elemento primario y
   *fd* es el descriptor de archivo del final maestro de El pseudo-
   terminal. Para un enfoque más portátil, use el módulo "pty". Si se
   produce un error se genera "OSError".

   Lanza un evento de auditoría "os.forkpty" sin argumentos.

   Advertencia:

     En macOS, el uso de esta función no es seguro cuando se combina
     con el uso de API de sistema de nivel superior, incluido el uso
     de "urllib.request".

   Distinto en la versión 3.8: Llamar a "forkpty()" en un
   subinterpretador ya no es compatible ("RuntimeError" está
   activado).

   Distinto en la versión 3.12: Si Python puede detectar que su
   proceso tiene varios subprocesos, esto ahora genera un error
   "DeprecationWarning". Consulte la explicación más extensa sobre
   "os.fork()".

   Availability: Unix, not WASI, not Android, not iOS.

os.kill(pid, sig, /)

   Enviar señal *sig* al proceso *pid*. Las constantes para las
   señales específicas disponibles en la plataforma host se definen en
   el módulo "signal".

   Windows: The "signal.CTRL_C_EVENT" and "signal.CTRL_BREAK_EVENT"
   signals are special signals which can only be sent to console
   processes which share a common console window, e.g., some
   subprocesses. Any other value for *sig* will cause the process to
   be unconditionally killed by the TerminateProcess API, and the exit
   code will be set to *sig*.

   Ver también "signal.pthread_kill()".

   Lanza un evento de auditoría "os.kill" con argumentos "pid", "sig".

   Availability: Unix, Windows, not WASI, not iOS.

   Distinto en la versión 3.2: Se agregó soporte para Windows.

os.killpg(pgid, sig, /)

   Envíe la señal *sig* al grupo de procesos *pgid*.

   Lanza un evento de auditoría "os.killpg" con argumentos "pgid",
   "sig".

   Availability: Unix, not WASI, not iOS.

os.nice(increment, /)

   Agregue *increment* a la "simpatía" del proceso. Retorna la nueva
   amabilidad.

   Availability: Unix, not WASI.

os.pidfd_open(pid, flags=0)

   Devuelve un descriptor de archivo que hace referencia al proceso
   *pid* con *flags* configurado. Este descriptor se puede utilizar
   para realizar la gestión de procesos sin carreras ni señales.

   Ver la página manual de *pidfd_open(2)* para mas detalles.

   Availability: Linux >= 5.3, Android >= "build-time" API level 31

   Added in version 3.9.

   os.PIDFD_NONBLOCK

      Esta bandera indica que el descriptor de archivo no será
      bloqueante. Si el proceso al que hace referencia el descriptor
      de archivo aún no ha finalizado, entonces un intento de esperar
      en el descriptor de archivo utilizando *waitid(2)* devolverá
      inmediatamente el error "EAGAIN" en lugar de bloquearse.

   Availability: Linux >= 5.10

   Added in version 3.12.

os.plock(op, /)

   Bloquee segmentos del programa en la memoria. El valor de *op*
   (definido en "<sys/lock.h>") determina qué segmentos están
   bloqueados.

   Availability: Unix, not WASI, not macOS, not iOS.

os.popen(cmd, mode='r', buffering=-1)

   Abre una tubería hacia o desde el comando *cmd*. El valor retornado
   es un objeto de archivo abierto conectado a la canalización, que se
   puede leer o escribir dependiendo de si *mode* es "'r'"
   (predeterminado) o "'w'". El argumento *buffering* tiene el mismo
   significado que el argumento correspondiente a la función integrada
   "open()". El objeto de archivo retornado lee o escribe cadenas de
   texto en lugar de bytes.

   El método "close" retorna "None" si el subproceso salió
   correctamente, o el código de retorno del subproceso si hubo un
   error. En los sistemas POSIX, si el código de retorno es positivo,
   representa el valor de retorno del proceso desplazado a la
   izquierda en un byte. Si el código de retorno es negativo, el
   proceso fue terminado por la señal dada por el valor negado del
   código de retorno. (Por ejemplo, el valor de retorno podría ser "-
   signal.SIGKILL" si se eliminó el subproceso). En los sistemas
   Windows, el valor de retorno contiene el código de retorno entero
   firmado del proceso secundario.

   En Unix, "waitstatus_to_exitcode()" puede ser usado para convertir
   el resultado del método "close" (estado de salida) en un código de
   salida si es que no es "None". En Windows, el resultado del método
   "close" es directamente el código de salida (o "None").

   Esto se implementa usando "subprocess.Popen"; consulte la
   documentación de esa clase para obtener formas más potentes de
   administrar y comunicarse con subprocesos.

   Availability: not WASI, not Android, not iOS.

   Nota:

     El Python UTF-8 Mode afecta las codificaciones utilizadas para
     *cmd* y el contenido de la canalización."popen()" es un
     contenedor simple alrededor de "subprocess.Popen". Use
     "subprocess.Popen" o "subprocess.run()" para controlar opciones
     como codificaciones.

   Soft deprecated since version 3.14: The "subprocess" module is
   recommended instead.

os.posix_spawn(path, argv, env, *, file_actions=None, setpgroup=None, resetids=False, setsid=False, setsigmask=(), setsigdef=(), scheduler=None)

   Envuelve la API de la biblioteca C "posix_spawn()" para su uso
   desde Python.

   La mayoría de los usuarios deberían usar "subprocess.run()" en
   lugar de "posix_spawn()".

   Los argumentos posicionales *path*, *args* y *env* son similares a
   "execve()". Se permite que *env* sea "None", en cuyo caso se
   utiliza el entorno del proceso actual.

   El parámetro *path* es la ruta al archivo ejecutable. La *path*
   debe contener un directorio. Utilice "posix_spawnp()" para pasar un
   archivo ejecutable sin directorio.

   El argumento *file_actions* puede ser una secuencia de tuplas que
   describen acciones para tomar descriptores de archivo específicos
   en el proceso secundario entre los pasos de implementación de la
   biblioteca C "fork()" y "exec()". El primer elemento de cada tupla
   debe ser uno de los tres indicadores de tipo que se enumeran a
   continuación y que describen los elementos de tupla restantes:

   os.POSIX_SPAWN_OPEN

      ("os.POSIX_SPAWN_OPEN", *fd*, *path*, *flags*, *mode*)

      Realiza "os.dup2(os.open(path, flags, mode), fd)".

   os.POSIX_SPAWN_CLOSE

      ("os.POSIX_SPAWN_CLOSE", *fd*)

      Realiza "os.close(fd)".

   os.POSIX_SPAWN_DUP2

      ("os.POSIX_SPAWN_DUP2", *fd*, *new_fd*)

      Realiza "os.dup2(fd, new_fd)".

   os.POSIX_SPAWN_CLOSEFROM

      ("os.POSIX_SPAWN_CLOSEFROM", *fd*)

      Ejecuta "os.closerange(fd, INF)".

   Estas tuplas corresponden a las llamadas API de la biblioteca C
   "posix_spawn_file_actions_addopen()",
   "posix_spawn_file_actions_addclose()",
   "posix_spawn_file_actions_adddup2()" y
   "posix_spawn_file_actions_addclosefrom_np()" utilizadas para
   preparar la propia llamada "posix_spawn()".

   El argumento *setpgroup* establecerá el grupo de procesos del hijo
   en el valor especificado. Si el valor especificado es 0, el ID del
   grupo de procesos del hijo será el mismo que el ID de su proceso.
   Si el valor de *setpgroup* no está establecido, el hijo heredará el
   ID del grupo de procesos del padre. Este argumento corresponde al
   indicador "POSIX_SPAWN_SETPGROUP" de la biblioteca C.

   Si el argumento *resetids* es "True", restablecerá el UID y GID
   efectivos del hijo al UID y GID reales del proceso padre. Si el
   argumento es "False", el hijo conserva el UID y GID efectivos del
   padre. En cualquier caso, si los bits de permiso set-user-ID y set-
   group-ID están habilitados en el archivo ejecutable, su efecto
   anulará la configuración del UID y GID efectivos. Este argumento
   corresponde al indicador "POSIX_SPAWN_RESETIDS" de la biblioteca C.

   Si el argumento *setsid* es "True", se creará un nuevo ID de sesión
   para "posix_spawn". *setsid* requiere el indicador
   "POSIX_SPAWN_SETSID" o "POSIX_SPAWN_SETSID_NP". De lo contrario, se
   activa "NotImplementedError".

   El argumento *setsigmask* establecerá la máscara de señal en el
   conjunto de señales especificado. Si no se utiliza el parámetro, el
   elemento secundario hereda la máscara de señal del elemento
   principal. Este argumento corresponde al indicador
   "POSIX_SPAWN_SETSIGMASK" de la biblioteca C.

   El argumento *sigdef* restablecerá la disposición de todas las
   señales en el conjunto especificado. Este argumento corresponde al
   indicador "POSIX_SPAWN_SETSIGDEF" de la biblioteca C.

   El argumento *scheduler* debe ser una tupla que contenga la
   política del programador (opcional) y una instancia de
   "sched_param" con los parámetros del programador. Un valor de
   "None" en lugar de la política del programador indica que no se
   proporciona. Este argumento es una combinación de los indicadores
   "POSIX_SPAWN_SETSCHEDPARAM" y "POSIX_SPAWN_SETSCHEDULER" de la
   biblioteca C.

   Lanza un evento de auditoría "os.posix_spawn" con argumentos
   "ruta", "argv", "env".

   Added in version 3.8.

   Distinto en la versión 3.13: El parámetro *env* acepta "None".
   "os.POSIX_SPAWN_CLOSEFROM" está disponible en plataformas donde
   existe "posix_spawn_file_actions_addclosefrom_np()".

   Availability: Unix, not WASI, not Android, not iOS.

os.posix_spawnp(path, argv, env, *, file_actions=None, setpgroup=None, resetids=False, setsid=False, setsigmask=(), setsigdef=(), scheduler=None)

   Envuelve la API de la biblioteca C "posix_spawnp()" para su uso
   desde Python.

   Similar a "posix_spawn()" excepto que el sistema busca el archivo
   *executable* en la lista de directorios especificada por la
   variable de entorno "PATH" (de la misma manera que para "execvp(3)"
   )

   Lanza un evento de auditoría "os.posix_spawn" con argumentos
   "ruta", "argv", "env".

   Added in version 3.8.

   Availability: POSIX, not WASI, not Android, not iOS.

   Consulte la documentación de "posix_spawn()".

os.register_at_fork(*, before=None, after_in_parent=None, after_in_child=None)

   Registra los invocables que se ejecutarán cuando se bifurca un
   nuevo proceso secundario utilizando "os.fork()" o API de clonación
   de procesos similares. Los parámetros son opcionales y solo de
   palabras clave. Cada uno especifica un punto de llamada diferente.

   * *before* es una función llamada antes de bifurcar un proceso
     hijo.

   * *after_in_parent* es una función llamada desde el proceso padre
     después de bifurcar un proceso hijo.

   * *after_in_child* es una función llamada desde el proceso hijo.

   Estas llamadas solo se realizan si se espera que el control regrese
   al intérprete de Python. Un lanzamiento típico "subprocess" no los
   activará ya que el niño no va a volver a ingresar al intérprete.

   Las funciones registradas para su ejecución antes de la bifurcación
   se invocan en orden de registro inverso. Las funciones registradas
   para la ejecución después de la bifurcación (ya sea en el padre o
   en el hijo) se invocan en orden de registro.

   Tenga en cuenta que las llamadas "fork()" realizadas por código C
   de terceros no pueden llamar a esas funciones, a menos que
   explícitamente llame a "PyOS_BeforeFork()",
   "PyOS_AfterFork_Parent()" y "PyOS_AfterFork_Child()".

   No hay forma de cancelar el registro de una función.

   Availability: Unix, not WASI, not Android, not iOS.

   Added in version 3.7.

os.spawnl(mode, path, ...)
os.spawnle(mode, path, ..., env)
os.spawnlp(mode, file, ...)
os.spawnlpe(mode, file, ..., env)
os.spawnv(mode, path, args)
os.spawnve(mode, path, args, env)
os.spawnvp(mode, file, args)
os.spawnvpe(mode, file, args, env)

   Ejecute el programa *path* en un nuevo proceso.

   (Tenga en cuenta que el módulo "subprocess" proporciona funciones
   más potentes para generar nuevos procesos y recuperar sus
   resultados; es preferible usar ese módulo que usar estas funciones.
   Compruebe especialmente la sección Replacing Older Functions with
   the subprocess Module.)

   Si *mode* es "P_NOWAIT", esta función retorna la identificación del
   proceso del nuevo proceso; if *mode* is "P_WAIT", retorna el código
   de salida del proceso si sale normalmente, o "-signal", donde
   *signal* es la señal que mató el proceso. En Windows, la
   identificación del proceso en realidad será el identificador del
   proceso, por lo que se puede usar con la función "waitpid()".

   Nota sobre VxWorks, esta función no retorna "-signal" cuando se
   cierra el nuevo proceso. En su lugar, genera una excepción OSError.

   Las variantes "l" y "v" de las funciones "spawn*" difieren en la
   forma en que se pasan los argumentos de la línea de comandos. Las
   variantes "l" son quizás las más fáciles de usar si el número de
   parámetros es fijo cuando se escribe el código; los parámetros
   individuales simplemente se convierten en parámetros adicionales
   para las funciones "spawnl*()". Las variantes "v" son buenas cuando
   el número de parámetros es variable, y los argumentos se pasan en
   una lista o tupla como el parámetro *args*. En cualquier caso, los
   argumentos del proceso hijo deben comenzar con el nombre del
   comando que se está ejecutando.

   Las variantes que incluyen una segunda "p" cerca del final
   ("spawnlp()", "spawnlpe()", "spawnvp()", y "spawnvpe()") usarán
   "PATH" variable de entorno para ubicar el programa *file*. Cuando
   se reemplaza el entorno (usando uno de los siguientes "spawn*e"
   variantes, discutidas en el siguiente párrafo), el nuevo entorno se
   utiliza como fuente de la variable "PATH". Las otras variantes,
   "spawnl()", "spawnle()", "spawnv()", y "spawnve()", no utilizarán
   la variable "PATH" para localizar el ejecutable; *path* debe
   contener una ruta absoluta o relativa apropiada.

   Para "spawnle()", "spawnlpe()", "spawnve()", y "spawnvpe()" (tenga
   en cuenta que todo esto termina en "e"), el parámetro *env* debe
   ser un mapeo que se utiliza para definir las variables de entorno
   para el nuevo proceso (se utilizan en lugar del entorno del proceso
   actual); las funciones "spawnl()", "spawnlp()", "spawnv()" y
   "spawnvp()" hacen que el nuevo proceso herede el entorno del
   proceso actual. Tenga en cuenta que las claves y los valores en el
   diccionario *env* deben ser cadenas; Las teclas o valores no
   válidos harán que la función falle, con un valor de retorno de
   "127".

   Como ejemplo, las siguientes llamadas a "spawnlp()" y "spawnvpe()"
   son equivalentes:

      import os
      os.spawnlp(os.P_WAIT, 'cp', 'cp', 'index.html', '/dev/null')

      L = ['cp', 'index.html', '/dev/null']
      os.spawnvpe(os.P_WAIT, 'cp', L, os.environ)

   Lanza un evento de auditoría "os.spawn" con argumentos "mode",
   "path", "args", "env".

   Availability: Unix, Windows, not WASI, not Android, not iOS.

   "spawnlp()", "spawnlpe()", "spawnvp()" y "spawnvpe()" no están
   disponibles en Windows. "spawnle()" y "spawnve()" no son seguros
   para subprocesos en Windows; le recomendamos que utilice el módulo
   "subprocess" en su lugar.

   Distinto en la versión 3.6: Acepta un *objeto tipo ruta*.

   Soft deprecated since version 3.14: The "subprocess" module is
   recommended instead.

os.P_NOWAIT
os.P_NOWAITO

   Valores posibles para el parámetro *mode* de la familia de
   funciones "spawn*". Si se proporciona cualquiera de estos valores,
   las funciones "spawn*" retornarán tan pronto como se haya creado el
   nuevo proceso, con el identificador del proceso como valor de
   retorno.

   Availability: Unix, Windows.

os.P_WAIT

   Valor posible para el parámetro *mode* de la familia de funciones
   "spawn*". Si se proporciona como *mode*, las funciones "spawn*" no
   regresarán hasta que el nuevo proceso se haya ejecutado por
   completo y devolverán el código de salida del proceso cuya
   ejecución se realizó correctamente, o "-signal" si una señal
   finaliza el proceso.

   Availability: Unix, Windows.

os.P_DETACH
os.P_OVERLAY

   Valores posibles para el parámetro *mode* para "spawn*" familia de
   funciones. Estos son menos portátiles que los enumerados
   anteriormente. "P_DETACH" es similar a "P_NOWAIT", pero el nuevo
   proceso se desconecta de la consola del proceso de llamada. Si se
   usa "P_OVERLAY", el proceso actual será reemplazado; la función
   "spawn*" no volverá.

   Availability: Windows.

os.startfile(path[, operation][, arguments][, cwd][, show_cmd])

   Inicie un archivo con su aplicación asociada.

   Cuando no se especifica *operation*, esto actúa como hacer doble
   clic en el archivo en el Explorador de Windows o dar el nombre del
   archivo como argumento al comando **start** desde el shell de
   comandos interactivo: el archivo se abre con cualquier aplicación
   (si hay alguna) con la que esté asociada su extensión.

   Cuando se proporciona otro *operation*, debe ser un "verbo de
   comando" que especifique qué se debe hacer con el archivo. Los
   verbos comunes documentados por Microsoft son "'open'", "'print'" y
   "'edit'" (para usar en archivos), así como "'explore'" y "'find'"
   (para usar en directorios).

   Al iniciar una aplicación, especifique *arguments* para que se pase
   como una sola cadena. Es posible que este argumento no tenga ningún
   efecto cuando se utiliza esta función para iniciar un documento.

   El directorio de trabajo predeterminado se hereda, pero el
   argumento *cwd* puede anularlo. Este debería ser un camino
   absoluto. Un *path* relativo se resolverá contra este argumento.

   Utilice *show_cmd* para anular el estilo de ventana predeterminado.
   El efecto que esto tenga dependerá de la aplicación que se esté
   ejecutando. Los valores son números enteros, tal como lo admite la
   función "ShellExecute()" de Win32.

   "startfile()" retorna tan pronto como se inicia la aplicación
   asociada. No hay opción para esperar a que se cierre la aplicación
   y no hay forma de recuperar el estado de salida de la aplicación.
   El parámetro *path* es relativo al directorio actual o *cwd*. Si
   desea utilizar una ruta absoluta, asegúrese de que el primer
   carácter no sea una barra ("'/'") Utilice "pathlib" o la función
   "os.path.normpath()" para asegurarse de que las rutas estén
   codificadas correctamente para Win32.

   Para reducir la sobrecarga de inicio del intérprete, la función
   Win32 "ShellExecute()" no se resuelve hasta que se la llama por
   primera vez. Si no se puede resolver la función, se generará
   "NotImplementedError".

   Lanza un evento de auditoría "os.startfile" con argumentos "path",
   "operation".

   Lanza un evento de auditoria "os.startfile/2" con argumentos
   "path", "operation", "arguments", "cwd", "show_cmd".

   Availability: Windows.

   Distinto en la versión 3.10: Se agregaron los argumentos
   *arguments*, *cwd* y *show_cmd*, y el evento de auditoría
   "os.startfile/2".

os.system(command)

   Ejecute el comando (una cadena) en una subcapa. Esto se implementa
   llamando a la función C estándar "system()" y tiene las mismas
   limitaciones. Los cambios en "sys.stdin", etc. no se reflejan en el
   entorno del comando ejecutado. Si *command* genera alguna salida,
   se enviará al flujo de salida estándar del intérprete. El estándar
   C no especifica el significado del valor de retorno de la función
   C, por lo que el valor de retorno de la función de Python depende
   del sistema.

   En Unix, el valor de retorno es el estado de salida del proceso
   codificado en el formato especificado para "wait()".

   En Windows, el valor de retorno es el que retorna el shell del
   sistema después de ejecutar *command*. El shell viene dado por la
   variable de entorno de Windows "COMSPEC": generalmente es
   **cmd.exe**, que retorna el estado de salida de la ejecución del
   comando; En sistemas que utilizan un shell no nativo, consulte la
   documentación del shell.

   The "subprocess" module provides more powerful facilities for
   spawning new processes and retrieving their results; using that
   module is recommended to using this function.  See the Replacing
   Older Functions with the subprocess Module section in the
   "subprocess" documentation for some helpful recipes.

   En Unix, "waitstatus_to_exitcode()" puede ser usado para convertir
   el resultado (estado de salida) en un código de salida. En Windows,
   el resultado es directamente el código de salida.

   Lanza un evento de auditoría "os.system" con argumento "command".

   Availability: Unix, Windows, not WASI, not Android, not iOS.

os.times()

   Retorna los tiempos de proceso globales actuales. El valor de
   retorno es un objeto con cinco atributos:

   * "user" - tiempo de usuario

   * "system" - tiempo de sistema

   * "children_user" - tiempo de usuario de todos los procesos
     secundarios

   * "children_system" - hora del sistema de todos los procesos
     secundarios

   * "elapsed": tiempo real transcurrido desde un punto fijo en el
     pasado

   Por compatibilidad con versiones anteriores, este objeto también se
   comporta como una tupla de cinco que contiene "user", "system",
   "children_user", "children_system" y "elapsed" en ese orden.

   Consulte las páginas del manual de Unix *times(2)* y times(3) en
   Unix o the GetProcessTimes MSDN en Windows. En Windows, solo se
   conocen "user" y "system"; los demás atributos son cero.

   Availability: Unix, Windows.

   Distinto en la versión 3.3: El tipo de objeto retornado cambió de
   una tupla a un objeto tipo tupla con atributos con nombre.

os.wait()

   Espere a que se complete un proceso secundario y retorna una tupla
   que contenga su indicación de estado pid y de salida: un número de
   16 bits, cuyo byte bajo es el número de señal que mató el proceso y
   cuyo byte alto es el estado de salida (si la señal el número es
   cero); el bit alto del byte bajo se establece si se produjo un
   archivo central.

   Si no hay niños a los que esperar, se genera "ChildProcessError".

   "waitstatus_to_exitcode()" puede ser usado para convertir el estado
   de salida en el código de salida.

   Availability: Unix, not WASI, not Android, not iOS.

   Ver también:

     Las demás funciones "wait*()" documentadas a continuación se
     pueden utilizar para esperar a que se complete un proceso
     secundario específico y tener más opciones. "waitpid()" es la
     única que también está disponible en Windows.

os.waitid(idtype, id, options, /)

   Esperar a que se complete un proceso secundario.

   *idtype* puede ser "P_PID", "P_PGID", "P_ALL" o (en Linux)
   "P_PIDFD". La interpretación de *id* depende de ello; consulte sus
   descripciones individuales.

   *options* es una combinación OR de indicadores. Se requiere al
   menos uno de "WEXITED", "WSTOPPED" o "WCONTINUED"; "WNOHANG" y
   "WNOWAIT" son indicadores opcionales adicionales.

   El valor de retorno es un objeto que representa los datos
   contenidos en la estructura "siginfo_t" con los siguientes
   atributos:

   * "si_pid" (identificación del proceso)

   * "si_uid" (ID de usuario real del niño)

   * "si_signo" (siempre "SIGCHLD")

   * "si_status" (el estado de salida o el número de señal, según
     "si_code")

   * "si_code" (consulte "CLD_EXITED" para conocer los posibles
     valores)

   Si se especifica "WNOHANG" y no hay elementos secundarios
   coincidentes en el estado solicitado, se devuelve "None". De lo
   contrario, si no hay elementos secundarios coincidentes que se
   puedan esperar, se genera "ChildProcessError".

   Availability: Unix, not WASI, not Android, not iOS.

   Added in version 3.3.

   Distinto en la versión 3.13: Esta función ahora también está
   disponible en macOS.

os.waitpid(pid, options, /)

   Los detalles de esta función difieren en Unix y Windows.

   En Unix: espere a que se complete un proceso secundario dado por la
   identificación del proceso *pid*, y retorna una tupla que contenga
   su identificación del proceso y la indicación del estado de salida
   (codificado como para "wait()"). La semántica de la llamada se ve
   afectada por el valor del número entero *options*, que debe ser "0"
   para el funcionamiento normal.

   Si *pid* es mayor que "0", "waitpid()" solicita información de
   estado para ese proceso específico. Si *pid* es "0", la solicitud
   es para el estado de cualquier hijo en el grupo de procesos del
   proceso actual. Si *pid* es "-1", la solicitud corresponde a
   cualquier elemento secundario del proceso actual. Si *pid* es menor
   que "-1", se solicita el estado de cualquier proceso en el grupo de
   procesos "-pid" (el valor absoluto de *pid*).

   *options* es una combinación OR de indicadores. Si contiene
   "WNOHANG" y no hay hijos coincidentes en el estado solicitado, se
   devuelve "(0, 0)". De lo contrario, si no hay hijos coincidentes
   que se puedan esperar, se genera "ChildProcessError". Otras
   opciones que se pueden utilizar son "WUNTRACED" y "WCONTINUED".

   En Windows: espere a que se complete un proceso dado por el
   identificador de proceso *pid*, y retorna una tupla que contiene
   *pid*, y su estado de salida se desplazó a la izquierda en 8 bits
   (el desplazamiento facilita el uso de la función en la plataforma).
   A *pid* menor o igual que "0" no tiene un significado especial en
   Windows y genera una excepción. El valor de entero *options* no
   tiene ningún efecto. *pid* puede referirse a cualquier proceso cuya
   identificación sea conocida, no necesariamente un proceso hijo. Las
   funciones "spawn*" llamadas con "P_NOWAIT" retornan manejadores de
   proceso adecuados.

   "waitstatus_to_exitcode()" puede ser usado para convertir el estado
   de salida en el código de salida.

   Availability: Unix, Windows, not WASI, not Android, not iOS.

   Distinto en la versión 3.5: Si la llamada al sistema se interrumpe
   y el controlador de señal no genera una excepción, la función
   vuelve a intentar la llamada del sistema en lugar de generar una
   excepción "InterruptedError" (ver **PEP 475** para la
   justificación).

os.wait3(options)

   Similar a "waitpid()", excepto que no se proporciona ningún
   argumento de identificación de proceso y se devuelve una tupla de 3
   elementos que contiene la identificación del proceso del hijo, la
   indicación del estado de salida y la información de uso de
   recursos. Consulte "resource.getrusage()" para obtener detalles
   sobre la información de uso de recursos. El argumento *options* es
   el mismo que se proporciona a "waitpid()" y "wait4()".

   "waitstatus_to_exitcode()" puede ser usado para convertir el estado
   de salida al código de salida.

   Availability: Unix, not WASI, not Android, not iOS.

os.wait4(pid, options)

   Similar a "waitpid()", excepto que se devuelve una tupla de 3
   elementos que contiene el identificador del proceso secundario, la
   indicación del estado de salida y la información de uso de
   recursos. Consulte "resource.getrusage()" para obtener detalles
   sobre la información de uso de recursos. Los argumentos de
   "wait4()" son los mismos que los proporcionados a "waitpid()".

   "waitstatus_to_exitcode()" puede ser usado para convertir el estado
   de salida al código de salida.

   Availability: Unix, not WASI, not Android, not iOS.

os.P_PID
os.P_PGID
os.P_ALL
os.P_PIDFD

   Estos son los valores posibles para *idtype* en "waitid()". Afectan
   a la interpretación de *id*:

   * "P_PID": espera al niño cuyo PID es *id*.

   * "P_PGID": espera a cualquier niño cuyo ID de grupo de progreso
     sea *id*.

   * "P_ALL" - espera a cualquier hijo; *id* se ignora.

   * "P_PIDFD": espera al niño identificado por el descriptor de
     archivo *id* (un descriptor de archivo de proceso creado con
     "pidfd_open()").

   Availability: Unix, not WASI, not Android, not iOS.

   Nota:

     "P_PIDFD" solo está disponible en Linux >= 5.4.

   Added in version 3.3.

   Added in version 3.9: La constante "P_PIDFD".

os.WCONTINUED

   Esta bandera *options* para "waitpid()", "wait3()", "wait4()" y
   "waitid()" hace que se informe sobre los procesos secundarios si
   han continuado desde una detención del control de trabajo desde que
   se informaron por última vez.

   Availability: Unix, not WASI, not Android, not iOS.

os.WEXITED

   Esta bandera *options* para "waitid()" hace que se informen los
   procesos secundarios que han finalizado.

   Las demás funciones "wait*" siempre informan sobre los hijos que
   han finalizado, por lo que esta opción no está disponible para
   ellos.

   Availability: Unix, not WASI, not Android, not iOS.

   Added in version 3.3.

os.WSTOPPED

   Esta bandera *options* para "waitid()" hace que se informen los
   procesos secundarios que se han detenido por la entrega de una
   señal.

   Esta opción no está disponible para las demás funciones "wait*".

   Availability: Unix, not WASI, not Android, not iOS.

   Added in version 3.3.

os.WUNTRACED

   Esta bandera *options* para "waitpid()", "wait3()" y "wait4()" hace
   que también se informe sobre los procesos secundarios si se han
   detenido pero no se ha informado sobre su estado actual desde que
   se detuvieron.

   Esta opción no está disponible para "waitid()".

   Availability: Unix, not WASI, not Android, not iOS.

os.WNOHANG

   Esta bandera *options* hace que "waitpid()", "wait3()", "wait4()" y
   "waitid()" regresen inmediatamente si no hay ningún estado de
   proceso secundario disponible inmediatamente.

   Availability: Unix, not WASI, not Android, not iOS.

os.WNOWAIT

   Esta bandera *options* hace que "waitid()" deje al niño en un
   estado de espera, de modo que se pueda usar una llamada "wait*()"
   posterior para recuperar nuevamente la información del estado del
   niño.

   Esta opción no está disponible para las demás funciones "wait*".

   Availability: Unix, not WASI, not Android, not iOS.

os.CLD_EXITED
os.CLD_KILLED
os.CLD_DUMPED
os.CLD_TRAPPED
os.CLD_STOPPED
os.CLD_CONTINUED

   Estos son los valores posibles para "si_code" en el resultado
   devuelto por "waitid()".

   Availability: Unix, not WASI, not Android, not iOS.

   Added in version 3.3.

   Distinto en la versión 3.9: Agregado los valores "CLD_KILLED" y
   "CLD_STOPPED".

os.waitstatus_to_exitcode(status)

   Convertir un estado de espera a un código de salida.

   En Unix:

   * Si el proceso termino con normalidad (if "WIFEXITED(status)" is
     true, se retornan el estado de salida del proceso (return
     "WEXITSTATUS(status)"): resultado mayor o igual a 0.

   * Si el proceso fue terminado por una señal (if
     "WIFSIGNALED(status)" is true), retorna "-signum" donde *signum*
     es el numero de la señal que cause que el proceso termine (return
     "-WTERMSIG(status)"): resultado menor que 0.

   * En el caso contrario, se lanza un "ValueError".

   En Windows, retorna *status* desplazado a la derecha en 8 bits.

   En Unix, si el proceso esta siendo rastreado o si "waitpid()" fue
   llamado con la opción "WUNTRACED", el que llama debe revisar
   primero si "WIFSTOPPED(status)" es verdadero. La función no debe de
   ser llamada si "WIFSTOPPED(status)" es verdadero.

   Ver también:

     Funciones "WIFEXITED()", "WEXITSTATUS()", "WIFSIGNALED()",
     "WTERMSIG()", "WIFSTOPPED()", "WSTOPSIG()".

   Availability: Unix, Windows, not WASI, not Android, not iOS.

   Added in version 3.9.

Las siguientes funciones toman un código de estado del proceso
retornado por "system()", "wait()", o "waitpid()" como parámetro.
Pueden usarse para determinar la disposición de un proceso.

os.WCOREDUMP(status, /)

   Retorna "True" si se generó un volcado de núcleo para el proceso;
   de lo contrario, retorna "False".

   Esta función debe emplearse solo si "WIFSIGNALED()" es verdadero.

   Availability: Unix, not WASI, not Android, not iOS.

os.WIFCONTINUED(status)

   Devuelve "True" si un hijo detenido se ha reanudado mediante la
   entrega de "SIGCONT" (si el proceso ha continuado desde una
   detención del control de trabajo); de lo contrario, devuelve
   "False".

   Ver opción "WCONTINUED".

   Availability: Unix, not WASI, not Android, not iOS.

os.WIFSTOPPED(status)

   Retorna "True" si el proceso se detuvo mediante la entrega de una
   señal; de lo contrario, retorna "False".

   "WIFSTOPPED()" solo retorna "True" si la llamada "waitpid()" se
   realizó utilizando la opción "WUNTRACED" o cuando se rastrea el
   proceso (consulte *ptrace(2)*)

   Availability: Unix, not WASI, not Android, not iOS.

os.WIFSIGNALED(status)

   Retorna "True" si el proceso finalizó con una señal; de lo
   contrario, retorna "False".

   Availability: Unix, not WASI, not Android, not iOS.

os.WIFEXITED(status)

   Retorna "True" si el proceso finalizó normalmente, es decir,
   llamando a "exit()" o "_exit()", o volviendo de "main()"; de lo
   contrario, retorna "False".

   Availability: Unix, not WASI, not Android, not iOS.

os.WEXITSTATUS(status)

   Retorna el estado de salida del proceso.

   Esta función debe emplearse solo si "WIFEXITED()" es verdadero.

   Availability: Unix, not WASI, not Android, not iOS.

os.WSTOPSIG(status)

   Retorna la señal que hizo que el proceso se detuviera.

   Esta función debe emplearse solo si "WIFSTOPPED()" es verdadero.

   Availability: Unix, not WASI, not Android, not iOS.

os.WTERMSIG(status)

   Retorna el número de la señal que provocó la finalización del
   proceso.

   Esta función debe emplearse solo si "WIFSIGNALED()" es verdadero.

   Availability: Unix, not WASI, not Android, not iOS.

## Interfaz al planificador

Estas funciones controlan cómo el sistema operativo asigna el tiempo
de CPU a un proceso. Solo están disponibles en algunas plataformas
Unix. Para obtener información más detallada, consulte las páginas de
manual de Unix.

Added in version 3.3.

Las siguientes políticas de programación están expuestas si son
compatibles con el sistema operativo.

os.SCHED_OTHER

   La política de programación predeterminada.

os.SCHED_BATCH

   Política de programación para procesos intensivos en CPU que
   intenta preservar la interactividad en el resto de la computadora.

os.SCHED_DEADLINE

   Scheduling policy for tasks with deadline constraints.

   Added in version 3.14.

os.SCHED_IDLE

   Política de programación para tareas en segundo plano de prioridad
   extremadamente baja.

os.SCHED_NORMAL

   Alias for "SCHED_OTHER".

   Added in version 3.14.

os.SCHED_SPORADIC

   Política de programación para programas de servidor esporádicos.

os.SCHED_FIFO

   Una política de programación *First In First Out*.

os.SCHED_RR

   Una política de programación round-robin.

os.SCHED_RESET_ON_FORK

   Esta flag se puede OR con cualquier otra política de programación.
   Cuando un proceso con este indicador establece bifurcaciones, la
   política de programación y la prioridad de su hijo se restablecen a
   los valores predeterminados.

class os.sched_param(sched_priority)

   Esta clase representa los parámetros de programación ajustables
   utilizados en "sched_setparam()", "sched_setscheduler()" y
   "sched_getparam()". Es inmutable.

   Por el momento, solo hay un parámetro posible:

   sched_priority

      La prioridad de programación para una política de programación.

os.sched_get_priority_min(policy)

   Obtiene el valor de prioridad mínimo para *policy*. *policy* es una
   de las constantes de política de programación anteriores.

os.sched_get_priority_max(policy)

   Obtiene el valor de prioridad máxima para *policy*. *policy* es una
   de las constantes de política de programación anteriores.

os.sched_setscheduler(pid, policy, param, /)

   Establece la política de programación para el proceso con PID
   *pid*. Un *pid* de 0 significa el proceso de llamada. *policy* es
   una de las constantes de política de programación anteriores.
   *param* es una instancia de "sched_param".

os.sched_getscheduler(pid, /)

   Retorna la política de programación para el proceso con PID *pid*.
   Un *pid* de 0 significa el proceso de llamada. El resultado es una
   de las constantes de política de programación anteriores.

os.sched_setparam(pid, param, /)

   Establece los parámetros de programación para el proceso con PID
   *pid*. Un *pid* de 0 significa el proceso de llamada. *param* es
   una instancia de "sched_param".

os.sched_getparam(pid, /)

   Retorna los parámetros de programación como una instancia de
   "sched_param" para el proceso con PID *pid*. Un *pid* de 0
   significa el proceso de llamada.

os.sched_rr_get_interval(pid, /)

   Retorna el round-robin quantum en segundos para el proceso con PID
   *pid*. Un *pid* de 0 significa el proceso de llamada.

os.sched_yield()

   Voluntarily relinquish the CPU. See *sched_yield(2)* for details.

os.sched_setaffinity(pid, mask, /)

   Restringe el proceso con PID *pid* (o el proceso actual si es cero)
   a un conjunto de CPU. *mask* es un entero iterable que representa
   el conjunto de CPU a las que se debe restringir el proceso.

os.sched_getaffinity(pid, /)

   Devuelve el conjunto de CPU a las que está restringido el proceso
   con PID *pid*.

   Si *pid* es cero, devuelve el conjunto de CPU a las que está
   restringido el hilo de llamada del proceso actual.

   Véase también la función "process_cpu_count()".

## Información miscelánea del sistema

os.confstr(name, /)

   Retorna valores de configuración del sistema con valores de cadena.
   *name* especifica el valor de configuración para recuperar; puede
   ser una cadena que es el nombre de un valor de sistema definido;
   estos nombres se especifican en varios estándares (POSIX, Unix 95,
   Unix 98 y otros). Algunas plataformas también definen nombres
   adicionales. Los nombres conocidos por el sistema operativo host se
   dan como las claves del diccionario "confstr_names". Para las
   variables de configuración no incluidas en esa asignación, también
   se acepta pasar un número entero para *name*.

   Si el valor de configuración especificado por *name* no está
   definido, se retorna "None".

   Si *name* es una cadena y no se conoce, se excita "ValueError". Si
   el sistema host no admite un valor específico para *name*, incluso
   si está incluido en "confstr_names", se lanza un "OSError" con
   "errno.EINVAL" para el número de error .

   Availability: Unix.

os.confstr_names

   Nombres de mapeo de diccionario aceptados por "confstr()" a los
   valores enteros definidos para esos nombres por el sistema
   operativo host. Esto se puede usar para determinar el conjunto de
   nombres conocidos por el sistema.

   Availability: Unix.

os.cpu_count()

   Devuelve la cantidad de CPU lógicas en **system**. Devuelve "None"
   si no se determina.

   La función "process_cpu_count()" se puede utilizar para obtener la
   cantidad de CPU lógicas que puede utilizar el hilo que llama a
   **current process**.

   Added in version 3.4.

   Distinto en la versión 3.13: If "-X cpu_count" is given or
   "PYTHON_CPU_COUNT" is set, "cpu_count()" returns the override value
   *n*.

os.getloadavg()

   Retorna el número de procesos en la cola de ejecución del sistema
   promediada durante los últimos 1, 5 y 15 minutos o aumentos
   "OSError" si el promedio de carga no se pudo obtener.

   Availability: Unix.

os.process_cpu_count()

   Obtiene la cantidad de CPU lógicas que puede utilizar el subproceso
   que realiza la llamada a **current process**. Devuelve "None" si no
   se determina. Puede ser menor que "cpu_count()" según la afinidad
   de la CPU.

   La función "cpu_count()" se puede utilizar para obtener la cantidad
   de CPU lógicas en **system**.

   If "-X cpu_count" is given or "PYTHON_CPU_COUNT" is set,
   "process_cpu_count()" returns the override value *n*.

   See also the "sched_getaffinity()" function.

   Added in version 3.13.

os.sysconf(name, /)

   Retorna valores de configuración del sistema con valores enteros.
   Si el valor de configuración especificado por *name* no está
   definido, se retorna "-1". Los comentarios sobre el parámetro
   *name* para "confstr()" se aplican aquí también; El diccionario que
   proporciona información sobre los nombres conocidos viene dado por
   "sysconf_names".

   Availability: Unix.

os.sysconf_names

   Nombres de asignación de diccionario aceptados por "sysconf()" a
   los valores enteros definidos para esos nombres por el sistema
   operativo host. Esto se puede usar para determinar el conjunto de
   nombres conocidos por el sistema.

   Availability: Unix.

   Distinto en la versión 3.11: Agregue el nombre "'SC_MINSIGSTKSZ'".

Los siguientes valores de datos se utilizan para admitir operaciones
de manipulación de rutas. Estos están definidos para todas las
plataformas.

Las operaciones de nivel superior en los nombres de ruta se definen en
el módulo "os.path".

os.curdir

   La cadena constante utilizada por el sistema operativo para
   referirse al directorio actual. Esto es "'.'" Para Windows y POSIX.
   También disponible a través de "os.path".

os.pardir

   La cadena constante utilizada por el sistema operativo para hacer
   referencia al directorio principal. Esto es "'...'" para Windows y
   POSIX. También disponible a través de "os.path".

os.sep

   El carácter utilizado por el sistema operativo para separar los
   componentes del nombre de ruta. Esto es "'/'" para POSIX y "'\\'"
   para Windows. Tenga en cuenta que saber esto no es suficiente para
   poder analizar o concatenar nombres de ruta --- use
   "os.path.split()" y "os.path.join()" --- pero en ocasiones es útil.
   También disponible a través de "os.path".

os.altsep

   Un carácter alternativo utilizado por el sistema operativo para
   separar los componentes del nombre de ruta, o "None" si solo existe
   un carácter separador. Esto se establece en "'/'" en los sistemas
   Windows donde "sep" es una barra invertida. También disponible a
   través de "os.path".

os.extsep

   El carácter que separa el nombre de archivo base de la extensión;
   por ejemplo, el "'.'" en "os.py". También disponible a través de
   "os.path".

os.pathsep

   El carácter utilizado convencionalmente por el sistema operativo
   para separar los componentes de la ruta de búsqueda (como en
   "PATH"), como "':'" para POSIX o "';'" para Windows. También
   disponible a través de "os.path".

os.defpath

   La ruta de búsqueda predeterminada utilizada por "exec*p*" y
   "spawn*p*" si el entorno no tiene una tecla "'RUTA'". También
   disponible a través de "os.path".

os.linesep

   La cadena utilizada para separar (o, más bien, terminar) líneas en
   la plataforma actual. Este puede ser un solo carácter, como "'\n'"
   para POSIX, o varios caracteres, por ejemplo, "'\r\n'" para
   Windows. No utilice *os.linesep* como terminador de línea cuando
   escriba archivos abiertos en modo texto (el valor predeterminado);
   use un solo "'\n'" en su lugar, en todas las plataformas.

os.devnull

   La ruta del archivo del dispositivo nulo. Por ejemplo:
   "'/dev/null'" para POSIX, "'nul'" para Windows. También disponible
   a través de "os.path".

os.RTLD_LAZY
os.RTLD_NOW
os.RTLD_GLOBAL
os.RTLD_LOCAL
os.RTLD_NODELETE
os.RTLD_NOLOAD
os.RTLD_DEEPBIND

   Flags para usar con las funciones "setdlopenflags()" y
   "getdlopenflags()". Consulte la página del manual de Unix
   *dlopen(3)* para saber qué significan las diferentes flags.

   Added in version 3.3.

## Números al azar

os.getrandom(size, flags=0)

   Obtiene hasta *size* bytes aleatorios. La función puede retornar
   menos bytes que los solicitados.

   Estos bytes se pueden usar para generar generadores de números
   aleatorios en el espacio del usuario o para fines criptográficos.

   "getrandom()" se basa en la entropía obtenida de los controladores
   de dispositivos y otras fuentes de ruido ambiental. La lectura
   innecesaria de grandes cantidades de datos tendrá un impacto
   negativo en otros usuarios de los dispositivos "/dev/random" y
   "/dev/urandom".

   El argumento de banderas es una máscara de bits que puede contener
   cero o más de los siguientes valores unidos mediante OR:
   "os.GRND_RANDOM" y "GRND_NONBLOCK".

   Véase también el Linux getrandom() manual page.

   Availability: Linux >= 3.17.

   Added in version 3.6.

os.urandom(size, /)

   Retorna una cadena de bytes de bytes aleatorios *size* adecuados
   para uso criptográfico.

   Esta función retorna bytes aleatorios de una fuente de aleatoriedad
   específica del sistema operativo. Los datos retornados deben ser lo
   suficientemente impredecibles para las aplicaciones criptográficas,
   aunque su calidad exacta depende de la implementación del sistema
   operativo.

   En Linux, si la llamada al sistema "getrandom()" está disponible,
   se usa en modo de bloqueo: bloquee hasta que el grupo de entropía
   urandom del sistema se inicialice (el núcleo recopila 128 bits de
   entropía). Ver el **PEP 524** para la justificación. En Linux, la
   función "getrandom()" puede usarse para obtener bytes aleatorios en
   modo sin bloqueo (usando el indicador "GRND_NONBLOCK") o para
   sondear hasta que el grupo de entropía urandom del sistema se
   inicialice.

   En un sistema tipo Unix, los bytes aleatorios se leen desde el
   dispositivo "/dev/urandom". Si el dispositivo "/dev/urandom" no
   está disponible o no es legible, se genera la excepción
   "NotImplementedError".

   En Windows, usará "BCryptGenRandom()".

   Ver también:

     El módulo "secrets" proporciona funciones de nivel superior. Para
     obtener una interfaz fácil de usar con el generador de números
     aleatorios proporcionado por su plataforma, consulte
     "random.SystemRandom".

   Distinto en la versión 3.5: En Linux 3.17 y versiones posteriores,
   la llamada al sistema "getrandom()" ahora se usa cuando está
   disponible. En OpenBSD 5.6 y posterior, ahora se usa la función C
   "getentropy()". Estas funciones evitan el uso de un descriptor de
   archivo interno.

   Distinto en la versión 3.5.2: En Linux, si el syscall "getrandom()"
   bloquea (el grupo de entropía urandom aún no está inicializado),
   recurra a la lectura "/dev/urandom".

   Distinto en la versión 3.6: En Linux, "getrandom()" ahora se usa en
   modo de bloqueo para aumentar la seguridad.

   Distinto en la versión 3.11: En Windows, se utiliza
   "BCryptGenRandom()" en lugar de "CryptGenRandom()", que está en
   desuso.

os.GRND_NONBLOCK

   Por defecto, cuando lee desde "/dev/random", "getrandom()" bloquea
   si no hay bytes aleatorios disponibles, y cuando lee desde
   "/dev/urandom", bloquea si el grupo de entropía no tiene, sin
   embargo, se ha inicializado.

   Si se establece el indicador "GRND_NONBLOCK", entonces
   "getrandom()" no se bloquea en estos casos, sino que inmediatamente
   genera "BlockingIOError".

   Added in version 3.6.

os.GRND_RANDOM

   Si se establece este bit, los bytes aleatorios se extraen del grupo
   "/dev/random" en lugar del grupo "/dev/urandom".

   Added in version 3.6.
