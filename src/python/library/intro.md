---
title: Introducción
source_url: https://docs.python.org/es/3
source_path: library/intro.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3020
---

# Introducción

La "biblioteca Python" contiene varios tipos de componentes
diferentes.

Contiene tipos de datos que normalmente se considerarían parte del
"núcleo" de un lenguaje, como números y listas.  Para estos tipos, el
núcleo del lenguaje Python define la forma de los literales y coloca
algunas restricciones a su semántica, pero no define completamente la
semántica.  (Por otro lado, el núcleo del lenguaje sí define
propiedades sintácticas como la ortografía y las prioridades de los
operadores.)

La biblioteca también contiene funciones y excepciones incorporadas
--- objetos que pueden ser utilizados por todo código Python sin la
necesidad de una declaración "import". Algunas de ellos están
definidas por el núcleo del lenguaje, pero muchos no son esenciales
para la semántica del núcleo y sólo se describen aquí.

La mayor parte de la biblioteca, sin embargo, consiste en una
colección de módulos. Hay muchas maneras de diseccionar esta
colección.  Algunos módulos están escritos en C y fueron incorporados
en el intérprete de Python; otros están escritos en Python y se
importan en código fuente.  Algunos módulos proporcionan interfaces
muy específicas de Python, como la impresión de un *stack trace*;
otros proporcionan interfaces que son específicas para determinados
sistemas operativos, como el acceso a hardware específico; otros
proveen interfaces específicas para un dominio de aplicación concreto,
como la World Wide Web. Algunos módulos están disponibles en todas las
versiones y plataformas de Python; otros sólo están disponibles cuando
el sistema subyacente los soporta o los requiere; otros solo están
disponibles cuando se ha elegido una opción de configuración
particular en el momento en que compiló e instaló Python.

Este manual está organizado "desde adentro hacia afuera:" primero
describe las funciones integradas, los tipos de datos y las
excepciones, y finalmente describe los módulos, agrupados en capítulos
de módulos relacionados.

Esto significa que si comienza a leer este manual desde el principio,
y salta al siguiente capítulo cuando se aburra, obtendrá una visión
general razonable de los módulos y áreas de aplicación disponibles que
son soportados por la biblioteca de Python.  Por supuesto, no *tienes*
que leerlo necesariamente como una novela --- sino que también puedes
navegar por la tabla de contenidos (al principio del manual), o buscar
una función, módulo o término específico en el glosario (en la parte
final del manual).  Y por último, si disfruta aprender sobre
diferentes temas de manera aleatoria, puede escoger un número de
página al azar (ver módulo "random") y leer una o dos secciones.
Independientemente del orden en que lea las secciones de este manual,
es útil comenzar con el capítulo Funciones incorporadas, ya que el
resto del manual asume la familiaridad con este material.

¡Que comience el espectáculo!

## Notas sobre la disponibilidad

* Una nota de "Disponibilidad: Unix" significa que esta función se
  encuentra comúnmente en los sistemas Unix.  Pero no hace ninguna
  afirmación sobre su existencia en un sistema operativo específico.

* If not separately noted, all functions that claim "Availability:
  Unix" are supported on macOS, iOS and Android, all of which build on
  a Unix core.

* Si una nota de disponibilidad contiene tanto una versión mínima del
  Kernel como una versión mínima de libc, entonces ambas condiciones
  deben cumplirse. Por ejemplo, una característica con la nota
  *Availability: Linux >= 3.17 with glibc >= 2.27* requiere tanto
  Linux 3.17 o posterior como glibc 2.27 o posterior.

### Plataformas WebAssembly

Las plataformas WebAssembly "wasm32-emscripten" (Emscripten) y
"wasm32-wasi" (WASI) proporcionan un subconjunto de APIs POSIX. Los
tiempos de ejecución de WebAssembly y los navegadores están aislados y
tienen acceso limitado al host y a los recursos externos. Cualquier
módulo de la biblioteca estándar de Python que utilice procesos,
hilos, redes, señales u otras formas de comunicación entre procesos
(IPC), no está disponible o puede no funcionar como en otros sistemas
tipo Unix. La E/S de archivos, el sistema de archivos y las funciones
relacionadas con permisos Unix también están restringidas. Emscripten
no permite el bloqueo de E/S. Otras operaciones bloqueantes como
"sleep()" bloquean el bucle de eventos del navegador.

