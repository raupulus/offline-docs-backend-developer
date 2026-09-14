---
title: '"email.headerregistry": Custom Header Objects'
source_url: https://docs.python.org/es/3
source_path: library/email.headerregistry.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2460
---

# "email.headerregistry": Custom Header Objects

**Código fuente:** Lib/email/headerregistry.py

======================================================================

Added in version 3.6: [1]

Los encabezados están representados por subclases personalizadas de
"str". La clase particular utilizada para representar un encabezado
dado está determinada por "header_factory" del "policy" vigente cuando
se crean los encabezados. Esta sección documenta el "header_factory"
particular implementado por el paquete de correo electrónico para el
manejo mensajes de correo electrónico compatibles con **RFC 5322**,
que no solo proporciona objetos de encabezado personalizados para
varios tipos de encabezados, sino que también proporciona un mecanismo
de extensión para que las aplicaciones agreguen sus propios tipos de
encabezados personalizados.

Cuando se utiliza cualquiera de los objetos de política derivados de
"EmailPolicy", todos los encabezados son producidos por
"HeaderRegistry" y tienen "BaseHeader" como su última clase base. Cada
clase de encabezado tiene una clase base adicional que está
determinada por el tipo de encabezado. Por ejemplo, muchos encabezados
tienen la clase "UnstructuredHeader" como su otra clase base. La
segunda clase especializada para un encabezado está determinada por el
nombre del encabezado, utilizando una tabla de búsqueda almacenada en
"HeaderRegistry". Todo esto se gestiona de forma transparente para el
programa de aplicación típico, pero se proporcionan interfaces para
modificar el comportamiento predeterminado para su uso por
aplicaciones más complejas.

Las secciones a continuación primero documentan las clases base de
encabezados y sus atributos, seguidas por la API para modificar el
comportamiento de "HeaderRegistry", y finalmente las clases de soporte
utilizadas para representar los datos analizados a partir de
encabezados estructurados.

class email.headerregistry.BaseHeader(name, value)

   *name* y *value* se pasan a "BaseHeader" desde la llamada
   "header_factory". El valor de cadena de caracteres de cualquier
   objeto de encabezado es el *value* completamente descodificado en
   unicode.

   Esta clase base define las siguientes propiedades de solo lectura:

   name

      El nombre del encabezado (la parte del campo antes del ':').
      Este es exactamente el valor pasado en "header_factory" llamada
      para *name*; es decir, se conserva el caso.

   defects

      Una tupla de instancias "HeaderDefect" que informan sobre
      cualquier problema de cumplimiento de RFC que se encuentre
      durante el análisis. El paquete de correo electrónico intenta
      estar completo para detectar problemas de cumplimiento. Vea el
      módulo "errors" para una discusión de los tipos de defectos que
      pueden ser reportados.

   max_count

      El número máximo de encabezados de este tipo que pueden tener el
      mismo "name". Un valor de "None" significa ilimitado. El valor
      de "BaseHeader" para este atributo es "None"; se espera que las
      clases de encabezado especializadas anulen este valor según sea
      necesario.

   "BaseHeader" también proporciona el siguiente método, que es
   llamado por el código de la biblioteca de correo electrónico y, en
   general, no debe ser llamado por programas de aplicación:

   fold(*, policy)

      Retorna una cadena que contenga "linesep" caracteres según sea
      necesario para doblar correctamente el encabezado de acuerdo con
      *policy*. Un atributo "cte_type" de "8bit" se tratará como si
      fuera "7bit", ya que los encabezados no pueden contener datos
      binarios arbitrarios. Si "utf8" es "False", los datos no ASCII
      estarán codificados **RFC 2047**.

   "BaseHeader" por sí solo no se puede utilizar para crear un objeto
   de encabezado. Define un protocolo con el que coopera cada
   encabezado especializado para producir el objeto de encabezado.
   Específicamente, "BaseHeader" requiere que la clase especializada
   proporcione un "classmethod()" llamado "parse". Este método se
   llama de la siguiente manera:

      parse(string, kwds)

   "kwds" is a dictionary containing one pre-initialized key,
   "defects". "defects" is an empty list.  The parse method should
   append any detected defects to this list.  On return, the "kwds"
   dictionary *must* contain values for at least the keys "decoded",
   "defects" and "parse_tree". "decoded" should be the string value
   for the header (that is, the header value fully decoded to
   unicode). "parse_tree" is set to the parse tree obtained from
   parsing the header. The parse method should assume that *string*
   may contain content-transfer-encoded parts, but should correctly
   handle all valid unicode characters as well so that it can parse
   un-encoded header values.

   Entonces, el "__new__" de "BaseHeader" crea la instancia del
   encabezado y llama a su método "init". La clase especializada solo
   necesita proporcionar un método "init" si desea establecer
   atributos adicionales más allá de los proporcionados por
   "BaseHeader". Tal método "init" debería verse así:

      def init(self, /, *args, **kw):
          self._myattr = kw.pop('myattr')
          super().init(*args, **kw)

   Es decir, cualquier cosa adicional que la clase especializada ponga
   en el diccionario "kwds" debe eliminarse y manejarse, y el
   contenido restante de "kw" (y "args") debe pasar "BaseHeader" al
   método "init".

