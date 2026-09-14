---
title: '"email.utils": Miscellaneous utilities'
source_url: https://docs.python.org/es/3
source_path: library/email.utils.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2530
---

# "email.utils": Miscellaneous utilities

**Código fuente:** Lib/email/utils.py

======================================================================

There are a couple of useful utilities provided in the "email.utils"
module:

email.utils.localtime(dt=None)

   Return local time as an aware datetime object.  If called without
   arguments, return current time.  Otherwise *dt* argument should be
   a "datetime" instance, and it is converted to the local time zone
   according to the system time zone database.  If *dt* is naive (that
   is, "dt.tzinfo" is "None"), it is assumed to be in local time.

   Added in version 3.3.

   Deprecated since version 3.12, removed in version 3.14: El
   parámetro *isdst*.

email.utils.make_msgid(idstring=None, domain=None)

   Retorna una cadena de caracteres apropiada para una cabecera
   *Message-ID*  que cumpla con **RFC 2822**. Si se especifica un
   *idstring* opcional, es una cadena de caracteres utilizada para
   reforzar la unicidad del identificador del mensaje. Si se
   especifica un *domain* opcional provee la porción del msgid después
   de '@'. El predeterminado es el hostname local. Normalmente no es
   necesario especificar este valor, pero puede ser útil en algunos
   casos, como cuando se está construyendo un sistema distribuido que
   utiliza un nombre de dominio consistente a lo largo de varios
   ordenadores.

   Distinto en la versión 3.2: Se añadió la palabra clave *domain*.

Las funciones que quedan son parte de la API de correo electrónico
heredada ("Compat32") . No hay necesidad de utilizarlas directamente
con el nuevo API, dado que el análisis sintáctico y formateo que
proporcionan es realizado automáticamente por el mecanismo de análisis
sintáctico de la nueva API.

email.utils.quote(str)

   Retorna una nueva cadena de caracteres con barras invertidas ("\")
   en *str* reemplazado por dos barras invertidas, y comillas dobles
   reemplazadas por barra invertida seguido de comillas dobles.

email.utils.unquote(str)

   Retorna una nueva cadena de caracteres que es una versión
   *unquoted* de *str*. Si *str* comienza y termina con comillas
   dobles, éstas son eliminadas. De igual manera si *str* empieza y
   termina con comillas angulares ("<" y ">"), éstas son eliminadas.

email.utils.parseaddr(address, *, strict=True)

   Interpreta *address* -- la cual debe ser el valor de un campo que
   contenga un campo tal como *To* o *Cc* -- para separarlo en sus
   componentes *realname* y *email address*. Retorna una tupla de
   información, a menos que la interpretación falle, en cuyo caso una
   2-tupla de "('','')" es retornada.

   If *strict* is true, use a strict parser which rejects malformed
   inputs.

   Distinto en la versión 3.13: Add *strict* optional parameter and
   reject malformed inputs by default.

email.utils.formataddr(pair, charset='utf-8')

   El inverso de "parseaddr()", este toma una 2-tupla de la forma
   "(realname,real, email_address)" y retorna una cadena de caracteres
   válido para una cabecera *To* o *Cc*. Si el primer elemento de
   *pair* es falso, entonces el segundo elemento es retornado sin
   modificación.

   El *charset* opcional es el conjunto de caracteres que será usado
   en la codificación **RFC 2047** del "real_name" si el "real_name"
   contiene caracteres que no sean ASCII. Puede ser una instancia de
   "str" o "Charset". El valor predeterminado es "utf-8".

   Distinto en la versión 3.3: Se añadió la opción *charset*.

email.utils.getaddresses(fieldvalues, *, strict=True)

   This method returns a list of 2-tuples of the form returned by
   "parseaddr()". *fieldvalues* is a sequence of header field values
   as might be returned by "Message.get_all".

   If *strict* is true, use a strict parser which rejects malformed
   inputs.

   Here's a simple example that gets all the recipients of a message:

      from email.utils import getaddresses

      tos = msg.get_all('to', [])
      ccs = msg.get_all('cc', [])
      resent_tos = msg.get_all('resent-to', [])
      resent_ccs = msg.get_all('resent-cc', [])
      all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs)

   Distinto en la versión 3.13: Add *strict* optional parameter and
   reject malformed inputs by default.

email.utils.parsedate(date)

   Intenta interpretar una fecha de acuerdo a las reglas en **RFC
   2822**. Sin embargo, algunos clientes de correo no siguen ese
   formato como está especificado, por lo cual "parsedate()" intenta
   adivinar correctamente en esos casos. *date* es una secuencia de
   caracteres que contiene una fecha **RFC 2822** como ""Mon, 20 Nov
   1995 19:12:08 -0500"". Si tiene éxito en interpretar la fecha,
   "parsedate()" retorna una 9-tupla que puede ser pasada directamente
   a "time.mktime()"; de lo contrario "None" es retornado. Observar
   que los índices 6,7 y 8 de la tupla resultante no son utilizables.

