---
title: '"email.generator": Generating MIME documents'
source_url: https://docs.python.org/es/3
source_path: library/email.generator.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2440
---

# "email.generator": Generating MIME documents

**Código fuente:** Lib/email/generator.py

======================================================================

One of the most common tasks is to generate the flat (serialized)
version of the email message represented by a message object
structure.  You will need to do this if you want to send your message
via "smtplib.SMTP.sendmail()", or print the message on the console.
Taking a message object structure and producing a serialized
representation is the job of the generator classes.

Al igual que con el módulo "email.parser", no se limita a la
funcionalidad del generador incluido; se podría escribir uno desde
cero. Sin embargo, el generador incluido sabe cómo generar la mayoría
del correo electrónico de una manera compatible con los estándares,
debería controlar los mensajes de correo electrónico MIME y no MIME
bien. Está diseñado para que las operaciones de análisis y generación
orientadas a bytes sean inversas, asumiendo que se utilice la misma
"policy" de no transformación para ambos. Es decir, analizar la
secuencia de bytes serializada a través de la clase "BytesParser" y, a
continuación, regenerar la secuencia de bytes serializada mediante
"BytesGenerator" debe producir una salida idéntica a la entrada [1].
(Por otro lado, el uso del generador en un "EmailMessage" construido
por el programa puede dar lugar a cambios en el objeto "EmailMessage"
a medida que se rellenan los valores predeterminados.)

La clase "Generator" se puede utilizar para acoplar un mensaje en una
representación serializada de texto (a diferencia de la binaria). Sin
embargo, como Unicode no puede representar datos binarios
directamente, el mensaje es necesariamente transformado en algo que
contiene sólo caracteres ASCII. Se utiliza las técnicas de
codificación de transferencia de contenido RFC de correo electrónico
estándar para codificar mensajes de correo electrónico para el
transporte a través de canales que no son "8 bits limpios".

Para adaptar procesamiento reproducible de mensajes firmados por
SMIME,  "Generator" deshabilita el encabezamiento para las partes del
mensaje de tipo "multipart/signed" y todas sus subpartes.

class email.generator.BytesGenerator(outfp, mangle_from_=None, maxheaderlen=None, *, policy=None)

   Retorna un objeto "BytesGenerator" que escribirá cualquier mensaje
   provisto por el método "flatten()", o cualquier texto de escape
   sustituto cifrado con el método "write()", al *file-like object*
   *outfp*. *outfp* debe soportar un método "write" que acepte datos
   binarios.

   Si *mangle_from_* opcional es "True", se coloca un carácter ''>''
   delante de cualquier línea del cuerpo que comience con la cadena
   exacta ""From "", es decir, "From" seguido de un espacio al
   principio de una línea. *mangle_from_* vuelve de forma
   predeterminada al valor de la configuración "mangle_from_" de la
   *policy* (que es "True" para la política "compat32" y "False" para
   todas las demás). *mangle_from_* está diseñado para su uso cuando
   los mensajes se almacenan en formato mbox de Unix (consulte
   "mailbox" y WHY THE CONTENT-LENGTH FORMAT IS BAD).

   Si *maxheaderlen* no es "None", se repliega las líneas de
   encabezado que son mayores que *maxheaderlen*, o si es "0", no se
   reenvuelve ningún encabezado. Si *manheaderlen* es "None"
   (predeterminado), se envuelven los encabezados y otras líneas de
   mensajes de acuerdo a los ajustes de *policy*.

   Si la *norma* es especificada, se usa esa norma para controlar la
   generación de mensajes. Si la *norma* es "None" (predeterminado),
   se usa la norma asociada con el "Message" o el objeto
   "EmailMessage" pasado para "flatten" para controlar la generación
   del mensaje. Se puede ver "email.policy" para detalles de que
   controla la *norma*.

   Added in version 3.2.

   Distinto en la versión 3.3: Agregada la palabra clave *norma*.

   Distinto en la versión 3.6: El comportamiento predeterminado de los
   parámetros *mangle_from_* y *maxheaderlen* es para seguir la norma.

   flatten(msg, unixfrom=False, linesep=None)

      Imprime la representación textual de la estructura del objeto de
      mensaje originada en *msg* al archivo de salida especificado
      cuando se creó la instancia "BytesGenerator".

      Si el tipo "cte_type" de la opción "policy" es "8bit" (valor
      predeterminado), se copia los encabezados en el mensaje
      analizado original que no se hayan modificado con ningún bytes a
      la salida con el conjunto de bits altos, reproducido como en el
      original, y se conserva el *Content-Transfer-Encoding* no ASCII
      de cualquier parte del cuerpo que los tenga. Si "cte_type" es
      "7bit", se convierte los bytes con el conjunto de bits altos
      según sea necesario utilizando un *Content-Transfer-Encoding*
      compatible con ASCII . Es decir, se transforma partes con
      *Content-Transfer-Encoding* no ASCII (*Content-Transfer-
      Encoding: 8bit*) en un conjunto de caracteres compatible con
      ASCII *Content-Transfer-Encoding*, y se codifica bytes inválidos
      RFC no ASCII en encabezados mediante el conjunto de caracteres
      MIME "unknown-8bit", lo que los convierte en compatibles con
      RFC.

      Si *unixfrom* es "True", se imprime el delimitador de encabezado
      de sobre utilizado por el formato de buzón de correo Unix
      (consulta "mailbox") antes del primero de los encabezados **RFC
      5322** del objeto de mensaje raíz. Si el objeto raíz no tiene
      encabezado de sobre, se crea uno estándar. El valor
      predeterminado es "False". Tener en cuenta que para las
      subpartes, nunca se imprime ningún encabezado de sobre.

      Si *linesep* no es "None", se usa como caracter separador entre
      todas las líneas del mensaje acoplado. Si *linesep* es "None"
      (predeterminado), se usa el valor especificado en la *norma*.

   clone(fp)

      Retorna un clon independiente de esta instancia de
      "BytesGenerator" con las mismas configuraciones exactas, y *fp*
      como el nuevo *outfp*.

   write(s)

      Codifica *s* usando el códec "ASCII" u el manipulador de error
      "escape sustituto", y lo pasa al método *write* del *outfp*
      pasado al constructor de la clase "BytesGenerator".