class email.headerregistry.UnstructuredHeader

   Un encabezado "sin estructura" es el tipo predeterminado de
   encabezado en **RFC 5322**. Cualquier encabezado que no tenga una
   sintaxis especificada se trata como no estructurado. El ejemplo
   clásico de un encabezado no estructurado es el encabezado
   *Subject*.

   En **RFC 5322**, un encabezado no estructurado es una ejecución de
   texto arbitrario en el conjunto de caracteres ASCII. **RFC 2047**,
   sin embargo, tiene un mecanismo compatible **RFC 5322** para
   codificar texto no ASCII como caracteres ASCII dentro de un valor
   de encabezado. Cuando un *value* que contiene palabras codificadas
   se pasa al constructor, el analizador "UnstructuredHeader"
   convierte dichas palabras codificadas en unicode, siguiendo las
   reglas **RFC 2047** para texto no estructurado. El analizador
   utiliza heurística para intentar decodificar ciertas palabras
   codificadas no compatibles. Los defectos se registran en tales
   casos, así como defectos por problemas como caracteres no válidos
   dentro de las palabras codificadas o el texto no codificado.

   Este tipo de encabezado no proporciona atributos adicionales.

class email.headerregistry.DateHeader

   **RFC 5322** especifica un formato muy específico para las fechas
   dentro de los encabezados de correo electrónico. El analizador
   "DateHeader" reconoce ese formato de fecha, además de reconocer una
   serie de formas variantes que a veces se encuentran "en la
   naturaleza" (*"in the wild"*).

   Este tipo de encabezado proporciona los siguientes atributos
   adicionales:

   datetime

      Si el valor del encabezado puede reconocerse como una fecha
      válida de una forma u otra, este atributo contendrá una
      instancia "datetime" que representa esa fecha. Si la zona
      horaria de la fecha de entrada se especifica como "-0000" (lo
      que indica que está en UTC pero no contiene información sobre la
      zona horaria de origen), entonces "datetime" será un ingenuo
      "datetime". Si se encuentra un desplazamiento de zona horaria
      específico (incluido "+0000"), entonces "datetime" contendrá un
      "datetime" consciente que usa "datetime.timezone" para registrar
      el desplazamiento de la zona horaria.

   El valor "decoded" del encabezado se determina formateando la
   "datetime" de acuerdo con las reglas **RFC 5322**; es decir, esto
   se establece en:

      email.utils.format_datetime(self.datetime)

   Al crear un "DateHeader", *value* puede ser "datetime" instancia.
   Esto significa, por ejemplo, que el siguiente código es válido y
   hace lo que cabría esperar:

      msg['Date'] = datetime(2011, 7, 15, 21)

   Debido a que se trata de una "datetime" naif, se interpretará como
   una marca de tiempo UTC, y el valor resultante tendrá una zona
   horaria de "-0000". Mucho más útil es usar la función "localtime()"
   del módulo "utils":

      msg['Date'] = utils.localtime()

   Este ejemplo establece el encabezado de la fecha en la hora y fecha
   actuales utilizando el desplazamiento de zona horaria actual.

