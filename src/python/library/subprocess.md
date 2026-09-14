---
title: '"subprocess" --- Subprocess management'
source_url: https://docs.python.org/es/3
source_path: library/subprocess.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3960
---

# "subprocess" --- Subprocess management

**Código fuente:** Lib/subprocess.py

======================================================================

The "subprocess" module allows you to spawn new processes, connect to
their input/output/error pipes, and obtain their return codes.  This
module intends to replace several older modules and functions:

   os.system
   os.spawn*

Information about how the "subprocess" module can be used to replace
these modules and functions can be found in the following sections.

Ver también: **PEP 324** -- PEP de proposición del módulo *subprocess*

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

## Using the "subprocess" Module

La opción recomendada para invocar subprocesos es utilizar la función
"run()" para todos los casos al alcance de ésta. Para usos más
avanzados, se puede utilizar la interfaz de más bajo nivel "Popen".

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)

   Ejecuta la orden descrita por *args*. Espera a que termine y
   retorna una instancia de "CompletedProcess".

   Los argumentos mostrados en la definición superior son sólo los más
   comunes; que se describen posteriormente en Argumentos
   frecuentemente empleados (de ahí el uso de la notación por clave en
   la signatura abreviada). La signatura completa de la función es a
   grandes rasgos la misma que la del constructor de "Popen"; la
   mayoría de los argumentos de esta función se pasan a esa interfaz
   (no es el caso de  *timeout*,  *input*, *check* ni
   *capture_output*).

   If *capture_output* is true, stdout and stderr will be captured.
   When used, the internal "Popen" object is automatically created
   with *stdout* and *stderr* both set to "PIPE". The *stdout* and
   *stderr* arguments may not be supplied at the same time as
   *capture_output*. If you wish to capture and combine both streams
   into one, set *stdout* to "PIPE" and *stderr* to "STDOUT", instead
   of using *capture_output*.

   A *timeout* may be specified in seconds, it is internally passed on
   to "Popen.communicate()". If the timeout expires, the child process
   will be killed and waited for. The "TimeoutExpired" exception will
   be re-raised after the child process has terminated. The initial
   process creation itself cannot be interrupted on many platform APIs
   so you are not guaranteed to see a timeout exception until at least
   after however long process creation takes.

   The *input* argument is passed to "Popen.communicate()" and thus to
   the subprocess's stdin.  If used it must be a byte sequence, or a
   string if *encoding* or *errors* is specified or *text* is true.
   When used, the internal "Popen" object is automatically created
   with *stdin* set to "PIPE", and the *stdin* argument may not be
   used as well.

   Si *check* es verdadero y el proceso retorna un resultado distinto
   de cero, se lanzará una excepción "CalledProcessError". Los
   atributos de dicha excepción contendrán los argumentos, el código
   retornado y tanto stdout como stderr si se capturaron.

   Si se especifican *encoding* o *errors* o *text* es verdadero, se
   abrirán los objetos fichero para stdin, stdout y stderr en modo
   texto, con los *encoding* y *errors* especificados o los valores
   predeterminados de "io.TextIOWrapper". El argumento
   *universal_newlines* equivale a *text* y se admite por
   compatibilidad hacia atrás. Los objetos fichero se abren en modo
   binario por defecto.

   If *env* is not "None", it must be a mapping that defines the
   environment variables for the new process; these are used instead
   of the default behavior of inheriting the current process'
   environment. It is passed directly to "Popen". This mapping can be
   str to str on any platform or bytes to bytes on POSIX platforms
   much like "os.environ" or "os.environb".

   Ejemplos:

      >>> subprocess.run(["ls", "-l"])  # doesn't capture output
      CompletedProcess(args=['ls', '-l'], returncode=0)

      >>> subprocess.run("exit 1", shell=True, check=True)
      Traceback (most recent call last):
        ...
      subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

      >>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
      CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
      stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')

   Added in version 3.5.

   Distinto en la versión 3.6: Se añadieron los parámetros *encoding*
   y *errors*

   Distinto en la versión 3.7: Se añadió el parámetro *text* como
   alias más comprensible de *universal_newlines*. Se añadió el
   parámetro *capture_output*.

   Distinto en la versión 3.12: Changed Windows shell search order for
   "shell=True". The current directory and "%PATH%" are replaced with
   "%COMSPEC%" and "%SystemRoot%\System32\cmd.exe". As a result,
   dropping a malicious program named "cmd.exe" into a current
   directory no longer works.

class subprocess.CompletedProcess

   El valor retornado por "run()", que representa un proceso ya
   terminado.

   args

      Los argumentos utilizados para lanzar el proceso. Pueden ser una
      lista o una cadena.

   returncode

      Estado de salida del proceso hijo. Típicamente, un estado de
      salida 0 indica que la ejecución tuvo éxito.

      Un valor negativo "-N" indica que el hijo fue forzado a terminar
      con la señal "N" (solamente POSIX).

   stdout

      La salida estándar capturada del proceso hijo. Una secuencia de
      bytes, o una cadena si se llamó a "run()" con *encoding*,
      *errors*, o *text* establecidos a "True". "None" si no se
      capturó el error estándar.

      Si se ejecutó el proceso con "stderr=subprocess.STDOUT", stdout
      y stderr se combinarán en este atributo, y "stderr" será "None".

   stderr

      El error estándar capturado del proceso hijo. Una secuencia de
      bytes, o una cadena si se llamó a "run()" con *encoding*,
      *errors*, o *text* establecidos a "True". "None" si no se
      capturó el error estándar.

   check_returncode()

      Si "returncode" no es cero, lanza un "CalledProcessError".

   Added in version 3.5.

subprocess.DEVNULL

   Valor especial que se puede usar como argumento *stdin*, *stdout* o
   *stderr* de "Popen" y que indica que se usará el fichero especial
   "os.devnull".

   Added in version 3.3.

subprocess.PIPE

   Valor especial que se puede usar como argumento *stdin*, *stdout* o
   *stderr* de "Popen" y que indica que se abrirá un pipe al flujo
   indicado. Es útil para usarlo con "Popen.communicate()".

subprocess.STDOUT

   Valor especial que se puede usar de argumento *stderr* a "Popen" y
   que indica que el error estándar debería ir al mismo gestor que la
   salida estándar.

exception subprocess.SubprocessError

   Clase base para el resto de excepciones de este módulo.

   Added in version 3.3.

exception subprocess.TimeoutExpired

   Subclase de "SubprocessError", se lanza cuando expira un plazo de
   ejecución esperando a un proceso hijo.

   cmd

      Orden que se utilizó para lanzar el proceso hijo.

   timeout

      Plazo de ejecución en segundos.

   output

      Salida del proceso hijo si fue capturado por "run()" o
      "check_output()". De lo contrario, "None". Siempre es "bytes"
      cuando se capturó cualquier salida, independientemente de la
      configuración de "text=True". Puede permanecer "None" en lugar
      de "b''" cuando no se observó ningún resultado.

   stdout

      Alias de *output*, por simetría con "stderr".

   stderr

      Salida Stderr del proceso hijo si fue capturado por "run()". De
      lo contrario, "None". Siempre es "bytes" cuando se capturó la
      salida de stderr independientemente de la configuración de
      "text=True". Puede permanecer como "None" en lugar de "b''"
      cuando no se observó ninguna salida de stderr.

   Added in version 3.3.

   Distinto en la versión 3.5: Se añadieron los atributos *stdout* y
   *stderr*

