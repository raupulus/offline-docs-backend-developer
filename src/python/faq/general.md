---
title: Preguntas frecuentes generales sobre Python
source_url: https://docs.python.org/es/3
source_path: faq/general.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: faq
order: 1060
---

# Preguntas frecuentes generales sobre Python

## Información general

### ¿Qué es Python?

Python es un lenguaje interpretado, interactivo y orientado a objetos.
Incorpora módulos, excepciones, tipado dinámico, tipos de datos de muy
alto nivel y clases. Python combina un poder destacado con una
sintaxis muy clara. Tiene interfaces a muchas llamadas de sistema y
bibliotecas, así como a varios sistemas de ventana, y es extensible en
C o C++. También es usable como un lenguaje de extensión para
aplicaciones que necesitan una interfaz programable. Por último,
Python es portable: corre en muchas variantes de Unix, en Mac y en
Windows 2000 y posteriores.

Para saber más, comienza con El tutorial de Python. La Beginner's
Guide to Python vincula a otros recursos y tutoriales introductorios
para aprender Python.

### ¿Que es la *Python Software Foundation*?

La *Python Software Foundation* es una organización independiente sin
fines de lucro que posee los derechos sobre Python desde la versión
2.1 en adelante. La misión de la PSF es hacer avanzar la tecnología
*open source* relacionada al lenguaje de programación Python y
publicitar su uso. El sitio web de la PSF es
https://www.python.org/psf/.

Las donaciones a la PSF están exentas de impuestos en Estados Unidos.
Si usas Python y lo encuentras útil, por favor contribuye a través de
la página de donaciones de la PSF.

### ¿Hay restricciones de *copyright* sobre el uso de Python?

Puedes hacer cualquier cosa que quieras con el código fuente mientras
mantengas y muestres los mensajes de derechos de autor en cualquier
documentación sobre Python que produzcas. Si respetas las reglas de
derechos de autor, está permitido usar Python para fines comerciales,
vender copias de Python en forma de código fuente o binarios
(modificados o no), o vender productos que incorporen Python de alguna
manera. De cualquier manera nos gustaría saber de todos los usos
comerciales de Python, por supuesto.

See the license page to find further explanations and the full text of
the PSF License.

El logo de Python tiene derechos comerciales (*trademarked*) y en
ciertos casos se requiere un permiso de uso. Consulta la Trademark
Usage Policy para más información.

### ¿Por qué se creó Python en primer lugar?

Aquí hay un *muy* breve resumen sobre qué fue lo que comenzó todo,
escrita por Guido van Rossum:

   Tenía vasta experiencia implementando un lenguaje interpretado en
   el grupo ABC en CWI y trabajando con este grupo había aprendido
   mucho sobre diseño de lenguajes. Este es el origen de muchas
   características de Python, incluyendo el uso de sangría para el
   agrupamiento de sentencias y la inclusión de tipos de datos de muy
   alto nivel (aunque los detalles son todos diferentes en Python).

   Tenía algunos resquemores sobre el lenguaje ABC pero también me
   gustaban muchas de sus características. Era imposible extenderlo
   (al lenguaje o sus implementaciones) para remediar mis quejas -- de
   hecho, la ausencia de extensibilidad fue uno de los mayores
   problemas. Contaba con alguna experiencia usando Modula-2+ y
   conversé con los diseñadores de Modula-3 y leí su reporte. Modula-3
   es el origen de la sintaxis y semántica que usé para las
   excepciones y otras características de Python.

   Estaba trabajando en Grupo del sistema operativo distribuido Amoeba
   en CWI. Necesitábamos una mejor manera de hacer administración de
   sistemas que escribir programas en C o *scripts* de *Bourne shell*,
   ya que Amoeba tenía sus propia interfaz de llamadas a sistema que
   no era fácilmente accesible desde *Bourne shell*. Mi experiencia
   con el manejo de errores de Amoeba me hizo muy consciente de la
   importancia de las excepciones como una característica de los
   lenguaje de programación.

   Se me ocurrió que un lenguaje de scripts con una sintaxis como ABC
   pero con acceso a las llamadas al sistema Amoeba satisfaría la
   necesidad. Me di cuenta de que sería una tontería escribir un
   lenguaje específico para Amoeba, así que decidí que necesitaba un
   lenguaje que fuera generalmente extensible.

   Durante las vacaciones de Navidad de 1989 tenía mucho tiempo libre,
   así que decidí hacer un intento. Durante el año siguiente, mientras
   seguía trabajando principalmente en él durante mi propio tiempo,
   Python se utilizó en el proyecto Amoeba con un éxito creciente, y
   los comentarios de mis colegas me hicieron agregar muchas mejoras
   iniciales.

   En febrero de 1991, justo después de un año de desarrollo, decidí
   publicarlo en USENET. El resto está en el archivo "Misc/HISTORY".

