---
title: '"netrc" --- netrc file processing'
source_url: https://docs.python.org/es/3
source_path: library/netrc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3310
---

# "netrc" --- netrc file processing

**Código fuente:** Lib/netrc.py

======================================================================

La clase "netrc" analiza y encapsula el formato del fichero netrc,
usado por el programa Unix **ftp** y otros clientes FTP.

class netrc.netrc([file])

   A "netrc" instance or subclass instance encapsulates data from  a
   netrc file.  The initialization argument, if present, specifies the
   file to parse.  If no argument is given, the file ".netrc" in the
   user's home directory -- as determined by "os.path.expanduser()" --
   will be read.  Otherwise, a "FileNotFoundError" exception will be
   raised. Parse errors will raise "NetrcParseError" with diagnostic
   information including the file name, line number, and terminating
   token.

   If no argument is specified on a POSIX system, the presence of
   passwords in the ".netrc" file will raise a "NetrcParseError" if
   the file ownership or permissions are insecure (owned by a user
   other than the user running the process, or accessible for read or
   write by any other user). This implements security behavior
   equivalent to that of ftp and other programs that use ".netrc".
   Such security checks are not available on platforms that do not
   support "os.getuid()".

   Distinto en la versión 3.4: Añadida la comprobación de permisos
   POSIX.

   Distinto en la versión 3.7: "os.path.expanduser()" se usa para
   encontrar la localización del fichero ".netrc" cuando *file* no se
   pasa como argumento.

   Distinto en la versión 3.10: "netrc" prueba la codificación UTF-8
   antes de usar la codificación específica en la configuración
   regional. Ya no es necesario que la entrada en el archivo netrc
   contenga todos los tokens. El valor predeterminado para los tokens
   faltantes es una cadena de caracteres vacía. Todos los tokens y sus
   valores ahora pueden contener caracteres arbitrarios, como espacios
   en blanco y caracteres no ASCII. Si el nombre de login es anónimo,
   no se disparará el chequeo de seguridad.

exception netrc.NetrcParseError

   Excepción lanzada por la clase "netrc" cuando se encuentran errores
   sintácticos en el texto origen. Las instancias de esta excepción
   ofrecen tres atributos interesantes:

   msg

      Explicación textual del error.

   filename

      El nombre del archivo fuente.

   lineno

      El número de línea donde se encontró el error.

## Objetos netrc

Una instancia "netrc" tiene los siguientes métodos:

netrc.authenticators(host)

   Retorna una 3-tupla "(login, account, password)" para autenticarse
   contra *host*. Si el fichero netrc no contiene una entrada para el
   host dado, retorna una tupla asociada con la entrada por defecto.
   Si no están disponibles ni el host correspondiente ni la entrada
   por defecto, retorna "None".

netrc.__repr__()

   Vuelca los datos de la clase como una cadena de caracteres en el
   formato de un fichero netrc. (Esto descarta comentarios y puede
   reordenar las entradas.)

Las instancias de "netrc" tienen variables de instancia públicas:

netrc.hosts

   Diccionario que asocia nombres de hosts a tuplas "(login, account,
   password)". La entrada por defecto, si existe, está representada
   como un pseudo-host por ese nombre.

netrc.macros

   Diccionario que asocia nombres de macros a listas de cadenas de
   caracteres.
