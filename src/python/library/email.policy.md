---
title: '"email.policy": Policy Objects'
source_url: https://docs.python.org/es/3
source_path: library/email.policy.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2510
---

# "email.policy": Policy Objects

Added in version 3.3.

**Código fuente:** Lib/email/policy.py

======================================================================

El enfoque principal del paquete "email" es la gestión de mensajes de
correo electrónico como se describe por los varios RFC de correos
electrónicos y MIME. Sin embargo, el formato general de los mensajes
de correo electrónico (un bloque de campos de cabecera cada uno
consistiendo en un nombre seguido de dos puntos seguido de un valor,
el bloque entero seguido por una línea blanca y un 'cuerpo'
arbitrario), es un formato que ha encontrado utilidad fuera del campo
de correos electrónicos. Algunos de estos usos cumplen bastante cerca
los RFC de correos electrónicos principales, alguno no.  Incluso
cuando se trabajo con correos electrónicos, hay veces cuando es
deseable romper la estricta conformidad con los RFC, tal como generar
correos electrónicos que se integran con servidores de correos
electrónicos que no siguen los estándares, o que implementan
extensiones que quieres usar en formas que violan los estándares.

Los objetos *policy* dan al paquete de correos electrónicos la
flexibilidad de manejar todos estos casos de uso diversos.

Un objeto "Policy" encapsula un conjunto de atributos y métodos que
controlan el comportamiento de varios componentes del paquete de
correos electrónicos durante el uso. Las instancias "Policy" pueden
ser pasadas a varias clases y métodos en el paquete de correos
electrónicos para alterar el comportamiento por defecto.  Los valores
que se pueden configurar y sus valores por defecto se describen abajo.

Hay una *policy* por defecto usada por todas las clases en el paquete
de correos electrónicos.  Para todos las clases "Parser" y las
funciones de conveniencia relacionadas, y para la clase "Message",
esta es una *policy* "Compat32", a través de sus correspondientes
instancias "compat32" pre-definidas.  Esta política mantiene una
compatibilidad (en algunos casos, compatibilidad con los bugs) con el
paquete de correos electrónicos de las versiones anteriores de
Python3.3.

El valor por defecto para la palabra clave *policy* de "EmailMessage"
es la *policy* "EmailPolicy", a través de su instancia pre-definida
"default".

Cuando un objeto "Message" o "EmailMessage" es creado, adquiere un
*policy*.  Si el mensaje es creado por un "parser", un *policy* pasado
al analizador será el *policy* usado por el mensaje que cree.  Si el
mensaje es creado por el programa, entonces el *policy* puede ser
especificado cuando sea creado.  Cuando un mensaje es pasado a un
"generator", el generador usa el *policy* del mensaje por defecto,
pero también puedes pasar un *policy* específico al generador que
anulará el que está guardado en el objeto mensaje.

El valor por defecto del argumento por palabra clave *policy* para las
clases "email.parser" y las funciones de conveniencia del analizador
**se cambiarán** en una futura versión de Python.  Por consiguiente,
**siempre debes especificar explícitamente qué policy quieres usar**
cuando se llama a cualquiera de las clases y funciones descritas en el
módulo "parser".

La primera parte de esta documentación cubre las características de
"Policy", un *abstract base class* que define las características que
son comunes a todos los objetos *policy*, incluyendo "compat32".  Esto
incluye ciertos métodos gancho (*hook*) que son llamados internamente
por el paquete de correos electrónicos, que un *policy* personalizado
puede invalidar para obtener un comportamiento diferente. La segunda
parte describe las clases concretas "EmailPolicy" y "Compat32", que
implementan los ganchos (*hooks*) que proporcionan el comportamiento
estándar y el comportamiento y características compatibles hacia
atrás, respectivamente.

Las instancias "Policy" son inmutables, pero pueden ser clonadas,
aceptando los mismos argumentos de palabra clave que el constructor de
clase y retorna una nueva instancia "Policy" que es una copia del
original pero con los valores de atributos específicos cambiados.