Como conveniencia, "EmailMessage" provee los métodos "as_bytes()" y
"bytes(aMessage)" (también conocido como "__bytes__()") que
simplifican la generación de la representación serializada binaria de
un objeto mensaje. Para más detalle, ver "email.message".

Dado que las cadenas de caracteres no pueden representar datos
binarios, la clase "Generator" debe convertir los datos binarios en
cualquier mensaje que aplane a un formato compatible con ASCII,
convirtiéndolos en un *Content-Transfer_Encoding* compatible con
ASCII. Usando la terminología de RFC de correo electrónico, se puede
pensar en esto como "Generator" serializando a una secuencia de E/S
que no es *"8 bit clean"*. En otras palabras, la mayoría de las
aplicaciones querrán usar "BytesGenerator", y no "Generator".

class email.generator.Generator(outfp, mangle_from_=None, maxheaderlen=None, *, policy=None)

   Retorna un objeto "Generator" que escribirá cualquier mensaje
   provisto al método "flatten()", o cualquier texto provisto al
   método "write()", al *file-like object* *outfp*. *outfp* debe
   soportar un método "write" que acepte datos de cadena de
   caracteres.

   Si *mangle_from_* opcional es "True", se coloca un carácter ''>''
   delante de cualquier línea del cuerpo que comience con la cadena
   exacta ""From "", es decir, "From" seguido de un espacio al
   principio de una línea. *mangle_from_* vuelve de forma
   predeterminada al valor de la configuración "mangle_from_" de la
   *policy* (que es "True" para la política "compat32" y "False" para
   todas las demás). *mangle_from_* está diseñado para su uso cuando
   los mensajes se almacenan en formato mbox de Unix (consulte
   "mailbox" y WHY THE CONTENT-LENGTH FORMAT IS BAD).

   Si *maxheaderlen* no es "None", se repliega las líneas de
   encabezado que son mayores que *maxheaderlen*, o si es "0", no se
   reenvuelve ningún encabezado. Si *manheaderlen* es "None"
   (predeterminado), se envuelven los encabezados y otras líneas de
   mensajes de acuerdo a los ajustes de *policy*.

   Si la *norma* es especificada, se usa esa norma para controlar la
   generación de mensajes. Si la *norma* es "None" (predeterminado),
   se usa la norma asociada con el "Message" o el objeto
   "EmailMessage" pasado para "flatten" para controlar la generación
   del mensaje. Se puede ver "email.policy" para detalles de que
   controla la *norma*.

   Distinto en la versión 3.3: Agregada la palabra clave *norma*.

   Distinto en la versión 3.6: El comportamiento predeterminado de los
   parámetros *mangle_from_* y *maxheaderlen* es para seguir la norma.

   flatten(msg, unixfrom=False, linesep=None)

      Imprime la representación textual de la estructura del objeto de
      mensaje originado en el *msg* al archivo especificado de salida
      cuando la instancia de "Generator" fue creada.

      Si la opción "policy" "cte_type" es "8bit", se genera el mensaje
      como si la opción estuviera establecida en "7bit". (Esto es
      necesario porque las cadenas de caracteres no pueden representar
      bytes que no sean ASCII). Convierte cualesquiera bytes con el
      conjunto de bits alto según sea necesario utilizando un
      *Content-Transfer-Encoding* compatible con ASCII. Es decir,
      transforma partes con *Content-Transfer-Encoding* (*Content-
      Transfer-Encoding: 8bit*) no ASCII en un conjunto de caracteres
      *Content-Transfer-Encoding* compatible con ASCII. Y codifica
      bytes no ASCII RFC inválidos ASCII en encabezados mediante el
      conjunto de caracteres MIME "unknown-8bit", lo que los convierte
      en compatibles con RFC.

      Si *unixfrom* es "True", se imprime el delimitador de encabezado
      de sobre utilizado por el formato de buzón de correo Unix
      (consulta "mailbox") antes del primero de los encabezados **RFC
      5322** del objeto de mensaje raíz. Si el objeto raíz no tiene
      encabezado de sobre, se crea uno estándar. El valor
      predeterminado es "False". Tener en cuenta que para las
      subpartes, nunca se imprime ningún encabezado de sobre.

      Si *linesep* no es "None", se usa como caracter separador entre
      todas las líneas del mensaje acoplado. Si *linesep* es "None"
      (predeterminado), se usa el valor especificado en la *norma*.

      Distinto en la versión 3.2: Agrega soporte para el recodificado
      de cuerpos de mensajes "8bit", y el argumento *linesep*.

   clone(fp)

      Retorna un clon independiente de esta instancia de  "Generator"
      con las mismas opciones exactas y *fp* como la nueva *outfp*.

   write(s)

      Escribe *s* al método *write* del *outfp* pasado al constructor
      de la "Generator". Esto provee justo la suficiente API de tipo
      archivo para instancias de "Generator" para ser usadas en la
      función "print()".

