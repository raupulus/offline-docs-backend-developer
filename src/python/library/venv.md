---
title: '"venv" --- Creation of virtual environments'
source_url: https://docs.python.org/es/3
source_path: library/venv.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4470
---

# "venv" --- Creation of virtual environments

Added in version 3.3.

**Código fuente:** Lib/venv/

======================================================================

The "venv" module supports creating lightweight "virtual
environments", each with their own independent set of Python packages
installed in their "site" directories. A virtual environment is
created on top of an existing Python installation, known as the
virtual environment's "base" Python, and by default is isolated from
the packages in the base environment, so that only those explicitly
installed in the virtual environment are available. See Virtual
Environments and "site"'s virtual environments documentation for more
information.

When used from within a virtual environment, common installation tools
such as pip will install Python packages into a virtual environment
without needing to be told to do so explicitly.

A virtual environment is (amongst other things):

* Used to contain a specific Python interpreter and software libraries
  and binaries which are needed to support a project (library or
  application). These are by default isolated from software in other
  virtual environments and Python interpreters and libraries installed
  in the operating system.

* Contained in a directory, conventionally named ".venv" or "venv" in
  the project directory, or under a container directory for lots of
  virtual environments, such as "~/.virtualenvs".

* Not checked into source control systems such as Git.

* Considered as disposable -- it should be simple to delete and
  recreate it from scratch. You don't place any project code in the
  environment.

* Not considered as movable or copyable -- you just recreate the same
  environment in the target location.

Ver **PEP 405** para más información sobre los entornos virtuales de
Python.

Ver también:

  Python Packaging User Guide: Creating and using virtual environments

Availability: not Android, not iOS, not WASI.

This module is not supported on mobile platforms or WebAssembly
platforms.

## Creación de entornos virtuales

Virtual environments are created by executing the "venv" module:

   python -m venv /path/to/new/virtual/environment

This creates the target directory (including parent directories as
needed) and places a "pyvenv.cfg" file in it with a "home" key
pointing to the Python installation from which the command was run. It
also creates a "bin" (or "Scripts" on Windows) subdirectory containing
a copy or symlink of the Python executable (as appropriate for the
platform or arguments used at environment creation time). It also
creates a "lib/pythonX.Y/site-packages" subdirectory (on Windows, this
is "Lib\site-packages"). If an existing directory is specified, it
will be re-used.

Distinto en la versión 3.5: The use of "venv" is now recommended for
creating virtual environments.

Deprecated since version 3.6, removed in version 3.8: **pyvenv** was
the recommended tool for creating virtual environments for Python 3.3
and 3.4, and replaced in 3.5 by executing "venv" directly.

On Windows, invoke the "venv" command as follows:

   PS> python -m venv C:\path\to\new\virtual\environment

The command, if run with "-h", will show the available options:

   usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
               [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps]
               [--without-scm-ignore-files]
               ENV_DIR [ENV_DIR ...]

   Creates virtual Python environments in one or more target directories.

   Once an environment has been created, you may wish to activate it, e.g. by
   sourcing an activate script in its bin directory.

ENV_DIR

   A required argument specifying the directory to create the
   environment in.

--system-site-packages

   Give the virtual environment access to the system site-packages
   directory.

--symlinks

   Try to use symlinks rather than copies, when symlinks are not the
   default for the platform.

--copies

   Try to use copies rather than symlinks, even when symlinks are the
   default for the platform.

--clear

   Delete the contents of the environment directory if it already
   exists, before environment creation.

--upgrade

   Upgrade the environment directory to use this version of Python,
   assuming Python has been upgraded in-place.

--without-pip

   Skips installing or upgrading pip in the virtual environment (pip
   is bootstrapped by default).

--prompt <PROMPT>

   Provides an alternative prompt prefix for this environment.

--upgrade-deps

   Upgrade core dependencies (pip) to the latest version in PyPI.

--without-scm-ignore-files

   Skips adding SCM ignore files to the environment directory (Git is
   supported by default).

Distinto en la versión 3.4: Installs pip by default, added the "--
without-pip"  and "--copies" options.

Distinto en la versión 3.4: In earlier versions, if the target
directory already existed, an error was raised, unless the "--clear"
or "--upgrade" option was provided.