Como un ejemplo, el siguiente código puede ser usado para leer un
mensaje de correo electrónico de un archivo en disco y pasarlo al
programa de sistema "sendmail" en un sistema Unix:

   >>> from email import message_from_binary_file
   >>> from email.generator import BytesGenerator
   >>> from email import policy
   >>> from subprocess import Popen, PIPE
   >>> with open('mymsg.txt', 'rb') as f:
   ...     msg = message_from_binary_file(f, policy=policy.default)
   ...
   >>> p = Popen(['sendmail', msg['To'].addresses[0]], stdin=PIPE)
   >>> g = BytesGenerator(p.stdin, policy=msg.policy.clone(linesep='\r\n'))
   >>> g.flatten(msg)
   >>> p.stdin.close()
   >>> rc = p.wait()

Aquí le estamos diciendo a "BytesGenerator" que use los caracteres de
separación de línea correctos de RFC cuando crea la cadena binaria
para alimentar a "stding" de "sendmail" ("sendmails's" "stdin"), donde
el *policy* por defecto usaría separadores de línea "\n".

Algunos métodos del paquete de correos electrónicos aceptan un
argumento de palabra clave *policy*, permitiendo que el *policy* pueda
ser anulado para ese método.  Por ejemplo, el siguiente código usa el
método "as_bytes()" del objeto *msg* del ejemplo anterior y escribe el
mensaje en un archivo usando los separadores de línea nativos para la
plataforma en el que esté corriendo:

   >>> import os
   >>> with open('converted.txt', 'wb') as f:
   ...     f.write(msg.as_bytes(policy=msg.policy.clone(linesep=os.linesep)))
   17

Los objetos *policy* puede ser combinados usando el operador de
adición, produciendo un objeto *policy* cuya configuración es una
combinación de los valores que de los objetos sumados:

   >>> compat_SMTP = policy.compat32.clone(linesep='\r\n')
   >>> compat_strict = policy.compat32.clone(raise_on_defect=True)
   >>> compat_strict_SMTP = compat_SMTP + compat_strict

Esta operación no es conmutativa; es decir, el orden en el que los
objetos son añadidos importa.  Para ilustrar:

   >>> policy100 = policy.compat32.clone(max_line_length=100)
   >>> policy80 = policy.compat32.clone(max_line_length=80)
   >>> apolicy = policy100 + policy80
   >>> apolicy.max_line_length
   80
   >>> apolicy = policy80 + policy100
   >>> apolicy.max_line_length
   100

