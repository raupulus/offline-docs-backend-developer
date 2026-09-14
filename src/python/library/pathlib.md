---
title: '"pathlib" --- Rutas de sistemas orientada a objetos'
source_url: https://docs.python.org/es/3
source_path: library/pathlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3410
---

# "pathlib" --- Rutas de sistemas orientada a objetos

Added in version 3.4.

**Código fuente:** Lib/pathlib/

======================================================================

Este módulo ofrece clases que representan rutas del sistema de
archivos con semántica apropiada para diferentes sistemas operativos.
Las clases ruta se dividen entre rutas puras, que proporcionan
operaciones puramente computacionales sin E/S; y rutas concretas, que
heredan de rutas puras pero también proporcionan operaciones de E/S.

[imagen: Diagrama de herencia que muestra las clases disponibles en
pathlib. La clase más básica es PurePath, que tiene tres subclases
directas: PurePosixPath, PureWindowsPath y Path. Además de estas
cuatro clases, hay dos clases que utilizan herencia múltiple:
subclases de PosixPath, PurePosixPath y Path, y subclases de
WindowsPath, PureWindowsPath y Path.][imagen]

Si nunca has usado este módulo o simplemente no estás seguro de qué
clase es la adecuada para tu tarea, "Path" es probablemente lo que
necesitas. Crea una instancia ruta concreta para la plataforma en la
que se ejecuta el código.

Las rutas puras son útiles en algunos casos especiales, por ejemplo:

1. Si deseas manipular las rutas de Windows en una máquina Unix (o
   viceversa). No puedes crear una instancia de "WindowsPath" cuando
   se ejecuta en Unix, pero puedes crear una instancia de
   "PureWindowsPath".

2. Desea asegurar que su código solo manipule rutas sin acceder
   realmente al sistema operativo. En este caso, crear instancias de
   una de las clases puras puede ser útil, ya que simplemente no
   tienen ninguna operación de acceso al sistema operativo.

Ver también:

  **PEP 428**: El módulo pathlib -- rutas de sistema orientadas a
  objetos.

Ver también:

  Para la manipulación de rutas de bajo nivel en cadenas, también
  puede usar el módulo "os.path".

## Uso básico

Importar la clase principal:

   >>> from pathlib import Path

Listado de subdirectorios:

   >>> p = Path('.')
   >>> [x for x in p.iterdir() if x.is_dir()]
   [PosixPath('.hg'), PosixPath('docs'), PosixPath('dist'),
    PosixPath('__pycache__'), PosixPath('build')]

Listado de archivos fuente de Python en este árbol de directorios:

   >>> list(p.glob('**/*.py'))
   [PosixPath('test_pathlib.py'), PosixPath('setup.py'),
    PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
    PosixPath('build/lib/pathlib.py')]

Navegar dentro de un árbol de directorios:

   >>> p = Path('/etc')
   >>> q = p / 'init.d' / 'reboot'
   >>> q
   PosixPath('/etc/init.d/reboot')
   >>> q.resolve()
   PosixPath('/etc/rc.d/init.d/halt')

Consultar propiedades de ruta:

   >>> q.exists()
   True
   >>> q.is_dir()
   False

Abrir un archivo:

   >>> with q.open() as f: f.readline()
   ...
   '#!/bin/bash\n'

## Excepciones

exception pathlib.UnsupportedOperation

   Una excepción que hereda "NotImplementedError" y que se genera
   cuando se llama a una operación no compatible en un objeto de ruta.

   Added in version 3.13.

## Rutas puras

Los objetos ruta pura proporcionan operaciones de manejo de rutas que
en realidad no acceden al sistema de archivos. Hay tres formas de
acceder a estas clases, que llamaremos *familias*:

class pathlib.PurePath(*pathsegments)

   Una clase genérica que representa la familia de rutas del sistema
   (al crear una instancia se crea "PurePosixPath" o
   "PureWindowsPath"):

      >>> PurePath('setup.py')      # Ejecutándose en una máquina Unix
      PurePosixPath('setup.py')

   Cada elemento de *pathsegments* puede ser una cadena que representa
   un segmento de ruta o un objeto que implemente la interfaz
   "os.PathLike" donde el método "__fspath__()" retorna una cadena
   como otro objeto de ruta:

      >>> PurePath('foo', 'some/path', 'bar')
      PurePosixPath('foo/some/path/bar')
      >>> PurePath(Path('foo'), Path('bar'))
      PurePosixPath('foo/bar')

   Cuando *pathsegments* está vacío, se asume el directorio actual:

      >>> PurePath()
      PurePosixPath('.')

   Si un segmento es una ruta absoluta, se ignoran todos los segmentos
   anteriores (como "os.path.join()"):

      >>> PurePath('/etc', '/usr', 'lib64')
      PurePosixPath('/usr/lib64')
      >>> PureWindowsPath('c:/Windows', 'd:bar')
      PureWindowsPath('d:bar')

   En Windows, la unidad no se restablece cuando se encuentra un
   segmento de ruta relativa en la raíz (por ejemplo, "r'\foo'"):

      >>> PureWindowsPath('c:/Windows', '/Program Files')
      PureWindowsPath('c:/Program Files')

   Las barras espurias y los puntos simples se colapsan, pero los
   puntos dobles ("'..'") y las barras dobles iniciales ("'//'") no,
   ya que esto cambiaría el significado de una ruta por varias razones
   (por ejemplo, enlaces simbólicos, rutas UNC):

      >>> PurePath('foo//bar')
      PurePosixPath('foo/bar')
      >>> PurePath('//foo/bar')
      PurePosixPath('//foo/bar')
      >>> PurePath('foo/./bar')
      PurePosixPath('foo/bar')
      >>> PurePath('foo/../bar')
      PurePosixPath('foo/../bar')

   (un enfoque naif haría pensar que "PurePosixPath('foo/../bar')" es
   equivalente a "PurePosixPath('bar')", lo cual es incorrecto si
   "foo" es un enlace simbólico a otro directorio)

   Los objetos ruta pura implementan la interfaz "os.PathLike", lo que
   permite su uso en cualquier lugar donde se acepte la interfaz.

   Distinto en la versión 3.6: Se agregó soporte para la interfaz
   "os.PathLike".

class pathlib.PurePosixPath(*pathsegments)

   Una subclase de "PurePath", esta *familia* representa rutas que no
   son del sistema de archivos de Windows:

      >>> PurePosixPath('/etc/hosts')
      PurePosixPath('/etc/hosts')

   *pathsegments* se especifica de manera similar a "PurePath".

class pathlib.PureWindowsPath(*pathsegments)

   Una subclase de "PurePath", este tipo de ruta representa las rutas
   del sistema de archivos de Windows, incluido UNC paths:

      >>> PureWindowsPath('c:/', 'Users', 'Ximénez')
      PureWindowsPath('c:/Users/Ximénez')
      >>> PureWindowsPath('//server/share/file')
      PureWindowsPath('//server/share/file')

   *pathsegments* se especifica de manera similar a "PurePath".

Independientemente del sistema en el que se encuentre, puede crear
instancias de todas estas clases, ya que no proporcionan ninguna
operación que llame al sistema operativo.

### Propiedades generales

Las rutas son inmutables y *hashable*. Las rutas de una misma familia
son comparables y ordenables. Estas propiedades respetan el orden
lexicográfico definido por la familia:

   >>> PurePosixPath('foo') == PurePosixPath('FOO')
   False
   >>> PureWindowsPath('foo') == PureWindowsPath('FOO')
   True
   >>> PureWindowsPath('FOO') in { PureWindowsPath('foo') }
   True
   >>> PureWindowsPath('C:') < PureWindowsPath('d:')
   True

Rutas de diferentes familias no son iguales y no se pueden ordenar:

   >>> PureWindowsPath('foo') == PurePosixPath('foo')
   False
   >>> PureWindowsPath('foo') < PurePosixPath('foo')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: '<' not supported between instances of 'PureWindowsPath' and 'PurePosixPath'

### Operadores

El operador de barra inclinada ayuda a crear rutas hijas, como
"os.path.join()". Si el argumento es una ruta absoluta, se ignora la
ruta anterior. En Windows, la unidad no se restablece cuando el
argumento es una ruta relativa en la raíz (por ejemplo, "r'\foo'"):

   >>> p = PurePath('/etc')
   >>> p
   PurePosixPath('/etc')
   >>> p / 'init.d' / 'apache2'
   PurePosixPath('/etc/init.d/apache2')
   >>> q = PurePath('bin')
   >>> '/usr' / q
   PurePosixPath('/usr/bin')
   >>> p / '/an_absolute_path'
   PurePosixPath('/an_absolute_path')
   >>> PureWindowsPath('c:/Windows', '/Program Files')
   PureWindowsPath('c:/Program Files')