exception subprocess.CalledProcessError

   Subclase de "SubprocessError", lanzada cuando un proceso ejecutado
   por "check_call()", "check_output()" o "run()" (con "check=True")
   devuelve un estado de salida distinto de cero.

   returncode

      Estado de salida del proceso hijo. Si el proceso terminó por
      causa de una señal, el estado será el número de la señal en
      negativo.

   cmd

      Orden que se utilizó para lanzar el proceso hijo.

   output

      Salida del proceso hijo si fue capturada por "run()" o
      "check_output()".  De otro modo, "None".

   stdout

      Alias de *output*, por simetría con "stderr".

   stderr

      Salida de *stderr* del proceso hijo si fue capturada por
      "run()". De otro modo, "None".

   Distinto en la versión 3.5: Se añadieron los atributos *stdout* y
   *stderr*

### Argumentos frecuentemente empleados

Para permitir una gran variedad de usos, el constructor de "Popen" (y
las funciones asociadas) aceptan un gran número de argumentos
opcionales. Para los usos más habituales, se pueden dejar de forma
segura los valores por defecto. Los argumentos más frecuentemente
necesarios son:

   *args* se requiere en todas las llamadas; debe ser una cadena o una
   secuencia de argumentos al programa. En general, es mejor
   proporcionar una secuencia de argumentos porque permite que el
   módulo se ocupe de las secuencias de escape y los entrecomillados
   de los argumentos (por ejemplo, para permitir espacios en los
   nombres de fichero). Si se pasa una cadena simple, se ha de
   especificar *shell* como "True" (ver más adelante) o la cadena debe
   ser el nombre del programa a ejecutar sin especificar ningún
   argumento.

   *stdin*, *stdout* and *stderr* specify the executed program's
   standard input, standard output and standard error file handles,
   respectively.  Valid values are "None", "PIPE", "DEVNULL", an
   existing file descriptor (a positive integer), and an existing
   *file object* with a valid file descriptor.  With the default
   settings of "None", no redirection will occur.  "PIPE" indicates
   that a new pipe to the child should be created.  "DEVNULL"
   indicates that the special file "os.devnull" will be used.
   Additionally, *stderr* can be "STDOUT", which indicates that the
   stderr data from the child process should be captured into the same
   file handle as for *stdout*.

   Si se especifican *encoding* o *errors*, o *text* (o su alias
   *universal_newlines*) es verdadero, se abrirán en modo texto los
   objetos fichero *stdin*, *stdout* y *stderr* usando los *encoding*
   y *errors* especificados en la llamada o los valores
   predeterminados de "io.TextIOWrapper".

   Para *stdin*, los saltos del línea "'\n'" de la entrada serán
   convertidos al separador de línea predeterminado "os.linesep". Para
   *stdout* y *stderr*, todos los saltos de línea de la salida serán
   convertidos a "'\n'". Hay más información en la documentación de la
   clase "io.TextIOWrapper" para el caso en que el argumento
   *newline* de su constructor es "None".

   Si no se usa el modo texto, *stdin*, *stdout* y *stderr* se abrirán
   como flujos binarios. No se realizará ninguna codificación ni
   conversión de salto de línea.

   Distinto en la versión 3.6: Added the *encoding* and *errors*
   parameters.

   Distinto en la versión 3.7: Se añadió el parámetro *text* como
   alias de *universal_newlines*.

   Nota:

     El atributo *newlines* de los objetos fichero "Popen.stdin",
     "Popen.stdout" y "Popen.stderr" no es actualizado por el método
     "Popen.communicate()".

   Si *shell* es "True", la orden especificada se ejecutará pasando
   por la shell. Esto tiene utilidad si se usa Python principalmente
   por el flujo de control mejorado sobre la mayoría de las shell de
   sistema, pero se desea también un acceso práctico a otras
   características de la shell, como pipes, nombres de fichero con
   comodines, expansión de variables de entorno o expansión de "~" al
   directorio *home* del usuario. Sin embargo, no se debe olvidar que
   el propio Python tiene implementaciones de muchas características
   tipo shell (en particular, "glob", "fnmatch", "os.walk()",
   "os.path.expandvars()", "os.path.expanduser()", y "shutil").

   Distinto en la versión 3.3: Cuando *universal_newlines* es "True",
   la clase usa la codificación "locale.getpreferredencoding(False)"
   en lugar de "locale.getpreferredencoding()".  Ver la clase
   "io.TextIOWrapper" para obtener más información sobre este cambio.

   Nota:

     Leer la sección Consideraciones sobre la seguridad antes de usar
     "shell=True".

Estas opciones y el resto se describen con más detalle en la
documentación del constructor de "Popen".

### El constructor de Popen

El proceso interno de creación y gestión de este módulo lo gestiona la
clase "Popen". Proporciona una gran flexibilidad para que los
desarrolladores sean capaces de gestionar los casos menos comunes que
quedan sin cubrir por las funciones auxiliares.