Distinto en la versión 3.9: Add "--upgrade-deps" option to upgrade pip
+ setuptools to the latest on PyPI.

Distinto en la versión 3.12: "setuptools" is no longer a core venv
dependency.

Distinto en la versión 3.13: Added the "--without-scm-ignore-files"
option.

Distinto en la versión 3.13: "venv" now creates a ".gitignore" file
for Git by default.

Nota:

  While symlinks are supported on Windows, they are not recommended.
  Of particular note is that double-clicking "python.exe" in File
  Explorer will resolve the symlink eagerly and ignore the virtual
  environment.

Nota:

  On Microsoft Windows, it may be required to enable the
  "Activate.ps1" script by setting the execution policy for the user.
  You can do this by issuing the following PowerShell command:

     PS C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

  See About Execution Policies for more information.

The created "pyvenv.cfg" file also includes the "include-system-site-
packages" key, set to "true" if "venv" is run with the "--system-site-
packages" option, "false" otherwise.

Unless the "--without-pip" option is given, "ensurepip" will be
invoked to bootstrap "pip" into the virtual environment.

Multiple paths can be given to "venv", in which case an identical
virtual environment will be created, according to the given options,
at each provided path.

## Cómo funcionan los venvs

When a Python interpreter is running from a virtual environment,
"sys.prefix" and "sys.exec_prefix" point to the directories of the
virtual environment, whereas "sys.base_prefix" and
"sys.base_exec_prefix" point to those of the base Python used to
create the environment. It is sufficient to check "sys.prefix !=
sys.base_prefix" to determine if the current interpreter is running
from a virtual environment.

A virtual environment may be "activated" using a script in its binary
directory ("bin" on POSIX; "Scripts" on Windows). This will prepend
that directory to your "PATH", so that running **python** will invoke
the environment's Python interpreter and you can run installed scripts
without having to use their full path. The invocation of the
activation script is platform-specific ("*<venv>*" must be replaced by
the path to the directory containing the virtual environment):

+---------------+--------------+----------------------------------------------------+
| Plataforma    | Shell        | Comando para activar el entorno virtual            |
|===============|==============|====================================================|
| POSIX         | bash/zsh     | "$ source *<venv>*/bin/activate"                   |
|               +--------------+----------------------------------------------------+
|               | fish         | "$ source *<venv>*/bin/activate.fish"              |
|               +--------------+----------------------------------------------------+
|               | csh/tcsh     | "$ source *<venv>*/bin/activate.csh"               |
|               +--------------+----------------------------------------------------+
## |               | pwsh         | "$ *<venv>*/bin/Activate.ps1"                      |

| Windows       | cmd.exe      | "C:\> *<venv>*\Scripts\activate.bat"               |
|               +--------------+----------------------------------------------------+
## |               | PowerShell   | "PS C:\> *<venv>*\Scripts\Activate.ps1"            |

Added in version 3.4: **fish** and **csh** activation scripts.

Added in version 3.8: Scripts de activación de PowerShell instalados
en POSIX para compatibilidad con PowerShell Core.

No *necesita* específicamente activar un entorno virtual, ya que puede
solo especificar la ruta completa al intérprete de Python de ese
entorno al invocar Python. Además, todos los scripts instalados en el
entorno deben poder ejecutarse sin activarlo.

In order to achieve this, scripts installed into virtual environments
have a "shebang" line which points to the environment's Python
interpreter, "#!/*<path-to-venv>*/bin/python". This means that the
script will run with that interpreter regardless of the value of
"PATH". On Windows, "shebang" line processing is supported if you have
the Python install manager installed. Thus, double-clicking an
installed script in a Windows Explorer window should run it with the
correct interpreter without the environment needing to be activated or
on the "PATH".

Cuando se ha activado un entorno virtual, la variable de entorno
"VIRTUAL_ENV" se establece en la ruta del entorno. Dado que no se
requiere activar explícitamente una entorno virtual para usarla, no se
puede confiar en "VIRTUAL_ENV" para determinar si se está usando un
entorno virtual.