Se puede usar un objeto ruta en cualquier lugar donde se acepte un
objeto que implemente "os.PathLike":

   >>> import os
   >>> p = PurePath('/etc')
   >>> os.fspath(p)
   '/etc'

La representación de una ruta en una cadena de caracteres es la ruta
del sistema de archivos sin procesar en sí (en forma nativa, por
ejemplo con barras invertidas en Windows), y que puede pasar a
cualquier función que tome una ruta como una cadena de caracteres:

   >>> p = PurePath('/etc')
   >>> str(p)
   '/etc'
   >>> p = PureWindowsPath('c:/Program Files')
   >>> str(p)
   'c:\\Program Files'

Del mismo modo, llamar a "bytes" en una ruta proporciona la ruta cruda
del sistema de archivos como un objeto bytes, codificado por
"os.fsencode()":

   >>> bytes(p)
   b'/etc'

Nota:

  Llamar a "bytes" solo se recomienda en Unix. En Windows, la forma
  unicode es la representación canónica de las rutas del sistema de
  archivos.

### Acceso a partes individuales

Para acceder a las "partes" (componentes) individuales de una ruta,
use la siguiente propiedad:

PurePath.parts

   Una tupla que da acceso a los diversos componentes de la ruta:

      >>> p = PurePath('/usr/bin/python3')
      >>> p.parts
      ('/', 'usr', 'bin', 'python3')

      >>> p = PureWindowsPath('c:/Program Files/PSF')
      >>> p.parts
      ('c:\\', 'Program Files', 'PSF')

   (obsérvese cómo la unidad y la raíz local se reagrupan en una sola
   parte)

### Métodos y propiedades

Las rutas puras proporcionan los siguientes métodos y propiedades:

PurePath.parser

   The implementation of the "os.path" module used for low-level path
   parsing and joining: either "posixpath" or "ntpath".

   Added in version 3.13.

PurePath.drive

   Una cadena que representa la letra o el nombre de la unidad, si
   corresponde:

      >>> PureWindowsPath('c:/Program Files/').drive
      'c:'
      >>> PureWindowsPath('/Program Files/').drive
      ''
      >>> PurePosixPath('/etc').drive
      ''

   Las localizaciones UNC también son consideradas como unidades:

      >>> PureWindowsPath('//host/share/foo.txt').drive
      '\\\\host\\share'

PurePath.root

   Una cadena que representa la raíz (local o global), si la hay:

      >>> PureWindowsPath('c:/Program Files/').root
      '\\'
      >>> PureWindowsPath('c:Program Files/').root
      ''
      >>> PurePosixPath('/etc').root
      '/'

   Las localizaciones UNC siempre tienen una raíz:

      >>> PureWindowsPath('//host/share').root
      '\\'

   Si la ruta comienza con más de dos barras diagonales sucesivas,
   "PurePosixPath" las contrae:

      >>> PurePosixPath('//etc').root
      '//'
      >>> PurePosixPath('///etc').root
      '/'
      >>> PurePosixPath('////etc').root
      '/'

   Nota:

     Este comportamiento se ajusta a *The Open Group Base
     Specifications Issue 6*, párrafo 4.11 Pathname Resolution:*"Un
     nombre de ruta que comienza con dos barras oblicuas sucesivas se
     puede interpretar de una manera definida por la implementación,
     aunque más de dos barras oblicuas iniciales se tratarán como una
     sola barra oblicua."*

PurePath.anchor

   La concatenación de la unidad y la raíz:

      >>> PureWindowsPath('c:/Program Files/').anchor
      'c:\\'
      >>> PureWindowsPath('c:Program Files/').anchor
      'c:'
      >>> PurePosixPath('/etc').anchor
      '/'
      >>> PureWindowsPath('//host/share').anchor
      '\\\\host\\share\\'

PurePath.parents

   Una secuencia inmutable que proporciona acceso a los ancestros
   lógicos de la ruta:

      >>> p = PureWindowsPath('c:/foo/bar/setup.py')
      >>> p.parents[0]
      PureWindowsPath('c:/foo/bar')
      >>> p.parents[1]
      PureWindowsPath('c:/foo')
      >>> p.parents[2]
      PureWindowsPath('c:/')

   Distinto en la versión 3.10: La secuencia de padres ahora admite
   *rebanada* y valores de índice negativos.

PurePath.parent

   El padre lógico de la ruta

      >>> p = PurePosixPath('/a/b/c/d')
      >>> p.parent
      PurePosixPath('/a/b/c')

   No puede ir más allá de un ancla o una ruta vacía:

      >>> p = PurePosixPath('/')
      >>> p.parent
      PurePosixPath('/')
      >>> p = PurePosixPath('.')
      >>> p.parent
      PurePosixPath('.')

   Nota:

     Esta es una operación puramente léxica, de ahí el siguiente
     comportamiento:

        >>> p = PurePosixPath('foo/..')
        >>> p.parent
        PurePosixPath('foo')

     Si desea recorrer una ruta de sistema de archivos arbitraria
     hacia arriba, se recomienda llamar primero a "Path.resolve()"
     para resolver los enlaces simbólicos y eliminar los componentes
     "".."".

PurePath.name

   Una cadena que representa el componente final de la ruta,
   excluyendo la unidad y la raíz, si hay alguna:

      >>> PurePosixPath('my/library/setup.py').name
      'setup.py'

   Los nombres de unidad UNC no se consideran:

      >>> PureWindowsPath('//some/share/setup.py').name
      'setup.py'
      >>> PureWindowsPath('//some/share').name
      ''

PurePath.suffix

   La última porción separada por puntos del componente final, si la
   hay:

      >>> PurePosixPath('my/library/setup.py').suffix
      '.py'
      >>> PurePosixPath('my/library.tar.gz').suffix
      '.gz'
      >>> PurePosixPath('my/library').suffix
      ''

   Esto comúnmente se llama extensión de archivo.

   Distinto en la versión 3.14: A single dot (""."") is considered a
   valid suffix.

PurePath.suffixes

   Una lista de los sufijos de la ruta, a menudo llamados extensiones
   de archivo:

      >>> PurePosixPath('my/library.tar.gar').suffixes
      ['.tar', '.gar']
      >>> PurePosixPath('my/library.tar.gz').suffixes
      ['.tar', '.gz']
      >>> PurePosixPath('my/library').suffixes
      []

   Distinto en la versión 3.14: A single dot (""."") is considered a
   valid suffix.

PurePath.stem

   El componente final de la ruta, sin su sufijo:

      >>> PurePosixPath('my/library.tar.gz').stem
      'library.tar'
      >>> PurePosixPath('my/library.tar').stem
      'library'
      >>> PurePosixPath('my/library').stem
      'library'

   Distinto en la versión 3.14: A single dot (""."") is considered a
   valid suffix.

PurePath.as_posix()

   Retorna una cadena que representa la ruta con barras invertidas
   ("/"):

      >>> p = PureWindowsPath('c:\\windows')
      >>> str(p)
      'c:\\windows'
      >>> p.as_posix()
      'c:/windows'

PurePath.is_absolute()

   Retorna si la ruta es absoluta o no. Una ruta se considera absoluta
   si tiene una raíz y (si la **familia** lo permite) una unidad:

      >>> PurePosixPath('/a/b').is_absolute()
      True
      >>> PurePosixPath('a/b').is_absolute()
      False

      >>> PureWindowsPath('c:/a/b').is_absolute()
      True
      >>> PureWindowsPath('/a/b').is_absolute()
      False
      >>> PureWindowsPath('c:').is_absolute()
      False
      >>> PureWindowsPath('//some/share').is_absolute()
      True

PurePath.is_relative_to(other)

   Retorna si esta ruta es relativa o no a la *otra* ruta.

   >>> p = PurePath('/etc/passwd')
   >>> p.is_relative_to('/etc')
   True
   >>> p.is_relative_to('/usr')
   False

   Este método se basa en cadenas; no accede al sistema de archivos ni
   trata los segmentos "".."" de manera especial. El siguiente código
   es equivalente:

   >>> u = PurePath('/usr')
   >>> u == p or u in p.parents
   False

   Added in version 3.9.

   Deprecated since version 3.12, removed in version 3.14: Está
   obsoleto pasar argumentos adicionales; si se suministran, se juntan
   con *other*.

PurePath.is_reserved()

   Con "PureWindowsPath", retorna "True" si la ruta se considera
   reservada en Windows, "False" en caso contrario. Con
   "PurePosixPath", siempre retorna "False".

   Distinto en la versión 3.13: Los nombres de ruta de Windows que
   contienen dos puntos o terminan con un punto o un espacio se
   consideran reservados. Las rutas UNC pueden estar reservadas.

   Deprecated since version 3.13, will be removed in version 3.15:
   Este método está obsoleto; utilice "os.path.isreserved()" para
   detectar rutas reservadas en Windows.