class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, group=None, extra_groups=None, user=None, umask=-1, encoding=None, errors=None, text=None, pipesize=-1, process_group=None)

   Ejecuta un programa hijo en un proceso nuevo. En POSIX, la clase
   usa  "os.execvp()" como comportamiento para lanzar el proceso hijo.
   En Windows, la clase usa la función "CreateProcess()" de Windows.
   Los argumentos de "Popen" son los siguientes.

   *args* debe ser o una secuencia de argumentos de programa o una
   cadena simple o un *objeto tipo ruta*. Por omisión, el programa a
   ejecutar es el primer elemento de *args* si *args* es una
   secuencia.  Si *args* es una cadena, la interpretación es
   dependiente de la plataforma, según se describe más abajo. Véase
   los argumentos *shell* y *executable* para más información sobre el
   comportamiento por defecto. Salvo que se indique, se recomienda
   pasar los *args* como una secuencia.

   Advertencia:

     Para obtener la máxima confiabilidad, use una ruta completa para
     el ejecutable. Para buscar un nombre no calificado en "PATH", use
     "shutil.which()". En todas las plataformas, pasar
     "sys.executable" es la forma recomendada de iniciar de nuevo el
     intérprete de Python actual y usar el formato de línea de
     comandos "-m" para iniciar un módulo instalado.La resolución de
     la ruta de *executable* (o el primer elemento de *args*) depende
     de la plataforma. Para POSIX, consulte "os.execvpe()", y tenga en
     cuenta que al resolver o buscar la ruta ejecutable, *cwd* anula
     el directorio de trabajo actual y *env* puede anular la variable
     de entorno "PATH". Para Windows, consulte la documentación de los
     parámetros "lpApplicationName" e "lpCommandLine" de WinAPI
     "CreateProcess", y tenga en cuenta que al resolver o buscar la
     ruta ejecutable con "shell = False", *cwd* no anula el directorio
     de trabajo actual y *env* no puede anular la variable de entorno
     "PATH". El uso de una ruta completa evita todas estas
     variaciones.

   Un ejemplo del paso de argumentos a un programa externo mediante
   una secuencia:

      Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])

   En POSIX, si *args* es una cadena se interpreta como el nombre o la
   ruta del programa que ejecutar. Sin embargo, esto solamente
   funciona si no hay que pasar argumentos al programa.

   Nota:

     Puede que no resulte evidente cómo descomponer una orden de la
     shell en una secuencia de argumentos, especialmente en casos
     complejos. "shlex.split()" puede aclarar cómo determinar la
     descomposición en tokens de *args*:

        >>> import shlex, subprocess
        >>> command_line = input()
        /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
        >>> args = shlex.split(command_line)
        >>> print(args)
        ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
        >>> p = subprocess.Popen(args) # Success!

     Hay que destacar en particular que las opciones (como *-input*) y
     los argumentos (como *eggs.txt*) que van separados por espacio en
     blanco en la shell van en elementos de lista separados, mientras
     los argumentos que necesitan entrecomillado o escapado de
     espacios cuando se usan en la shell (como los nombres de ficheros
     con espacios o la orden *echo* anteriormente mostrada) son
     elementos simples de la lista.

   En Windows, si *args* es una secuencia, se convertirá a cadena del
   modo descrito en Cómo convertir una secuencia de argumentos a una
   cadena en Windows. Esto es así porque la función de bajo nivel
   "CreateProcess()" funciona sobre cadenas.

   Distinto en la versión 3.6: El parámetro *args* toma un *objeto
   tipo ruta* si *shell* es "False" y una secuencia de objetos tipo
   fichero en POSIX.

   Distinto en la versión 3.8: El parámetro *args* toma un *objeto
   tipo ruta* si *shell* es "False" y una secuencia de bytes y objetos
   tipo fichero en Windows.

   El argumento *shell* ("False" por defecto) especifica si usar la
   shell como programa a ejecutar. Si *shell* es "True", se recomienda
   pasar *args* como cadena mejor que como secuencia.

   En POSIX con "shell=True", la shell predeterminada es "/bin/sh".
   Si *args* es una cadena, ésta especifica la orden a ejecutar por la
   shell. Esto significa que la cadena tiene que tener el formato que
   tendría si se tecleara en la línea de órdenes. Esto incluye, por
   ejemplo, el entrecomillado y las secuencias de escape necesarias
   para los nombres de fichero que contengan espacios. Si *args* es
   una secuencia, el primer elemento especifica la cadena de la orden
   y cualquier otro elemento será tratado como argumentos adicionales
   a la propia shell. De este modo, "Popen" hace el equivalente de:

      Popen(['/bin/sh', '-c', args[0], args[1], ...])

   En Windows con "shell=True", la variable de entorno "COMSPEC"
   especifica la shell predeterminada. Solamente hace falta
   especificar "shell=True" en Windows cuando la orden que se desea
   ejecutar es interna a la shell (como. **dir** o **copy**).  No hace
   falta especificar "shell=True" para ejecutar un fichero por lotes o
   un ejecutable de consola.

   Nota:

     Leer la sección Consideraciones sobre la seguridad antes de usar
     "shell=True".

   Se proporcionará *bufsize* como el argumento correspondiente a la
   función "open()" cuando se creen los objetos fichero de los flujos
   stdin/stdout/stderr:

   * "0" means unbuffered (read and write are one system call and can
     return short)

   * "1" means line buffered (only usable if "text=True" or
     "universal_newlines=True")

   * cualquier otro valor positivo indica que hay que usar un búfer de
     aproximadamente dicho tamaño

   * *bufsize* negativo (el valor por defecto) indica que se use el
     valor predeterminado del sistema, *io.DEFAULT_BUFFER_SIZE*.

   Distinto en la versión 3.3.1: *bufsize* now defaults to -1 to
   enable buffering by default to match the behavior that most code
   expects.  In versions prior to Python 3.2.4 and 3.3.1 it
   incorrectly defaulted to "0" which was unbuffered and allowed short
   reads.  This was unintentional and did not match the behavior of
   Python 2 as most code expected.

   El argumento *executable* especifica un programa de reemplazo que
   ejecutar. Esto es muy poco frecuente. Cuando "shell=False",
   *executable* reemplaza al programa especificado por *args*. Sin
   embargo, se pasan los *args* originales al programa. La mayoría de
   los programas tratan el programa especificado en los *args* como el
   nombre del programa, que puede ser diferente del programa realmente
   ejecutado. En POSIX, el nombre en *args* funciona como nombre
   visible en utilidades como  **ps**.  Si "shell=True", en POSIX el
   argumento *executable* especifica una shell de reemplazo de la
   predeterminada "/bin/sh".

   Distinto en la versión 3.6: El parámetro *executable* acepta un
   *objeto tipo ruta* en POSIX.

   Distinto en la versión 3.8: El parámetro *executable* acepta bytes
   y un *objeto tipo ruta* en POSIX.

   Distinto en la versión 3.12: Changed Windows shell search order for
   "shell=True". The current directory and "%PATH%" are replaced with
   "%COMSPEC%" and "%SystemRoot%\System32\cmd.exe". As a result,
   dropping a malicious program named "cmd.exe" into a current
   directory no longer works.

   *stdin*, *stdout* and *stderr* specify the executed program's
   standard input, standard output and standard error file handles,
   respectively.  Valid values are "None", "PIPE", "DEVNULL", an
   existing file descriptor (a positive integer), and an existing
   *file object* with a valid file descriptor.  With the default
   settings of "None", no redirection will occur.  "PIPE" indicates
   that a new pipe to the child should be created.  "DEVNULL"
   indicates that the special file "os.devnull" will be used.
   Additionally, *stderr* can be "STDOUT", which indicates that the
   stderr data from the applications should be captured into the same
   file handle as for *stdout*.

   Si se establece *preexec_fn* a un objeto invocable, se llamará a
   dicho objeto en el proceso hijo justo antes de que se ejecute el
   hijo. (solamente POSIX)

   Advertencia:

     El parámetro *preexec_fn* NO ES SEGURO para usar en presencia de
     hilos en su aplicación. El subproceso podría bloquearse antes de
     que se llame a exec.

   Nota:

     Si necesita modificar el entorno para el subproceso, use el
     parámetro *env* en lugar de hacerlo en un *preexec_fn*. Los
     parámetros *start_new_session* y *process_group* deben ocupar el
     lugar del código que usa *preexec_fn* para llamar a "os.setsid()"
     o "os.setpgid()" en el subproceso

   Distinto en la versión 3.8: Se ha abandonado el soporte de
   *preexec_fn* en subintérpretes. El uso de dicho parámetro en un
   subintérprete lanza "RuntimeError". La nueva restricción puede
   afectar a aplicaciones desplegadas en *mod_wsgi*, *uWSGI* y otros
   entornos incrustados.

   If *close_fds* is true, all file descriptors except "0", "1" and
   "2" will be closed before the child process is executed.  Otherwise
   when *close_fds* is false, file descriptors obey their inheritable
   flag as described in Herencia de los descriptores de archivos.

   En Windows, si *close_fds* es verdadero el proceso hijo no heredará
   ningún gestor de fichero salvo que se le pasen explícitamente en el
   elemento "handle_list" de "STARTUPINFO.lpAttributeList", o mediante
   redirección estándar.

   Distinto en la versión 3.2: El valor predeterminado de *close_fds*
   se cambió de "False" a lo antes descrito.

   Distinto en la versión 3.7: En Windows, el valor predeterminado de
   *close_fds* se cambió de "False" a "True" al redirigir los gestores
   estándar. Ahora es posible establecer *close_fds* a "True" cuando
   se redirigen los gestores estándar.

   *pass_fds* es una secuencia de descriptor de ficheros opcional que
   han de mantenerse abiertos entre el proceso padre e hijo. Si se
   proporciona un valor a *pass_fds* se fuerza *close_fds* a "True".
   (solamente POSIX)

   Distinto en la versión 3.2: Se añadió el parámetro *pass_fds*.

   Si *cwd* no es "None", la función cambia el directorio de trabajo a
   *cwd* antes de ejecutar el proceso hijo.  *cwd* puede ser una
   cadena, o un objeto bytes o *tipo ruta*. En POSIX, la función busca
   *executable* (o el primer elemento de *args*) relativo a *cwd* si
   la ruta del ejecutable es relativa.

   Distinto en la versión 3.6: El parámetro *cwd* acepta un *objeto
   tipo ruta* en POSIX.

   Distinto en la versión 3.7: El parámetro *cwd* acepta un *objeto
   tipo ruta* en Windows.

   Distinto en la versión 3.8: El parámetro *cwd* acepta un objeto
   bytes en Windows.

   Si *restore_signals* es verdadero (el valor por defecto) todas las
   señales que Python ha establecido a  SIG_IGN se restauran a SIG_DFL
   en el proceso hijo antes del *exec*. En la actualidad, esto incluye
   las señales SIGPIPE, SIGXFZ y SIGXFSZ (solamente POSIX).

   Distinto en la versión 3.2: Se añadió *restore_signals*.

   Si *start_new_session* es verdadero, la llamada al sistema
   "setsid()" se realizará en el proceso secundario antes de la
   ejecución del subproceso.

   Availability: POSIX

   Distinto en la versión 3.2: Se añadió *start_new_session*.

   Si *process_group* es un entero no negativo, la llamada al sistema
   "setpgid(0, value)" se realizará en el proceso secundario antes de
   la ejecución del subproceso.

   Availability: POSIX

   Distinto en la versión 3.11: Se agregó *process_group*.

   If *group* is not "None", the setregid() system call will be made
   in the child process prior to the execution of the subprocess. If
   the provided value is a string, it will be looked up via
   "grp.getgrnam()" and the value in "gr_gid" will be used. If the
   value is an integer, it will be passed verbatim. (POSIX only)

   Availability: POSIX

   Added in version 3.9.

   If *extra_groups* is not "None", the setgroups() system call will
   be made in the child process prior to the execution of the
   subprocess. Strings provided in *extra_groups* will be looked up
   via "grp.getgrnam()" and the values in "gr_gid" will be used.
   Integer values will be passed verbatim. (POSIX only)

   Availability: POSIX

   Added in version 3.9.

   If *user* is not "None", the setreuid() system call will be made in
   the child process prior to the execution of the subprocess. If the
   provided value is a string, it will be looked up via
   "pwd.getpwnam()" and the value in "pw_uid" will be used. If the
   value is an integer, it will be passed verbatim. (POSIX only)

   Nota:

     Specifying *user* will not drop existing supplementary group
     memberships! The caller must also pass "extra_groups=()" to
     reduce the group membership of the child process for security
     purposes.

   Availability: POSIX

   Added in version 3.9.

   Si *umask* no es negativo, la llamada a sistema umask() se hará en
   el proceso hijo antes de la ejecución del subproceso.

   Availability: POSIX

   Added in version 3.9.

   If *env* is not "None", it must be a mapping that defines the
   environment variables for the new process; these are used instead
   of the default behavior of inheriting the current process'
   environment. This mapping can be str to str on any platform or
   bytes to bytes on POSIX platforms much like "os.environ" or
   "os.environb".

   Nota:

     If specified, *env* must provide any variables required for the
     program to execute.  On Windows, in order to run a side-by-side
     assembly the specified *env* **must** include a valid
     "%SystemRoot%".

   Si se especifican *encoding* o *errors*, o *text* es verdadero, los
   objetos de archivo *stdin*, *stdout* y *stderr* se abren en modo de
   texto con los *encoding* y *errors* especificados, como se describe
   anteriormente en Argumentos frecuentemente empleados. El argumento
   *universal_newlines* es equivalente a *text* y se proporciona para
   compatibilidad con versiones anteriores. De forma predeterminada,
   los objetos de archivo se abren en modo binario.

   Added in version 3.6: Se añadieron *encoding* y *errors*.

   Added in version 3.7: Se añadió *text* como alias más legible de
   *universal_newlines*.

   If given, *startupinfo* will be a "STARTUPINFO" object, which is
   passed to the underlying "CreateProcess" function.

   If given, *creationflags*, can be one or more of the following
   flags:

   * "CREATE_NEW_CONSOLE"

   * "CREATE_NEW_PROCESS_GROUP"

   * "ABOVE_NORMAL_PRIORITY_CLASS"

   * "BELOW_NORMAL_PRIORITY_CLASS"

   * "HIGH_PRIORITY_CLASS"

   * "IDLE_PRIORITY_CLASS"

   * "NORMAL_PRIORITY_CLASS"

   * "REALTIME_PRIORITY_CLASS"

   * "CREATE_NO_WINDOW"

   * "DETACHED_PROCESS"

   * "CREATE_DEFAULT_ERROR_MODE"

   * "CREATE_BREAKAWAY_FROM_JOB"

   *pipeize* se puede usar para cambiar el tamaño de la tubería cuando
   "PIPE" se usa para *stdin*, *stdout* o *stderr*. El tamaño de la
   tubería solo se cambia en plataformas que lo admiten (solo Linux en
   este momento de redacción). Otras plataformas ignorarán este
   parámetro.

   Distinto en la versión 3.10: Added the *pipesize* parameter.

   Se puede usar los objetos Popen como gestores de contexto mediante
   sentencia "with": a la salida, los descriptores de flujo se cierran
   y se espera a que acabe el proceso.

      with Popen(["ifconfig"], stdout=PIPE) as proc:
          log.write(proc.stdout.read())

   Popen y el resto de las funciones de este módulo que la usan lanzan
   un evento de auditoría "subprocess.Popen" con argumentos
   "executable", "args", "cwd" y "env". El valor de "args" puede ser
   una cadena simple o un alista de cadenas, dependiendo de la
   plataforma.

   Distinto en la versión 3.2: Se añadió la funcionalidad de gestor de
   contexto.

   Distinto en la versión 3.6: El destructor de Popen ahora emite una
   advertencia "ResourceWarning" si el proceso hijo todavía se está
   ejecutando.

   Distinto en la versión 3.8: Popen puede usar "os.posix_spawn()" en
   algunos casos para obtener mejor rendimiento. En el Subsistema de
   Windows para Linux (WSL) y en la emulación del modo usuario de
   QEMU, el constructor de Popen que use "os.posix_spawn()" ya no
   lanzará una excepción cuando se den errores tales como que un
   programa no esté, sino que el proceso hijo fracasará con un
   "returncode" distinto de cero.

