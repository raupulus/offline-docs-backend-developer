---
title: '"email.message": Representing an email message'
source_url: https://docs.python.org/es/3
source_path: library/email.message.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2480
---

# "email.message": Representing an email message

**Código fuente:** Lib/email/message.py

======================================================================

Added in version 3.6: [1]

The central class in the "email" package is the "EmailMessage" class,
imported from the "email.message" module.  It is the base class for
the "email" object model.  "EmailMessage" provides the core
functionality for setting and querying header fields, for accessing
message bodies, and for creating or modifying structured messages.

Un mensaje de correo electrónico consiste en *headers* y un *payload*
(al que también nos referimos como *content*). *Headers* como **RFC
5322** o **RFC 6532** son nombres de campos de estilo y valores, donde
el nombre y valor están separados por un ':'. Los dos puntos no son
parte ni del nombre ni del valor. El *payload* puede ser un simple
mensaje, un objeto binario, o una secuencia estructurada de sub-
mensajes, cada uno con su propio conjunto de *headers* y su propio
*payload*. El último tipo de *payload* es indicado por el mensaje con
un MIME como *multipart/** o *message/rfc822* .

El modelo conceptual provisto por un objeto "EmailMessage" es el de un
diccionario ordenado de cabeceras emparejadas con una carga útil que
representa al cuerpo del mensaje **RFC 5322**, que podría ser una
lista de objetos sub-"EmailMessage". Además de los métodos normales de
diccionario para acceder a las cabeceras y valores, tiene métodos para
acceder a información especializada desde las cabeceras (por ejemplo,
el tipo de contenido MIME), para operar en la carga útil, generar una
versión serializada del mensaje, y recorrer recursivamente el árbol de
objetos.

The "EmailMessage" dictionary-like interface is indexed by the header
names, which must be ASCII values.  The values of the dictionary are
strings with some extra methods.  Headers are stored and returned in
case-preserving form, but field names are matched case-insensitively.
The keys are ordered, but unlike a real dict, there can be duplicates.
Additional methods are provided for working with headers that have
duplicate keys.

La carga útil es un objeto de cadena de caracteres o bytes, en el caso
de objetos de mensaje simples, o una lista de objetos "EmailMessage",
para documentos de contenedor MIME como *multipart/** y objetos de
mensaje *message/rfc822*.

class email.message.EmailMessage(policy=default)

   If *policy* is specified use the rules it specifies to update and
   serialize the representation of the message.  If *policy* is not
   set, use the "default" policy, which follows the rules of the email
   RFCs except for line endings (instead of the RFC mandated "\r\n",
   it uses the Python standard "\n" line endings).  For more
   information see the "policy" documentation. [2]

   as_string(unixfrom=False, maxheaderlen=None, policy=None)

      Retorna el mensaje entero como cadena de caracteres. Cuando la
      opción *unixform* es verdadera, la cabecera está incluida en la
      cadena de caracteres retornada. *unixform* está predeterminado
      con valor "False". Por compatibilidad con versiones anteriores,
      la clase base "Message" *maxheaderlen* es aceptada pero con
      valor "None" como predeterminado, por lo que la longitud de
      línea se controla mediante "max_line_length" de la política. El
      argumento *policy* puede ser usado para sobrescribir la política
      predeterminada obtenida de la instancia del mensaje. Esto puede
      ser usado para controlar parte del formato producido por el
      método, ya que la *policy* especificada pasará a "Generator".

      Aplanar el mensaje puede acarrear cambios en "EmailMessage" si
      es necesario rellenar los valores predeterminados para completar
      la transformación a una cadena de caracteres (por ejemplo, se
      pueden generar o modificar límites MIME).

      Tenga en cuenta que este método se proporciona como una
      comodidad y quizás no sea la forma más eficiente de serializar
      mensajes en su aplicación, especialmente si estás tratando con
      múltiples mensajes. Consulte "Generator" por una API más
      flexible para serializar mensajes. No olvide también que este
      método está restringido a producir mensajes serializados como "7
      bit clean" cuando "utf8" es "False", que es el valor
      predeterminado.

      Distinto en la versión 3.6: el comportamiento predeterminado
      cuando *maxheaderlen* no está especificado cambió de 0 al valor
      de *max_line_length* de la política .

   __str__()

      Equivalente a "as_string(policy=self.policy.clone(utf8=True))".
      Permite "str(msg)" para producir una cadena que contenga un
      mensaje serializado en un formato legible.

      Distinto en la versión 3.4: el método se cambió para usar
      "utf8=True", produciendo así un **RFC 6531** como representación
      del mensaje, en vez de ser un alias de "as_string()".

   as_bytes(unixfrom=False, policy=None)

      Retorna el mensaje plano como un objeto de bytes. Cuando
      *unixform* es verdadero, la cabecera es incluida en la cadena de
      caracteres retornada. El valor predeterminado de *unixform* es
      "False". El argumento *policy* puede ser usado para
      sobreescribir el valor predeterminado obtenido de la instancia
      del mensaje. Esto puede ser usado para controlar parte del
      formato producido por el método, ya que la política especificada
      pasará a "Generator".

      Aplanar el mensaje puede acarrear cambios en "EmailMessage" si
      es necesario rellenar los valores predeterminados para completar
      la transformación a una cadena de caracteres (por ejemplo, se
      pueden generar o modificar límites MIME).

      Tenga en cuenta que este método se proporciona como una
      comodidad y quizás no sea la forma más eficiente de serializar
      mensajes en su aplicación, especialmente si estas tratando con
      múltiples mensajes. Consulte "Generator" por una API más
      flexible para serializar mensajes.

   __bytes__()

      Equivalent to "as_bytes()".  Allows "bytes(msg)" to produce a
      bytes object containing the serialized message.

   is_multipart()

      Retorna "True" si la carga útil del mensaje es una lista de
      objetos de sub-"EmailMessage", de otra manera retorna "False".
      Cuando "is_multipart()" retorna "False", la carga útil deberá
      ser un objeto cadena de caracteres (que podría ser una carga
      útil binaria codificada con CTE). Note que si "is_multipart()"
      retorna "True" no necesariamente significa que
      "msg.get_content_maintype() == 'multipart'" retornará "True".
      Por ejemplo, "is_multipart" retornará "True" cuando la
      "EmailMessage" sea del tipo "message/rfc822".

   set_unixfrom(unixfrom)

      Configura la cabecera del mensaje a *unixform*, que debería ser
      una cadena de caracteres. (Consulte "mboxMessage" para una
      descripción de esta cabecera)

   get_unixfrom()

      Retorna la cabecera del mensaje. Predeterminado "None" si la
      cabecera no ha sido configurada.

   Los siguientes métodos implementan el mapeo como una interfaz para
   acceder a la cabecera del mensaje. Tenga en cuenta que hay algunas
   diferencias semánticas entre esos métodos y una interfaz de mapeo
   normal(es decir, diccionario). Por ejemplo, en un diccionario no
   hay claves duplicadas, pero pueden haber cabeceras duplicadas.
   Además, en los diccionarios no hay un orden garantizado para las
   claves retornadas por "keys()", pero en un objeto "EmailMessage",
   las cabeceras siempre regresan en orden de aparición en el mensaje
   original, o en el que fueron agregadas luego. Cualquier cabecera
   borrada y vuelta a añadir siempre se agrega al final de la lista.

   Estas diferencias semánticas son intencionales y están sesgadas
   hacia la conveniencia en los casos de uso más comunes.

   Note que en todos los casos, cualquier cabecera presente en el
   mensaje no se incluye en la interfaz de mapeo.

   __len__()

      Retorna el número total de cabeceras, incluidas las duplicadas.

   __contains__(name)

      Retorna "True" si el objeto del mensaje tiene un campo llamado
      'nombre'. La comparación se realiza sin tener en cuenta
      mayúsculas o minúsculas y 'nombre' no incluye ':'.  Se utiliza
      para el operador "in" Por ejemplo:

         if 'message-id' in myMessage:
            print('Message-ID:', myMessage['message-id'])

   __getitem__(name)

      Retorna el valor de la cabecera nombrada. *name* no incluye el
      separador de dos puntos, ':'. Si la cabecera se pierde, regresa
      "None", un "KeyError" no se genera nunca.

      Tenga en cuenta que si el campo nombrado aparece más de una vez
      en la cabecera del mensaje, esa cantidad de veces el valor
      regresado será indefinido. Use el método "get_all()" para
      obtener los valores de todas las cabeceras existentes llamadas
      *name*.

      Usando el *standard non-'compat32'*, el valor regresado es una
      instancia de una subclase de "email.headerregistry.BaseHeader".

   __setitem__(name, val)

      Agrega una cabecera al mensaje con un campo 'nombre' y un valor
      'val'. El campo se agrega al final de las cabeceras existentes
      en el mensaje.

      Tenga en cuenta que esto no sobrescribe ni borra ninguna
      cabecera con el mismo nombre. Si quiere asegurarse de que la
      nueva cabecera es la única en el mensaje con el campo 'nombre',
      borre el campo primero, por ejemplo:

         del msg['subject']
         msg['subject'] = 'Python roolz!'

      Si el "policy" define ciertas cabeceras para ser únicas (como lo
      hacen las políticas estándares), este método puede generar un
      "ValueError" cuando se intenta asignar un valor a esta cabecera
      si una ya existe. Este comportamiento es intencional por
      consistencia, pero no dependa de ello, ya que podemos optar por
      hacer que tales asignaciones eliminen la cabecera en el futuro.

   __delitem__(name)

      Elimine todas las apariciones del campo 'nombre' de las
      cabeceras del mensaje. No se genera ninguna excepción si el
      campo nombrado no está presente en las cabeceras.

   keys()

      Retorna una lista de los nombres de todos los campos de la
      cabecera del mensaje.

   values()

      Retorna una lista de todos los valores de los campos del
      mensaje.

   items()

      Retorna una lista de tuplas de dos elementos que contienen todos
      los campos cabeceras y valores del mensaje.

   get(name, failobj=None)

      Return the value of the named header field.  This is identical
      to "__getitem__()" except that optional *failobj* is returned if
      the named header is missing (*failobj* defaults to "None").

   Aquí hay algunos métodos adicionales útiles relacionados con la
   cabecera:

   get_all(name, failobj=None)

      Retorna una lista de todos los valores para el campo *nombre*.
      Si no se nombran tales cabeceras en el mensaje, regresa
      *failobj* (por defecto "None")

   add_header(_name, _value, **_params)

      Configuración extendida de cabeceras. Este método es similar a
      "__setitem__()", excepto que se pueden proporcionar parámetros
      de cabecera adicionales como argumentos de palabras clave.

      Por cada ítem en los parámetros del diccionario *_params*, la
      clave se toma como el nombre del parámetro, con barra baja ('_')
      convertidos a guiones ('-') (ya que en Python no se permiten '-'
      como identificadores). Normalmente, el parámetro debe ser
      añadido como "key='value'" a menos que el valor sea "None", en
      ese caso solo la clave debe ser añadida.

      Si el valor contiene caracteres no-ASCII, el *charset* y el
      lenguaje deben ser controlados especificando el valor como una
      triple tupla en formato "(CHARSET, LANGUAJE, VALUE)", donde
      "CHARSET" es una *string* llamando al *charset* usado para
      codificar el valor, "LANGUAJE" generalmente se establece en
      "None" o en una cadena de caracteres vacía (consulte **RFC
      2231** para más opciones), y "VALUE" es el valor de la cadena de
      caracteres que contiene puntos de código no-ASCII. Si la triple
      tupla no pasa y el valor contiene caracteres no-ASCII, es
      automáticamente codificada en formato **RFC 2231**, usando
      "CHARSET" de "utf-8" y "LANGUAJE" "None".

      Aquí hay un ejemplo:

         msg.add_header('Content-Disposition', 'attachment', filename='bud.gif')

      Esto agregará una cabecera que se ve como:

         Content-Disposition: attachment; filename="bud.gif"

      Un ejemplo de la interfaz extendida con caracteres no-ASCII:

         msg.add_header('Content-Disposition', 'attachment',
                        filename=('iso-8859-1', '', 'Fußballer.ppt'))

   replace_header(_name, _value)

      Reemplaza una cabecera. Reemplaza la primer cabecera encontrada
      en el mensaje que coincida con *_name*, conservando el orden de
      cabeceras y uso de minúsculas (y mayúsculas) del nombre de campo
      de la cabecera original. Si no hay coincidencia, se lanzará un
      "KeyError".

   get_content_type()

      Retorna el tipo de contenido del mensaje, pasado a minúsculas de
      la forma *maintype/subtype*. Si no hay cabecera llamada
      *Content-Type* en el mensaje, regresa el valor de
      "get_default_type()". Si *Content-Type* no es válido, retorna
      "text/plain".

      (De acuerdo con **RFC 2045**, los mensajes siempre tienen un
      tipo predeterminado, "get_content_type`siempre retornará un
      valor. :rfc:`2045`define el tipo predeterminado de un mensaje
      como :mimetype:`text/plain()" a menos que aparezca dentro de un
      contenedor *multipart/digest*, en cuyo caso sería
      *message/rfc822*. Si la cabecera *Content-Type* tiene una
      especificación de tipo que sea inválida, **RFC 2045** exige que
      el tipo predeterminado sea *text/plain*.)

   get_content_maintype()

      Retorna el tipo de contenido principal del mensaje. Esta es la
      parte  *maintype* de la cadena retornada por
      "get_content_type()".

   get_content_subtype()

      Retorna el tipo del sub-contenido del mensaje. Esta es la parte
      *subtype* de la cadena retornada por "get_content_type()".

   get_default_type()

      Retorna el tipo de contenido predeterminado. La mayoría de los
      mensajes tienen como tipo de contenido predeterminado a
      *text/plain*, a excepción de los mensajes que son sub-partes de
      contenedores *multipart/digest*. Estas sub-partes tienen como
      tipo de contenido predeterminado a *message/rfc822*.

   set_default_type(ctype)

      Establece el tipo de contenido predeterminado. *ctype* debería
      ser *text/plain* o *message/rfc822*, aunque esto no está
      impuesto. El tipo de contenido predeterminado no se almacena en
      la cabecera *Content-Type*, así que sólo afecta al valor de
      retorno de los métodos "get_content_type" cuando ninguna
      cabecera *Content-Type* está presente en el mensaje.

   set_param(param, value, header='Content-Type', requote=True, charset=None, language='', replace=False)

      Establece un parámetro en el encabezado *Content-Type*. Si el
      parámetro ya existe en el encabezado, reemplace su valor con
      *value*. Cuando *header* es "Content-Type" (el predeterminado) y
      el encabezado aún no existe en el mensaje, agréguelo, establece
      su valor en *text/plain* y agregue el nuevo valor del parámetro.
      *header* opcional especifica un encabezado alternativo a
      *Content-Type*.

      Si el valor contiene caracteres *non-ASCII*, el *charset* y el
      lenguaje pueden ser especificados explícitamente con los
      parámetros *charset* y *language*. Opcionalmente *language*
      especifica el lenguaje **RFC 2231**, por defecto una cadena
      vacía. Ambos *charset* y *language* deberán ser cadenas. los
      valores predeterminados son "utf8" para *charset* y "None" para
      *language*.

      Si *replace* es "False" (predeterminado) la cabecera se mueve al
      final de la lista de cabeceras. Si *replace* es "True", la
      cabecera se actualizará en su lugar.

      El uso del parámetro *requote* con objetos "EmailMessage" está
      obsoleto.

      Tenga en cuenta que se puede acceder a los parámetros existentes
      de las cabeceras a través del atributo "params" de la cabecera
      (por ejemplo, "msg['Content-Type'].params['charset']").

      Distinto en la versión 3.4: Se agregó la palabra clave
      "replace".

   del_param(param, header='content-type', requote=True)

      Elimina completamente el parámetro dado de la cabecera *Content-
      Type*. La cabecera será reescrita en su lugar, sin el parámetro
      o su valor. Opcionalmente *header* especifica una alternativa a
      *Content-Type*.

      El uso del parámetro *requote* con objetos "EmailMessage" está
      obsoleto.

   get_filename(failobj=None)

      Retorna el valor del parámetro "filename" de la cabecera
      *Content-Disposition* del mensaje. Si la cabecera no tiene un
      parámetro "filename", este método recae a buscar el parámetro
      "name" en la cabecera *Content-Type*. Si ninguno se encuentra o
      falta la cabecera, se retorna *failobj*. La cadena retornada
      siempre estará sin comillas según "email.utils.unquote()".

   get_boundary(failobj=None)

      Retorna el parámetro "boundary" de la cabecera *Content-Type*
      del mensaje, o *failobj* si la cabecera no se encuentra o si no
      tiene un parámetro "boundary". La cadena retornada siempre
      estará sin comillas según "email.utils.unquote()".

   set_boundary(boundary)

      Establece el parámetro "boundary" de la cabecera *Content-Type*
      como *boundary*.  "set_boundary()" siempre que sea necesario
      pondrá comillas a *boundary*. Si el objeto mensaje no tiene
      cabecera *Content-Type* se lanza "HeaderParseError".

      Note que usar este método es sutilmente diferente a borrar la
      cabecera *Content-Type* antigua y agregar una nueva con el nuevo
      límite utilizando "add_header()", porque "set_boundary()"
      preserva el orden de la cabecera *Content-Type* en la lista de
      cabeceras.

   get_content_charset(failobj=None)

      Retorna el parámetro "charset" de la cabecera *Content-
      Type`forzado a minúsculas. Si no hay una cabecera :mailheader
      :`Content-Type*, o si esa cabecera no tiene el parámetro
      "charset", se retorna *failobj*.

   get_charsets(failobj=None)

      Retorna una lista que contiene los nombres de los *charset* en
      el mensaje. Si el mensaje es *multipart*, la lista contendrá un
      elemento por cada subparte en la carga útil, de lo contrario
      será una lista de longitud 1.

      Cada elemento de la lista será una cadena que tendrá el valor
      del parámetro "charset" en la cabecera *Content-Type* para la
      subparte representada. Si la subparte no tiene cabecera
      *Content-Type*, no tiene parámetro "charset", o no es del tipo
      MIME principal *text*, entonces ese elemento en la lista
      retornada será *failobj*.

   is_attachment()

      Retorna "True" si hay una cabecera *Content-Disposition* y su
      valor (sensible a mayúsculas) es "attachment", de lo contrario
      retorna "False".

      Distinto en la versión 3.4.2: *is_attachment* ahora es un método
      en lugar de una propiedad, por consistencia con
      "is_multipart()".

   get_content_disposition()

      Retorna el valor en minúsculas (sin parámetros) de la cabecera
      *Content-Disposition* si el mensaje la tiene, de lo contrario
      retorna "None". Los valores posibles para este método son
      *inline*, *attachment* o "None" si el mensaje sigue **RFC
      2183**.

      Added in version 3.5.

   Los siguientes métodos se refieren a interrogar y manipular el
   contenido (*payload*) del mensaje.

   walk()

      El método "walk()" es un generador multipropósito que puede
      usarse para iterar sobre todas las partes y subpartes del árbol
      de un objeto mensaje, ordenando el recorrido en profundidad
      primero. Típicamente se usaría "walk()" como el iterador en un
      ciclo "for"; cada iteración retornará la siguiente subparte.

      Aquí hay un ejemplo que imprime el tipo MIME de cada parte de
      una estructura de mensaje de varias partes:

         >>> for part in msg.walk():
         ...     print(part.get_content_type())
         multipart/report
         text/plain
         message/delivery-status
         text/plain
         text/plain
         message/rfc822
         text/plain

      "walk" itera sobre las subpartes de cualquier parte donde
      "is_multipart()" retorna "True", aun si
      "msg.get_content_maintype() == 'multipart'" pueda retornar
      "False". Podemos ver esto en nuestro ejemplo al hacer uso de la
      función auxiliar de depuración "_structure":

         >>> from email.iterators import _structure
         >>> for part in msg.walk():
         ...     print(part.get_content_maintype() == 'multipart',
         ...           part.is_multipart())
         True True
         False False
         False True
         False False
         False False
         False True
         False False
         >>> _structure(msg)
         multipart/report
             text/plain
             message/delivery-status
                 text/plain
                 text/plain
             message/rfc822
                 text/plain

      Aquí las partes "message" no son "multiparts", pero sí contienen
      subpartes. "is_multipart()" retorna "True" y "walk" desciende a
      las subpartes.

   get_body(preferencelist=('related', 'html', 'plain'))

      Retorna la parte MIME que es la mejor candidata para ser el
      "cuerpo" del mensaje.

      *preferencelist* debe ser una secuencia de cadenas del conjunto
      "related", "html", y "plain", e Indica el orden de preferencia
      para el tipo de contenido de la parte retornada.

      Empieza a buscar coincidencias candidatas con el objeto en el
      que se llama al método "get_body"'.

      Si "related" no está incluido en la *preferencelist*, considere
      la parte raíz (o subparte de la parte raíz) de cualquier
      relacionado encontrado como candidato si la (sub-)parte coincide
      con una preferencia.

      Cuando se encuentra una "multipart/related", verifica el
      parámetro "start" y si se encuentra una parte con un *Content-
      ID* que coincida, considera solamente a ésta cuando se busca
      coincidencias candidatas. De otra forma considera sólo la
      primera parte (predeterminado *root*) de la "multipart/related".

      Si una parte tiene una cabecera *Content-Disposition* , sólo se
      considera a ésta parte como coincidencia candidata si el valor
      de la cabecera es "inline".

      Si ninguno de los candidatos coincide con ninguna de las
      preferencias en *preferencelist*, retorna "None".

      Notas: (1) Para la mayoría de las aplicaciones las únicas
      combinaciones de *preferencelist* que realmente tienen sentido
      son "('plain',)", "('html', 'plain')", y la predeterminada
      "('related', 'html', 'plain')". (2) Debido a que la coincidencia
      comienza con el objeto en el que se llama a "get_body", llamar a
      "get_body" en un "multipart/related" devolverá el objeto en sí a
      menos que la *preferencelist* tenga un valor no predeterminado.
      (3) Los mensajes (o partes de mensajes) que no especifican un
      *Content-Type* o cuya cabecera *Content-Type* sea inválida se
      tratarán como si fueran del tipo "text/plain", que
      ocasionalmente puede ocasionar que "get_body" retorne resultados
      inesperados.

   iter_attachments()

      Devuelve un iterador sobre todas las subpartes inmediatas del
      mensaje que no son partes candidatas del "body". Es decir,
      omitir la primer ocurrencia de cada "text/plain", "text/html",
      "multipart/related", o "multipart/alternative" (a menos que
      estén marcados explícitamente como adjuntos a través de
      *Content-Disposition: attachment*) y retornar todas las partes
      restantes. Cuando se aplica directamente a un
      "multipart/related", retorna un iterador sobre todas las partes
      relacionadas excepto la parte raíz (es decir, la parte apuntada
      por el parámetro "start", o la primera parte si no hay un
      parámetro "start" o el parámetro "start" no coincide con el
      *Content-ID* de ninguna de las partes). Cuando se aplica
      directamente a un "multipart/alternative" o a un no-"multipart",
      retorna un iterador vacío.

   iter_parts()

      Retorna un iterador sobre todas las partes inmediatas del
      mensaje, que estará vacío para una no-"multipart". (vea también
      "walk()".)

   get_content(*args, content_manager=None, **kw)

      Llama al método "get_content()" del *content_manager*, pasando
      *self* como el objeto del mensaje y pasando cualquier otro
      argumento o palabra clave como argumentos adicionales. Si no se
      especifica *content_manager* se usa el "content_manager"
      especificado por la "policy" actual.

   set_content(*args, content_manager=None, **kw)

      Llama al método "set_content()" del *content_manager*, pasando
      *self* como el objeto *message* y pasando cualquier otro
      argumento o palabra clave como argumentos adicionales. Si no se
      especifica *content_manager* se usa el "content_manager"
      especificado por la "policy" actual.

   make_related(boundary=None)

      Convierte un mensaje no-"multipart" a un mensaje
      "multipart/related", moviendo cualquier cabecera *Content-* y la
      carga útil a una (nueva) primera parte del "multipart". Si
      *boundary* se especifica, se utiliza como la cadena límite en el
      *multipart*, de otra forma deja que el límite se cree
      automáticamente cuando se necesite (por ejemplo, cuando se
      serializa el mensaje).

   make_alternative(boundary=None)

      Convierte un mensaje no-"multipart" o un mensaje
      "multipart/related" a uno "multipart/alternative" moviendo
      cualquier cabecera *Content-* y la carga útil existentes a una
      (nueva) primera parte del "multipart". Si *boundary* se
      especifica, se utiliza como la cadena límite en el *multipart*,
      de otra forma deja que el límite se cree automáticamente cuando
      se necesite (por ejemplo, cuando se serializa el mensaje).

   make_mixed(boundary=None)

      Convierte un mensaje no-"multipart", "multipart/related" o
      "multipart-alternative" a uno "multipart/mixed" moviendo
      cualquier cabecera *Content-* y la carga útil existentes a una
      (nueva) primera parte del "multipart". Si *boundary* se
      especifica, se utiliza como la cadena límite en el *multipart*,
      de otra forma deja que el límite se cree automáticamente cuando
      se necesite (por ejemplo, cuando se serializa el mensaje).

   add_related(*args, content_manager=None, **kw)

      Si el mensaje es un "multipart/related", crea un nuevo objeto
      mensaje, pasa todos los argumentos a su método "set_content()" y
      lo une al "multipart" con "attach()". Si el mensaje es un
      no-"multipart", llama a "make_related()" y procede como arriba.
      Si el mensaje es cualquier otro tipo de "multipart", lanza
      "TypeError". Si *content_manager* no es especificado, usa el
      "content_manager" especificado por la "policy" actual. Si la
      parte agregada no tiene un encabezado *Content-Disposition*, se
      agrega uno con el valor "inline".

   add_alternative(*args, content_manager=None, **kw)

      Si el mensaje es un "multipart/alternative", crea un nuevo
      objeto mensaje, pasa todos los argumentos a su método
      "set_content()" y lo une al "multipart" con "attach()". Si el
      mensaje es un no-"multipart" o "multipart/related", llama a
      "make_alternative()" y procede como arriba. Si el mensaje es
      cualquier otro tipo de "multipart", lanza "TypeError". Si
      *content_manager* no es especificado, usa el "content_manager"
      especificado por la "policy" actual.

   add_attachment(*args, content_manager=None, **kw)

      Si el mensaje es un "multipart/mixed", cree un nuevo objeto de
      mensaje, pase todos los argumentos a su método "set_content()" y
      "attach()" al "multipart". Si el mensaje no es "multipart",
      "multipart/related" o "multipart/alternative", llame
      "make_mixed()" y luego proceda como se indicó anteriormente. Si
      no se especifica *content_manager*, use el "content_manager"
      especificado por el actual "policy". Si la parte agregada no
      tiene encabezado *Content-Disposition*, agregue uno con el valor
      "attachment". Este método se puede utilizar tanto para adjuntos
      explícitos (*Content-Disposition: attachment*) como para
      adjuntos "inline" (*Content-Disposition: inline*), pasando las
      opciones apropiadas al "content_manager".

   clear()

      Elimina la carga útil y todas las cabeceras.

   clear_content()

      Elimina la carga útil y todos las cabeceras *!Content-*, dejando
      a las demás cabeceras intactas y en su orden original.

   Los objetos "EmailMessage" tienen los siguientes atributos de
   instancia:

   preamble

      El formato de un documento MIME permite algo de texto entre la
      linea en blanco después de las cabeceras y la primera cadena
      límite de multiparte. Normalmente, este texto nunca es visible
      en un lector de correo compatible con MIME porque queda fuera de
      la armadura MIME estándar. Sin embargo, al ver el texto sin
      formato del mensaje, o al ver el mensaje en un lector no
      compatible con MIME, este texto puede volverse visible.

      El atributo *preamble* contiene este texto extra para documentos
      MIME. Cuando el "Parser" descubre texto después de las cabeceras
      pero antes de la primer cadena límite, asigna este texto al
      atributo *preamble* del mensaje. Cuando el "Generator" escribe
      la representación de texto sin formato de un mensaje MIME y
      encuentra que el mensaje tiene un atributo *preamble* escribirá
      este texto en el área entre las cabeceras y el primer límite.
      Véase "email.parser" y "email.generator" para conocer detalles.

      Cabe señalar que si el objeto *message* no tiene preámbulo, el
      atributo *preamble* será igual a "None".

   epilogue

      El atributo *epilogue* actúa de igual forma al atributo
      *preamble* con la excepción de que contiene texto que aparece
      entre el último límite y el fin del mensaje. Como con el
      "preamble", si no hay texto de epílogo este atributo será
      "None".

   defects

      El atributo *defects* contiene una lista de todos los errores
      encontrados al hacer el análisis sintáctico del mensaje. Vea
      "email.errors" para una descripción detallada de los posibles
      efectos del análisis sintáctico.

class email.message.MIMEPart(policy=default)

   Esta clase representa una subparte de un mensaje MIME. Es idéntica
   a "EmailMessage", excepto que las cabeceras *MIME-Version* son
   añadidas cuando se llama a "set_content()", ya que las subpartes no
   necesitan su propia cabecera *MIME-Version*.

-[ Notas al pie ]-

[1] Añadido originalmente en la versión 3.4 como un *módulo
    provisional*. La documentación para la clase heredada *message* se
    movió a  email.message.Message: Representar un mensaje de correo
    electrónico usando la API compat32.

[2] The "EmailMessage" class requires a policy that provides a
    "content_manager" attribute for content management methods like
    "set_content()" and "get_content()" to work. The legacy "compat32"
    policy does not support these methods and should not be used with
    "EmailMessage".