Para conveniencia, "EmailMessage"  provee los métodos  "as_string()" y
"str(aMessage)" (también conocido como "__str__()"), que simplifican
la generación de una representación de una cadena de caracteres
formateada de un objeto mensaje. Para más detalles, ver
"email.message".

The "email.generator" module also provides a derived class,
"DecodedGenerator", which is like the "Generator" base class, except
that non-*text* parts are not serialized, but are instead represented
in the output stream by a string derived from a template filled in
with information about the part.

class email.generator.DecodedGenerator(outfp, mangle_from_=None, maxheaderlen=None, fmt=None, *, policy=None)

   Se actúa como "Generator", excepto para cualquier subparte del
   mensaje pasado a "Generator.flatten()", si la subparte es de tipo
   principal *text*, se imprime la carga útil decodificada de la
   subparte, y si el tipo principal no es *text*, en lugar de
   imprimirlo se rellena la cadena de caracteres *fmt* utilizando la
   información de la parte y se imprime la cadena de caracteres
   rellenada resultante.

   Para llenar *fmt*, se ejecuta "fmt % part_info", donde "part_info"
   es un diccionario compuesto por las siguientes claves y valores:

   * "type" -- Todo el tipo MIME de la parte no*text*

   * "maintype" -- Principal tipo MIME de la parte no*text*

   * "subtype" -- Tipo sub-MIME de la parte no-*text*

   * "filename" -- Nombre de archivo de la parte no*text*

   * "description" -- Descripción asociada con la parte no*text*

   * "encoding" -- Codificado de la transferencia del contenido de la
     parte no-*text*

   Si *fmt* es "None", se usa el siguiente *fmt* predeterminado:

      "[Non-text (%(type)s) part of message omitted, filename
      %(filename)s]"

   Los opcionales *_mangle_from_* y *maxheaderlen* son como en la
   clase base "Generator".

-[ Notas al pie ]-

[1] Esta instrucción supone que se utiliza la configuración adecuada
    para "unixfrom", y que no hay ninguna configuración "email.policy"
    que llame a ajustes automáticos (por ejemplo, "refold_source" debe
    ser "none", que es *no* es el valor predeterminado). Esto tampoco
    es 100% verdadero, ya que si el mensaje no se ajusta a los
    estándares RFC ocasionalmente la información sobre el texto
    original exacto se pierde durante la el análisis de recuperación
    de errores. Es un objetivo fijar estos últimos casos extremos
    cuando sea posible.