### Excepciones

Las excepciones lanzadas en el proceso hijo, antes de que el nuevo
programa haya empezado a ejecutarse, se relanzarán en el padre.

La excepción más común que se lanza es "OSError". Esto ocurre, por
ejemplo, al intentar ejecutar un archivo inexistente. Las aplicaciones
deben prepararse para excepciones "OSError". Tenga en cuenta que,
cuando "shell = True", "OSError" será lanzado por el hijo solo si no
se encontró el shell seleccionado. Para determinar si el shell no pudo
encontrar la aplicación solicitada, es necesario verificar el código
de retorno o la salida del subproceso.

Se lanzará un "ValueError" si se llama a "Popen" con argumentos no
válidos.

"check_call()" y "check_output()" lanzarán un "CalledProcessError" si
el proceso invocado retorna un código de retorno distinto de cero.

All of the functions and methods that accept a *timeout* parameter,
such as "run()" and "Popen.communicate()" will raise "TimeoutExpired"
if the timeout expires before the process exits.

Todas las excepciones definidas en este módulo heredan de
"SubprocessError".

Added in version 3.3: Se añadió la clase base "SubprocessError".

## Consideraciones sobre seguridad

Unlike some other popen functions, this library will not implicitly
choose to call a system shell.  This means that all characters,
including shell metacharacters, can safely be passed to child
processes. If the shell is invoked explicitly, via "shell=True", it is
the application's responsibility to ensure that all whitespace and
metacharacters are quoted appropriately to avoid shell injection
vulnerabilities. On some platforms, it is possible to use
"shlex.quote()" for this escaping.