class email.headerregistry.AddressHeader

   Los encabezados de dirección son uno de los tipos de encabezados
   estructurados más complejos. La clase "AddressHeader" proporciona
   una interfaz genérica para cualquier encabezado de dirección.

   Este tipo de encabezado proporciona los siguientes atributos
   adicionales:

   groups

      Una tupla de objetos "Group" que codifican las direcciones y los
      grupos que se encuentran en el valor del encabezado. Las
      direcciones que no forman parte de un grupo se representan en
      esta lista como "Groups" de una sola dirección cuyo
      "display_name" es "None".

   addresses

      Una tupla de objetos "Address" que codifican todas las
      direcciones individuales del valor del encabezado. Si el valor
      del encabezado contiene algún grupo, las direcciones
      individuales del grupo se incluyen en la lista en el punto donde
      el grupo aparece en el valor (es decir, la lista de direcciones
      se "aplana" (*"flattened"*) en una lista unidimensional).

   El valor "decoded" del encabezado tendrá todas las palabras
   codificadas decodificadas a Unicode. Los nombres de dominio
   codificados "idna" también se decodifican en Unicode. El valor
   "decoded" se establece concatenando el valor "str" de los elementos
   del atributo "groups" con "', '".

   Se puede utilizar una lista de objetos "Address" y "Group" en
   cualquier combinación para establecer el valor de un encabezado de
   dirección. Los objetos "Group" cuyo "display_name" sea "None" se
   interpretarán como direcciones únicas, lo que permite copiar una
   lista de direcciones con los grupos intactos utilizando la lista
   obtenida del atributo "groups" de el encabezado de origen.

class email.headerregistry.SingleAddressHeader

   Una subclase de "AddressHeader" que agrega un atributo adicional:

   address

      La única dirección codificada por el valor del encabezado. Si el
      valor del encabezado en realidad contiene más de una dirección
      (lo que sería una violación del RFC bajo el valor predeterminado
      "policy"), acceder a este atributo resultará en un "ValueError".

Muchas de las clases anteriores también tienen una variante "Unique"
(por ejemplo,``UniqueUnstructuredHeader``). La única diferencia es que
en la variante "Unique", "max_count" se establece en 1.

class email.headerregistry.MIMEVersionHeader

   En realidad, solo hay un valor válido para el encabezado *MIME-
   Version*, y ese es "1.0". Para pruebas futuras, esta clase de
   encabezado admite otros números de versión válidos. Si un número de
   versión tiene un valor válido por **RFC 2045**, entonces el objeto
   de encabezado tendrá valores distintos de "None" para los
   siguientes atributos:

   version

      El número de versión como una cadena de caracteres, con
      cualquier espacio en blanco y/o comentarios eliminados.

   major

      El número de versión mayor como un entero

   minor

      El número de versión menor como un entero

class email.headerregistry.ParameterizedMIMEHeader

   Todos los encabezados *MIME* comienzan con el prefijo *'Content-'*.
   Cada encabezado específico tiene un valor determinado, que se
   describe en la clase de ese encabezado. Algunos también pueden
   tomar una lista de parámetros complementarios, que tienen un
   formato común. Esta clase sirve como base para todos los
   encabezados *MIME* que toman parámetros.

   params

      Un diccionario que asigna nombres de parámetros a valores de
      parámetros.

class email.headerregistry.ContentTypeHeader

   Una clase "ParameterizedMIMEHeader" que maneja el encabezado
   *Content-Type*.

   content_type

      La cadena de caracteres de tipo de contenido, en la forma
      "maintype/subtype".

   maintype

   subtype

class email.headerregistry.ContentDispositionHeader

   Una clase "ParameterizedMIMEHeader" que maneja el encabezado
   *Content-Disposition*.

   content_disposition

      "inline" y "attachment" son los únicos valores válidos de uso
      común.

class email.headerregistry.ContentTransferEncodingHeader

   Maneja el encabezado de *Content-Transfer-Encoding*.

   cte

      Los valores válidos son "7bit", "8bit", "base64", y "quoted-
      printable". Consulte **RFC 2045** para obtener más información.

