---
title: '"platform" ---  Access to underlying platform''s identifying data'
source_url: https://docs.python.org/es/3
source_path: library/platform.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3480
---

# "platform" ---  Access to underlying platform's identifying data

**código fuente:** Lib/platform.py

======================================================================

Nota:

  Plataformas específicas listadas alfabéticamente, con Linux incluido
  en la sección de Unix.

## Cross platform

platform.architecture(executable=sys.executable, bits='', linkage='')

   Consulta el ejecutable provisto (por defecto el archivo binario del
   intérprete de Python) para obtener información de diversas
   arquitecturas.

   Retorna una tupla "(bits, linkage)", siendo *bits* la información
   sobre la arquitectura del procesador y *linkage* el formato de
   conexión usado por el ejecutable. Ambos valores se retornan como
   cadenas.

   Los valores que no se pueden determinar se retornan según lo
   indicado por los ajustes por defecto de los parámetros. Si bits se
   da como "''", el "sizeof(pointer)" (o "sizeof(long)" en la versión
   de Python < 1.5.2) se utiliza como indicador para el tamaño del
   puntero admitido.

   La función se basa en el comando "file" del sistema para realizar
   la tarea. Está disponible en la mayoría de las plataformas Unix, si
   no en todas, y en algunas plataformas que no son de Unix y solo si
   el ejecutable apunta al intérprete de Python. Unos valores por
   defecto se utilizan cuando no se satisfacen las necesidades
   anteriores.

   Nota:

     En macOS (y quizás en otras plataformas), los archivos
     ejecutables pueden ser archivos universales que contienen
     múltiples arquitecturas.Para saber si el intérprete actual es de
     64-bits, es más fiable consultar el atributo "sys.maxsize":

        is_64bits = sys.maxsize > 2**32

platform.machine()

   Retorna el tipo de máquina, por ejemplo "'i386'". Si no se puede
   determinar el valor, retorna una cadena vacía.

   The output is platform-dependent and may differ in casing and
   naming conventions.

platform.node()

   Retorna el nombre de la red del ordenador (¡tal vez no sea el
   nombre completo!). Si no se puede determinar el valor, se retorna
   una cadena vacía.

platform.platform(aliased=False, terse=False)

   Retorna una sola cadena identificando la plataforma subyacente con
   la mayor información útil posible.

   La salida se intenta que sea *humanamente legible* más que tratable
   por una máquina. Tal vez la salida sea diferente en diversas
   plataformas y eso mismo es lo que se pretende.

   Si *aliased* es verdadero, la función usará aliases para varias
   plataformas que informen de nombres de sistema que sean diferentes
   a sus nombres comunes. Por ejemplo, SunOS se reportará como
   Solaris. La función "system_alias()" ha sido usada para implementar
   esto.

   Estableciendo *terse* a verdadero provoca que la función retorne el
   mínimo de información necesaria para identificar la plataforma.

   Distinto en la versión 3.8: En macOS, la función ahora usa
   "mac_ver()", si retorna una cadena no vacía para obtener la versión
   de macOS más que la versión de darwin.

platform.processor()

   Retorna el nombre (real) del procesador. E.j. "'amdk6'".

   Una cadena vacía se retorna si el valor no se puede determinar.
   Destacar que muchas plataformas no proveen esta información o
   simplemente retorna los mismos valores que para "machine()", como
   hace NetBSD.

platform.python_build()

   Retorna una tupla "(buildno, builddate)" con *buildno* indicando el
   número de la build de Python y *builddate* su fecha de publicación
   como cadenas.

platform.python_compiler()

   Retorna la string con la identificación del compilador usado para
   compilar Python.

platform.python_branch()

   Retorna la string identificando la implementación de la rama SCM de
   Python.

platform.python_implementation()

   Retorna la string identificando la implementación de Python.
   Algunos valores posibles son: 'CPython', 'IronPython', 'Jython',
   'PyPy'.

platform.python_revision()

   Retorna la string identificando la implementación de la revisión
   SCM de Python.

platform.python_version()

   Retorna la versión de Python en formato de cadena de caracteres con
   la forma "'major.minor.patchlevel'" siendo *major* la versión
   principal, *minor* la versión menor y *patchlevel* el último parche
   aplicado.

   Destacar que a diferencia del "sys.version" de Python, el valor
   retornado siempre incluirá el último parche aplicado (siendo 0 por
   defecto).