On Windows, batch files ("*.bat" or "*.cmd") may be launched by the
operating system in a system shell regardless of the arguments passed
to this library. This could result in arguments being parsed according
to shell rules, but without any escaping added by Python. If you are
intentionally launching a batch file with arguments from untrusted
sources, consider passing "shell=True" to allow Python to escape
special characters. See gh-114539 for additional discussion.

## Objetos Popen

Las instancias de la clase "Popen" cuentan con los siguientes métodos:

Popen.poll()

   Comprueba si el proceso hijo ha finalizado. Establece y retorna el
   atributo "returncode". De lo contrario, retorna "None".

Popen.wait(timeout=None)

   Espera a que termine el proceso hijo. Establece y retorna el
   atributo "returncode".

   Si el proceso no finaliza tras *timeout* segundos, lanza una
   excepción "TimeoutExpired". Se puede capturar esta excepción para
   reintentar la espera.

   Nota:

     Esto causará un bloqueo cuando se use "stdout=PIPE" o
     "stderr=PIPE" y el proceso hijo genere suficiente salida hacia un
     pipe como para bloquear esperando que el búfer del pipe del SO
     acepte más datos. Se debe usar "Popen.communicate()" cuando se
     usen pipes para evitar esto.

   Nota:

     When the "timeout" parameter is not "None", then (on POSIX) the
     function is implemented using a busy loop (non-blocking call and
     short sleeps). Use the "asyncio" module for an asynchronous wait:
     see "asyncio.create_subprocess_exec".

   Distinto en la versión 3.3: Se añadió *timeout*.

Popen.communicate(input=None, timeout=None)

   Interactúa con el proceso: Envía datos a stdin. Lee datos de stdout
   y stderr hasta encontrar un fin-de-fichero. Espera a que termine el
   proceso y escribe el atributo "returncode". El argumento opcional
   *input* debe contener los datos que hay que enviar al proceso hijo
   o "None" si no hay que enviar datos al proceso hijo. Si se abrieron
   los flujos en modo texto, *input* ha de ser una cadena de
   caracteres. En caso contrario, debe contener bytes.

   "communicate()" retorna una tupla "(stdout_data, stderr_data)". Los
   datos serán cadenas si se abrieron los flujos en modo texto, en
   caso contrario serán bytes.

   Adviértase que si se desea enviar datos al stdin del proceso, se ha
   de crear el objeto Popen con "stdin=PIPE". Análogamente, para
   obtener algo diferente de "None" en la tupla del resultado, hay que
   suministrar "stdout=PIPE" o "stderr=PIPE" también.

   If the process does not terminate after *timeout* seconds, a
   "TimeoutExpired" exception will be raised.  Catching this exception
   and retrying communication will not lose any output.  Supplying
   *input* to a subsequent post-timeout "communicate()" call is in
   undefined behavior and may become an error in the future.

   No se matará el proceso si vence el plazo de ejecución, así que
   para hacer limpieza, una aplicación correcta debería matar el
   proceso y terminar la comunicación:

      proc = subprocess.Popen(...)
      try:
          outs, errs = proc.communicate(timeout=15)
      except TimeoutExpired:
          proc.kill()
          outs, errs = proc.communicate()

   After a call to "communicate()" raises "TimeoutExpired", do not
   call "wait()". Use an additional "communicate()" call to finish
   handling pipes and populate the "returncode" attribute.

   Nota:

     Los datos leídos pasan por un búfer en memoria, así que no se ha
     de usar este método para un tamaño de datos grande o ilimitado.

   Distinto en la versión 3.3: Se añadió *timeout*.

Popen.send_signal(signal)

   Envía la señal *signal* al proceso hijo.

   No hace nada si el proceso ya ha terminado.

   Nota:

     En Windows, SIGTERM es un alias de "terminate()". CTRL_C_EVENT y
     CTRL_BREAK_EVENT se pueden enviar a procesos iniciados con un
     parámetro *creationflags* que incluye "CREATE_NEW_PROCESS_GROUP".

Popen.terminate()

   Stop the child. On POSIX OSs the method sends "SIGTERM" to the
   child. On Windows the Win32 API function "TerminateProcess()" is
   called to stop the child.

Popen.kill()

   Mata el proceso hijo. En sistemas operativos POSIX la función envía
   SIGKILL al proceso hijo. En Windows "kill()" es un alias de
   "terminate()".

The following attributes are also set by the class for you to access.
Reassigning them to new values is unsupported:

Popen.args

   El argumento *args* según se pasó a "Popen": o una secuencia de
   argumentos del programa o una cadena sencilla.

   Added in version 3.3.

Popen.stdin

   If the *stdin* argument was "PIPE", this attribute is a writeable
   stream object as returned by "open()". If the *encoding* or
   *errors* arguments were specified or the *text* or
   *universal_newlines* argument was "True", the stream is a text
   stream, otherwise it is a byte stream. If the *stdin* argument was
   not "PIPE", this attribute is "None".

Popen.stdout

   If the *stdout* argument was "PIPE", this attribute is a readable
   stream object as returned by "open()". Reading from the stream
   provides output from the child process. If the *encoding* or
   *errors* arguments were specified or the *text* or
   *universal_newlines* argument was "True", the stream is a text
   stream, otherwise it is a byte stream. If the *stdout* argument was
   not "PIPE", this attribute is "None".