class email.headerregistry.HeaderRegistry(base_class=BaseHeader, default_class=UnstructuredHeader, use_default_map=True)

   This is the factory used by "EmailPolicy" by default.
   "HeaderRegistry" builds the class used to create a header instance
   dynamically, using *base_class* and a specialized class retrieved
   from a registry that it holds.  When a given header name does not
   appear in the registry, the class specified by *default_class* is
   used as the specialized class.  When *use_default_map* is "True"
   (the default), the standard mapping of header names to classes is
   copied in to the registry during initialization.  *base_class* is
   always the last class in the generated class's "__bases__" list.

   Las asignaciones predeterminadas son:

      subject:
         UniqueUnstructuredHeader

      date:
         UniqueDateHeader

      resent-date:
         DateHeader

      orig-date:
         UniqueDateHeader

      sender:
         UniqueSingleAddressHeader

      resent-sender:
         SingleAddressHeader

      to:
         UniqueAddressHeader

      resent-to:
         AddressHeader

      cc:
         UniqueAddressHeader

      resent-cc:
         AddressHeader

      bcc:
         UniqueAddressHeader

      resent-bcc:
         AddressHeader

      from:
         UniqueAddressHeader

      resent-from:
         AddressHeader

      reply-to:
         UniqueAddressHeader

      mime-version:
         MIMEVersionHeader

      content-type:
         ContentTypeHeader

      content-disposition:
         ContentDispositionHeader

      content-transfer-encoding:
         ContentTransferEncodingHeader

      message-id:
         MessageIDHeader

   "HeaderRegistry" tiene los siguientes métodos:

   map_to_type(self, name, cls)

      *name* es el nombre del encabezado que se asignará. Se
      convertirá a minúsculas en el registro. *cls* es la clase
      especializada que se utilizará, junto con *base_class*, para
      crear la clase utilizada para instanciar encabezados que
      coincidan con *name*.

   __getitem__(name)

      Construye y retorna una clase para manejar la creación de un
      encabezado *nombre*.

   __call__(name, value)

      Recupera el encabezado especializado asociado con *name* del
      registro (usando *default_class* si *name* no aparece en el
      registro) y lo compone con *base_class* para producir una clase,
      llama al constructor de la clase construida, pasándole el mismo
      lista de argumentos y, finalmente, retorna la instancia de clase
      creada de ese modo.

Las siguientes clases son las clases que se utilizan para representar
datos analizados a partir de encabezados estructurados y, en general,
pueden ser utilizadas por un programa de aplicación para construir
valores estructurados para asignar a encabezados específicos.

class email.headerregistry.Address(display_name='', username='', domain='', addr_spec=None)

   La clase utilizada para representar una dirección de correo
   electrónico. La forma general de una dirección es:

      [display_name] <username@domain>

   or:

      username@domain

   donde cada parte debe ajustarse a reglas de sintaxis específicas
   explicadas en **RFC 5322**.

   Para su comodidad, se puede especificar *addr_spec* en lugar de
   *username* y *domain*, en cuyo caso *username* y *domain* se
   analizarán a partir de *addr_spec*. Un *addr_spec* debe ser una
   cadena de caracteres entre comillas RFC adecuada; si no es
   "Address", se lanzará un error. Se permiten caracteres Unicode y se
   codificarán como propiedad cuando se serialicen. Sin embargo, según
   las RFC, *no* se permite unicode en la parte del nombre de usuario
   de la dirección.

   display_name

      La parte del nombre para mostrar de la dirección, si la hubiera,
      con todas las citas eliminadas. Si la dirección no tiene un
      nombre para mostrar, este atributo será una cadena vacía.

   username

      La parte del "username" de la dirección, con todas las citas
      eliminadas.

   domain

      La parte de "domain" de la dirección.

   addr_spec

      La parte de la dirección "username@domain", citada correctamente
      para usarla como dirección simple (el segundo formulario que se
      muestra arriba). Este atributo no es mutable.

   __str__()

      El valor "str" del objeto es la dirección citada de acuerdo con
      las reglas **RFC 5322**, pero sin codificación de transferencia
      de contenido de ningún carácter que no sea ASCII.

   Para admitir SMTP (**RFC 5321**), "Address" maneja un caso
   especial: si "username" y "domain" son ambos la cadena de
   caracteres vacía (o "None"), entonces el valor de cadena de
   caracteres "Address" es "<>".

class email.headerregistry.Group(display_name=None, addresses=None)

   La clase utilizada para representar un grupo de direcciones. La
   forma general de un grupo de direcciones es:

      display_name: [address-list];

   Para facilitar el procesamiento de listas de direcciones que
   constan de una mezcla de grupos y direcciones únicas, también se
   puede utilizar un "Group" para representar direcciones únicas que
   no forman parte de un grupo al establecer *display_name* en "None"
   y proporcionando una lista de direcciones únicas como *addresses*.

   display_name

      El "display_name" del grupo. Si es "None" y hay exactamente una
      "Address" en "addresses", entonces el "Group" representa una
      única dirección que no está en un grupo.

   addresses

      Posiblemente una tupla vacía de "Address" que representan las
      direcciones en el grupo.

   __str__()

      El valor "str" de un "Group" se formatea de acuerdo con **RFC
      5322**, pero sin codificación de transferencia de contenido de
      ningún carácter que no sea ASCII. Si "display_name" no es
      ninguno y hay una sola "Address" en la lista de "addresses", el
      valor de "str" será el mismo que el "str" de ese single
      "Address".

-[ Pie de notas ]-

[1] Originalmente añadido en 3.3 como módulo provisional *provisional
    module*