Las propiedades y el comportamiento de Python en plataformas
WebAssembly dependen de la versión del SDK Emscripten o del SDK WASI,
de los tiempos de ejecución WASM (navegador, NodeJS, wasmtime) y de
los indicadores de tiempo de compilación de Python. WebAssembly,
Emscripten, y WASI son estándares en evolución; algunas
características como las redes pueden ser soportadas en el futuro.

Para Python en el navegador, los usuarios deberían considerar Pyodide
o PyScript. PyScript está construido sobre Pyodide, que a su vez está
construido sobre CPython y Emscripten. Pyodide proporciona acceso a
las APIs JavaScript y DOM de los navegadores, así como capacidades de
red limitadas con las APIs "XMLHttpRequest" y "Fetch" de JavaScript.

* Las APIs relacionadas con procesos no están disponibles o siempre
  fallan con un error. Esto incluye APIs que generan nuevos procesos
  ("fork()", "execve()"), esperan procesos ("waitpid()"), envían
  señales ("kill()"), o interactúan con procesos. El "subprocess" se
  puede importar pero no funciona.

* El módulo "socket" está disponible, pero es limitado y se comporta
  de forma diferente a otras plataformas. En Emscripten, los sockets
  son siempre no bloqueantes y requieren código JavaScript adicional y
  auxiliares en el servidor para proxy TCP a través de WebSockets; ver
  Emscripten Networking para más información. Vista previa de
  instantánea WASI  1 permite sólo sockets desde un descriptor de
  fichero existente.

* Algunas funciones son stubs que no hacen nada y siempre devuelven
  valores codificados.

* Las funciones relacionadas con descriptores de archivos, permisos de
  archivos, propiedad de archivos y enlaces son limitadas y no admiten
  algunas operaciones. Por ejemplo, WASI no permite enlaces simbólicos
  con nombres de archivo absolutos.

### Mobile platforms

Android and iOS are, in most respects, POSIX operating systems. File
I/O, socket handling, and threading all behave as they would on any
POSIX operating system. However, there are several major differences:

* Mobile platforms can only use Python in "embedded" mode. There is no
  Python REPL, and no ability to use separate executables such as
  **python** or **pip**. To add Python code to your mobile app, you
  must use the Python embedding API. For more details, see Using
  Python on Android and Using Python on iOS.

* Subprocesses:

  * On Android, creating subprocesses is possible but officially
    unsupported. In particular, Android does not support any part of
    the System V IPC API, so "multiprocessing" is not available.

  * An iOS app cannot use any form of subprocessing, multiprocessing,
    or inter-process communication. If an iOS app attempts to create a
    subprocess, the process creating the subprocess will either lock
    up, or crash. An iOS app has no visibility of other applications
    that are running, nor any ability to communicate with other
    running applications, outside of the iOS-specific APIs that exist
    for this purpose.

* Mobile apps have limited access to modify system resources (such as
  the system clock). These resources will often be *readable*, but
  attempts to modify those resources will usually fail.

* Console input and output:

  * On Android, the native "stdout" and "stderr" are not connected to
    anything, so Python installs its own streams which redirect
    messages to the system log. These can be seen under the tags
    "python.stdout" and "python.stderr" respectively.

  * iOS apps have a limited concept of console output. "stdout" and
    "stderr" *exist*, and content written to "stdout" and "stderr"
    will be visible in logs when running in Xcode, but this content
    *won't* be recorded in the system log. If a user who has installed
    your app provides their app logs as a diagnostic aid, they will
    not include any detail written to "stdout" or "stderr".

  * Mobile apps have no usable "stdin" at all. While apps can display
    an on-screen keyboard, this is a software feature, not something
    that is attached to "stdin".

    As a result, Python modules that involve console manipulation
    (such as "curses" and "readline") are not available on mobile
    platforms.