Popen.stderr

   If the *stderr* argument was "PIPE", this attribute is a readable
   stream object as returned by "open()". Reading from the stream
   provides error output from the child process. If the *encoding* or
   *errors* arguments were specified or the *text* or
   *universal_newlines* argument was "True", the stream is a text
   stream, otherwise it is a byte stream. If the *stderr* argument was
   not "PIPE", this attribute is "None".

Advertencia:

  Se ha de usar "communicate()" en lugar de ".stdin.write",
  ".stdout.read" o ".stderr.read" para evitar bloqueos por búfer de
  pipes del SO llenos que puedan bloquear el proceso hijo.

Popen.pid

   El ID de proceso del hijo.

   Adviértase que si se establece el argumento *shell* a "True", éste
   es el ID de proceso del la shell generada.

Popen.returncode

   The child return code. Initially "None", "returncode" is set by a
   call to the "poll()", "wait()", or "communicate()" methods if they
   detect that the process has terminated.

   A "None" value indicates that the process hadn't yet terminated at
   the time of the last method call.

   Un valor negativo "-N" indica que el hijo fue forzado a terminar
   con la señal "N" (solamente POSIX).

   When "shell=True", the return code reflects the exit status of the
   shell itself (e.g. "/bin/sh"), which may map signals to codes such
   as "128+N". See the documentation of the shell (for example, the
   Bash manual's Exit Status) for details.

## Elementos auxiliares de Popen en Windows

La clase "STARTUPINFO" y las siguientes constantes sólo están
disponibles en Windows.

class subprocess.STARTUPINFO(*, dwFlags=0, hStdInput=None, hStdOutput=None, hStdError=None, wShowWindow=0, lpAttributeList=None)

   Se utiliza un soporte parcial de la estructura STARTUPINFO de
   Windows para la creación de "Popen". Se pueden establecer los
   siguientes atributos pasándolos como argumentos sólo por clave.

   Distinto en la versión 3.7: Se añadió el soporte de argumentos sólo
   por clave.

   dwFlags

      Un campo bit que determina si se usan ciertos atributos de
      "STARTUPINFO" cuando el proceso crea una ventana.

         si = subprocess.STARTUPINFO()
         si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW

   hStdInput

      Si "dwFlags" especifica "STARTF_USESTDHANDLES", este atributo es
      el gestor de entrada estándar del proceso. Si no se especifica
      "STARTF_USESTDHANDLES", el valor predeterminado de entrada
      estándar es el búfer de teclado.

   hStdOutput

      Si "dwFlags" especifica "STARTF_USESTDHANDLES", este atributo es
      el gestor de salida estándar del proceso. En caso contrario, se
      hace caso omiso del atributo y el valor predeterminado de salida
      estándar es el búfer de ventana.

   hStdError

      Si "dwFlags" especifica "STARTF_USESTDHANDLES", este atributo es
      el gestor de error estándar del proceso. En caso contrario, se
      hace caso omiso del atributo y el valor predeterminado de error
      estándar es el búfer de ventana.

   wShowWindow

      Si "dwFlags" especifica "STARTF_USESHOWWINDOW", este atributo
      puede ser cualquiera de los valores que pueden especificarse en
      el parámetro "nCmdShow" para la función ShowWindow, salvo
      "SW_SHOWDEFAULT". De otro modo, se hace caso omiso del atributo.

      Se proporciona "SW_HIDE" para este atributo. Se usa cuando se
      llama a "Popen" con "shell=True".

   lpAttributeList

      Un diccionario de atributos adicionales para la creación del
      proceso, según "STARTUPINFOEX", véase UpdateProcThreadAttribute.

      Atributos admitidos:

      **handle_list**
         Una secuencia de gestores que se heredará. *close_fds* debe
         ser verdadero si no viene vacío.

         Los gestores deben hacerse temporalmente heredables por
         "os.set_handle_inheritable()" cuando se pasan al constructor
         de "Popen" o de lo contrario, se lanzará "OSError" con el
         error de Windows "ERROR_INVALID_PARAMETER" (87).

         Advertencia:

           En un proceso multihilo, hay que evitar filtrar gestores no
           heredables cuando se combina esta característica con
           llamadas concurrentes a otras funciones de creación de
           procesos que heredan todos los gestores, como
           "os.system()". Esto también rige para la redirección de
           gestores estándar, que crea temporalmente gestores
           heredables.

      Added in version 3.7.

### Constantes de Windows

The "subprocess" module exposes the following constants.

subprocess.STD_INPUT_HANDLE

   El dispositivo de entrada estándar. Inicialmente, es el búfer de
   entrada de la consola, "CONIN$".

subprocess.STD_OUTPUT_HANDLE

   El dispositivo de salida estándar. Inicialmente, es el búfer de
   pantalla de la consola activa, "CONOUT$".

subprocess.STD_ERROR_HANDLE

   El dispositivo de error estándar. Inicialmente, es el búfer de
   pantalla de la consola activa, "CONOUT$".

subprocess.SW_HIDE

   Oculta la ventana. Se activará otra ventana.

subprocess.STARTF_USESTDHANDLES

   Especifica que los atributos "STARTUPINFO.hStdInput",
   "STARTUPINFO.hStdOutput", y "STARTUPINFO.hStdError" contienen
   información adicional.

subprocess.STARTF_USESHOWWINDOW

   Especifica que el atributo "STARTUPINFO.wShowWindow" contiene
   información adicional.

subprocess.STARTF_FORCEONFEEDBACK

   A "STARTUPINFO.dwFlags" parameter to specify that the *Working in
   Background* mouse cursor will be displayed while a process is
   launching. This is the default behavior for GUI processes.

   Added in version 3.13.

subprocess.STARTF_FORCEOFFFEEDBACK

   A "STARTUPINFO.dwFlags" parameter to specify that the mouse cursor
   will not be changed when launching a process.

   Added in version 3.13.

subprocess.CREATE_NEW_CONSOLE

   El nuevo proceso obtiene una nueva consola, en lugar de heredar la
   consola del padre (que es el comportamiento predeterminado).

subprocess.CREATE_NEW_PROCESS_GROUP

   Un parámetro "Popen" "creationflags" para especificar que se cree
   un nuevo grupo de procesos. Este indicador es necesario para usar
   "os.kill()" sobre el subproceso.

   Este indicador no se tiene en cuenta si se especifica
   "CREATE_NEW_CONSOLE".

subprocess.ABOVE_NORMAL_PRIORITY_CLASS

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso tendrá una prioridad superior a la media.

   Added in version 3.7.

subprocess.BELOW_NORMAL_PRIORITY_CLASS

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso tendrá una prioridad inferior a la media.

   Added in version 3.7.

subprocess.HIGH_PRIORITY_CLASS

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso tendrá una prioridad elevada.

   Added in version 3.7.

subprocess.IDLE_PRIORITY_CLASS

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso tendrá una la mínima prioridad.

   Added in version 3.7.

subprocess.NORMAL_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have a normal priority. (default)

   Added in version 3.7.

subprocess.REALTIME_PRIORITY_CLASS

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso tendrá una prioridad de tiempo real. Raramente se debería
   usar REALTIME_PRIORITY_CLASS, porque esto interrumpe los hilos que
   gestionan la entrada del ratón y del teclado, así como la gestión
   del volcado de búfer del disco. Esta clase es apropiada para
   aplicaciones que se comunican directamente con el hardware o que
   llevan a cabo tareas breves que no admitan interrupciones.

   Added in version 3.7.

subprocess.CREATE_NO_WINDOW

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso no creará una ventana.

   Added in version 3.7.

subprocess.DETACHED_PROCESS

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso no heredará la consola del padre. Este valor es
   incompatible con CREATE_NEW_CONSOLE.

   Added in version 3.7.

subprocess.CREATE_DEFAULT_ERROR_MODE

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso no hereda el modo de error del proceso padre. En su lugar,
   el proceso parte del modo de error predeterminado. Esta
   característica es particularmente útil para aplicaciones de shell
   multihilo que se ejecutan con los errores 'duros' desactivados.

   Added in version 3.7.

subprocess.CREATE_BREAKAWAY_FROM_JOB

   Parámetro "Popen" "creationflags" para especificar que el nuevo
   proceso no está asociado a la tarea.

   Added in version 3.7.

## Antigua API de alto nivel

Antes de Python 3.5, estas tres funciones conformaban la API de alto
nivel para subprocesos. Ahora se puede usar "run()" en muchos casos,
pero hay mucho código escrito con estas funciones.

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)

   Ejecutar la orden descrita por *args*. Esperar que la orden se
   complete y retornar al atributo "returncode".

   El código que requiera capturar stdout o stderr debería usar
   "run()" en su lugar:

      run(...).returncode

   Para suprimir stdout o stderr se ha de proporcionar un valor de
   "DEVNULL".

   Se muestran algunos argumentos comunes. La signatura completa de la
   función es la misma que la del constructor de "Popen"; esta función
   pasa todos los argumentos proporcionados (salvo *timeout*)
   directamente a esa interfaz.

   Nota:

     No usar "stdout=PIPE" ni "stderr=PIPE" con esta función. El
     proceso hijo se bloqueará si genera suficiente salida a un pipe
     como para saturar el búfer del pipe del sistema operativo
     mientras no se lee de los pipes.

   Distinto en la versión 3.3: Se añadió *timeout*.

   Distinto en la versión 3.12: Changed Windows shell search order for
   "shell=True". The current directory and "%PATH%" are replaced with
   "%COMSPEC%" and "%SystemRoot%\System32\cmd.exe". As a result,
   dropping a malicious program named "cmd.exe" into a current
   directory no longer works.

subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)

   Ejecuta la instrucción con argumentos. Espera a que la instrucción
   se complete. Si el código de retorno es cero retorna; en caso
   contrario, lanza "CalledProcessError". El objeto
   "CalledProcessError" tendrá el código de retorno en el atributo
   "returncode".Si "check_call()" no pudo iniciar el proceso,
   propagará la excepción que fue lanzada.

   El código que requiera capturar stdout o stderr debería usar
   "run()" en su lugar:

      run(..., check=True)

   Para suprimir stdout o stderr se ha de proporcionar un valor de
   "DEVNULL".

   Se muestran algunos argumentos comunes. La signatura completa de la
   función es la misma que la del constructor de "Popen"; esta función
   pasa todos los argumentos proporcionados (salvo *timeout*)
   directamente a esa interfaz.

   Nota:

     No usar "stdout=PIPE" ni "stderr=PIPE" con esta función. El
     proceso hijo se bloqueará si genera suficiente salida a un pipe
     como para saturar el búfer del pipe del sistema operativo
     mientras no se lee de los pipes.

   Distinto en la versión 3.3: Se añadió *timeout*.

   Distinto en la versión 3.12: Changed Windows shell search order for
   "shell=True". The current directory and "%PATH%" are replaced with
   "%COMSPEC%" and "%SystemRoot%\System32\cmd.exe". As a result,
   dropping a malicious program named "cmd.exe" into a current
   directory no longer works.

subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, cwd=None, encoding=None, errors=None, universal_newlines=None, timeout=None, text=None, **other_popen_kwargs)

   Ejecuta orden con argumentos y retorna su salida.

   Si el código de retorno fue diferente de cero lanza un
   "CalledProcessError". El objeto "CalledProcessError" tendrá el
   código de retorno en el atributo "returncode" y los datos de salida
   en el atributo "output".

   Esto equivale a:

      run(..., check=True, stdout=PIPE).stdout

   Los argumentos mostrados arriba son meramente algunos de los
   comunes. La signatura completa de la función es casi la misma que
   la de "run()" - la mayoría de los argumentos se pasa directamente a
   esa interfaz. Existe una diferencia con la interfaz de "run()"
   respecto al comportamiento: pasar "input=None" genera el mismo
   comportamiento que "input=b''" (o "input=''", dependiendo de otros
   argumentos) en vez de usar el flujo entrada estándar del padre.

   Por omisión, esta función retornará los datos como bytes
   codificados. La codificación real de los datos podría depender de
   la orden invocada, por lo que la decodificación a texto se deberá
   hacer al nivel de la aplicación.

   Este comportamiento se puede modificar estableciendo *text*,
   *encoding*, *errors*, o *universal_newlines* a "True", como se
   describe en Argumentos frecuentemente empleados y "run()".

   Para capturar también el error estándar del resultado se debe usar
   "stderr=subprocess.STDOUT":

      >>> subprocess.check_output(
      ...     "ls non_existent_file; exit 0",
      ...     stderr=subprocess.STDOUT,
      ...     shell=True)
      'ls: non_existent_file: No such file or directory\n'

   Added in version 3.1.

   Distinto en la versión 3.3: Se añadió *timeout*.

   Distinto en la versión 3.4: Se añadió soporte para el argumento por
   clave *input*.

   Distinto en la versión 3.6: Se añadieron *encoding* y *errors*.
   Ver "run()" para más detalles.

   Added in version 3.7: Se añadió *text* como alias más legible de
   *universal_newlines*.

   Distinto en la versión 3.12: Changed Windows shell search order for
   "shell=True". The current directory and "%PATH%" are replaced with
   "%COMSPEC%" and "%SystemRoot%\System32\cmd.exe". As a result,
   dropping a malicious program named "cmd.exe" into a current
   directory no longer works.

## Replacing Older Functions with the "subprocess" Module

En esta sección, "a se convierte en b" significa que b se puede usar
en lugar de.

Nota:

  Todas las funciones "a" de esta sección fracasan silenciosamente (o
  casi) si no se halla el programa ejecutado; las funciones de
  reemplazo "b" lanzan "OSError" en lugar de esto.Además, las
  funciones de reemplazo que usan "check_output()" fracasarán con un
  error "CalledProcessError" si la operación solicitada produce un
  código de retorno diferente de cero. La salida queda disponible en
  el atributo "output" de la excepción lanzada.

In the following examples, we assume that the relevant functions have
already been imported from the "subprocess" module.

### Cómo reemplazar la sustitución de órdenes de **/bin/sh**

   output=$(mycmd myarg)

se convierte en:

   output = check_output(["mycmd", "myarg"])