email.utils.parsedate_tz(date)

   Realiza la misma función que "parsedate()", pero retorna "None" o
   una 10-tupla; los primeros 9 elementos forman una tupla que puede
   ser pasada directamente a "time.mktime()", y el décimo es el
   desfase de la zona horaria de la fecha con respecto a UTC (que es
   el término oficial para Greenwich Mean Time) [1]. Si la cadena de
   caracteres de entrada no tiene zona horaria, el último elemento de
   la tupla retornada es "0", el cual representa UTC. Nótese que los
   índices 6, 7 y 8 de la tupla resultante no son utilizables.

email.utils.parsedate_to_datetime(date)

   Lo inverso de "format_datetime()". Realiza la misma función que
   "parsedate()", pero en caso de éxito retorna un "datetime"; de lo
   contrario, "ValueError" se lanza si *date* contiene un valor no
   válido, como una hora superior a 23 o una diferencia de zona
   horaria no comprendida entre -24 y 24 horas. Si la fecha de entrada
   tiene una zona horaria de "-0000", el "datetime" será un "datetime"
   ingenuo, y si la fecha se ajusta a las RFC, representará una hora
   en UTC pero sin indicación de la zona horaria de origen real del
   mensaje de donde proviene la fecha. . Si la fecha de entrada tiene
   cualquier otra compensación de zona horaria válida, el "datetime"
   será un "datetime" consciente con el correspondiente "timezone"
   "tzinfo".

   Added in version 3.3.

email.utils.mktime_tz(tuple)

   Cambia una 10-tupla, como la retornada por "parsedate_tz()" a una
   marca de tiempo UTC (segundos desde la Época). Si la zona horaria
   en la tupla es "None", asume el tiempo local.

email.utils.formatdate(timeval=None, localtime=False, usegmt=False)

   Retorna una fecha como una cadena de caracteres de acuerdo a **RFC
   2822**, por ejemplo:

      Fri, 09 Nov 2001 01:08:47 -0000

   Optional *timeval* if given is a floating-point time value as
   accepted by "time.gmtime()" and "time.localtime()", otherwise the
   current time is used.

   *localtime* opcional, es una bandera que cuando es "True",
   interpreta *timeval* y retorna una fecha relativa a la zona horaria
   local en lugar de UTC, tomando apropiadamente en cuenta el horario
   de verano. El valor predeterminado es "False" con lo cual UTC es
   utilizado.

   *usegmt* opcional, es una bandera que cuando es "True" retorna una
   fecha como cadena de caracteres con la zona horaria como una cadena
   de caracteres ascii "GMT", en lugar de un numérico "-0000". Esto es
   necesario para algunos protocolos (como HTTP). Sólo aplica cuando
   *localtime* es "False". El valor predeterminado es "False".

email.utils.format_datetime(dt, usegmt=False)

   Similar a "formatdate", pero la entrada es una instancia
   "datetime". Si es un datetime naíf, se asume ser "UTC sin
   información sobre la zona horaria de origen", y el "-0000"
   convencional es usado para la zona horaria. Si es un "datetime"
   consciente entonces el desfase numérico de la zona horaria es
   utilizado. Si es una zona horaria consciente con un desfase cero,
   entonces *usegmt* puede ser "True", en cuyo caso la cadena de
   caracteres "GMT" es utilizada en lugar del desfase numérico de zona
   horaria. Esto provee una manera de generar cabeceras de fecha HTTP
   conforme estándares.

   Added in version 3.3.

email.utils.decode_rfc2231(s)

   Decodifica la cadena de caracteres *s* de acuerdo a **RFC 2231**.

email.utils.encode_rfc2231(s, charset=None, language=None)

   Codifica la cadena de caracteres *s* de acuerdo a **RFC 2231**.
   *charset* y *language* opcionales, si son dados es el conjunto de
   caracteres y nombre del lenguaje a utilizar. Si ninguno es dado,
   *s* es retornado sin modificar. Si *charset* es dado pero
   *language* no, la cadena de caracteres es codificada usando la
   cadena de  caracteres vacía para *language*.

email.utils.collapse_rfc2231_value(value, errors='replace', fallback_charset='us-ascii')

   Cuando un parámetro de cabecera está codificado en formato **RFC
   2231**, "Message.get_param" puede retornar una 3-tupla conteniendo
   el conjunto de caracteres, lenguaje y valor.
   "collapse_rfc2231_value()" convierte esto en una cadena de
   caracteres unicode. El parámetro opcional *errors* es pasado al
   argumento *errors* del método "encode()" de "str"; de manera
   predeterminada recae en "'replace'". *fallback_charset* opcional,
   especifica el conjunto de caracteres a utilizar si el especificado
   en la cabecera **RFC 2231** no es conocido por Python; su valor
   predeterminado es "'us-ascii'".

   Por conveniencia, si el *value* pasado a "collapse_rfc2231_value()"
   no es una tupla, debería ser una cadena de caracteres y se retorna
   sin citar.

email.utils.decode_params(params)

   Decodifica la lista de parámetros de acuerdo a **RFC 2231**.
   *params* es una secuencia de 2-tuplas conteniendo elementos de la
   forma "(content-type, string-value)".

-[ Notas a pie de página ]-

[1] Nótese que el signo del desfase de la zona horaria es opuesto al
    signo de la variable "time.timezone" para la misma zona horaria;
    este último sigue el estándar POSIX mientras que este módulo sigue
    **RFC 2822**.