PurePath.joinpath(*pathsegments)

   Llamar a este método es equivalente a combinar la ruta con cada uno
   de los *pathsegments* dados sucesivamente:

      >>> PurePosixPath('/etc').joinpath('passwd')
      PurePosixPath('/etc/passwd')
      >>> PurePosixPath('/etc').joinpath(PurePosixPath('passwd'))
      PurePosixPath('/etc/passwd')
      >>> PurePosixPath('/etc').joinpath('init.d', 'apache2')
      PurePosixPath('/etc/init.d/apache2')
      >>> PureWindowsPath('c:').joinpath('/Program Files')
      PureWindowsPath('c:/Program Files')

PurePath.full_match(pattern, *, case_sensitive=None)

   Compare esta ruta con el patrón de estilo glob proporcionado.
   Devuelva "True" si la coincidencia es exitosa, "False" en caso
   contrario. Por ejemplo:

      >>> PurePath('a/b.py').full_match('a/*.py')
      True
      >>> PurePath('a/b.py').full_match('*.py')
      False
      >>> PurePath('/a/b/c.py').full_match('/a/**')
      True
      >>> PurePath('/a/b/c.py').full_match('**/*.py')
      True

   Ver también: Documentación Lenguaje de patrones.

   Al igual que con otros métodos, la distinción entre mayúsculas y
   minúsculas sigue los valores predeterminados de la plataforma:

      >>> PurePosixPath('b.py').full_match('*.PY')
      False
      >>> PureWindowsPath('b.py').full_match('*.PY')
      True

   Establece *case_sensitive* en "True" o "False" para invalidar este
   comportamiento.

   Added in version 3.13.

PurePath.match(pattern, *, case_sensitive=None)

   Compare esta ruta con el patrón de estilo glob no recursivo
   proporcionado. Devuelva "True" si la coincidencia es exitosa,
   "False" en caso contrario.

   Este método es similar a "full_match()", pero no se permiten
   patrones vacíos (se genera "ValueError"), no se admite el comodín
   recursivo ""**"" (actúa como ""*"" no recursivo) y, si se
   proporciona un patrón relativo, la coincidencia se realiza desde la
   derecha:

      >>> PurePath('a/b.py').full_match('a/*.py')
      True
      >>> PurePath('a/b.py').full_match('*.py')
      False
      >>> PurePath('/a/b/c.py').full_match('/a/**')
      True
      >>> PurePath('/a/b/c.py').full_match('**/*.py')
      True

   Distinto en la versión 3.12: El parámetro *pattern* acepta un
   *path-like object*.

   Distinto en la versión 3.12: Se agregó el parámetro
   *case_sensitive*.

PurePath.relative_to(other, walk_up=False)

   Computa una versión de esta ruta relativa a la ruta representada
   por *other*. Si es imposible, se lanza "ValueError":

      >>> p = PurePosixPath('/etc/passwd')
      >>> p.relative_to('/')
      PurePosixPath('etc/passwd')
      >>> p.relative_to('/etc')
      PurePosixPath('passwd')
      >>> p.relative_to('/usr')
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "pathlib.py", line 941, in relative_to
          raise ValueError(error_message.format(str(self), str(formatted)))
      ValueError: '/etc/passwd' is not in the subpath of '/usr' OR one path is relative and the other is absolute.

   Cuando *walk_up* es falso (el valor predeterminado), la ruta debe
   comenzar con *other*. Cuando el argumento es verdadero, se pueden
   agregar entradas ".." para formar la ruta relativa. En todos los
   demás casos, como las rutas que hacen referencia a diferentes
   unidades, se genera "ValueError".:

      >>> p.relative_to('/usr', walk_up=True)
      PurePosixPath('../etc/passwd')
      >>> p.relative_to('foo', walk_up=True)
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "pathlib.py", line 941, in relative_to
          raise ValueError(error_message.format(str(self), str(formatted)))
      ValueError: '/etc/passwd' is not on the same drive as 'foo' OR one path is relative and the other is absolute.

   Advertencia:

     Esta función es parte de "PurePath" y trabaja con cadenas de
     caracteres. No revisa ni accede a la estructura de archivos
     subyacentes. Esto puede afectar la opción *walk_up* ya que supone
     que no hay enlaces simbólicos en la ruta; si es necesario llame
     primero "resolve()" para resolver los enlaces simbólicos.

   Distinto en la versión 3.12: Se agregó el parámetro *walk_up* (el
   comportamiento anterior es el mismo que "walk_up=False").

   Deprecated since version 3.12, removed in version 3.14: Está
   obsoleto pasar argumentos posicionales adicionales; si se
   suministran, se juntan con *other*.

PurePath.with_name(name)

   Retorna una nueva ruta con "name" cambiado. Si la ruta original no
   tiene nombre, se genera *ValueError*:

      >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
      >>> p.with_name('setup.py')
      PureWindowsPath('c:/Downloads/setup.py')
      >>> p = PureWindowsPath('c:/')
      >>> p.with_name('setup.py')
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/antoine/cpython/default/Lib/pathlib.py", line 751, in with_name
          raise ValueError("%r has an empty name" % (self,))
      ValueError: PureWindowsPath('c:/') has an empty name

PurePath.with_stem(stem)

   Retorna una nueva ruta con "stem" cambiado. Si la ruta original no
   tiene nombre, se lanza *ValueError*:

      >>> p = PureWindowsPath('c:/Downloads/draft.txt')
      >>> p.with_stem('final')
      PureWindowsPath('c:/Downloads/final.txt')
      >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
      >>> p.with_stem('lib')
      PureWindowsPath('c:/Downloads/lib.gz')
      >>> p = PureWindowsPath('c:/')
      >>> p.with_stem('')
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/antoine/cpython/default/Lib/pathlib.py", line 861, in with_stem
          return self.with_name(stem + self.suffix)
        File "/home/antoine/cpython/default/Lib/pathlib.py", line 851, in with_name
          raise ValueError("%r has an empty name" % (self,))
      ValueError: PureWindowsPath('c:/') has an empty name

   Added in version 3.9.

PurePath.with_suffix(suffix)

   Retorna una nueva ruta con "suffix" cambiado. Si la ruta original
   no tiene un sufijo, se agrega el nuevo *suffix*. Si *suffix* es una
   cadena vacía, el sufijo original se elimina:

      >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
      >>> p.with_suffix('.bz2')
      PureWindowsPath('c:/Downloads/pathlib.tar.bz2')
      >>> p = PureWindowsPath('README')
      >>> p.with_suffix('.txt')
      PureWindowsPath('README.txt')
      >>> p = PureWindowsPath('README.txt')
      >>> p.with_suffix('')
      PureWindowsPath('README')

   Distinto en la versión 3.14: A single dot (""."") is considered a
   valid suffix. In previous versions, "ValueError" is raised if a
   single dot is supplied.

PurePath.with_segments(*pathsegments)

   Crea un nuevo objeto de ruta del mismo tipo combinando los
   *pathsegments* dados. Este método se llama siempre que se crea una
   ruta derivada, como "parent" y "relative_to()". Las subclases
   pueden anular este método para pasar información a las rutas
   derivadas, por ejemplo:

      from pathlib import PurePosixPath

      class MyPath(PurePosixPath):
          def __init__(self, *pathsegments, session_id):
              super().__init__(*pathsegments)
              self.session_id = session_id

          def with_segments(self, *pathsegments):
              return type(self)(*pathsegments, session_id=self.session_id)

      etc = MyPath('/etc', session_id=42)
      hosts = etc / 'hosts'
      print(hosts.session_id)  # 42

   Added in version 3.12.

## Rutas concretas

Las rutas concretas son subclases de las rutas puras. Además de las
operaciones proporcionadas por estas últimas, también proporcionan
métodos realizar llamadas del sistema a objetos ruta. Hay tres formas
de crear instancias de rutas concretas:

class pathlib.Path(*pathsegments)

   Una subclase de "PurePath", esta clase representa rutas concretas
   de la *familia* ruta del sistema (al crear una instancia crea ya
   sea "PosixPath" o "WindowsPath"):

      >>> Path('setup.py')
      PosixPath('setup.py')

   *pathsegments* se especifica de manera similar a "PurePath".

class pathlib.PosixPath(*pathsegments)

   Una subclase de "Path" y "PurePosixPath", esta clase representa
   rutas concretas de sistemas de archivos que no son de Windows:

      >>> PosixPath('/etc/hosts')
      PosixPath('/etc/hosts')

   *pathsegments* se especifica de manera similar a "PurePath".

   Distinto en la versión 3.13: Genera el error "UnsupportedOperation"
   en Windows. En versiones anteriores, se generaba el error
   "NotImplementedError".