platform.python_version_tuple()

   Retorna la versión de Python como una tupla "(major, minor,
   patchlevel)" de cadena, siendo *major* la versión principal,
   *minor* la versión menor y *patchlevel* último parche aplicado.

   Destacar que a diferencia del "sys.version" de Python, el valor
   retornado siempre incluirá el último parche aplicado (siendo "'0'"
   por defecto).

platform.release()

   Retorna la versión de publicación del sistema. Por ejemplo
   "'2.2.0'" o "'NT'". Si no se puede determinar el valor, retorna una
   cadena vacía.

   On iOS and Android, this is the user-facing OS release. To obtain
   the Darwin or Linux kernel release, use "os.uname()".

platform.system()

   Retorna el nombre del sistema/SO, como "'Linux'", "'Darwin'",
   "'Java'", "'Windows'". Si no se puede determinar el valor, retorna
   una cadena vacía.

   On iOS and Android, this returns the user-facing OS name (i.e,
   "'iOS", "'iPadOS'" or "'Android'"). To obtain the kernel name
   ("'Darwin'" or "'Linux'"), use "os.uname()".

platform.system_alias(system, release, version)

   Retorna la tupla "(system, release, version)" con los alias de los
   nombres comerciales usados por algunos sistemas siendo *system* el
   nombre comercial del sistema, *release* como la versión principal
   de publicación y *version* como el número de la versión del
   sistema. También hace cierta reordenación de la información en
   algunos casos donde se produjera algún tipo de confusión.

platform.version()

   Retorna la versión de la publicación del sistema. Por ejemplo: "'#3
   on degas'". Una cadena vacía se retorna en el caso de que el valor
   no pueda ser determinado.

platform.uname()

   Interfaz uname relativamente portable. Retorna una "namedtuple()"
   con seis atributos: "system", "node", "release", "version",
   "machine", and "processor".

   "processor" es resuelto de forma tardía, bajo demanda.

   Note: the first two attribute names differ from the names presented
   by "os.uname()", where they are named "sysname" and "nodename".

   Cualquier entrada que no pueda ser determinada se establece como
   "''".

   Distinto en la versión 3.3: El resultado ha cambiado de tupla
   "namedtuple()"..

   Distinto en la versión 3.9: "processor" es resuelto de forma tardía
   en lugar de inmediatamente.

platform.invalidate_caches()

   Clear out the internal cache of information, such as the "uname()".
   This is typically useful when the platform's "node()" is changed by
   an external process and one needs to retrieve the updated value.

   Added in version 3.14.

## Java platform

platform.java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))

   Versión de la interfaz de Jython.

   Retorna una tupla "(release, vendor, vminfo, osinfo)" con *vminfo*
   siendo una tupla "(vm_name, vm_release, vm_vendor)" y *osinfo*
   siendo una tupla "(os_name, os_version, os_arch)". Los valores que
   no se pueden determinar son establecidos por defecto por los
   parámetros (todos los valores predeterminados son "''").

   Deprecated since version 3.13, will be removed in version 3.15: It
   was largely untested, had a confusing API, and was only useful for
   Jython support.

## Windows platform

platform.win32_ver(release='', version='', csd='', ptype='')

   Obtiene información adicional de la versión de registro de windows
   y retorna una tupla "(release, version, csd, ptype)" la cual se
   refiere a la versión del sistema operativo, número de su versión ,
   nivel CSD (service pack) y el tipo de sistema operativo
   (multi/único procesador). Los valores que no se pueden determinar
   son establecidos por defecto por los parámetros (todos los valores
   predeterminados son una cadena vacía).

   As a hint: *ptype* is "'Uniprocessor Free'" on single processor NT
   machines and "'Multiprocessor Free'" on multi processor machines.
   The "'Free'" refers to the OS version being free of debugging code.
   It could also state "'Checked'" which means the OS version uses
   debugging code, i.e. code that checks arguments, ranges, etc.

platform.win32_edition()

   Retorna una cadena que representa la edición actual de Windows o
   "None" si el valor no puede ser determinado. Los valores posibles
   incluyen, entre otros, "'Enterprise'", "'IoTUAP'",
   "'ServerStandard'"  y "'nanoserver'".

   Added in version 3.8.

platform.win32_is_iot()

   Retorna "True" si la edición de Windows retornada por
   "win32_edition()" se reconoce como una edición IoT.

   Added in version 3.8.

## macOS platform