class email.policy.Policy(**kw)

   Este es el *abstract base class* para todas las clases *policy*.
   Proporciona las implementaciones por defecto para un par de métodos
   triviales, también como la implementación de las propiedades de
   inmutabilidad, el método "clone()", y las semánticas del
   constructor.

   Se pueden pasar varios argumentos de palabra clave al constructor
   de una clase *policy*.  Los argumentos que pueden ser especificados
   son cualquier propiedad que no sea método en esta clase, además de
   cualquier otra propiedad adicional que no sea método en la clase
   concreta.  Un valor especificado en el constructor anulará el valor
   por defecto para los atributos correspondientes.

   Esta clase define las siguientes propiedades, y por consiguiente
   los valores a continuación pueden ser pasados al constructor de
   cualquier clase *policy*:

   max_line_length

      El tamaño máximo de cualquier línea en la salida serializada,
      sin contar el fin de la línea de carácter(res).  Por defecto es
      78, por el **RFC 5322**. Un valor de "0" o "None" indica que
      ningún envolvimiento de líneas puede ser hecha en lo más mínimo.

   linesep

      La cadena de caracteres a ser usada para terminar las líneas en
      una salida serializada.  El valor por defecto es "\n" porque esa
      es la disciplina del fin de línea interna usada por Python,
      aunque "\r\n" es requerida por los RFCs.

   cte_type

      Controla el tipo de Codificaciones de Transferencia de Contenido
      que pueden ser o son necesarios para ser usados.  Los valores
      posibles son:

      +----------+-----------------------------------------------------------------+
      | "7bit"   | todos los datos deben ser "compatibles con 7 bit (*7 bit        |
      |          | clean*)" (ASCII-only).  Esto significa que donde sea necesario, |
      |          | los datos serán codificados usando o codificación imprimible    |
      |          | entre comillas o base64.                                        |
      +----------+-----------------------------------------------------------------+
      | "8bit"   | los datos no son limitados a ser compatibles con 7 bits (*7 bit |
      |          | clean*).  Se requiere que los datos en las cabeceras todavía    |
      |          | sean sólo ASCII y por lo tanto estarán codificadas (véase       |
      |          | "fold_binary()" y "utf8" abajo por las excepciones), pero las   |
      |          | partes del cuerpo pueden usar "8bit" CTE.                       |
      +----------+-----------------------------------------------------------------+

      Un valor "cte_type" de "`8bit" sólo trabaja con
      "BytesGenerator", no "Generator", porque las cadenas no pueden
      contener datos binarios.  Si un "Generator" está operando bajo
      un *policy* que especifica "cte_type=8bit", actuará como si
      "cte_type" fuese "7bit".

   raise_on_defect

      Si es "True", cualquier defecto encontrado será lanzado como
      error.  Si es "False" (el valor por defecto), los defectos serán
      pasados al método "register_defect()".

   mangle_from_

      Si es "True", las líneas empezando con *"From "* en el cuerpo
      son saltados al poner un ">" en frente de ellos. Este parámetro
      es usado cuando el mensaje está siendo serializado por un
      generador. El valor por defecto es: "False".

      Added in version 3.5.

   message_factory

      Una función de fábrica para construir un nuevo objeto mensaje
      vacío.  Usado por el analizador cuando construye mensajes.  Por
      defecto es "None", en cuyo caso "Message" es usado.

      Added in version 3.6.

   verify_generated_headers

      If "True" (the default), the generator will raise
      "HeaderWriteError" instead of writing a header that is
      improperly folded or delimited, such that it would be parsed as
      multiple headers or joined with adjacent data. Such headers can
      be generated by custom header classes or bugs in the "email"
      module.

      As it's a security feature, this defaults to "True" even in the
      "Compat32" policy. For backwards compatible, but unsafe,
      behavior, it must be set to "False" explicitly.

      Added in version 3.13.

   El siguiente método de "Policy" está destinado a ser llamado por
   código usando la librería de correos electrónicos para crear
   instancias de *policy* con configuraciones personalizadas:

   clone(**kw)

      Retorna una nueva instancia de "Policy" cuyos atributos tienen
      los mismos valores que la instancia actual, excepto donde se le
      dan, a esos atributos, nuevos valores por los argumentos de
      palabra clave.

   Los métodos de "Policy" restantes son llamados por el código de
   paquete de correos electrónicos, y no están destinados a ser
   llamados por una aplicación usando el paquete de correos
   electrónicos. Un *policy* personalizado debe implementar todos
   estos métodos.

   handle_defect(obj, defect)

      Handle a *defect* found on *obj*.  When the email package calls
      this method, *defect* will always be a subclass of
      "MessageDefect".

      La implementación por defecto verifica la bandera
      "raise_on_defect".  Si es "True", *defect* es lanzado como una
      excepción. Si es "False" (el valor por defecto), *obj* y
      *defect* son pasados a "register_defect()".

   register_defect(obj, defect)

      Register a *defect* on *obj*.  In the email package, *defect*
      will always be a subclass of "MessageDefect".

      La implementación por defecto llama al método "append" del
      atributo "defects" de *obj*.  Cuando un paquete de correos
      electrónicos llama a "handle_defect", *obj* normalmente tendrá
      un atributo "defects" que tiene un método "append".  Los tipos
      de objetos personalizados usados con el paquete de correos
      electrónicos (por ejemplo, objetos "Message" personalizados)
      también deben proporcionar tal atributo, de otro modo, los
      defectos en los mensajes analizados levantarán errores no
      esperados.

   header_max_count(name)

      Retorna el máximo número permitido de cabeceras llamadas *name*.

      Llamado cuando una cabecera es añadida a un objeto
      "EmailMessage" o "Message".  Si el valor retornado no es "0" o
      "None", y ya hay un número de cabeceras con el nombre *name*
      mayor o igual que el valor retornado, un "ValueError" es
      lanzado.

      Porque el comportamiento por defecto de "Message.__setitem__" es
      agregar el valor a la lista de cabeceras, es fácil crear
      cabeceras duplicadas sin darse cuenta.  Este método permite que
      ciertas cabeceras sean limitadas en el número de instancias de
      esa cabecera que puede ser agregada a "Message"
      programáticamente.  (El límite no es observado por el
      analizador, que fielmente producirá tantas cabeceras como
      existen en el mensaje siendo analizado.)

      La implementación por defecto retorna "None" para todos los
      nombres de cabeceras.

   header_source_parse(sourcelines)

      El paquete de correos electrónicos llama a este método con una
      lista de cadenas de caracteres, cada terminación de cadena con
      los caracteres de separación de línea encontrada en la fuente
      siendo analizada.   La primera línea incluye el campo del nombre
      de cabecera y el separador.  Todos los espacios en blanco en la
      fuente son preservados.  El método debe retornar la tupla
      "(name,value)" que va a ser guardada en el "Message" para
      representar la cabecera analizada.

      Si una implementación desea mantener compatibilidad con los
      *policy* del paquete de correos electrónicos existentes, *name*
      debe ser el nombre con las letras preservadas (todos los
      caracteres hasta el separador '":"'), mientras que *value* debe
      ser el valor desdoblado (todos los caracteres de separación de
      líneas eliminados, pero los espacios en blanco intactos),
      privado de espacios en blanco al comienzo.

      *sourcelines* puede contener datos binarios *surrogateescaped*.

      No hay implementación por defecto

   header_store_parse(name, value)

      El paquete de correos electrónicos llama a este método con el
      nombre y valor proporcionados por el programa de aplicación
      cuando la aplicación está modificando un "Message"
      programáticamente (en lugar de un "Message" creado por un
      analizador). El método debe retornar la tupla "(name,value)" que
      va a ser almacenada en el "Message" para representar la
      cabecera.

      Si una implementación desea retener compatibilidad con los
      *policy* del paquete de correos electrónicos existentes, el
      *name* y *value* deben ser cadenas de caracteres o subclases de
      cadenas que no cambien el contenido de los pasados en los
      argumentos.

      No hay implementación por defecto

   header_fetch_parse(name, value)

      El paquete de correos electrónicos llama a este método con el
      *name* y *valor* actualmente guardados en "Message" (el mensaje)
      cuando la cabecera es solicitada por el programa de aplicación,
      y lo que sea que el método retorne es lo que es pasado de vuelta
      a la aplicación como el valor de la cabecera siendo recuperado.
      Note que puede haber más de una cabecera con el mismo nombre
      guardado en "Message"; el método es pasado al nombre específico
      y valor de la cabecera destinado a ser retornado a la
      aplicación.

      *value* puede contener datos binarios *surrogateescaped*.  No
      debe haber datos binarios *surrogateescaped* en el valor
      retornado por el método.

      No hay implementación por defecto

   fold(name, value)

      El paquete de correos electrónicos llama a este método con los
      *name* y *value* actualmente guardados en "Message" para una
      cabecera dada.  El método debe retornar una cadena de caracteres
      que represente esa cabecera "doblada" correctamente (de acuerdo
      a los ajustes del *policy*) al componer *name* con *value* e
      insertar caracteres "linesep" en los lugares apropiados.  Véase
      **RFC 5322** para una discusión de las reglas para doblar
      cabeceras de correos electrónicos.

      *value* puede contener datos binarios *surrogateescaped*.  No
      debe haber datos binarios *surrogateescaped* en la cadena de
      caracteres retornada por el método.

   fold_binary(name, value)

      Igual que "fold()", excepto que el valor retornado debe ser un
      objeto bytes en vez de una cadena de caracteres.

      *value* puede contener datos binarios *surrogateescaped*.  Estos
      pueden ser convertidos de vuelta a datos binarios en el objeto
      de bytes retornado.