class pathlib.WindowsPath(*pathsegments)

   Una subclase de "Path" y "PureWindowsPath", esta clase representa
   rutas concretas del sistema de archivos de Windows:

      >>> WindowsPath('c:/', 'Users', 'Ximénez')
      WindowsPath('c:/Users/Ximénez')

   *pathsegments* se especifica de manera similar a "PurePath".

   Distinto en la versión 3.13: Genera el error "UnsupportedOperation"
   en plataformas que no sean Windows. En versiones anteriores, se
   generaba el error "NotImplementedError".

Solo puedes crear instancias de la *familia* de clase que corresponde
a su sistema operativo (permitir llamadas del sistema no compatibles
podría provocar errores o fallas en su aplicación):

   >>> import os
   >>> os.name
   'posix'
   >>> Path('setup.py')
   PosixPath('setup.py')
   >>> PosixPath('setup.py')
   PosixPath('setup.py')
   >>> WindowsPath('setup.py')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "pathlib.py", line 798, in __new__
       % (cls.__name__,))
   UnsupportedOperation: cannot instantiate 'WindowsPath' on your system

Algunos métodos de ruta concretos pueden generar un "OSError" si falla
una llamada del sistema (por ejemplo, porque la ruta no existe).

### Análisis y generación de URI

Los objetos de ruta concretos se pueden crear y representar como URI
de "archivo" que cumplan con **RFC 8089**.

Nota:

  Los URI de archivos no son portables entre máquinas con diferentes
  filesystem encodings.

classmethod Path.from_uri(uri)

   Devuelve un nuevo objeto de ruta a partir del análisis de una URL
   de "archivo". Por ejemplo:

      >>> p = Path.from_uri('file:///etc/hosts')
      PosixPath('/etc/hosts')

   En Windows, los dispositivos DOS y las rutas UNC se pueden analizar
   desde las URI:

      >>> p = Path.from_uri('file:///c:/windows')
      WindowsPath('c:/windows')
      >>> p = Path.from_uri('file://server/share')
      WindowsPath('//server/share')

   Se admiten varias formas variantes:

      >>> p = Path.from_uri('file:////server/share')
      WindowsPath('//server/share')
      >>> p = Path.from_uri('file://///server/share')
      WindowsPath('//server/share')
      >>> p = Path.from_uri('file:c:/windows')
      WindowsPath('c:/windows')
      >>> p = Path.from_uri('file:/c|/windows')
      WindowsPath('c:/windows')

   Se genera "ValueError" si la URI no comienza con "file:" o la ruta
   analizada no es absoluta.

   Added in version 3.13.

   Distinto en la versión 3.14: The URL authority is discarded if it
   matches the local hostname. Otherwise, if the authority isn't empty
   or "localhost", then on Windows a UNC path is returned (as before),
   and on other platforms a "ValueError" is raised.

Path.as_uri()

   Representa la ruta como una URL de "archivo". Se genera
   "ValueError" si la ruta no es absoluta.

      >>> p = PosixPath('/etc/passwd')
      >>> p.as_uri()
      'file:///etc/passwd'
      >>> p = WindowsPath('c:/Windows')
      >>> p.as_uri()
      'file:///c:/Windows'

   Deprecated since version 3.14, will be removed in version 3.19:
   Calling this method from "PurePath" rather than "Path" is possible
   but deprecated. The method's use of "os.fsencode()" makes it
   strictly impure.

### Ampliando y resolviendo caminos

classmethod Path.home()

   Retorna un nuevo objeto ruta que representa el directorio de inicio
   del usuario (como lo retorna "os.path.expanduser()" con el agregado
   "~"). Si el directorio de inicio no se puede resolver, se lanza
   "RuntimeError".

      >>> Path.home()
      PosixPath('/home/antoine')

   Added in version 3.5.

Path.expanduser()

   Retorna una nueva ruta con las construcciones "~" y "~user"
   expandidas, como lo retorna "os.path.expanduser()". Si el
   directorio de inicio no se puede resolver, se lanza "RuntimeError".

      >>> p = PosixPath('~/films/Monty Python')
      >>> p.expanduser()
      PosixPath('/home/eric/films/Monty Python')

   Added in version 3.5.

classmethod Path.cwd()

   Retorna un nuevo objeto ruta que representa el directorio actual
   (como lo retorna "os.getcwd()"):

      >>> Path.cwd()
      PosixPath('/home/antoine/pathlib')

Path.absolute()

   Hace que la ruta sea absoluta, sin normalización ni resolución de
   enlaces simbólicos. Retorna un nuevo objeto de ruta:

      >>> p = Path('tests')
      >>> p
      PosixPath('tests')
      >>> p.absolute()
      PosixPath('/home/antoine/pathlib/tests')

Path.resolve(strict=False)

   Hace que la ruta sea absoluta, resolviendo los enlaces simbólicos.
   Se retorna un nuevo objeto ruta:

      >>> p = Path()
      >>> p
      PosixPath('.')
      >>> p.resolve()
      PosixPath('/home/antoine/pathlib')

   Los componentes "".."" también se eliminan (este es el único método
   para hacerlo):

      >>> p = Path('docs/../setup.py')
      >>> p.resolve()
      PosixPath('/home/antoine/pathlib/setup.py')

   Si no existe una ruta o se encuentra un bucle de enlace simbólico y
   *strict* es "True", se genera "OSError". Si *strict* es "False", la
   ruta se resuelve en la medida de lo posible y cualquier resto se
   agrega sin verificar si existe.

   Distinto en la versión 3.6: Se agregó el parámetro *strict* (el
   comportamiento previo a 3.6 es *strict*).

   Distinto en la versión 3.13: Los bucles de enlaces simbólicos se
   tratan como otros errores: "OSError" se genera en modo estricto y
   no se genera ninguna excepción en modo no estricto. En versiones
   anteriores, "RuntimeError" se genera sin importar el valor de
   *strict*.

Path.readlink()

   Retorna la ruta a la que apunta el vínculo simbólico (como lo
   retorna "os.readlink()"):

      >>> p = Path('mylink')
      >>> p.symlink_to('setup.py')
      >>> p.readlink()
      PosixPath('setup.py')

   Added in version 3.9.

   Distinto en la versión 3.13: Genera "UnsupportedOperation" si
   "os.readlink()" no está disponible. En versiones anteriores, se
   generaba "NotImplementedError".

### Consulta de tipo de archivo y estado

Distinto en la versión 3.8: "exists()", "is_dir()", "is_file()",
"is_mount()", "is_symlink()", "is_block_device()", "is_char_device()",
"is_fifo()", "is_socket()" ahora devuelven "False" en lugar de generar
una excepción para las rutas que contienen caracteres no
representables en el nivel del sistema operativo.

Distinto en la versión 3.14: The methods given above now return
"False" instead of raising any "OSError" exception from the operating
system. In previous versions, some kinds of "OSError" exception are
raised, and others suppressed. The new behaviour is consistent with
"os.path.exists()", "os.path.isdir()", etc. Use "stat()" to retrieve
the file status without suppressing exceptions.

Path.stat(*, follow_symlinks=True)

   Devuelve un objeto "os.stat_result" que contiene información sobre
   esta ruta, como "os.stat()". El resultado se consulta en cada
   llamada a este método.

   Este método normalmente sigue enlaces simbólicos; para evitar
   enlaces simbólicos, agregue el argumento "follow_symlinks = False",
   o use "lstat()".

      >>> p = Path('setup.py')
      >>> p.stat().st_size
      956
      >>> p.stat().st_mtime
      1327883547.852554

   Distinto en la versión 3.10: Se agregó el parámetro
   *follow_symlinks*.

Path.lstat()

   Del mismo modo que "Path.stat()" pero si la ruta apunta a un enlace
   simbólico, retorna la información del enlace simbólico en lugar de
   la de su objetivo.

Path.exists(*, follow_symlinks=True)

   Return "True" if the path points to an existing file or directory.
   "False" will be returned if the path is invalid, inaccessible or
   missing. Use "Path.stat()" to distinguish between these cases.

   Este método normalmente sigue enlaces simbólicos; para comprobar si
   existe un enlace simbólico, agregue el argumento
   "follow_symlinks=False".

      >>> Path('.').exists()
      True
      >>> Path('setup.py').exists()
      True
      >>> Path('/etc').exists()
      True
      >>> Path('nonexistentfile').exists()
      False

   Distinto en la versión 3.12: Se agregó el parámetro
   *follow_symlinks*.

Path.is_file(*, follow_symlinks=True)

   Return "True" if the path points to a regular file. "False" will be
   returned if the path is invalid, inaccessible or missing, or if it
   points to something other than a regular file. Use "Path.stat()" to
   distinguish between these cases.

   Este método normalmente sigue los enlaces simbólicos; para
   excluirlos, agregue el argumento "follow_symlinks=False".

   Distinto en la versión 3.13: Se agregó el parámetro
   *follow_symlinks*.