platform.mac_ver(release='', versioninfo=('', '', ''), machine='')

   Obtenga información de la versión de macOS y devuélvala como tupla
   "(release, versioninfo, machine)" con *versioninfo* como tupla
   "(version, dev_stage, non_release_version)".

   Cualquier registro que no puede ser determinado se establece como
   "''". Todas los registros de la tupla son cadenas.

## iOS platform

platform.ios_ver(system='', release='', model='', is_simulator=False)

   Get iOS version information and return it as a "namedtuple()" with
   the following attributes:

   * "system" is the OS name; either "'iOS'" or "'iPadOS'".

   * "release" is the iOS version number as a string (e.g., "'17.2'").

   * "model" is the device model identifier; this will be a string
     like "'iPhone13,2'" for a physical device, or "'iPhone'" on a
     simulator.

   * "is_simulator" is a boolean describing if the app is running on a
     simulator or a physical device.

   Entries which cannot be determined are set to the defaults given as
   parameters.

## Unix platforms

platform.libc_ver(executable=sys.executable, lib='', version='', chunksize=16384)

   Intenta determinar la versión libc al que está enlazado el fichero
   ejecutable (por defecto el intérprete de Python). Retorna una tupla
   de cadenas "(lib, version)" que tiene por defecto los parámetros
   que han sido introducidos en caso de que la búsqueda fallase.

   Destacar que esta función tiene un conocimiento íntimo de cómo las
   diferentes versiones de libc agregan símbolos al ejecutable.
   Probablemente sólo se puede utilizar para los ejecutables
   compilados mediante **gcc**.

   El archivo se lee y se analiza en fragmentos de bytes *chunksize*.

## Linux platforms

platform.freedesktop_os_release()

   Obtiene la identificación del sistema operativo del archivo "os-
   release" y la retorna como dict. El archivo "os-release" es un
   freedesktop.org standard y está disponible en la mayoría de las
   distribuciones de Linux. Una excepción notable son las
   distribuciones de Android y basadas en Android.

   Lanza "OSError" o subclase cuando no se pueden leer ni "/etc/os-
   release" ni "/usr/lib/os-release".

   En caso de éxito, la función retorna un diccionario donde las
   claves y los valores son cadenas de caracteres. Los valores tienen
   sus caracteres especiales como """ y "$" sin comillas. Los campos
   "NAME", "ID" y "PRETTY_NAME" siempre se definen de acuerdo con el
   estándar. Todos los demás campos son opcionales. Los proveedores
   pueden incluir campos adicionales.

   Tenga en cuenta que campos como "NAME", "VERSION" y "VARIANT" son
   cadenas de caracteres adecuadas para la presentación a los
   usuarios. Los programas deben usar campos como "ID", "ID_LIKE",
   "VERSION_ID" o "VARIANT_ID" para identificar distribuciones de
   Linux.

   Ejemplo:

      def get_like_distro():
          info = platform.freedesktop_os_release()
          ids = [info["ID"]]
          if "ID_LIKE" in info:
              # ids are space separated and ordered by precedence
              ids.extend(info["ID_LIKE"].split())
          return ids

   Added in version 3.10.

## Android platform

platform.android_ver(release='', api_level=0, manufacturer='', model='', device='', is_emulator=False)

   Get Android device information. Returns a "namedtuple()" with the
   following attributes. Values which cannot be determined are set to
   the defaults given as parameters.

   * "release" - Android version, as a string (e.g. ""14"").

   * "api_level" - API level of the running device, as an integer
     (e.g. "34" for Android 14). To get the API level which Python was
     built against, see "sys.getandroidapilevel()".

   * "manufacturer" - Manufacturer name.

   * "model" - Model name – typically the marketing name or model
     number.

   * "device" - Device name – typically the model number or a
     codename.

   * "is_emulator" - "True" if the device is an emulator; "False" if
     it's a physical device.

   Google maintains a list of known model and device names.

   Added in version 3.13.

## Command-line usage

"platform" can also be invoked directly using the "-m" switch of the
interpreter:

   python -m platform [--terse] [--nonaliased] [{nonaliased,terse} ...]

The following options are accepted:

--terse

   Print terse information about the platform. This is equivalent to
   calling "platform.platform()" with the *terse* argument set to
   "True".

--nonaliased

   Print platform information without system/OS name aliasing. This is
   equivalent to calling "platform.platform()" with the *aliased*
   argument set to "True".

You can also pass one or more positional arguments ("terse",
"nonaliased") to explicitly control the output format. These behave
similarly to their corresponding options.