class email.policy.EmailPolicy(**kw)

   Este "Policy" concreto proporciona el comportamiento que sirve para
   cumplir con los RFCs actuales para correos electrónicos.  Estos
   incluyen (pero no están limitados a) **RFC 5322**, **RFC 2047**, y
   los actuales RFCs MIME.

   Esta *policy* incorpora nuevos analizadores de cabeceras y
   algoritmos de doblado.  En vez de cadenas de caracteres simples,
   las cabeceras son subclases de "str" con atributos que dependen del
   tipo del campo.  El analizado y algoritmo de doblado implementan
   los **RFC 2047** y **RFC 5322** por completo.

   El valor por defecto para el atributo "message_factory" es
   "EmailMessage".

   Además de los atributos que se pueden configurar listados arriba
   que aplican a todas los *policies*, este *policy* añade los
   siguientes atributos adicionales:

   Added in version 3.6: [1]

   utf8

      Si es "False", se sigue el **RFC 5322**, siendo compatible con
      caracteres non-ASCII en las cabeceras al codificarlas como
      "palabras codificadas".  Si es "True", sigue el **RFC 6532** y
      usa el formato de codificación "utf-8" para las cabeceras. Los
      mensajes formateados de esta manera puede ser pasados a
      servidores SMTP que admitan la extensión "SMTPUTF8" (**RFC
      6531**).

   refold_source

      Si el valor para una cabecera en el objeto "Message" se originó
      de un "parser" (en lugar de ser establecido por el programa),
      este atributo indica tanto si un generador debe redoblar ese
      valor cuando se transforma al mensaje de vuelta a la forma
      serializada o no.  Los valores posibles son:

      +----------+-----------------------------------------------------------------+
      | "none"   | todos los valores de la fuente usan el doblamiento original     |
      +----------+-----------------------------------------------------------------+
      | "long"   | los valores de la fuente que tengan una línea que sea más       |
      |          | grande que "max_line_length" serán redoblados                   |
      +----------+-----------------------------------------------------------------+
      | "all"    | todos los valores son redoblados.                               |
      +----------+-----------------------------------------------------------------+

      El valor por defecto es "long".

   header_factory

      Un invocable que toma dos argumentos, "name" y "value", donde
      "name" es un nombre de campo de cabecera y "value" es un valor
      del campo de la cabecera no doblado, y retorna una subclase de
      cadenas de caracteres que representan la cabecera.  Un valor por
      defecto "header_factory" (véase "headerregistry") es
      proporcionado que admite el análisis personalizado para los
      varios tipos de cabecera **RFC 5322** de direcciones y fechas, y
      los tipos del cabeceras MIME principales.  La compatibilidad de
      analizadores personalizados adicionales será agregada en el
      futuro.

   content_manager

      Un objeto con al menos dos métodos: get_content and set_content.
      Cuando los métodos "get_content()" o "set_content()" del objeto
      "messageEmailMessage" son llamados, llama al método
      correspondiente de este objeto, pasándole el mensaje objeto como
      su primer argumento, y cualquier argumento o palabra clave que
      fuese pasado como un argumento adicional.  Por defecto
      "content_manager" se pone a "raw_data_manager".

      Added in version 3.4.

   La clase proporciona las siguientes implementaciones concretas de
   los métodos abstractos de "Policy":

   header_max_count(name)

      Retorna el valor del atributo "max_count" de la clase
      especializada usada para representar la cabecera con el nombre
      dado.

   header_source_parse(sourcelines)

      El nombre es analizado como todo hasta el '":"' y retornado
      inalterado.  El valor es determinado al remover los espacios en
      blanco al principio del resto de la primera línea, juntando
      todas las subsecuentes líneas, y removiendo cualquier carácter
      CR o LF.

   header_store_parse(name, value)

      El nombre es retornado inalterado.  Si el valor de la entrada
      tiene un atributo "name" y coincide con *name* ignorando
      mayúsculas y minúsculas, el valor es retornado inalterado.  Si
      no, el *name* y *value* son pasados a "header_factory" , y el
      objeto cabecera resultante es retornado como el valor.  En este
      caso un "ValueError" es lanzado si el valor de la entrada
      contiene caracteres CR o LF.

   header_fetch_parse(name, value)

      Si el valor tiene un atributo "name", es retornado inalterado.
      De otra manera el *name*, y el *value* con cualquier carácter CR
      o LF eliminado, son pasados a la "header_factory", y el objeto
      cabecera resultante es retornado.  Cualquier byte
      *surrogateescaped* es convertido al glifo de carácter
      desconocido de unicode.

   fold(name, value)

      El doblamiento de la cabecera es controlado por la configuración
      de *policy* "refold_source". Se considera que un valor es
      *source value* (valor fuente) si y sólo si no tiene un atributo
      "name" (tener un atributo "name" significa que es un objeto
      cabecera de algún tipo). Si un valor fuente necesita ser
      redoblado de acuerdo a la política, es convertido en un objeto
      cabecera al pasarle el *name* y *value* con cualquier carácter
      CR y LF eliminado al "header_factory".  El doblamiento de un
      objeto cabecera es hecho al llamar a su método "fold" con el
      *policy* actual.

      Los valores fuente son separadas en líneas usando el método
      "splitlines()". Si el valor no va a ser redoblado, las líneas
      son unidas de nuevo usando el "linesep" del *policy* y
      retornadas.  La excepción son las líneas que contienen datos
      binarios non-ascii.  En ese caso el valor es redoblado a pesar
      de la configuración de "refold_source", que causa que los datos
      binarios sean codificados CTE usando el juego de caracteres
      (charset) "unknown-8bit".

   fold_binary(name, value)

      Igual que "fold()" si "cte_type" fuese "7bit", excepto que el
      valor retornado son bytes.

      Si "cte_type" es "8bit", los datos binarios non-ASCII son
      convertidos de vuelta a bytes.  Las cabeceras con datos binarios
      son redoblados, sin considerar la configuración de
      "refold_header", ya que no hay forma de saber si los datos
      binarios consisten en caracteres de un sólo byte o caracteres
      con múltiples bytes.