Path.is_dir(*, follow_symlinks=True)

   Return "True" if the path points to a directory. "False" will be
   returned if the path is invalid, inaccessible or missing, or if it
   points to something other than a directory. Use "Path.stat()" to
   distinguish between these cases.

   Este método normalmente sigue los enlaces simbólicos; para excluir
   los enlaces simbólicos a directorios, agregue el argumento
   "follow_symlinks=False".

   Distinto en la versión 3.13: Se agregó el parámetro
   *follow_symlinks*.

Path.is_symlink()

   Return "True" if the path points to a symbolic link, even if that
   symlink is broken. "False" will be returned if the path is invalid,
   inaccessible or missing, or if it points to something other than a
   symbolic link. Use "Path.stat()" to distinguish between these
   cases.

Path.is_junction()

   Retorna "True" si la ruta apunta a una unión y "False" para
   cualquier otro tipo de archivo. Actualmente, solo Windows admite
   uniones.

   Added in version 3.12.

Path.is_mount()

   Retorna "True" si la ruta es un *mount point*: un punto en un
   sistema de archivos donde otro sistema de archivo se encuentra
   montado. En POSIX, la función comprueba si el padre de *path* ,
   "path/..", se encuentra en un dispositivo diferente que *path*, o
   si "path/.." y *path* apuntan al mismo i-nodo en el mismo
   dispositivo --- esto debería detectar puntos de montajes para todas
   las variantes Unix y POSIX. En Windows, se considera que un punto
   de montaje es una letra de unidad de raíz (por ejemplo, "c:\"), un
   recurso compartido UNC (por ejemplo, "\\server\share") o un
   directorio de sistema de archivos montado.

   Added in version 3.7.

   Distinto en la versión 3.12: Se agregó soporte para Windows.

Path.is_socket()

   Return "True" if the path points to a Unix socket. "False" will be
   returned if the path is invalid, inaccessible or missing, or if it
   points to something other than a Unix socket. Use "Path.stat()" to
   distinguish between these cases.

Path.is_fifo()

   Return "True" if the path points to a FIFO. "False" will be
   returned if the path is invalid, inaccessible or missing, or if it
   points to something other than a FIFO. Use "Path.stat()" to
   distinguish between these cases.

Path.is_block_device()

   Return "True" if the path points to a block device. "False" will be
   returned if the path is invalid, inaccessible or missing, or if it
   points to something other than a block device. Use "Path.stat()" to
   distinguish between these cases.

Path.is_char_device()

   Return "True" if the path points to a character device. "False"
   will be returned if the path is invalid, inaccessible or missing,
   or if it points to something other than a character device. Use
   "Path.stat()" to distinguish between these cases.

Path.samefile(other_path)

   Retorna si la ruta apunta al mismo archivo que *other_path*, que
   puede ser un objeto *Path* o una cadena. La semántica es similar a
   "os.path.samefile()" y "os.path.samestat()".

   Se puede generar "OSError" si no se accede a alguno de los archivos
   por algún motivo.

      >>> p = Path('spam')
      >>> q = Path('eggs')
      >>> p.samefile(q)
      False
      >>> p.samefile('spam')
      True

   Added in version 3.5.

Path.info

   A "PathInfo" object that supports querying file type information.
   The object exposes methods that cache their results, which can help
   reduce the number of system calls needed when switching on file
   type. For example:

      >>> p = Path('src')
      >>> if p.info.is_symlink():
      ...     print('symlink')
      ... elif p.info.is_dir():
      ...     print('directory')
      ... elif p.info.exists():
      ...     print('something else')
      ... else:
      ...     print('not found')
      ...
      directory

   If the path was generated from "Path.iterdir()" then this attribute
   is initialized with some information about the file type gleaned
   from scanning the parent directory. Merely accessing "Path.info"
   does not perform any filesystem queries.

   To fetch up-to-date information, it's best to call "Path.is_dir()",
   "is_file()" and "is_symlink()" rather than methods of this
   attribute. There is no way to reset the cache; instead you can
   create a new path object with an empty info cache via "p =
   Path(p)".

   Added in version 3.14.

### Lectura y escritura de archivos

Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)

   Abre el archivo señalado por la ruta, como lo hace la función
   incorporada "open()":

      >>> p = Path('setup.py')
      >>> with p.open() as f:
      ...     f.readline()
      ...
      '#!/usr/bin/env python3\n'

Path.read_text(encoding=None, errors=None, newline=None)

   Retorna el contenido decodificado del archivo apuntado como una
   cadena:

      >>> p = Path('my_text_file')
      >>> p.write_text('Text file contents')
      18
      >>> p.read_text()
      'Text file contents'

   El archivo se abre y luego se cierra. Los parámetros opcionales
   funcionan de la misma manera que en "open()".

   Added in version 3.5.

   Distinto en la versión 3.13: Se agregó el parámetro *newline*.

Path.read_bytes()

   Retorna el contenido binario del archivo apuntado como un objeto
   bytes:

      >>> p = Path('my_binary_file')
      >>> p.write_bytes(b'Binary file contents')
      20
      >>> p.read_bytes()
      b'Binary file contents'

   Added in version 3.5.

Path.write_text(data, encoding=None, errors=None, newline=None)

   Abre el archivo apuntado en modo texto, escribe *data* y cierra el
   archivo:

      >>> p = Path('my_text_file')
      >>> p.write_text('Text file contents')
      18
      >>> p.read_text()
      'Text file contents'

   Se sobrescribe un archivo existente con el mismo nombre. Los
   parámetros opcionales tienen el mismo significado que en "open()".

   Added in version 3.5.

   Distinto en la versión 3.10: Se agregó el parámetro *newline*.

Path.write_bytes(data)

   Abre el archivo apuntado en modo bytes, escribe *data* y cierra el
   archivo:

      >>> p = Path('my_binary_file')
      >>> p.write_bytes(b'Binary file contents')
      20
      >>> p.read_bytes()
      b'Binary file contents'

   Se sobrescribe un archivo existente con el mismo nombre.

   Added in version 3.5.

### Directorios de lectura

Path.iterdir()

   Cuando la ruta apunta a un directorio, produce objetos de ruta del
   contenido del directorio:

      >>> p = Path('docs')
      >>> for child in p.iterdir(): child
      ...
      PosixPath('docs/conf.py')
      PosixPath('docs/_templates')
      PosixPath('docs/make.bat')
      PosixPath('docs/index.rst')
      PosixPath('docs/_build')
      PosixPath('docs/_static')
      PosixPath('docs/Makefile')

   Los elementos secundarios se obtienen en un orden arbitrario y no
   se incluyen las entradas especiales "'.'" y "'..'". Si se elimina o
   se agrega un archivo al directorio después de crear el iterador, no
   se especifica si se incluye un objeto de ruta para ese archivo.

   Si la ruta no es un directorio o es inaccesible por algún motivo,
   se genera "OSError".

Path.glob(pattern, *, case_sensitive=None, recurse_symlinks=False)

   Analiza el patrón comodín relativo a esta ruta para producir todos
   los archivos coincidentes (de cualquier tipo):

      >>> sorted(Path('.').glob('*.py'))
      [PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]
      >>> sorted(Path('.').glob('*/*.py'))
      [PosixPath('docs/conf.py')]
      >>> sorted(Path('.').glob('**/*.py'))
      [PosixPath('build/lib/pathlib.py'),
       PosixPath('docs/conf.py'),
       PosixPath('pathlib.py'),
       PosixPath('setup.py'),
       PosixPath('test_pathlib.py')]

   Nota:

     The paths are returned in no particular order. If you need a
     specific order, sort the results.

   Ver también: Documentación Lenguaje de patrones.

   De forma predeterminada, o cuando el argumento de sólo palabra
   clave *case_sensitive* está configurado en "None", este método
   coincide con las rutas utilizando reglas de mayúsculas y minúsculas
   específicas de la plataforma: normalmente, distingue entre
   mayúsculas y minúsculas en POSIX y no distingue entre mayúsculas y
   minúsculas en Windows. Se configura *case_sensitive* en "True" o
   "False" para anular este comportamiento.

   De forma predeterminada, o cuando el argumento de palabra clave
   *recurse_symlinks* se establece en "False", este método sigue los
   enlaces simbólicos excepto cuando se expanden los comodines ""**"".
   Establezca *recurse_symlinks* en "True" para seguir siempre los
   enlaces simbólicos.

   Nota:

     Any "OSError" exceptions raised from scanning the filesystem are
     suppressed. This includes "PermissionError" when accessing
     directories without read permission.

   Levanta un auditing event "pathlib.Path.glob" con argumentos
   "self", "pattern".

   Distinto en la versión 3.12: Se agregó el parámetro
   *case_sensitive*.

   Distinto en la versión 3.13: Se agregó el parámetro
   *recurse_symlinks*.

   Distinto en la versión 3.13: El parámetro *pattern* acepta un
   *path-like object*.

   Distinto en la versión 3.13: Se suprimen todas las excepciones
   "OSError" generadas al escanear el sistema de archivos. En
   versiones anteriores, dichas excepciones se suprimían en muchos
   casos, pero no en todos.

