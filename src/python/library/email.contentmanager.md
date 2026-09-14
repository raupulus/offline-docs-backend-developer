---
title: '"email.contentmanager": Managing MIME Content'
source_url: https://docs.python.org/es/3
source_path: library/email.contentmanager.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2400
---

# "email.contentmanager": Managing MIME Content

**Código fuente:** Lib/email/contentmanager.py

======================================================================

Added in version 3.6: [1]

class email.contentmanager.ContentManager

   Clase base para gestores de contenido.  Proporciona los mecanismos
   de registro estándar para registrar convertidores entre contenido
   MIME y otras representaciones, así como los métodos de envío
   "get_content" y "set_content".

   get_content(msg, *args, **kw)

      Busca una función de controlador basada en el "mimetype" de
      *msg* (ver el siguiente párrafo), la llama, le pasa todos los
      argumentos y retorna el resultado de la llamada.  La expectativa
      es que el controlador extraiga la carga útil de *msg* y retorne
      un objeto que codifica información sobre los datos extraídos.

      Para encontrar el controlador, busca las siguientes llaves en el
      registro, deteniéndose con la primera que encuentre:

      * la cadena que representa el tipo MIME completo
        ("maintype/subtype")

      * la cadena de caracteres que representa el "maintype"

      * la cadena de caracteres vacía

      Si ninguna de estas llaves produce un controlador, se lanza una
      excepción "KeyError" para el tipo MIME completo.

   set_content(msg, obj, *args, **kw)

      Si el "maintype" es "multipart", se lanza un "TypeError"; de lo
      contrario, busca una función de controlador basada en el tipo de
      *obj* (ver el siguiente párrafo), llama a "clear_content()" en
      el *msg* y llama a la función de controlador, pasando todos los
      argumentos.  La expectativa es que el controlador transforme y
      almacene *obj* en *msg*, posiblemente realizando otros cambios a
      *msg* también, como agregar varios encabezados MIME para
      codificar la información necesaria para interpretar los datos
      almacenados.

      Para encontrar el controlador, obtiene el tipo de *obj* ("typ =
      type(obj)"), y busca las siguientes llaves en el registro,
      deteniéndose con la primera encontrada:

      * el tipo en sí ("typ")

      * el nombre completo de calificación del tipo ("typ.__module__ +
        '.' + typ.__qualname__").

      * the type's "qualname" ("typ.__qualname__")

      * the type's "name" ("typ.__name__").

      If none of the above match, repeat all of the checks above for
      each of the types in the *MRO* ("typ.__mro__"). Finally, if no
      other key yields a handler, check for a handler for the key
      "None".  If there is no handler for "None", raise a "KeyError"
      for the fully qualified name of the type.

      También agrega un encabezado *MIME-Version* si no hay uno
      presente (vea también "MIMEPart").

   add_get_handler(key, handler)

      Registra el *handler* de funciones como el manejador de *key*.
      Para los posibles valores de *key*, consulte "get_content()".

   add_set_handler(typekey, handler)

      Registra el *handler* como la función a llamar cuando un objeto
      de un tipo coincidente *typekey* se pasa a "set_content()".
      Para los posibles valores de *typekey*, consulte
      "set_content()".

## Instancias gestoras de contenido

Actualmente, el paquete de correo electrónico solo proporciona un
administrador de contenido concreto, "raw_data_manager", aunque en el
futuro se pueden agregar más. "raw_data_manager" es el
"content_manager" proporcionado por "EmailPolicy" y sus derivados.

email.contentmanager.raw_data_manager

   Este administrador de contenido proporciona sólo una interfaz
   mínima más allá de la proporcionada por "Message" en sí:  trata
   solo con texto, cadenas de bytes sin procesar, y objetos "Message".
   Sin embargo, proporciona ventajas significativas en comparación con
   la API base: "get_content" en una parte de texto retornará una
   cadena de caracteres unicode sin que la aplicación tenga que
   decodificarla manualmente, "set_content" proporciona un amplio
   conjunto de opciones para controlar los encabezados añadidos a una
   parte y controlar la codificación de transferencia de contenido, y
   permite el uso de los diversos métodos "add_", simplificando así la
   creación de mensajes multiparte.

   email.contentmanager.get_content(msg, errors='replace')

      Retorna la carga útil de la parte como una cadena de caracteres
      (para partes de "text"), un objeto "EmailMessage" (para partes
      de "message/rfc822"), o un objeto de "bytes" (para todos los
      demás tipos que no son multiparte).  Lanza un "KeyError" si se
      llama en un "multipart".  Si la parte es una parte de "text" y
      se especifica *errors*, se usa como el controlador de errores al
      decodificar la carga útil a unicode.  El controlador de errores
      predeterminado es "replace".

   email.contentmanager.set_content(msg, <'str'>, subtype="plain", charset='utf-8', cte=None, disposition=None, filename=None, cid=None, params=None, headers=None)
   email.contentmanager.set_content(msg, <'bytes'>, maintype, subtype, cte="base64", disposition=None, filename=None, cid=None, params=None, headers=None)
   email.contentmanager.set_content(msg, <'EmailMessage'>, cte=None, disposition=None, filename=None, cid=None, params=None, headers=None)

      Añade cabeceras y carga útil al *msg*:

      Añade un encabezado *Content-Type* con un valor
      "maintype/subtype".

      * Para "str", establece el "maintype" de MIME en "text", y
        establece el subtipo en *subtype* si se especifica, o "plain"
        si no está presente.

      * Para "bytes", usa el *maintype* y *subtype* especificados, o
        lanza un "TypeError" si no se especifican.

      * Para objetos "EmailMessage", establece el *maintype* en
        "message", y establece el *subtype* en *subtype* si se
        especifica o "rfc822" si no se especifica. Si *subtype* es
        "partial", se lanza un error (los objetos de "bytes" deben
        usarse para construir partes "message/partial").

      Si se proporciona *charset* (lo cual solo es válido para "str"),
      codifica la cadena de caracteres en bytes utilizando el conjunto
      de caracteres especificado.  El valor por defecto es "utf-8".
      Si el *charset* especificado es un alias conocido del nombre de
      un conjunto de caracteres del estándar MIME, utiliza el conjunto
      de caracteres estándar en su lugar.

      Si se establece *cte*, codifica la carga útil mediante la
      codificación de transferencia de contenido especificada y
      establece el encabezado *Content-Transfer-Encoding* en ese
      valor.  Los valores posibles para *cte* son "quoted-printable",
      "base64", "7bit", "8bit", y "binary".  Si la entrada no se puede
      codificar en la codificación especificada (por ejemplo,
      especificando un *cte* de "7bit" para una entrada que contiene
      valores no ASCII), se lanza un "ValueError".

      * For "str" objects, if *cte* is not set use heuristics to
        determine the most compact encoding.  Prior to encoding,
        "str.splitlines()" is used to normalize all line boundaries,
        ensuring that each line of the payload is terminated by the
        current policy's "linesep" property (even if the original
        string did not end with one).

      * For "bytes" objects, *cte* is taken to be base64 if not set,
        and the aforementioned newline translation is not performed.

      * Para "EmailMessage", según **RFC 2046**, se lanza un error si
        se solicita un *cte* de "quoted-printable" o "base64" para el
        *subtype* "rfc822", y para cualquier *cte* que no sea "7bit"
        para el *subtype* "external-body".  Para "message/rfc822", se
        usa "8bit" si no se especifica *cte*.  Para todos los demás
        valores de *subtype*, se usa "7bit".

      Nota:

        Un *cte* de "binary" todavía no funciona correctamente. El
        objeto "EmailMessage" modificado por "set_content" es
        correcto, pero "BytesGenerator" no lo serializa correctamente.

      Si se establece *disposición*, se usa como valor del encabezado
      *Content-Disposition*.  Si no se especifica y se especifica
      *filename*, agrega el encabezado con el valor "attachment". Si
      no se especifica *disposition* y tampoco se especifica
      *filename*, no agrega el encabezado.  Los únicos valores válidos
      para *disposition* son "attachment" e "inline".

      Si se especifica el *filename*, se usa como el valor del
      parámetro "filename" del encabezado *Content-Disposition*.

      Si se especifica *cid*, agrega un encabezado *Content-ID* con
      valor *cid*.

      Si se especifica *params*, itera su método "items" y use los
      pares resultantes "(key, value)" para establecer parámetros
      adicionales en el encabezado *Content-Type*.

      Si se especifica *headers* y es una lista de cadenas de
      caracteres de la forma "headername: headervalue" o una lista de
      objetos "header" (que se distinguen de las cadenas de caracteres
      por tener un atributo "name"), agrega los encabezados a *msg*.

-[ Notas al pie de página ]-

[1] Originalmente añadido en la versión 3.4 como un *módulo
    provisional*
