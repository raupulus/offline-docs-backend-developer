---
title: '"email.message.Message": Representar un mensaje de correo electrónico usando
  la API "compat32"'
source_url: https://docs.python.org/es/3
source_path: library/email.compat32-message.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2390
---

# "email.message.Message": Representar un mensaje de correo electrónico usando la API "compat32"

La clase "Message" es muy similar a la clase "EmailMessage", sin los
métodos añadidos por esa clase y con el comportamiento predeterminado
de algunos otros métodos siendo ligeramente diferente. También
documentamos aquí algunos métodos que, aun siendo soportados por
"EmailMessage", no están recomendados a no ser que estés lidiando con
código heredado.

Por lo demás, la filosofía y estructura de las dos clases es la misma.

Este documento describe el comportamiento bajo la política por defecto
(para "Message") "Compat32". Si vas a usar otra política, deberías
estar usando la clase "EmailMessage" en su lugar.

Un mensaje de correo electrónico consta de *headers* y *payload*. Los
encabezados deben ser nombres y valores de estilo **RFC 5322**, donde
el nombre del campo y el valor están separados por dos puntos. Los dos
puntos no forman parte del nombre del campo ni del valor del campo. La
carga útil puede ser un mensaje de texto simple, un objeto binario o
una secuencia estructurada de submensajes, cada uno con su propio
conjunto de encabezados y su propia carga útil. El último tipo de
carga útil se indica mediante el mensaje que tiene un tipo MIME como
*multipart/** o *message/rfc822*.

El modelo conceptual proporcionado por un objeto "Message" es el de un
diccionario ordenado de encabezados con métodos adicionales para
acceder a información especializada de los encabezados, para acceder a
la carga, para generar una versión serializada del mensaje y para
recorrer recursivamente el árbol del objeto. Ten en cuenta que son
soportados encabezados duplicados pero deben ser usados métodos
especiales para acceder a ellos.

El pseudodiccionario "Message" es indexado por los nombres de
encabezados, los cuales deben ser valores ASCII. Los valores del
diccionario son cadenas que se supone que contienen sólo caracteres
ASCII; hay algún manejo especial para la entrada no ASCII, pero esta
no siempre produce los resultados correctos. Los encabezados son
almacenados y retornados preservando mayúsculas y minúsculas, pero los
nombres de campos son emparejados sin distinción entre mayúsculas y
minúsculas. También puede haber sólo un encabezado de envoltura,
también conocido como el encabezado *Unix-From* o el encabezado
"From_". La carga (*payload*) es una cadena o bytes, en el caso de
objetos de mensajes simples, o una lista de objetos "Message", para
contenedores de documentos MIME (ej. *multipart/** y
*message/rfc822*).

Aquí están los métodos de la clase "Message":

class email.message.Message(policy=compat32)

   Si se especifica *policy* (debe ser una instancia de una clase
   "policy") utiliza las reglas que especifica para actualizar y
   serializar la representación del mensaje. Si no se define *policy*,
   utiliza la política "compat32", la cual mantiene compatibilidad con
   la versión de Python 3.2 del paquete email. Para más información
   consulta la documentación de "policy".

   Distinto en la versión 3.3: El argumento de palabra clave *policy*
   fue añadido.

   as_string(unixfrom=False, maxheaderlen=0, policy=None)

      Retorna el mensaje completo aplanado como una cadena. Cuando el
      parámetro opcional *unixfrom* es verdadero, el encabezado de
      envoltura se incluye en la cadena retornada. *unixfrom* es por
      defecto "False". Por razones de compatibilidad con versiones
      anteriores, *maxheaderlen* es "0" por defecto, por lo que si
      quieres un valor diferente debes debes sobreescribirlo
      explícitamente (el valor especificado por *max_line_length* en
      la política será ignorado por este método). El argumento
      *policy* puede ser usado para sobrescribir la política por
      defecto obtenida de la instancia del mensaje. Esto puede ser
      usado para controlar algo del formato producido por el método,
      ya que la *policy* especificada puede ser pasada al "Generator".

      Aplanar el mensaje puede desencadenar cambios en "Message" si
      por defecto necesita ser rellenado para completar la
      transformación a una cadena (por ejemplo, límites MIME pueden
      ser generados o modificados).

      Ten en cuenta que este método es proporcionado como conveniencia
      y puede no siempre formatear el mensaje de la forma que quieres.
      Por ejemplo, de forma predeterminada no realiza la manipulación
      de líneas que comienzan con "From" que es requerida por el
      formato mbox de Unix. Para mayor flexibilidad, instancia un
      "Generator" y utiliza su método "flatten()" directamente. Por
      ejemplo:

         from io import StringIO
         from email.generator import Generator
         fp = StringIO()
         g = Generator(fp, mangle_from_=True, maxheaderlen=60)
         g.flatten(msg)
         text = fp.getvalue()

      Si el objeto de mensaje contiene datos binarios que no están
      codificados de acuerdo a los estándares RFC, los datos no
      compatibles serán reemplazados por puntos de código Unicode de
      "carácter desconocido". (Consulta también "as_bytes()" y
      "BytesGenerator".)

      Distinto en la versión 3.4: el argumento de palabra clave
      *policy* fue añadido.

   __str__()

      Equivalent to "as_string()".  Allows "str(msg)" to produce a
      string containing the formatted message.

   as_bytes(unixfrom=False, policy=None)

      Retorna el mensaje completo aplanado como un objeto de bytes.
      Cuando el argumento opcional *unixfrom* es verdadero, el
      encabezado de envoltura se incluye en la cadena retornada.
      *unixfrom* es por defecto "False". El argumento *policy* puede
      ser usado para sobrescribir la política por defecto obtenida
      desde la instancia del mensaje. Esto puede ser usado para
      controlar algo del formato producido por el método, ya que el
      *policy* especificado será pasado al "BytesGenerator".

      Aplanar el mensaje puede desencadenar cambios en "Message" si
      por defecto necesita ser rellenado para completar la
      transformación a una cadena (por ejemplo, límites MIME pueden
      ser generados o modificados).

      Ten en cuenta que este método es proporcionado como conveniencia
      y puede no siempre formatear el mensaje de la forma que quieres.
      Por ejemplo, de forma predeterminada no realiza la manipulación
      de líneas que comienzan con "From" que es requerida por el
      formato mbox de Unix. Para mayor flexibilidad, instancia un
      "BytesGenerator" y utiliza su método "flatten()" directamente.
      Por ejemplo:

         from io import BytesIO
         from email.generator import BytesGenerator
         fp = BytesIO()
         g = BytesGenerator(fp, mangle_from_=True, maxheaderlen=60)
         g.flatten(msg)
         text = fp.getvalue()

      Added in version 3.4.

   __bytes__()

      Equivalent to "as_bytes()".  Allows "bytes(msg)" to produce a
      bytes object containing the formatted message.

      Added in version 3.4.

   is_multipart()

      Retorna "True" si la carga del mensaje es una lista de objetos
      heredados de "Message", si no retorna "False". Cuando
      "is_multipart()" retorna "False", la carga debe ser un objeto de
      cadena (el cual puede ser una carga CTE codificada en binario).
      (Ten en cuenta que "is_multipart()" retornando "True" no
      significa necesariamente que "msg.get_content_maintype() ==
      'multipart'" retornará "True". Por ejemplo, "is_multipart"
      retornará "True" cuando el "Message" es de tipo
      "message/rfc822".)

   set_unixfrom(unixfrom)

      Establece el mensaje del encabezado de envoltura a *unixfrom*,
      el cual debe ser una cadena.

   get_unixfrom()

      Retorna el mensaje del encabezado de envoltura. Por defecto a
      "None" si el encabezado de envoltura nunca fue definido.

   attach(payload)

      Añade el *payload* dado a la carga actual, la cual debe ser
      "None" o una lista de objetos "Message" antes de la invocación.
      Después de la invocación, la carga siempre será una lista de
      objetos "Message". Si quieres definir la carga a un objeto
      escalar (ej. una cadena), usa "set_payload()" en su lugar.

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by "set_content()" and the related
      "make" and "add" methods.

   get_payload(i=None, decode=False)

      Retorna la carga (*payload*) actual, la cual será una lista de
      objetos "Message" cuando "is_multipart()" es "True", o una
      cadena cuando "is_multipart()" es "False". Si la carga es una
      lista y mutas el objeto de lista, modificarás la carga del
      mensaje.

      Con el argumento opcional *i*, "get_payload()" retornará el
      elemento número *i* de la carga (*payload*), contando desde
      cero, si "is_multipart()" es "True". Un "IndexError" será
      generado si *i* es menor que 0 ó mayor o igual que el número de
      elementos en la carga. Si la carga es una cadena (ej.
      "is_multipart()" es "False") y se define *i*, se genera un
      "TypeError".

      El argumento opcional *decode* es un indicador que determina si
      una carga debería ser decodificada o no, de acuerdo al
      encabezado *Content-Transfer-Encoding*. Cuando es "True" y el
      mensaje no es multiparte, la carga será decodificada si el valor
      de su encabezado es "quoted-printable" o "base64". Si se usa
      alguna otra codificación o falta el encabezado *Content-
      Transfer-Encoding*, la carga es retornada tal cual (sin
      decodificar). En todos los casos el valor retornado son datos
      binarios. Si el mensaje es multiparte y el indicador *decode* es
      "True", entonces se retorna "None". Si la carga es base64 y no
      fue perfectamente formada (falta relleno, tiene caracteres fuera
      del alfabeto base64), entonces un defecto apropiado será añadido
      a la propiedad defect del mensaje ("InvalidBase64PaddingDefect"
      o "InvalidBase64CharactersDefect", respectivamente).

      Cuando *decode* es "False" (por defecto) el cuerpo es retornado
      como una cadena sin decodificar el *Content-Transfer-Encoding*.
      Sin embargo, para un *Content-Transfer-Encoding* de 8bit, se
      realiza un intento para decodificar los bytes originales usando
      el "charset" especificado por el encabezado *Content-Type*,
      usando el manejador de error "replace". Si ningún "charset" es
      especificado o si el "charset" dado no es reconocido por el
      paquete email, el cuerpo es decodificado usando el conjunto de
      caracteres ASCII por defecto.

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by "get_content()" and "iter_parts()".

   set_payload(payload, charset=None)

      Define la carga completa del objeto mensaje a *payload*. Es
      responsabilidad del cliente asegurar invariantes de carga. El
      argumento opcional *charset* define el conjunto de caracteres
      por defecto del mensaje; consulta "set_charset()" para más
      detalles.

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by "set_content()".

   set_charset(charset)

      Define el junto de caracteres de la carga a *charset*, el cual
      puede ser tanto una instancia "Charset" (ver "email.charset"),
      una cadena denominando un conjunto de caracteres, o "None". Si
      es una cadena, será convertida a una instancia "Charset". Si
      *charset* es "None", el parámetro "charset" será eliminado del
      encabezado *Content-Type* (el mensaje no será modificado de otra
      manera). Cualquier otro valor lanzará un "TypeError".

      Si no hay un encabezado existente *MIME-Version*, será añadido
      uno. Si no hay un encabezado existente *Content-Type*, será
      añadido uno con valor *text/plain*. Tanto como si el encabezado
      *Content-Type* existe actualmente como si no, su parámetro
      "charset" será establecido a *charset.output_charset*. Si
      *charset.input_charset* y *charset.output_charset* difieren, la
      carga será recodificada al *output_charset*. Si no hay un
      encabezado existente *Content-Transfer-Encoding*, entonces la
      carga será codificada por transferencia, si es necesario, usando
      el "Charset" especificado y un encabezado con el valor apropiado
      será añadido. Si ya existe un encabezado *Content-Transfer-
      Encoding*, la carga se asume que ya está correctamente
      codificada usando ese *Content-Transfer-Encoding* y no es
      modificada.

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by the *charset* parameter of the
      "email.message.EmailMessage.set_content()" method.

   get_charset()

      Retorna la instancia "Charset" asociada con la carga del
      mensaje.

      This is a legacy method.  On the "EmailMessage" class it always
      returns "None".

   Los siguientes métodos implementan una interfaz parecida a un mapeo
   para acceder a los encabezados **RFC 2822** del mensaje. Ten en
   cuenta que hay algunas diferencias semánticas entre esos métodos y
   una interfaz de mapeo normal (ej. diccionario). Por ejemplo, en un
   diccionario no hay claves duplicadas, pero aquí pueden haber
   encabezados de mensaje duplicados. También, en diccionarios no hay
   un orden garantizado de las claves retornadas por "keys()", pero en
   un objeto "Message", los encabezados siempre son retornados en el
   orden que aparecieron en el mensaje original, o en el que fueron
   añadidos al mensaje más tarde. Cualquier encabezado eliminado y
   vuelto a adicionar siempre es añadido al final de la lista de
   encabezados.

   Esas diferencias semánticas son intencionales y están sesgadas
   hacia la máxima comodidad.

   Ten en cuenta que en todos los casos, cualquier encabezado de
   envoltura presente en el mensaje no está incluido en la interfaz de
   mapeo.

   En un modelo generado desde bytes, cualesquiera valores de
   encabezado que (en contravención de los RFCs) contienen bytes no
   ASCII serán representados, cuando sean obtenidos mediante esta
   interfaz, como objetos "Header" con un conjunto de caracteres
   "unknown-8bit".

   __len__()

      Retorna el número total de encabezados, incluyendo duplicados.

   __contains__(name)

      Retorna "True" si el objeto mensaje tiene un campo llamado
      *name*. La concordancia se realiza sin distinguir mayúsculas de
      minúsculas y *name* no debería incluir el caracter de doble
      punto final. Usado para el operador "in", ej:

         if 'message-id' in myMessage:
            print('Message-ID:', myMessage['message-id'])

   __getitem__(name)

      Retorna el valor del campo del encabezado nombrado. *name* no
      debe incluir el separador de campo de doble punto. Si falta un
      encabezado, se retorna "None"; nunca se genera un error
      "KeyError".

      Ten en cuenta que si el campo nombrado aparece más de una vez en
      los encabezados del mensaje, no se define cuales serán
      exactamente aquellos valores de campos retornados. Usa el método
      "get_all()" para obtener los valores de todos los encabezados
      nombrados existentes.

   __setitem__(name, val)

      Añade un encabezado al mensaje con el nombre de campo *name* y
      el valor *val*. El campo es añadido al final de los campos
      existentes del mensaje.

      Ten en cuenta que esto no sobreescribe ni elimina ningún
      encabezado existente con el mismo nombre. Si quieres asegurar
      que el nuevo encabezado es el único presente en el mensaje con
      el nombre de campo *name*, elimina el campo primero, ej:

         del msg['subject']
         msg['subject'] = 'Python roolz!'

   __delitem__(name)

      Elimina todas las ocurrencias de un campo con el nombre *name*
      de los encabezados del mensaje. No se genera ninguna excepción
      si el encabezado nombrado no está presente en los encabezados.

   keys()

      Retorna una lista de todos los nombres de campos de encabezados
      del mensaje.

   values()

      Retorna una lista de todos los valores de campos del mensaje.

   items()

      Retorna una lista de tuplas de dos elementos conteniendo todos
      los campos y valores de encabezados del mensaje.

   get(name, failobj=None)

      Return the value of the named header field.  This is identical
      to "__getitem__()" except that optional *failobj* is returned if
      the named header is missing (defaults to "None").

   Aquí hay algunos métodos útiles adicionales:

   get_all(name, failobj=None)

      Retorna una lista de todos los valores para el campo denominado
      *name*. Si no hay tales encabezados nombrados en el mensaje,
      retorna *failobj* (por defecto "None").

   add_header(_name, _value, **_params)

      Configuración de encabezado extendida. Este método es similar a
      "__setitem__()" excepto que pueden ser provistos parámetros
      adicionales de encabezado como argumentos de palabra clave.
      *_name* es el campo de encabezado a añadir y *_value* es el
      valor *primario* para el encabezado.

      Para cada elemento en el diccionario de argumentos de palabra
      clave *_params*, la clave se toma como el nombre del parámetro
      con guiones bajos convertidos a guiones medios (ya que los
      guiones medios son ilegales como identificadores en Python).
      Normalmente, el parámetro será añadido como  "key="value"" a no
      ser que el valor sea "None", en cuyo caso sólo la clave será
      añadida. Si el valor contiene caracteres no ASCII, puede ser
      especificado como una tupla de tres elementos en el formato
      "(CHARSET, LANGUAGE, VALUE)", donde "CHARSET" es una cadena que
      nombra el conjunto de caracteres a ser usado al codificar el
      valor, "LANGUAGE" puede normalmente ser definido a "None" o una
      cadena vacía (ver **RFC 2231** para otras posibilidades) y
      "VALUE" es la cadena del valor conteniendo puntos de caracteres
      no ASCII. Si no se pasa una tupla de tres elementos y el valor
      contiene caracteres no ASCII, se codifica automáticamente en
      formato **RFC 2231** usando "CHARSET" como "utf-8" y "LANGUAGE"
      como "None".

      Aquí hay un ejemplo:

         msg.add_header('Content-Disposition', 'attachment', filename='bud.gif')

      Esto añadirá un encabezado que se verá como

         Content-Disposition: attachment; filename="bud.gif"

      Un ejemplo con caracteres no ASCII:

         msg.add_header('Content-Disposition', 'attachment',
                        filename=('iso-8859-1', '', 'Fußballer.ppt'))

      Lo que produce

         Content-Disposition: attachment; filename*="iso-8859-1''Fu%DFballer.ppt"

   replace_header(_name, _value)

      Reemplaza un encabezado. Reemplaza el primer encabezado
      encontrado en el mensaje que concuerda con *_name*, conservando
      el orden del encabezado y el nombre del campo. Si no se
      encuentra ningún encabezado que concuerde, se genera un error
      "KeyError".

   get_content_type()

      Retorna el tipo de contenido del mensaje. La cadena retornada se
      fuerza a letras minúsculas de la forma *maintype/subtype*. Si no
      hay ningún encabezado *Content-Type* en el mensaje será
      retornado el tipo por defecto como es dado por
      "get_default_type()". Dado que según **RFC 2045**, los mensajes
      tienen siempre un tipo predeterminado, "get_content_type()"
      siempre retornará un valor.

      **RFC 2045** define el tipo predeterminado del mensaje a
      *text/plain* a no ser que aparezca dentro de un contenedor
      *multipart/digest*, en cuyo caso sería *message/rfc822*. Si el
      encabezado *Content-Type* tiene una especificación de tipo
      inválido, **RFC 2045** ordena que el tipo por defecto sea
      *text/plain*.

   get_content_maintype()

      Retorna el tipo de contenido principal del mensaje. Esta es la
      parte *maintype* de la cadena retornada por
      "get_content_type()".

   get_content_subtype()

      Retorna el tipo del subcontenido del mensaje. Esta es la parte
      *subtype* de la cadena retornada por "get_content_type()".

   get_default_type()

      Retorna el tipo del contenido por defecto. La mayoría de
      mensajes tienen un tipo de contenido por defecto de
      *text/plain*, excepto para mensajes que son subpartes de
      contenedores *multipart/digest*. Tales subpartes tienen como
      tipo de contenido predeterminado *message/rfc822*.

   set_default_type(ctype)

      Establece el tipo de contenido por defecto. *ctype* debería ser
      *text/plain* o *message/rfc822*, aunque esto no es obligatorio.
      El tipo de contenido predeterminado no se almacena en el
      encabezado *Content-Type*.

   get_params(failobj=None, header='content-type', unquote=True)

      Retorna los parámetros del *Content-Type* del mensaje como una
      lista. Los elementos de la lista retornada son tuplas de dos
      elementos de pares clave/valor, tal y como son partidas por el
      signo "'='". El lado izquierdo del "'='" es la clave, mientras
      el lado derecho es el valor. Si no hay signo "'='" en el
      parámetro, el valor es la cadena vacía, en caso contrario el
      valor es como se describe en "get_param()" y no está citado si
      el parámetro opcional *unquote* es "True" (por defecto).

      El parámetro opcional *failobj* es el objeto a retornar si no
      hay encabezado *Content-Type*. El parámetro opcional *header* es
      el encabezado a buscar en lugar de *Content-Type*.

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by the *params* property of the
      individual header objects returned by the header access methods.

   get_param(param, failobj=None, header='content-type', unquote=True)

      Retorna el valor del parámetro *param* del encabezado *Content-
      Type* como una cadena. Si el mensaje no tiene encabezado
      *Content-Type* o si no existe tal parámetro, entonces se retorna
      *failobj* (por defecto es "None").

      El parámetro opcional *header*, si es definido, especifica el
      encabezado del mensaje a usar en lugar de *Content-Type*.

      Las claves de parámetros siempre son comparadas distinguiendo
      entre mayúsculas y minúsculas. El valor de retorno puede ser una
      cadena, una tupla de 3 elementos si el parámetro fue codificado
      según **RFC 2231**. Cuando es una tupla de 3 elementos, los
      elementos del valor tienen la forma "(CHARSET, LANGUAGE,
      VALUE)". Ten en cuenta que "CHARSET" y "LANGUAGE" pueden ser
      "None", en cuyo caso debes considerar "VALUE" como codificado en
      el conjunto de caracteres "us-ascii". Generalmente puedes
      ignorar "LANGUAGE".

      Si a tu aplicación no le importa si el parámetro fue codificado
      según **RFC 2231**, puedes contraer el valor del parámetro
      invocando "email.utils.collapse_rfc2231_value()", pasando el
      valor de retorno desde "get_param()". Esto retornará una cadena
      Unicode convenientemente decodificada cuando el valor es una
      tupla o la cadena original sin entrecomillar si no lo es. Por
      ejemplo:

         rawparam = msg.get_param('foo')
         param = email.utils.collapse_rfc2231_value(rawparam)

      En cualquier caso, el valor del parámetro (tanto la cadena
      retornada o el elemento "VALUE" en la tupla de 3 elementos)
      siempre está sin entrecomillar, a no ser que *unquote* está
      establecido a "False".

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by the *params* property of the
      individual header objects returned by the header access methods.

   set_param(param, value, header='Content-Type', requote=True, charset=None, language='', replace=False)

      Establece un parámetro en el encabezado *Content-Type*. Si el
      parámetro ya existe en el encabezado, su valor será remplazado
      con *value*. Si el encabezado *Content-Type* no ha sido definido
      todavía para este mensaje, será establecido a *text/plain* y el
      nuevo valor del parámetro será añadido según **RFC 2045**.

      El parámetro opcional *header* especifica una alternativa a
      *Content-Type* y todos los parámetros serán entrecomillados si
      es necesario a no ser que el parámetro opcional *requote* sea
      "False" (por defecto es "True").

      Si se especifica el parámetro opcional *charset*, el parámetro
      será codificado de acuerdo a **RFC 2231**. El parámetro opcional
      *language* especifica el lenguaje RFC 2231, por defecto una
      cadena vacía. Tanto *charset* como *language* deberían ser
      cadenas.

      Si *replace* es "False" (por defecto) el encabezado será movido
      al final de la lista de encabezados. Si *replace* es "True", el
      encabezado será actualizado.

      Distinto en la versión 3.4: el parámetro de palabra clave
      "replace" fue añadido.

   del_param(param, header='content-type', requote=True)

      Elimina el parámetro dado completamente del encabezado *Content-
      Type*. El encabezado será reescrito en sí mismo sin el parámetro
      o su valor. Todos los valores serán entrecomillados si es
      necesario a no ser que *requote* sea "False" (por defecto es
      "True"). El parámetro opcional *header* especifica una
      alternativa a *Content-Type*.

   set_type(type, header='Content-Type', requote=True)

      Establece el tipo y subtipo principal para el encabezado
      *Content-Type*. *type* debe ser una cadena de la forma
      *maintype/subtype*, si no será generado un "ValueError".

      Este método remplaza el encabezado *Content-Type*, manteniendo
      todos los parámetros en su lugar. Si *requote* es "False", este
      dejará el encabezado existente tal como está, en caso contrario
      los parámetros serán entrecomillados (por defecto).

      Un encabezado alternativo puede ser especificado en el argumento
      *header*. Cuando el encabezado *Content-Type* es definido, un
      encabezado *MIME-Version* también es añadido.

      This is a legacy method.  On the "EmailMessage" class its
      functionality is replaced by the "make_" and "add_" methods.

   get_filename(failobj=None)

      Retorna el valor del parámetro "filename" del encabezado
      *Content-Disposition* del mensaje. Si el encabezado no tiene un
      parámetro "filename", este método recurre a buscar el parámetro
      "name" en el encabezado *Content-Type*. Si tampoco se encuentra
      o falta el encabezado, entonces retorna *failobj*. La cadena
      retornada siempre será sin entrecomillar según
      "email.utils.unquote()".

   get_boundary(failobj=None)

      Retorna el valor del parámetro "boundary" del encabezado
      *Content-Type* del mensaje o *failobj* tanto si falta el
      encabezado como si no tiene parámetro "boundary". La cadena
      retornada siempre será sin entrecomillar según
      "email.utils.unquote()".

   set_boundary(boundary)

      Establece el parámetro "boundary" del encabezado *Content-Type*
      a *boundary*. "set_boundary()" siempre entrecomillará *boundary*
      si es necesario. Se genera "HeaderParseError" si el objeto de
      mensaje no tiene encabezado *Content-Type*.

      Ten en cuenta que usar este método es sutilmente diferente a
      borrar el antiguo encabezado *Content-Type* y añadir uno nuevo
      con el nuevo límite mediante "add_header()" porque
      "set_boundary()" preserva el orden del encabezado *Content-Type*
      en la lista de encabezados. Sin embargo, no conserva ninguna
      línea de continuación que pueden haber estado presentes en el
      encabezado original *Content-Type*.

   get_content_charset(failobj=None)

      Retorna el parámetro "charset" del encabezado *Content-Type*,
      forzado a letras minúsculas. Si no hay un encabezado *Content-
      Type* o si ese encabezado no tiene parámetro "charset", se
      retorna *failobj*.

      Ten en cuenta que este método difiere de "get_charset()", el
      cual retorna la instancia "Charset" para la codificación por
      defecto del cuerpo del mensaje.

   get_charsets(failobj=None)

      Retorna una lista conteniendo los nombres de los conjuntos de
      caracteres en el mensaje. Si el mensaje es *multipart*, entonces
      la lista contendrá un elemento para cada subparte en la carga
      (*payload*), en caso contrario será una lista de un elemento.

      Cada elemento en la lista será una cadena la cual es el valor
      del parámetro "charset" en el encabezado *Content-Type* para la
      subparte representada. Sin embargo, si la subparte no tiene
      encabezado *Content-Type*, no tiene parámetro "charset" o no es
      del tipo MIME *text* principal, entonces ese elemento en la
      lista retornada será *failobj*.

   get_content_disposition()

      Retorna el valor en minúsculas (sin parámetros) del encabezado
      del mensaje *Content-Disposition* si tiene uno o "None". Los
      valores posibles para este método son *inline*, *attachment* o
      "None" si el mensaje sigue el **RFC 2183**.

      Added in version 3.5.

   walk()

      El método "walk()" es un generador de todo propósito el cual
      puede ser usado para iterar sobre todas las partes y subpartes
      de árbol de objeto de mensaje, en orden de recorrido de
      profundidad primero. Siempre usarás típicamente "walk()" como
      iterador en un bucle "for"; cada iteración retorna la siguiente
      subparte.

      Aquí hay un ejemplo que imprime el tipo MIME de cada parte de
      una estructura de mensaje multiparte:

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
      "is_multipart()" retorna "True", aunque
      "msg.get_content_maintype() == 'multipart'" puede retornar
      "False". Vemos esto en nuestro ejemplo haciendo uso de la
      función de ayuda de depuración "_structure":

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

      Aquí las partes de "message" no son "multiparts", pero contienen
      subpartes. "is_multipart()" retorna "True" y "walk" desciende a
      las subpartes.

   Los objetos "Message" pueden contener opcionalmente dos atributos
   de instancia, los cuales pueden ser usados al generar el texto
   plano de un mensaje MIME.

   preamble

      El formato de un documento MIME permite algo de texto entre la
      línea en blanco que sigue a los encabezados y la primera cadena
      límite multiparte. Normalmente, este texto nunca es visible en
      un lector de correo compatible con MIME porque queda fuera de la
      armadura MIME estándar. Sin embargo, viendo el texto del mensaje
      en crudo o viendo el mensaje en un lector no compatible con
      MIME, este texto puede volverse visible.

      El atributo *preamble* contiene este texto de refuerzo adicional
      para documentos MIME. Cuando el "Parser" descubre algo de texto
      después de los encabezados pero antes de la primera cadena
      límite, asigna este texto al atributo *preamble* del mensaje.
      Cuando el "Generator" está escribiendo la representación de
      texto sin formato de un mensaje MIME y puede encontrar el
      mensaje como un atributo *preamble*, escribirá este texto en el
      área entre los encabezados y el primer límite. Consulta
      "email.parser" y "email.generator" para más detalles.

      Ten en cuenta que si el objeto de mensaje no tiene preámbulo, el
      atributo *preamble* será "None".

   epilogue

      El atributo *epilogue* actúa de la misma manera que el atributo
      *preamble*, excepto que contiene texto que aparece entre el
      último límite y el fin del mensaje.

      No necesitas establecer el epílogo de la cadena vacía en orden
      para el "Generator" para imprimir una nueva línea al final del
      archivo.

   defects

      El atributo *defects* contiene una lista de todos los problemas
      encontrados al analizar este mensaje. Consulta "email.errors"
      para una descripción detallada de los posibles defectos de
      análisis.