### ¿Para qué es bueno Python?

Python es un lenguaje de programación de propósito general de alto
nivel que se puede aplicar a muchas clases diferentes de problemas.

El lenguaje viene con una gran biblioteca estándar que cubre áreas
como procesamiento de cadenas de caracteres (expresiones regulares,
Unicode, cálculo de diferencias entre archivos), protocolos de
Internet (HTTP, FTP, SMTP, XML-RPC, POP, IMAP), ingeniería de
software. (pruebas unitarias, registro, análisis de rendimiento
(*profiling*), análisis de código Python) e interfaces del sistema
operativo (llamadas al sistema, sistemas de archivos, sockets TCP /
IP). Mira la tabla de contenido de La biblioteca estándar de Python
para tener una idea de lo que está disponible. También hay disponible
una amplia variedad de extensiones de terceros. Consulta the Python
Package Index para encontrar paquetes de interés.

### ¿Cómo funciona el esquema numérico de versiones de Python?

Las versions de Python son numeradas "A.B.C" o "A.B":

* *A* es el número de version principal -- sólo es incrementada en
  cambios realmente importantes en el lenguaje.

* *B* es el número de versión menor -- se incrementa para cambios
  menos trascendentales.

* *C* es el número de versión micro -- se incrementa para cada versión
  de corrección de errores.

Not all releases are bugfix releases.  In the run-up to a new feature
release, a series of development releases are made, denoted as alpha,
beta, or release candidate.  Alphas are early releases in which
interfaces aren't yet finalized; it's not unexpected to see an
interface change between two alpha releases. Betas are more stable,
preserving existing interfaces but possibly adding new modules, and
release candidates are frozen, making no changes except as needed to
fix critical bugs.

Las versiones *alpha*, *beta* o *release candidate* tienen un sufijo
adicional:

* El sufijo para una versión alfa es "aN" para un pequeño número *N*.

* El sufijo para una versión beta es "bN" para un pequeño número *N*.

* El sufijo para una versión *release candidate * es "rcN" para un
  pequeño número *N*.

En otras palabras, todas las versiones con la etiqueta *2.0aN*
preceden a las versiones con la etiqueta *2.0bN*, que preceden a las
versiones con la etiqueta *2.0rcN*, y *esas* preceden a la 2.0.

También puedes encontrar números de versión con un sufijo "+", por
ejemplo "2.2+". Estas son versiones sin lanzar, construidas
directamente desde el repositorio de desarrollo de CPython. En la
práctica, luego de que un lanzamiento menor se realiza, la versión es
incrementada a la siguiente versión menor, que se vuelve "a0", por
ejemplo "2.4a0".

See the Developer's Guide for more information about the development
cycle, and **PEP 387** to learn more about Python's backward
compatibility policy.  See also the documentation for "sys.version",
"sys.hexversion", and "sys.version_info".

### ¿Cómo obtengo una copia del código fuente de Python?

El código fuente de la versión más reciente de Python está siempre
disponible desde python.org, en https://www.python.org/downloads/.  El
código fuente en desarrollo más reciente se puede obtener en
https://github.com/python/cpython/.

La distribución de fuentes es un archivo tar comprimido con gzip que
contiene el código C completo, documentación en formato Sphinx, los
módulos de la biblioteca de Python, programas de ejemplo y varias
piezas útiles de software libremente distribuibles. El código fuente
compilará y se ejecutará sin problemas en la mayoría de las
plataformas Unix.

Consulta Getting Started section of the Python Developer's Guide para
más información sobre cómo obtener el código fuente y compilarlo.

### ¿Cómo consigo documentación sobre Python?

The standard documentation for the current stable version of Python is
available at https://docs.python.org/3/.  EPUB, plain text, and
downloadable HTML versions are also available at
https://docs.python.org/3/download.html.

La documentación está escrita en reStructuredText y procesada con la
herramienta de documentación Sphinx. Las fuentes reStructuredText de
la documentación son parte de la distribución fuente de Python.

### Nunca he programado antes. ¿Hay un tutorial de Python?

Hay numerosos tutoriales y libros disponibles.  La documentación
estándar incluye  El tutorial de Python.

Consulta the Beginner's Guide para encontrar información para
principiantes en Python, incluyendo una lista de tutoriales.

### ¿Hay un *newsgroup* o una lista de correo dedicada a Python?