Advertencia:

  Debido a que los scripts instalados en entornos no deben esperar a
  que el entorno se active, sus líneas shebang contienen las rutas
  absolutas a los intérpretes de su entorno. Debido a esto, los
  entornos son inherentemente no portables, en el caso general.
  Siempre debe tener un medio simple para recrear un entorno (por
  ejemplo, si tiene un archivo de requisitos "requirements.txt", puede
  invocar "pip install -r requirements.txt" al usar "pip" del entorno
  para instalar todos los paquetes que necesite el entorno). Si por
  alguna razón necesita mover el entorno a una nueva ubicación, debe
  recrearlo en la ubicación deseada y eliminar el de la ubicación
  anterior. Si mueve un entorno porque movió un directorio principal
  del mismo, debe recrear el entorno en su nueva ubicación. De lo
  contrario, el software instalado en el entorno puede no funcionar
  como se espera.

Puede desactivar un entorno virtual al escribir "deactivate" en el
shell. El mecanismo exacto es específico de la plataforma y es un
detalle de implementación interno (se usará normalmente una función de
script o shell).

## API

El método de alto nivel descrito anteriormente utiliza una sencilla
API que proporciona mecanismos para que les creadores de entornos
virtuales de terceras/os puedan personalizar la creación de entornos
según sus necesidades, la clase "EnvBuilder".