Path.rglob(pattern, *, case_sensitive=None, recurse_symlinks=False)

   Incorpore de forma recursiva el *pattern* relativo dado. Es como
   llamar a "Path.glob()" con ""**/"" agregado delante de *pattern*.

   Nota:

     The paths are returned in no particular order. If you need a
     specific order, sort the results.

   Nota:

     Any "OSError" exceptions raised from scanning the filesystem are
     suppressed. This includes "PermissionError" when accessing
     directories without read permission.

   Ver también: Documentación Lenguaje de patrones y "Path.glob()".

   Levanta un auditing event "pathlib.Path.rglob" con argumentos
   "self", "pattern".

   Distinto en la versión 3.12: Se agregó el parámetro
   *case_sensitive*.

   Distinto en la versión 3.13: Se agregó el parámetro
   *recurse_symlinks*.

   Distinto en la versión 3.13: El parámetro *pattern* acepta un
   *path-like object*.

Path.walk(top_down=True, on_error=None, follow_symlinks=False)

   Genera los nombres de archivos en un árbol de directorios
   recorriendo el árbol de arriba hacia abajo o de abajo hacia arriba.

   Para cada directorio en el árbol de directorios con raíz en *self*
   (incluyendo *self* pero excluyendo '.' y '..'), el método produce
   una tupla de 3 de elementos (o tripleta) "(dirpath, dirnames,
   filenames)".

   *dirpath* es un objeto "Path" al directorio que se está recorriendo
   actualmente, *dirnames* es una lista de cadenas de caracteres para
   los nombres de los subdirectorios en *dirpath* (excluyendo "'.'" y
   "'..'"), y *filenames* es una lista de cadenas de caracteres para
   los nombres de los archivos que no son directorios en *dirpath*.
   Para obtener una ruta completa (que comienza con *self*) a un
   archivo o directorio en *dirpath*, se ejecuta "dirpath / name". El
   orden de las listas depende del sistema de archivos.

   Si el argumento opcional *top_down* es verdadero (que es el valor
   predeterminado), la tripleta de un directorio se genera antes que
   las tripletas de cualquiera de sus subdirectorios (los directorios
   se recorren de arriba hacia abajo). Si *top_down* es falso, la
   tripleta de un directorio se genera después de las tripletas de
   todos sus subdirectorios (los directorios se recorren de abajo
   hacia arriba). Sin importar el valor de *top_down*, la lista de
   subdirectorios se recupera antes de que se recorran las tripletas
   del directorio y sus subdirectorios.

   Cuando *top_down* es verdadero, el llamador puede modificar la
   lista *dirnames* en el lugar (por ejemplo, utilizando "del" o la
   asignación de sectores), y "Path.walk()" solo recurrirá a los
   subdirectorios cuyos nombres permanezcan en *dirnames*. Esto se
   puede utilizar para podar la búsqueda, o para imponer un orden
   específico de visita, o incluso para informar a "Path.walk()" sobre
   los directorios que el llamador crea o renombra antes de reanudar
   "Path.walk()" nuevamente. Modificar *dirnames* cuando *top_down* es
   falso no tiene ningún efecto sobre el comportamiento de
   "Path.walk()" ya que los directorios en *dirnames* ya se han
   generado en el momento en que *dirnames* se cede al llamador.

   De forma predeterminada, los errores de "os.scandir()" se ignoran.
   Si se especifica el argumento opcional *on_error*, debe ser un
   objeto invocable; se llamará con un argumento, una instancia de
   "OSError". El objeto invocable puede manejar el error para
   continuar la ejecución o volver a generarlo para detenerla. Tenga
   en cuenta que el nombre del archivo está disponible como el
   atributo "filename" del objeto de excepción.

   De forma predeterminada, "Path.walk()" no sigue los enlaces
   simbólicos, sino que los agrega a la lista *filenames*. Establezca
   *follow_symlinks* como verdadero para resolver los enlaces
   simbólicos y colocarlos en *dirnames* y *filenames* según
   corresponda para sus destinos y, en consecuencia, visitar los
   directorios a los que apuntan los enlaces simbólicos (donde sea
   compatible).

   Nota:

     Tener en cuenta que establecer *follow_symlinks* como verdadero
     puede generar una recursión infinita si un enlace apunta a un
     directorio principal de sí mismo. "Path.walk()" no realiza un
     seguimiento de los directorios que ya ha visitado.

   Nota:

     "Path.walk()" asume que los directorios que recorre no se
     modifican durante la ejecución. Por ejemplo, si un directorio de
     *dirnames* ha sido reemplazado por un enlace simbólico y
     *follow_symlinks* es falso, "Path.walk()" intentará descender a
     él. Para evitar este comportamiento, elimine los directorios de
     *dirnames* según corresponda.

   Nota:

     A diferencia de "os.walk()", "Path.walk()" enumera enlaces
     simbólicos a directorios en *filenames* si *follow_symlinks* es
     falso.

   Este ejemplo muestra la cantidad de bytes utilizados por todos los
   archivos en cada directorio, mientras ignora los directorios
   "__pycache__":

      from pathlib import Path
      for root, dirs, files in Path("cpython/Lib/concurrent").walk(on_error=print):
        print(
            root,
            "consumes",
            sum((root / file).stat().st_size for file in files),
            "bytes in",
            len(files),
            "non-directory files"
        )
        if '__pycache__' in dirs:
              dirs.remove('__pycache__')

   El siguiente ejemplo es una implementación simple de
   "shutil.rmtree()". Recorrer el árbol de abajo a arriba es esencial
   ya que "rmdir()" no permite eliminar un directorio antes de que
   esté vacío:

      # Delete everything reachable from the directory "top".
      # CAUTION:  This is dangerous! For example, if top == Path('/'),
      # it could delete all of your files.
      for root, dirs, files in top.walk(top_down=False):
          for name in files:
              (root / name).unlink()
          for name in dirs:
              (root / name).rmdir()

   Added in version 3.12.

### Creando archivos y directorios

Path.touch(mode=0o666, exist_ok=True)

   Crea un archivo en esta ruta dada. Si se proporciona *mode*, se
   combina con el valor "umask" del proceso para determinar el modo de
   archivo y los indicadores de acceso. Si el archivo ya existe, la
   función se ejecuta correctamente cuando *exist_ok* es verdadero (y
   su hora de modificación se actualiza a la hora actual); de lo
   contrario, se genera "FileExistsError".

   Ver también:

     Los métodos "open()", "write_text()" y "write_bytes()" se
     utilizan a menudo para crear archivos.