### Cómo remplazar los flujos de la shell

   output=$(dmesg | grep hda)

se convierte en:

   p1 = Popen(["dmesg"], stdout=PIPE)
   p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
   p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
   output = p2.communicate()[0]

La llamada a "p1.stdout.close()" tras lanzar *p2* es importante para
que *p1* reciba un SIGPIPE si *p2* retorna antes que *p1*.

Alternativamente, para entrada de confianza, se puede usar el propio
soporte de pipeline de la shell directamente:

   output=$(dmesg | grep hda)

se convierte en:

   output = check_output("dmesg | grep hda", shell=True)

### Cómo reemplazar "os.system()"

   sts = os.system("mycmd" + " myarg")
   # becomes
   retcode = call("mycmd" + " myarg", shell=True)

Notas:

* No suele hacer falta llamar al programa a través de la shell.

* El valor de retorno de "call()" se codifica de forma diferente al de
  "os.system()".

* The "os.system()" function ignores SIGINT and SIGQUIT signals while
  the command is running, but the caller must do this separately when
  using the "subprocess" module.

Un ejemplo más creíble:

   try:
       retcode = call("mycmd" + " myarg", shell=True)
       if retcode < 0:
           print("Child was terminated by signal", -retcode, file=sys.stderr)
       else:
           print("Child returned", retcode, file=sys.stderr)
   except OSError as e:
       print("Execution failed:", e, file=sys.stderr)

### Cómo reemplazar la familia "os.spawn"

Ejemplo de P_NOWAIT:

   pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
   ==>
   pid = Popen(["/bin/mycmd", "myarg"]).pid

Ejemplo de P_WAIT:

   retcode = os.spawnlp(os.P_WAIT, "/bin/mycmd", "mycmd", "myarg")
   ==>
   retcode = call(["/bin/mycmd", "myarg"])

Ejemplo de vector:

   os.spawnvp(os.P_NOWAIT, path, args)
   ==>
   Popen([path] + args[1:])

Ejemplo de entorno:

   os.spawnlpe(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg", env)
   ==>
   Popen(["/bin/mycmd", "myarg"], env={"PATH": "/usr/bin"})

### Replacing "os.popen()"

La gestión del código de retorno se traduce así:

   pipe = os.popen(cmd, 'w')
   ...
   rc = pipe.close()
   if rc is not None and rc >> 8:
       print("There were some errors")
   ==>
   process = Popen(cmd, stdin=PIPE)
   ...
   process.stdin.close()
   if process.wait() != 0:
       print("There were some errors")

## Funciones de llamada a la shell de retrocompatibilidad

Este módulo también proporciona las siguientes funciones de
compatibilidad del módulo "commands" de las versiones 2.X. Estas
operaciones invocan implícitamente a la shell del sistema y no se les
aplican ninguna de las garantías descritas anteriormente respecto a
seguridad o consistencia en la gestión de excepciones.

subprocess.getstatusoutput(cmd, *, encoding=None, errors=None)

   Retorna "(exitcode, output)" de ejecutar *cmd* en una shell.

   Execute the string *cmd* in a shell with "check_output()" and
   return a 2-tuple "(exitcode, output)". *encoding* and *errors* are
   used to decode output; see the notes on Argumentos frecuentemente
   empleados for more details.

   Se elimina un salto de línea final de la salida. El código de
   salida de la orden se puede interpretar como el código de retorno
   del subproceso. Por ejemplo:

      >>> subprocess.getstatusoutput('ls /bin/ls')
      (0, '/bin/ls')
      >>> subprocess.getstatusoutput('cat /bin/junk')
      (1, 'cat: /bin/junk: No such file or directory')
      >>> subprocess.getstatusoutput('/bin/junk')
      (127, 'sh: /bin/junk: not found')
      >>> subprocess.getstatusoutput('/bin/kill $$')
      (-15, '')

   Availability: Unix, Windows.

   Distinto en la versión 3.3.4: Se añadió soporte de Windows.La
   función ahora retorna "(exitcode, output)" en lugar de "(status,
   output)" como en Python 3.3.3 y anteriores.  *exitcode* tiene el
   mismo valor que "returncode".

   Distinto en la versión 3.11: Added the *encoding* and *errors*
   parameters.

subprocess.getoutput(cmd, *, encoding=None, errors=None)

   Retorna la salida (stdout y stderr) de ejecutar *cmd* en una shell.

   Como "getstatusoutput()", salvo que se ignora el código de salida y
   el valor retornado es una cadena que contiene la salida del
   comando. Por ejemplo:

      >>> subprocess.getoutput('ls /bin/ls')
      '/bin/ls'

   Availability: Unix, Windows.

   Distinto en la versión 3.3.4: Se añadió soporte de Windows

   Distinto en la versión 3.11: Added the *encoding* and *errors*
   parameters.

## Notas

### Timeout Behavior

When using the "timeout" parameter in functions like "run()",
"Popen.wait()", or "Popen.communicate()", users should be aware of the
following behaviors:

1. **Process Creation Delay**: The initial process creation itself
   cannot be interrupted on many platform APIs. This means that even
   when specifying a timeout, you are not guaranteed to see a timeout
   exception until at least after however long process creation takes.

2. **Extremely Small Timeout Values**: Setting very small timeout
   values (such as a few milliseconds) may result in almost immediate
   "TimeoutExpired" exceptions because process creation and system
   scheduling inherently require time.

### Cómo convertir una secuencia de argumentos a una cadena en Windows

En Windows, para convertir una secuencia *args* en una cadena que
puede ser analizada con las siguientes reglas (correspondientes a las
reglas que usa la biblioteca de ejecución de MS C):

1. Los argumentos se separan por espacio en blanco, que debe ser un
   espacio o un tabulador.

2. Una cadena entre comillas dobles se interpreta como un argumento
   simple, sin importar los espacios en blanco que contenga. Se puede
   incrustar una cadena entre comillas en un argumento.

3. Una comilla doble precedida de una barra invertida se interpreta
   literalmente como una comilla doble.

4. Las barras invertidas se interpretan literalmente, salvo que
   precedan a una comilla doble.

5. Si las barras invertidas preceden inmediatamente a una doble
   comilla, cada par de barras invertidas se interpreta como una barra
   invertida literal. Si el número de barras invertidas es impar, la
   última barra invertida escapa la siguiente comilla doble según se
   describe en la regla 3.

Ver también:

  "shlex"
     Módulo que proporciona una función para analizar y escapar líneas
     de órdenes.

### Disable use of "posix_spawn()"

On Linux, "subprocess" defaults to using the "vfork()" system call
internally when it is safe to do so rather than "fork()". This greatly
improves performance.

   subprocess._USE_POSIX_SPAWN = False  # See CPython issue gh-NNNNNN.

It is safe to set this to false on any Python version. It will have no
effect on older or newer versions where unsupported. Do not assume the
attribute is available to read. Despite the name, a true value does
not indicate the corresponding function will be used, only that it may
be.

Presente los problemas cada vez que tenga que usar estas perillas
privadas con una forma de reproducir el problema que estaba viendo.
Enlace a ese problema desde un comentario en su código.

Added in version 3.8: "_USE_POSIX_SPAWN"