Las siguientes instancias de "EmailPolicy" proporcionan valores por
defecto apropiados para dominios de aplicaciones específicas.  Note
que en el futuro el comportamiento de estas instancias (en particular
la instancia "HTTP") puede ser ajustado para cumplir incluso más de
cerca a los RFC relevantes a sus dominios.

email.policy.default

   Una instancia de "EmailPolicy" con todos los valores por defecto
   sin cambiar.  Este *policy* usa la terminación de línea "\n"
   estándar de Python en vez de correcto por el RFC "\r\n".

email.policy.SMTP

   Apropiado para la serialización de mensajes en cumplimiento con los
   RFC de correos electrónicos.  Como "default", pero con "linesep"
   puesto en "\r\n", que es conforme con el RFC.

email.policy.SMTPUTF8

   Igual que "SMTP" excepto que "utf8" es "True". Útil para serializar
   mensajes a un almacén de mensajes sin usar palabras codificadas en
   las cabeceras.  Sólo debe ser utilizada para transmisiones por SMTP
   si las direcciones del remitente o recipiente tienen caracteres
   non-ASCII (el método "smtplib.SMTP.send_message()" gestiona esto
   automáticamente).

email.policy.HTTP

   Apropiado para serializar cabeceras con uso en tráfico de HTTP.
   Como "SMTP" excepto que "max_line_length" es puesto en "None"
   (ilimitado).