Hay un grupo de noticias, *comp.lang.python*, y una lista de correo,
python-list. Tanto el grupo de noticias como la lista de correo están
interconectadas entre sí -- si puedes leer las noticias no es
necesario que te suscribas a la lista de correo. *comp.lang.python*
tiene mucho tráfico, recibiendo cientos de publicaciones cada día. y
los lectores de Usenet suelen ser más capaces de hacer frente a este
volumen.

Announcements of new software releases and events can be found in
comp.lang.python.announce, a low-traffic moderated list that receives
about five postings per day.  It's available as the python-announce
mailing list.

Más información sobre listas de correo o grupos de noticias puede
hallarse en  https://www.python.org/community/lists/.

### ¿Cómo obtengo una versión de prueba *beta* de Python?

Las versiones alpha y beta están disponibles desde
https://www.python.org/downloads/.  Todos los lanzamientos son
anunciados en el grupo de noticias comp.lang.python y
comp.lang.python.announce, así como también en la página principal de
Python en https://www.python.org/; un *feed* RSS está disponible.

También puedes acceder a la versión en desarrollo de Python desde Git.
Mira The Python Developer's Guide para los detalles.

### ¿Cómo envío un reporte de *bug* y parches para Python?

Para reportar un *bug* o enviar un parche, usa el rastreador de
problemas en https://github.com/python/cpython/issues.

Para más información sobre cómo se desarrolla Python, consulta the
Python Developer's Guide.

### ¿Hay algún artículo publicado sobre Python que pueda referir?

Lo más probable es que lo mejor sea citar a tu libro preferido sobre
Python.

The very first article about Python was written in 1991 and is now
quite outdated.

   Guido van Rossum y Jelke de Boer, "*Interactively Testing Remote
   Servers Using the Python Programming Language", CWI Quarterly,
   Volume 4, Issue 4 (Diembre de 1991), Amsterdam, pp 283--303*.

### ¿Hay libros sobre Python?

Sí, hay muchos, y hay más siendo publicados. Mira la wiki de
python.org en https://wiki.python.org/moin/PythonBooks para ver una
lista.

También puedes buscar "Python" en las librerías en línea y excluir las
que refieran a los Monty Python; o quizás buscar "Python" y
"lenguaje".

### ¿En qué parte del mundo está ubicado www.python.org?

La infraestructura del proyecto Python está ubicada alrededor de todo
el mundo y es gestionada por el *Python Infraestructure Team*.
Detalles aquí.

### ¿Por qué se llama Python?

Cuando comenzó a implementar Python, Guido van Rossum también estaba
leyendo los guiones publicados de "Monty Python's Flying Circus", una
serie de comedia producida por la BBC de los 70'. Van Rossum pensó que
necesitaba un nombre que fuera corto, único y ligeramente misterioso,
entonces decidió llamar al lenguaje Python.

### ¿Debe gustarme "Monty Python's Flying Circus"?

No, pero ayuda. :)

## Python en el mundo real

### ¿Cuán estable es Python?

Very stable.  New, stable releases have been coming out roughly every
6 to 18 months since 1991, and this seems likely to continue.  As of
version 3.9, Python will have a new feature release every 12 months
(**PEP 602**).

The developers issue bugfix releases of older versions, so the
stability of existing releases gradually improves.  Bugfix releases,
indicated by a third component of the version number (e.g. 3.5.3,
3.6.2), are managed for stability; only fixes for known problems are
included in a bugfix release, and it's guaranteed that interfaces will
remain the same throughout a series of bugfix releases.

The latest stable releases can always be found on the Python download
page. Python 3.x is the recommended version and supported by most
widely used libraries. Python 2.x **is not maintained anymore**.

### ¿Cuánta gente usa Python?

Probablemente hay decenas de miles de usuarios y usuarias, aunque es
difícil obtener una cuenta exacta.

Python está disponible gratuitamente para ser descargado por lo que no
existen cifras de ventas, a su vez se incluye en muchos sitios
diferentes y está empaquetado en muchas distribuciones de Linux, por
lo que las estadísticas de descarga tampoco cuentan toda la historia.

El grupo de noticias comp.lang.python es muy activo, pero no todos los
usuarios de Python publican allí o incluso lo leen.

### ¿Hay proyectos significativos hechos con Python?

Mira https://www.python.org/about/success para una lista de proyecto
que usan Python. Consultar las actas de conferencias de Python pasadas
revelará contribuciones de diferentes empresas y organizaciones.

Proyectos en Python de alto perfil incluyen el gestor de listas de
correo Mailman y el servidor de aplicaciones Zope. Muchas
distribuciones de Linux, más notoriamente Red Hat, han escrito partes
de sus instaladores y software de administración en Python. Entre las
empresas que usan Python internamente se encuentran Google, Yahoo y
Lucasfilm Ltd.