class venv.EnvBuilder(system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=False, prompt=None, upgrade_deps=False, *, scm_ignore_files=frozenset())

   La clase "EnvBuilder" acepta los siguientes argumentos de palabras
   clave en la instanciación:

   * *system_site_packages* -- a boolean value indicating that the
     system Python site-packages should be available to the
     environment (defaults to "False").

   * *clear* -- a boolean value which, if true, will delete the
     contents of any existing target directory, before creating the
     environment.

   * *symlinks* -- a boolean value indicating whether to attempt to
     symlink the Python binary rather than copying.

   * *upgrade* -- a boolean value which, if true, will upgrade an
     existing environment with the running Python - for use when that
     Python has been upgraded in-place (defaults to "False").

   * *with_pip* -- a boolean value which, if true, ensures pip is
     installed in the virtual environment. This uses "ensurepip" with
     the "--default-pip" option.

   * *prompt* -- a string to be used after virtual environment is
     activated (defaults to "None" which means directory name of the
     environment would be used). If the special string ""."" is
     provided, the basename of the current directory is used as the
     prompt.

   * *upgrade_deps* -- Update the base venv modules to the latest on
     PyPI

   * *scm_ignore_files* -- Create ignore files based for the specified
     source control managers (SCM) in the iterable. Support is defined
     by having a method named "create_{scm}_ignore_file". The only
     value supported by default is ""git"" via
     "create_git_ignore_file()".

   Distinto en la versión 3.4: Añadido el parámetro "with_pip"

   Distinto en la versión 3.6: Añadido el parámetro "prompt"

   Distinto en la versión 3.9: Se agregó el parámetro "upgrade_deps"

   Distinto en la versión 3.13: Added the "scm_ignore_files" parameter

   "EnvBuilder" may be used as a base class.

   create(env_dir)

      Crear un entorno virtual especificando el directorio de destino
      (de forma absoluta o relativa al directorio actual) que ha de
      contener el entorno virtual. El método "create" creará el
      entorno en el directorio especificado, o lanzará la
      correspondiente excepción.

      El método "create" de la clase "EnvBuilder" ilustra los enlaces
      disponibles para la personalización de la subclase:

         def create(self, env_dir):
             """
             Create a virtualized Python environment in a directory.
             env_dir is the target directory to create an environment in.
             """
             env_dir = os.path.abspath(env_dir)
             context = self.ensure_directories(env_dir)
             self.create_configuration(context)
             self.setup_python(context)
             self.setup_scripts(context)
             self.post_setup(context)

      Cada uno de los métodos "ensure_directories()",
      "create_configuration()", "setup_python()", "setup_scripts()" y
      "post_setup()" pueden ser anulados.

   ensure_directories(env_dir)

      Crea el directorio del entorno y todos los subdirectorios
      necesarios que aún no existen, y retorna un objeto de contexto.
      Este objeto de contexto es solo un contenedor de atributos (como
      rutas) para que lo usen otros métodos. Si se crea "EnvBuilder"
      con el argumento "clear=True", se borrará el contenido del
      directorio del entorno y luego se recrearán todos los
      subdirectorios necesarios.

      El objeto de contexto que retorna es un "types.SimpleNamespace"
      con los siguientes atributos:

      * "env_dir" - La ubicación del entorno virtual. Se usa para
        "__VENV_DIR__" en scripts de activación (ver
        "install_scripts()").

      * "env_name" - El nombre del entorno virtual. Se usa para
        "__VENV_NAME__" en scripts de activación (ver
        "install_scripts()").

      * "prompt" - El prompt que utilizarán los scripts de activación.
        Se usa para "__VENV_PROMPT__" en scripts de activación (ver
        "install_scripts()").

      * "executable" - El ejecutable de Python subyacente que se
        utiliza por el entorno virtual. Esto tiene en cuenta el caso
        donde se crea un entorno virtual a partir de otro entorno
        virtual.

      * "inc_path" - La ruta de include para el entorno virtual.

      * "lib_path" - La ruta de purelib para el entorno virtual.

      * "bin_path" - La ruta del script para el entorno virtual.

      * "bin_name" - El nombre de la ruta del script en relación con
        la ubicación del entorno virtual. Se usa para
        "__VENV_BIN_NAME__" en scripts de activación (ver
        "install_scripts()").

      * "env_exe" - El nombre del intérprete de Python en el entorno
        virtual. Se usa para "__VENV_PYTHON__" en scripts de
        activación (ver "install_scripts()").

      * "env_exec_cmd" - El nombre del intérprete de Python, teniendo
        en cuenta las redirecciones del sistema de archivos. Se puede
        utilizar para ejecutar Python en el entorno virtual.

      Distinto en la versión 3.11: El esquema de instalación de
      sysconfig de *venv* se utiliza para construir las rutas de los
      directorios creados.

      Distinto en la versión 3.12: Se agregó el atributo "lib_path" al
      contexto y se documentó el objeto de contexto.

   create_configuration(context)

      Crea el archivo de configuración "pyvenv.cfg" en el entorno.

   setup_python(context)

      Crea una copia o enlace simbólico al ejecutable Python en el
      entorno. En los sistemas POSIX, si se usó un ejecutable
      específico "python3.x", se crearán enlaces simbólicos a "python"
      y "python3" apuntando a ese ejecutable, a menos que ya existan
      archivos con esos nombres.

   setup_scripts(context)

      Instala los scripts de activación apropiados para la plataforma
      en el entorno virtual.

   upgrade_dependencies(context)

      Upgrades the core venv dependency packages (currently pip) in
      the environment. This is done by shelling out to the "pip"
      executable in the environment.

      Added in version 3.9.

      Distinto en la versión 3.12: setuptools is no longer a core venv
      dependency.

   post_setup(context)

      Un método de marcador de posición que puede ser anulado en
      implementaciones de terceros/as para previo instalar paquetes en
      el entorno virtual o realizar otros pasos posteriores a la
      creación.

   install_scripts(context, path)

      This method can be called from "setup_scripts()" or
      "post_setup()" in subclasses to assist in installing custom
      scripts into the virtual environment.

      *path* is the path to a directory that should contain
      subdirectories "common", "posix", "nt"; each containing scripts
      destined for the "bin" directory in the environment.  The
      contents of "common" and the directory corresponding to
      "os.name" are copied after some text replacement of
      placeholders:

      * "__VENV_DIR__" se sustituye por la ruta absoluta del
        directorio del entorno.

      * "__VENV_NAME__" se sustituye por el nombre del entorno (parte
        final de la ruta del directorio del entorno).

      * "__VENV_PROMPT__" se sustituye por el *prompt* (el nombre del
        entorno entre paréntesis y con un espacio posterior)

      * "__VENV_BIN_NAME__" se sustituye con el nombre del directorio
        *bin* (ya sea "bin" o "Scripts").

      * "__VENV_PYTHON__" se sustituye con la ruta absoluta del
        ejecutable del entorno.

      Se permite la existencia de los directorios (para cuando se está
      actualizando un entorno existente).

   create_git_ignore_file(context)

      Creates a ".gitignore" file within the virtual environment that
      causes the entire directory to be ignored by the Git source
      control manager.

      Added in version 3.13.

   Distinto en la versión 3.7.2: Windows ahora usa scripts de
   redireccionamiento para "python[w].exe" en lugar de copiar los
   propios binarios. Para 3.7.2 solamente "setup_python()" no hace
   nada a menos que se ejecute desde una compilación en el árbol de
   directorios fuente.

   Distinto en la versión 3.7.3: Windows copia los scripts de
   redireccionamiento como parte de "setup_python()" en lugar de
   "setup_scripts()". Este no era el caso para 3.7.2. Cuando se usan
   enlaces simbólicos, los ejecutables originales se enlazan.