email.policy.strict

   Instancias de conveniencia. Igual que "default" excepto que
   "raise_of_defect" es puesto en "True".  Esto permite que cualquier
   *policy* sea hecho estricto al escribir:

      somepolicy + policy.strict

Con todos estos "EmailPolicies", el API efectivo del paquete de
correos electrónicos es cambiado del API de Python 3.2 en las
siguientes maneras:

* Estableciendo una cabecera en una "Message" resulta en que la
  cabecera sea analizada y un objeto cabecera sea creado.

* Buscar una valor de cabecera de un "Message" resulta en que la
  cabecera sea analizada y un objeto cabecera sea creado y retornado.

* Cualquier objeto cabecera, o cualquier cabecera que sea redoblada
  debido a las configuraciones del *policy*, es doblado usando un
  algoritmo que implementa el algoritmo de doblado del RFC por
  completo, incluyendo saber dónde las palabras codificadas son
  requeridas y permitidas.

Desde la vista de la aplicación, significa que cualquier cabecera
obtenida a través de "EmailMessage" es un objeto cabecera con
atributos extra, cuyo valor de cadena es el valor Unicode de la
cabecera completamente decodificada. Asimismo, se le puede asignar un
nuevo valor a una cabecera, o a una nueva cabecera creada, usando una
cadena de caracteres Unicode, y el *policy* se ocupará de convertir la
cadena Unicode en la forma decodificada correcta según el RFC.