### ¿Qué nuevos desarrollos se esperan para Python en el futuro?

Consulta https://peps.python.org/ para conocer las propuestas de
mejora de Python (PEP). Los PEP son documentos de diseño que describen
una nueva característica sugerida para Python, que proporciona una
especificación técnica concisa y una justificación. Busca un PEP
titulado "Python X.Y Release Schedule", donde X.Y es una versión que
aún no se ha lanzado públicamente.

New development is discussed on the python-dev mailing list.

### ¿Es razonable proponer cambios incompatibles a Python?

En general no. Ya existen millones de líneas de código Python
alrededor del mundo, por lo que cualquier cambio en el lenguaje que
invalide más que una fracción muy pequeña de los programas existentes
tiene que ser mal visto. Incluso si puedes proporcionar un programa de
conversión, todavía existe el problema de actualizar toda la
documentación; se han escrito muchos libros sobre Python y no queremos
invalidarlos a todos de un plumazo.

Si una funcionalidad se debe cambiar,  es necesario proporcionar una
ruta de actualización gradual.  **PEP 5** describe el procedimiento
seguido para introducir cambios incompatibles con versiones anteriores
para minimizar disrupciones a los usuarios y usuarias.

### ¿Python es un buen lenguaje para principiantes?

Sí.

Todavía es común hacer comenzar a estudiantes con lenguajes
procedimentales de tipado estático como Pascal, C o un subconjunto de
C++ o Java. Los y las estudiantes pueden verse favorecidos si aprenden
Python como primer lenguaje. Python tiene una sintaxis simple y
consistente y una gran biblioteca estándar. Y, más importante, usar
Python en cursos introductorios de programación permite a los
estudiantes concentrarse en lo importante de las habilidades de
programación como la descomposición de problemas y el diseño de tipos
de datos. Con Python los estudiantes pueden ser rápidamente
introducidos a conceptos como bucles y procedimientos. Incluso puede
trabajar con objetos definidos por el usuario en su primer curso.

Para estudiantes que nunca han programado antes, usar un lenguaje de
tipado estático parece antinatural. Presenta complejidades adicionales
que deben ser dominadas y ralentizan el ritmo del curso. Quienes están
aprendiendo intentan pensar como la computadora, descomponer
problemas, diseñar interfaces consistentes y encapsular datos. Si bien
aprender a usar un lenguaje de tipado estático es importante en el
largo plazo, no es necesariamente el mejor tema a tratar en un primer
curso de programación.

Muchos otros aspectos de Python lo vuelven un buen primer lenguaje.
Como Java, Python tiene una biblioteca estándar, de manera que los y
las estudiantes pueden recibir, de manera temprana, consignas para
realizar proyectos de programación que *hagan* algo. Estas consignas
no están restringidas a las típicas calculadoras de cuatro operaciones
o programas de balances contables. Al usar la biblioteca estándar,
pueden ganar la satisfacción de trabajar en aplicaciones realistas
mientras aprenden los fundamentos de la programación. Usar la
biblioteca estándar también enseña a reusar código. Módulos de
terceros, como PyGame, también ayudan a extender los alcances de los y
las estudiantes.

El intérprete interactivo de Python les permite probar funcionalidades
del lenguaje mientras programan. Pueden tener una ventana con el
intérprete corriendo mientras escriben el código de su programa en
otra. Si no recuerdan los métodos para una lista, pueden hacer algo
así:

   >>> L = []
   >>> dir(L)
   ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
   '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
   '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
   '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
   '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
   '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
   '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear',
   'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
   'reverse', 'sort']
   >>> [d for d in dir(L) if '__' not in d]
   ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

   >>> help(L.append)
   Help on built-in function append:

   append(...)
       L.append(object) -> None -- append object to end

   >>> L.append(1)
   >>> L
   [1]

Con el intérprete, la documentación nunca está lejos de los o las
estudiantes mientras están programando.

También hay buenos IDE para Python. IDLE es un IDE multiplataforma
para Python que está escrito en Python usando Tkinter. Los usuarios de
Emacs estarán felices de saber que hay un muy buen modo de Python para
Emacs. Todos estos entornos de programación proporcionan resaltado de
sintaxis, indentación automática y acceso al intérprete interactivo
durante la codificación. Consulta la wiki de Python para obtener una
lista completa de los entornos de edición de Python.

Si quieres discutir el uso de Python en la educación, quizás te
interese unirte a la la lista de correo edu-sig.