Path.mkdir(mode=0o777, parents=False, exist_ok=False)

   Crea un nuevo directorio en esta ruta indicada. Si se proporciona
   *mode*, se combina con el valor "umask" del proceso para determinar
   el modo de archivo y los indicadores de acceso. Si la ruta ya
   existe, se genera "FileExistsError".

   Si *parents* es verdadero, los padres que faltan de esta ruta se
   crean según sea necesario; se crean con los permisos
   predeterminados sin tener en cuenta *mode* (imitando el comando
   POSIX "mkdir -p").

   Si *parents* es falso (el valor predeterminado), se genera un padre
   que falta "FileNotFoundError".

   Si *exist_ok* es falso (el valor predeterminado), se genera
   "FileExistsError" si el directorio de destino ya existe.

   Si *exist_ok* es verdadero, no se generará "FileExistsError" a
   menos que la ruta dada ya exista en el sistema de archivos y no sea
   un directorio (el mismo comportamiento que el comando POSIX "mkdir
   -p").

   Distinto en la versión 3.5: Se agregó el parámetro *exist_ok*.

Path.symlink_to(target, target_is_directory=False)

   Convierte esta ruta en un enlace simbólico que apunte a *target*.

   En Windows, un enlace simbólico representa un archivo o un
   directorio y no se transforma en el destino de forma dinámica. Si
   el destino está presente, se creará el tipo de enlace simbólico
   para que coincida. De lo contrario, el enlace simbólico se creará
   como un directorio si *target_is_directory* es verdadero o como un
   enlace simbólico de archivo (el valor predeterminado) en caso
   contrario. En plataformas que no sean Windows, se ignora
   *target_is_directory*.

      >>> p = Path('mylink')
      >>> p.symlink_to('setup.py')
      >>> p.resolve()
      PosixPath('/home/antoine/pathlib/setup.py')
      >>> p.stat().st_size
      956
      >>> p.lstat().st_size
      8

   Nota:

     El orden de los argumentos (*link*, *target*) es el reverso de
     "os.symlink()"'s.

   Distinto en la versión 3.13: Genera "UnsupportedOperation" si
   "os.symlink()" no está disponible. En versiones anteriores, se
   generaba "NotImplementedError".

Path.hardlink_to(target)

   Hace de esta ruta un enlace fijo que apunta al mismo archivo que
   *target*.

   Nota:

     El orden de los argumentos (link, target) es el reverso de
     "os.link()".

   Added in version 3.10.

   Distinto en la versión 3.13: Genera "UnsupportedOperation" si
   "os.link()" no está disponible. En versiones anteriores, se
   generaba "NotImplementedError".

### Copying, moving and deleting

Path.copy(target, *, follow_symlinks=True, preserve_metadata=False)

   Copy this file or directory tree to the given *target*, and return
   a new "Path" instance pointing to *target*.

   If the source is a file, the target will be replaced if it is an
   existing file. If the source is a symlink and *follow_symlinks* is
   true (the default), the symlink's target is copied. Otherwise, the
   symlink is recreated at the destination.

   If *preserve_metadata* is false (the default), only directory
   structures and file data are guaranteed to be copied. Set
   *preserve_metadata* to true to ensure that file and directory
   permissions, flags, last access and modification times, and
   extended attributes are copied where supported. This argument has
   no effect when copying files on Windows (where metadata is always
   preserved).

   Nota:

     Where supported by the operating system and file system, this
     method performs a lightweight copy, where data blocks are only
     copied when modified. This is known as copy-on-write.

   Added in version 3.14.

Path.copy_into(target_dir, *, follow_symlinks=True, preserve_metadata=False)

   Copy this file or directory tree into the given *target_dir*, which
   should be an existing directory. Other arguments are handled
   identically to "Path.copy()". Returns a new "Path" instance
   pointing to the copy.

   Added in version 3.14.

Path.rename(target)

   Cambie el nombre de este archivo o directorio al *target* indicado
   y devuelva una nueva instancia de "Path" que apunte a *target*. En
   Unix, si *target* existe y es un archivo, se reemplazará de forma
   silenciosa si el usuario tiene permiso. En Windows, si *target*
   existe, se generará "FileExistsError". *target* puede ser una
   cadena u otro objeto de ruta:

      >>> p = Path('foo')
      >>> p.open('w').write('some text')
      9
      >>> target = Path('bar')
      >>> p.rename(target)
      PosixPath('bar')
      >>> target.open().read()
      'some text'

   La ruta de destino puede ser absoluta o relativa. Las rutas
   relativas se interpretan en relación con el directorio de trabajo
   actual, *not* el directorio del objeto "Path".

   Se implementa en términos de "os.rename()" y ofrece las mismas
   garantías.

   Distinto en la versión 3.8: Se agregó valor de retorno, devuelve la
   nueva instancia "Path".

Path.replace(target)

   Cambie el nombre de este archivo o directorio por el *target*
   indicado y devuelva una nueva instancia de "Path" que apunte a
   *target*. Si *target* apunta a un archivo existente o a un
   directorio vacío, se reemplazará sin condiciones.

   La ruta de destino puede ser absoluta o relativa. Las rutas
   relativas se interpretan en relación con el directorio de trabajo
   actual, *not* el directorio del objeto "Path".

   Distinto en la versión 3.8: Se agregó valor de retorno, devuelve la
   nueva instancia "Path".

Path.move(target)

   Move this file or directory tree to the given *target*, and return
   a new "Path" instance pointing to *target*.

   If the *target* doesn't exist it will be created. If both this path
   and the *target* are existing files, then the target is
   overwritten. If both paths point to the same file or directory, or
   the *target* is a non-empty directory, then "OSError" is raised.

   If both paths are on the same filesystem, the move is performed
   with "os.replace()". Otherwise, this path is copied (preserving
   metadata and symlinks) and then deleted.

   Added in version 3.14.

Path.move_into(target_dir)

   Move this file or directory tree into the given *target_dir*, which
   should be an existing directory. Returns a new "Path" instance
   pointing to the moved path.

   Added in version 3.14.

Path.unlink(missing_ok=False)

   Elimine el archivo o enlace simbólico. Si la ruta apunta a un
   directorio, use "Path.rmdir()" en su lugar.

   Si *missing_ok* es falso (el valor predeterminado), se genera
   "FileNotFoundError" si la ruta no existe.

   Si *missing_ok* es verdadero, las excepciones "FileNotFoundError"
   serán ignoradas (el mismo comportamiento que el comando POSIX "rm
   -f").

   Distinto en la versión 3.8: Se agregó el parámetro *missing_ok*.

Path.rmdir()

   Elimina el directorio. El directorio debe estar vacío.

### Permisos y propiedad

Path.owner(*, follow_symlinks=True)

   Devuelve el nombre del usuario propietario del archivo. Se genera
   el error "KeyError" si el identificador de usuario (UID) del
   archivo no se encuentra en la base de datos del sistema.

   Este método normalmente sigue enlaces simbólicos; para obtener el
   propietario del enlace simbólico, agregue el argumento
   "follow_symlinks=False".

   Distinto en la versión 3.13: Genera "UnsupportedOperation" si el
   módulo "pwd" no está disponible. En versiones anteriores, se
   generaba "NotImplementedError".

   Distinto en la versión 3.13: Se agregó el parámetro
   *follow_symlinks*.

Path.group(*, follow_symlinks=True)

   Devuelve el nombre del grupo propietario del archivo. Se genera
   "KeyError" si no se encuentra el identificador de grupo (GID) del
   archivo en la base de datos del sistema.

   Este método normalmente sigue enlaces simbólicos; para obtener el
   grupo del enlace simbólico, agregue el argumento
   "follow_symlinks=False".

   Distinto en la versión 3.13: Genera "UnsupportedOperation" si el
   módulo "grp" no está disponible. En versiones anteriores, se
   generaba "NotImplementedError".

   Distinto en la versión 3.13: Se agregó el parámetro
   *follow_symlinks*.

Path.chmod(mode, *, follow_symlinks=True)

   Cambia el modo y los permisos de archivo, como "os.chmod()".

   Este método normalmente sigue enlaces simbólicos. Algunas versiones
   de Unix admiten el cambio de permisos en el enlace simbólico en sí;
   en estas plataformas puede agregar el argumento
   "follow_symlinks=False", o usar "lchmod()".

      >>> p = Path('setup.py')
      >>> p.stat().st_mode
      33277
      >>> p.chmod(0o444)
      >>> p.stat().st_mode
      33060

   Distinto en la versión 3.10: Se agregó el parámetro
   *follow_symlinks*.

Path.lchmod(mode)

   Del mismo modo que "Path.chmod()" pero si la ruta apunta a un
   enlace simbólico, el modo del enlace simbólico cambia en lugar del
   de su objetivo.

## Lenguaje de patrones

Los siguientes comodines son compatibles con los patrones para
"full_match()", "glob()" y "rglob()":

"**" (segmento completo)
   Coincide con cualquier número de segmentos de archivo o directorio,
   incluido cero.

"*" (segmento completo)
   Coincide con un segmento de archivo o directorio.

"*" (parte de un segmento)
   Coincide con cualquier número de caracteres no separadores,
   incluido el cero.

"?"
   Coincide con un carácter no separador.

"[seq]"
   Matches one character in *seq*, where *seq* is a sequence of
   characters. Range expressions are supported; for example, "[a-z]"
   matches any lowercase ASCII letter. Multiple ranges can be
   combined: "[a-zA-Z0-9_]" matches any ASCII letter, digit, or
   underscore.

"[!seq]"
   Matches one character not in *seq*, where *seq* follows the same
   rules as above.

Para una coincidencia literal, encierre los metacaracteres entre
corchetes. Por ejemplo, ""[?]"" coincide con el carácter ""?"".

El comodín ""**"" permite la codificación recursiva. Algunos ejemplos:

+---------------------------+-----------------------------------------------------------------------+
| Patrón                    | Significado                                                           |
|===========================|=======================================================================|
## | ""**/*""                  | Cualquier camino con al menos un segmento.                            |

## | ""**/*.py""               | Cualquier ruta con un segmento final que termine "".py"".             |

## | ""assets/**""             | Cualquier ruta que comience con ""assets/"".                          |

| ""assets/**/*""           | Cualquier ruta que comience con ""assets/"", excluyendo ""assets/""   |
## |                           | en sí.                                                                |

Nota:

  Al utilizar el comodín ""**"", se visitan todos los directorios del
  árbol. Las búsquedas en árboles de directorios grandes pueden llevar
  mucho tiempo.

Distinto en la versión 3.13: La codificación con un patrón que termina
en ""**"" devuelve tanto archivos como directorios. En versiones
anteriores, solo se devolvían directorios.

En "Path.glob()" y "rglob()", se puede agregar una barra diagonal
final al patrón para que coincida solo con directorios.

Distinto en la versión 3.11: El uso de un patrón que termina con un
separador de componentes de ruta de acceso ("sep" o "altsep") solo
devuelve directorios.

## Comparación con el módulo "glob"

Los patrones aceptados y los resultados generados por "Path.glob()" y
"Path.rglob()" difieren ligeramente de los del módulo "glob":

1. Los archivos que comienzan con un punto no son especiales en
   pathlib. Es como pasar "include_hidden=True" a "glob.glob()".

2. Los componentes del patrón ""**"" siempre son recursivos en
   pathlib. Esto es como pasar "recursive=True" a "glob.glob()".

3. Los componentes del patrón ""**"" no siguen los enlaces simbólicos
   de forma predeterminada en pathlib. Este comportamiento no tiene
   equivalente en "glob.glob()", pero puede pasar
   "recurse_symlinks=True" a "Path.glob()" para lograr un
   comportamiento compatible.

4. Al igual que todos los objetos "PurePath" y "Path", los valores
   devueltos por "Path.glob()" y "Path.rglob()" no incluyen barras
   diagonales finales.

5. Los valores devueltos de "path.glob()" y "path.rglob()" de pathlib
   incluyen *path* como prefijo, a diferencia de los resultados de
   "glob.glob(root_dir=path)".

6. Los valores devueltos de "path.glob()" y "path.rglob()" de pathlib
   pueden incluir el propio *path*, por ejemplo, al incluir ""**"",
   mientras que los resultados de "glob.glob(root_dir=path)" nunca
   incluyen una cadena vacía que corresponda a *path*.

## Comparación con los módulos "os" y "os.path"

pathlib implementa operaciones de ruta utilizando objetos "PurePath" y
"Path", por lo que se dice que es *object-oriented*. Por otro lado,
los módulos "os" y "os.path" proporcionan funciones que funcionan con
objetos "str" y "bytes" de bajo nivel, lo que es un enfoque más propio
de *procedural*. Algunos usuarios consideran que el estilo orientado a
objetos es más legible.

Muchas funciones de "os" y "os.path" admiten rutas "bytes" y paths
relative to directory descriptors. Estas funciones no están
disponibles en pathlib.

Los tipos "str" y "bytes" de Python, y partes de los módulos "os" y
"os.path", están escritos en C y son muy rápidos. pathlib está escrito
en Python puro y a menudo es más lento, pero rara vez lo
suficientemente lento como para ser importante.

la normalización de rutas de pathlib es ligeramente más estricta y
consistente que la de "os.path". Por ejemplo, mientras que
"os.path.abspath()" elimina los segmentos "".."" de una ruta, que
pueden cambiar su significado si hay enlaces simbólicos involucrados,
"Path.absolute()" conserva estos segmentos para mayor seguridad.

la normalización de rutas de pathlib puede hacer que no sea adecuado
para algunas aplicaciones:

1. pathlib normaliza "Path("my_folder/")" a "Path("my_folder")", lo
   que cambia el significado de una ruta cuando se proporciona a
   varias API del sistema operativo y utilidades de línea de comandos.
   En concreto, la ausencia de un separador final puede permitir que
   la ruta se resuelva como un archivo o directorio, en lugar de solo
   como un directorio.

2. pathlib normaliza "Path("./my_program")" a "Path("my_program")", lo
   que cambia el significado de una ruta cuando se utiliza como ruta
   de búsqueda ejecutable, como en un shell o al generar un proceso
   secundario. En concreto, la ausencia de un separador en la ruta
   puede obligar a que se busque en "PATH" en lugar de en el
   directorio actual.

Como consecuencia de estas diferencias, pathlib no es un reemplazo
directo para "os.path".

### Herramientas correspondientes

A continuación se muestra una tabla que asigna varias funciones "os" a
sus equivalentes en "PurePath"/"Path".

+---------------------------------------+------------------------------------------------+
| "os" y "os.path"                      | "pathlib"                                      |
|=======================================|================================================|
## | "os.path.dirname()"                   | "PurePath.parent"                              |

## | "os.path.basename()"                  | "PurePath.name"                                |

## | "os.path.splitext()"                  | "PurePath.stem", "PurePath.suffix"             |

## | "os.path.join()"                      | "PurePath.joinpath()"                          |

## | "os.path.isabs()"                     | "PurePath.is_absolute()"                       |

## | "os.path.relpath()"                   | "PurePath.relative_to()" [1]                   |

## | "os.path.expanduser()"                | "Path.expanduser()" [2]                        |

## | "os.path.realpath()"                  | "Path.resolve()"                               |

## | "os.path.abspath()"                   | "Path.absolute()" [3]                          |

## | "os.path.exists()"                    | "Path.exists()"                                |

## | "os.path.isfile()"                    | "Path.is_file()"                               |

## | "os.path.isdir()"                     | "Path.is_dir()"                                |

## | "os.path.islink()"                    | "Path.is_symlink()"                            |

## | "os.path.isjunction()"                | "Path.is_junction()"                           |

## | "os.path.ismount()"                   | "Path.is_mount()"                              |

## | "os.path.samefile()"                  | "Path.samefile()"                              |

## | "os.getcwd()"                         | "Path.cwd()"                                   |

## | "os.stat()"                           | "Path.stat()"                                  |

## | "os.lstat()"                          | "Path.lstat()"                                 |

## | "os.listdir()"                        | "Path.iterdir()"                               |

## | "os.walk()"                           | "Path.walk()" [4]                              |

## | "os.mkdir()", "os.makedirs()"         | "Path.mkdir()"                                 |

## | "os.link()"                           | "Path.hardlink_to()"                           |

## | "os.symlink()"                        | "Path.symlink_to()"                            |

## | "os.readlink()"                       | "Path.readlink()"                              |

## | "os.rename()"                         | "Path.rename()"                                |

## | "os.replace()"                        | "Path.replace()"                               |

## | "os.remove()", "os.unlink()"          | "Path.unlink()"                                |

## | "os.rmdir()"                          | "Path.rmdir()"                                 |

## | "os.chmod()"                          | "Path.chmod()"                                 |

## | "os.lchmod()"                         | "Path.lchmod()"                                |

-[ Notas al pie ]-

[1] "os.path.relpath()" llama a "abspath()" para hacer que las rutas
    sean absolutas y eliminar partes "".."", mientras que
    "PurePath.relative_to()" es una operación léxica que genera
    "ValueError" cuando los anclajes de sus entradas difieren (por
    ejemplo, si una ruta es absoluta y la otra relativa).

[2] "os.path.expanduser()" devuelve la ruta sin cambios si no se puede
    resolver el directorio de inicio, mientras que "Path.expanduser()"
    genera "RuntimeError".

[3] "os.path.abspath()" elimina los componentes "".."" sin resolver
    los enlaces simbólicos, lo que puede cambiar el significado de la
    ruta, mientras que "Path.absolute()" deja cualquier componente
    "".."" en la ruta.

[4] "os.walk()" siempre sigue los enlaces simbólicos al categorizar
    rutas en *dirnames* y *filenames*, mientras que "Path.walk()"
    categoriza todos los enlaces simbólicos en *filenames* cuando
    *follow_symlinks* es falso (el valor predeterminado).

## Protocols

The "pathlib.types" module provides types for static type checking.

Added in version 3.14.

class pathlib.types.PathInfo

   A "typing.Protocol" describing the "Path.info" attribute.
   Implementations may return cached results from their methods.

   exists(*, follow_symlinks=True)

      Return "True" if the path is an existing file or directory, or
      any other kind of file; return "False" if the path doesn't
      exist.

      If *follow_symlinks* is "False", return "True" for symlinks
      without checking if their targets exist.

   is_dir(*, follow_symlinks=True)

      Return "True" if the path is a directory, or a symbolic link
      pointing to a directory; return "False" if the path is (or
      points to) any other kind of file, or if it doesn't exist.

      If *follow_symlinks* is "False", return "True" only if the path
      is a directory (without following symlinks); return "False" if
      the path is any other kind of file, or if it doesn't exist.

   is_file(*, follow_symlinks=True)

      Return "True" if the path is a file, or a symbolic link pointing
      to a file; return "False" if the path is (or points to) a
      directory or other non-file, or if it doesn't exist.

      If *follow_symlinks* is "False", return "True" only if the path
      is a file (without following symlinks); return "False" if the
      path is a directory or other non-file, or if it doesn't exist.

   is_symlink()

      Return "True" if the path is a symbolic link (even if broken);
      return "False" if the path is a directory or any kind of file,
      or if it doesn't exist.