Los objetos cabecera y sus atributos son descritos en
"headerrregistry".

class email.policy.Compat32(**kw)

   This concrete "Policy" is the backward compatibility policy.  It
   replicates the behavior of the email package in Python 3.2.  The
   "policy" module also defines an instance of this class, "compat32",
   that is used as the default policy.  Thus the default behavior of
   the email package is to maintain compatibility with Python 3.2.

   Los siguientes atributos tienen valores que son diferentes del
   "Policy" por defecto:

   mangle_from_

      El valor por defecto es "True".

   La clase proporciona las siguientes implementaciones concretas de
   los métodos abstractos de "Policy":

   header_source_parse(sourcelines)

      El nombre es analizado como todo hasta el '":"' y retornado
      inalterado.  El valor es determinado al remover los espacios en
      blanco al principio del resto de la primera línea, juntando
      todas las subsecuentes líneas, y removiendo cualquier carácter
      CR o LF.

   header_store_parse(name, value)

      El nombre y valor son retornados inalterados.

   header_fetch_parse(name, value)

      Si el valor contiene datos binarios, es convertido a un objeto
      "Header" usando el juego de caracteres (*charset*) "unknown-
      8bit". De otro modo, es retornado sin modificar.

   fold(name, value)

      Las cabeceras son dobladas usando el algoritmo de doblado de
      "Header", lo que preserva los saltos de líneas existentes en el
      valor, y envuelve cada línea resultante hasta el
      "max_line_length". Los datos binarios Non-ASCII son codificados
      por *CTE* usando el juego de caracteres (*charset*) "unknown-
      8bit".

   fold_binary(name, value)

      Las cabeceras son dobladas usando el algoritmo de doblado
      "Header", lo que preserva los saltos de línea existentes en el
      valor, y envuelve cada línea resultante hasta "max_line_length".
      Si "cte_type" es "7bit", los datos binarios non-ascii son
      codificados por *CTE* usando el juego de caracteres "unknown-
      8bit".  De otro modo, la cabecera fuente original es usada, con
      sus saltos de línea existentes y cualquier (inválido según el
      RFC) dato binario que puede contener.

email.policy.compat32

   Una instancia de "Compat32", proporcionando compatibilidad hacia
   atrás con el comportamiento del paquete de correos electrónicos en
   Python 3.2.

   Nota:

     The "compat32" policy should not be used as a policy for
     "EmailMessage" objects, and should only be used to serialize
     messages that were created using the "compat32" policy.

-[ Notas al pie de página ]-

[1] Se añadió originalmente en 3.3 como un *característica
    provisional*.