También hay una función de conveniencia a nivel de módulo:

venv.create(env_dir, system_site_packages=False, clear=False, symlinks=False, with_pip=False, prompt=None, upgrade_deps=False, *, scm_ignore_files=frozenset())

   Crea un "EnvBuilder" con los argumentos de la palabra clave dada, y
   llama a su método "create()" con el argumento *env_dir*.

   Added in version 3.3.

   Distinto en la versión 3.4: Added the *with_pip* parameter

   Distinto en la versión 3.6: Added the *prompt* parameter

   Distinto en la versión 3.9: Added the *upgrade_deps* parameter

   Distinto en la versión 3.13: Added the *scm_ignore_files* parameter

## Un ejemplo de la extensión de "EnvBuilder"

El siguiente script muestra como extender "EnvBuilder" implementando
una subclase que instala setuptools y pip en un entorno virtual
creado:

   import os
   import os.path
   from subprocess import Popen, PIPE
   import sys
   from threading import Thread
   from urllib.parse import urlsplit
   from urllib.request import urlretrieve
   import venv

   class ExtendedEnvBuilder(venv.EnvBuilder):
       """
       This builder installs setuptools and pip so that you can pip or
       easy_install other packages into the created virtual environment.

       :param nodist: If true, setuptools and pip are not installed into the
                      created virtual environment.
       :param nopip: If true, pip is not installed into the created
                     virtual environment.
       :param progress: If setuptools or pip are installed, the progress of the
                        installation can be monitored by passing a progress
                        callable. If specified, it is called with two
                        arguments: a string indicating some progress, and a
                        context indicating where the string is coming from.
                        The context argument can have one of three values:
                        'main', indicating that it is called from virtualize()
                        itself, and 'stdout' and 'stderr', which are obtained
                        by reading lines from the output streams of a subprocess
                        which is used to install the app.

                        If a callable is not specified, default progress
                        information is output to sys.stderr.
       """

       def __init__(self, *args, **kwargs):
           self.nodist = kwargs.pop('nodist', False)
           self.nopip = kwargs.pop('nopip', False)
           self.progress = kwargs.pop('progress', None)
           self.verbose = kwargs.pop('verbose', False)
           super().__init__(*args, **kwargs)

       def post_setup(self, context):
           """
           Set up any packages which need to be pre-installed into the
           virtual environment being created.

           :param context: The information for the virtual environment
                           creation request being processed.
           """
           os.environ['VIRTUAL_ENV'] = context.env_dir
           if not self.nodist:
               self.install_setuptools(context)
           # Can't install pip without setuptools
           if not self.nopip and not self.nodist:
               self.install_pip(context)

       def reader(self, stream, context):
           """
           Read lines from a subprocess' output stream and either pass to a progress
           callable (if specified) or write progress information to sys.stderr.
           """
           progress = self.progress
           while True:
               s = stream.readline()
               if not s:
                   break
               if progress is not None:
                   progress(s, context)
               else:
                   if not self.verbose:
                       sys.stderr.write('.')
                   else:
                       sys.stderr.write(s.decode('utf-8'))
                   sys.stderr.flush()
           stream.close()

       def install_script(self, context, name, url):
           _, _, path, _, _ = urlsplit(url)
           fn = os.path.split(path)[-1]
           binpath = context.bin_path
           distpath = os.path.join(binpath, fn)
           # Download script into the virtual environment's binaries folder
           urlretrieve(url, distpath)
           progress = self.progress
           if self.verbose:
               term = '\n'
           else:
               term = ''
           if progress is not None:
               progress('Installing %s ...%s' % (name, term), 'main')
           else:
               sys.stderr.write('Installing %s ...%s' % (name, term))
               sys.stderr.flush()
           # Install in the virtual environment
           args = [context.env_exe, fn]
           p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=binpath)
           t1 = Thread(target=self.reader, args=(p.stdout, 'stdout'))
           t1.start()
           t2 = Thread(target=self.reader, args=(p.stderr, 'stderr'))
           t2.start()
           p.wait()
           t1.join()
           t2.join()
           if progress is not None:
               progress('done.', 'main')
           else:
               sys.stderr.write('done.\n')
           # Clean up - no longer needed
           os.unlink(distpath)

       def install_setuptools(self, context):
           """
           Install setuptools in the virtual environment.

           :param context: The information for the virtual environment
                           creation request being processed.
           """
           url = "https://bootstrap.pypa.io/ez_setup.py"
           self.install_script(context, 'setuptools', url)
           # clear up the setuptools archive which gets downloaded
           pred = lambda o: o.startswith('setuptools-') and o.endswith('.tar.gz')
           files = filter(pred, os.listdir(context.bin_path))
           for f in files:
               f = os.path.join(context.bin_path, f)
               os.unlink(f)

       def install_pip(self, context):
           """
           Install pip in the virtual environment.

           :param context: The information for the virtual environment
                           creation request being processed.
           """
           url = 'https://bootstrap.pypa.io/get-pip.py'
           self.install_script(context, 'pip', url)

   def main(args=None):
       import argparse

       parser = argparse.ArgumentParser(prog=__name__,
                                        description='Creates virtual Python '
                                                    'environments in one or '
                                                    'more target '
                                                    'directories.')
       parser.add_argument('dirs', metavar='ENV_DIR', nargs='+',
                           help='A directory in which to create the '
                                'virtual environment.')
       parser.add_argument('--no-setuptools', default=False,
                           action='store_true', dest='nodist',
                           help="Don't install setuptools or pip in the "
                                "virtual environment.")
       parser.add_argument('--no-pip', default=False,
                           action='store_true', dest='nopip',
                           help="Don't install pip in the virtual "
                                "environment.")
       parser.add_argument('--system-site-packages', default=False,
                           action='store_true', dest='system_site',
                           help='Give the virtual environment access to the '
                                'system site-packages dir.')
       if os.name == 'nt':
           use_symlinks = False
       else:
           use_symlinks = True
       parser.add_argument('--symlinks', default=use_symlinks,
                           action='store_true', dest='symlinks',
                           help='Try to use symlinks rather than copies, '
                                'when symlinks are not the default for '
                                'the platform.')
       parser.add_argument('--clear', default=False, action='store_true',
                           dest='clear', help='Delete the contents of the '
                                              'virtual environment '
                                              'directory if it already '
                                              'exists, before virtual '
                                              'environment creation.')
       parser.add_argument('--upgrade', default=False, action='store_true',
                           dest='upgrade', help='Upgrade the virtual '
                                                'environment directory to '
                                                'use this version of '
                                                'Python, assuming Python '
                                                'has been upgraded '
                                                'in-place.')
       parser.add_argument('--verbose', default=False, action='store_true',
                           dest='verbose', help='Display the output '
                                                'from the scripts which '
                                                'install setuptools and pip.')
       options = parser.parse_args(args)
       if options.upgrade and options.clear:
           raise ValueError('you cannot supply --upgrade and --clear together.')
       builder = ExtendedEnvBuilder(system_site_packages=options.system_site,
                                      clear=options.clear,
                                      symlinks=options.symlinks,
                                      upgrade=options.upgrade,
                                      nodist=options.nodist,
                                      nopip=options.nopip,
                                      verbose=options.verbose)
       for d in options.dirs:
           builder.create(d)

   if __name__ == '__main__':
       rc = 1
       try:
           main()
           rc = 0
       except Exception as e:
           print('Error: %s' % e, file=sys.stderr)
       sys.exit(rc)

Este script está también disponible para su descarga online.
