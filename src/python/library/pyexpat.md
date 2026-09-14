---
title: '"xml.parsers.expat" --- Fast XML parsing using Expat'
source_url: https://docs.python.org/es/3
source_path: library/pyexpat.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3590
---

# "xml.parsers.expat" --- Fast XML parsing using Expat

======================================================================

Nota:

  If you need to parse untrusted or unauthenticated data, see XML
  security.

The "xml.parsers.expat" module is a Python interface to the Expat non-
validating XML parser. The module provides a single extension type,
"xmlparser", that represents the current state of an XML parser.
After an "xmlparser" object has been created, various attributes of
the object can be set to handler functions.  When an XML document is
then fed to the parser, the handler functions are called for the
character data and markup in the XML document.

Este módulo utiliza el módulo "pyexpat" para proporcionar acceso al
analizador Expat.  El uso directo del módulo "pyexpat" está obsoleto.

Este módulo proporciona una excepción y un tipo de objeto:

exception xml.parsers.expat.ExpatError

   La excepción que se lanza cuando Expat informa un error.  Consulte
   la sección Excepciones de ExpatError para obtener más información
   sobre cómo interpretar los errores de Expat.

exception xml.parsers.expat.error

   Alias para "ExpatError".

xml.parsers.expat.XMLParserType

   El tipo de los valores de retorno de la función "ParserCreate()".

The "xml.parsers.expat" module contains two functions:

xml.parsers.expat.ErrorString(errno)

   Retorna una cadena explicativa para un número de error dado
   *errno*.

xml.parsers.expat.ParserCreate(encoding=None, namespace_separator=None)

   Crea y retorna un nuevo objeto "xmlparser".  *encoding*, si se
   especifica, debe ser una cadena que nombre la codificación
   utilizada  por los datos XML.  Expat no admite tantas
   codificaciones como Python, y su repertorio de codificaciones no se
   puede ampliar; es compatible con UTF-8, UTF-16, ISO-8859-1 (Latin1)
   y ASCII.  Si se proporciona *encoding* [1], anulará la codificación
   implícita o explícita del documento.

   Parsers created through "ParserCreate()" are called "root" parsers,
   in the sense that they do not have any parent parser attached. Non-
   root parsers are created by "parser.ExternalEntityParserCreate".

   Expat puede, opcionalmente, realizar el procesamiento del espacio
   de nombres XML por usted, habilitado al proporcionar un valor para
   *namespace_separator*.  El valor debe ser una cadena de un
   carácter; a "ValueError" se lanzará si la cadena tiene una longitud
   ilegal ("None" se considera lo mismo que una omisión).  Cuando el
   procesamiento de espacios de nombres está habilitado, se expandirán
   los nombres de tipos de elementos y los nombres de atributos que
   pertenecen a un espacio de nombres.  El nombre del elemento pasado
   a los controladores de elementos "StartElementHandler" y
   "EndElementHandler" será la concatenación del URI del espacio de
   nombres, el carácter separador del espacio de nombres y la parte
   local del nombre.  Si el separador del espacio de nombres es un
   byte cero ("chr(0)"), el URI del espacio de nombres y la parte
   local se concatenarán sin ningún separador.

   Por ejemplo, si *namespace_separator* se establece en un carácter
   de espacio ("' '") y se analiza el siguiente documento:

      <?xml version="1.0"?>
      <root xmlns    = "http://default-namespace.org/"
            xmlns:py = "http://www.python.org/ns/">
        <py:elem1 />
        <elem2 xmlns="" />
      </root>

   "StartElementHandler" recibirá las siguientes cadenas para cada
   elemento:

      http://default-namespace.org/ root
      http://www.python.org/ns/ elem1
      elem2

   Debido a las limitaciones en la biblioteca "Expat" utilizada por
   "pyexpat", la instancia "xmlparser" retorna solo se puede usar para
   analizar un solo documento XML.  Llame a "ParserCreate" para cada
   documento para proporcionar instancias de analizador únicas.

Ver también:

  El Expat XML Parser
     Página de inicio del proyecto Expat.

## Objetos XMLParser

Los objetos "xmlparser" tienen los siguientes métodos:

xmlparser.Parse(data[, isfinal])

   Analiza el contenido de la cadena *data*, llamando a las funciones
   del controlador apropiadas para procesar los datos analizados.
   *isfinal* debe ser verdadero en la última llamada a este método;
   permite el análisis de un solo archivo en fragmentos, no el envío
   de varios archivos. *data* puede ser la cadena vacía en cualquier
   momento.

xmlparser.ParseFile(file)

   Analizar la lectura de datos XML del objeto *file*.  *file* solo
   necesita proporcionar el método "read(nbytes)", devolviendo la
   cadena vacía cuando no hay más datos.

xmlparser.SetBase(base)

   Establece la base que se utilizará para resolver URIs relativos en
   identificadores de sistema en declaraciones.  La resolución de los
   identificadores relativos se deja en manos de la aplicación: este
   valor se pasará como el argumento *base* a las funciones
   "ExternalEntityRefHandler()", "NotationDeclHandler()", y
   "UnparsedEntityDeclHandler()".

xmlparser.GetBase()

   Retorna una cadena que contiene la base establecida por una llamada
   anterior a "SetBase()", o "None" si no se ha llamado a
   "SetBase()".

xmlparser.GetInputContext()

   Retorna los datos de entrada que generaron el evento actual como
   una cadena. Los datos están en la codificación de la entidad que
   contiene el texto. Cuando se llama mientras un controlador de
   eventos no está activo, el valor de retorno es "None".

xmlparser.ExternalEntityParserCreate(context[, encoding])

   Cree un analizador "child" que se pueda utilizar para analizar una
   entidad analizada externa a la que hace referencia el contenido
   analizado por el analizador principal.  El parámetro *context* debe
   ser la cadena pasada a la función del controlador
   "ExternalEntityRefHandler()", que se describe a continuación. El
   analizador secundario se crea con "order_attributes" y
   "specific_attributes" establecidos en los valores de este
   analizador.

xmlparser.SetParamEntityParsing(flag)

   Controle el análisis de las entidades de parámetros (incluido el
   subconjunto DTD externo). Los posibles valores de *flag* son
   "XML_PARAM_ENTITY_PARSING_NEVER",
   "XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE" y
   "XML_PARAM_ENTITY_PARSING_ALWAYS".  Retorna verdadero si el
   establecimiento de la bandera fue exitoso.

xmlparser.UseForeignDTD([flag])

   Llamar a esto con un valor verdadero para *flag* (el
   predeterminado) hará que Expat llame a "ExternalEntityRefHandler"
   con "None" para todos los argumentos para permitir que se cargue
   una DTD alternativa. Si el documento no contiene una declaración de
   tipo de documento, se seguirá llamando a
   "ExternalEntityRefHandler", pero no se llamará a
   "StartDoctypeDeclHandler" y "EndDoctypeDeclHandler".

   Pasar un valor falso para *flag* cancelará una llamada anterior que
   pasó un valor verdadero, pero por lo demás no tiene ningún efecto.

   Este método sólo se puede llamar antes de que se llamen los métodos
   "Parse()" o "ParseFile()"; llamarlo después de que cualquiera de
   ellos haya sido llamado causa que "ExpatError" se lanza con el
   atributo "code" establecido en
   "errors.codes[errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING]".

xmlparser.SetReparseDeferralEnabled(enabled)

   Advertencia:

     Calling "SetReparseDeferralEnabled(False)" has security
     implications, as detailed below; please make sure to understand
     these consequences prior to using the "SetReparseDeferralEnabled"
     method.

   Expat 2.6.0 introduced a security mechanism called "reparse
   deferral" where instead of causing denial of service through
   quadratic runtime from reparsing large tokens, reparsing of
   unfinished tokens is now delayed by default until a sufficient
   amount of input is reached. Due to this delay, registered handlers
   may — depending of the sizing of input chunks pushed to Expat — no
   longer be called right after pushing new input to the parser.
   Where immediate feedback and taking over responsibility of
   protecting against denial of service from large tokens are both
   wanted, calling "SetReparseDeferralEnabled(False)" disables reparse
   deferral for the current Expat parser instance, temporarily or
   altogether. Calling "SetReparseDeferralEnabled(True)" allows re-
   enabling reparse deferral.

   Note that "SetReparseDeferralEnabled()" has been backported to some
   prior releases of CPython as a security fix.  Check for
   availability of "SetReparseDeferralEnabled()" using "hasattr()" if
   used in code running across a variety of Python versions.

   Added in version 3.13.

xmlparser.GetReparseDeferralEnabled()

   Returns whether reparse deferral is currently enabled for the given
   Expat parser instance.

   Added in version 3.13.

"xmlparser" objects have the following methods to tune protections
against some common XML vulnerabilities.

xmlparser.SetBillionLaughsAttackProtectionActivationThreshold(threshold, /)

   Sets the number of output bytes needed to activate protection
   against billion laughs attacks.

   The number of output bytes includes amplification from entity
   expansion and reading DTD files.

   Parser objects usually have a protection activation threshold of 8
   MiB, but the actual default value depends on the underlying Expat
   library.

   An "ExpatError" is raised if this method is called on a non-root
   parser. The corresponding "lineno" and "offset" should not be used
   as they may have no special meaning.

   Nota:

     Activation thresholds below 4 MiB are known to break support for
     DITA 1.3 payload and are hence not recommended.

   Added in version 3.14.6.

xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification(max_factor, /)

   Sets the maximum tolerated amplification factor for protection
   against billion laughs attacks.

   The amplification factor is calculated as "(direct + indirect) /
   direct" while parsing, where "direct" is the number of bytes read
   from the primary document in parsing and "indirect" is the number
   of bytes added by expanding entities and reading of external DTD
   files.

   The *max_factor* value must be a non-NaN "float" value greater than
   or equal to 1.0. Peak amplifications of factor 15,000 for the
   entire payload and of factor 30,000 in the middle of parsing have
   been observed with small benign files in practice. In particular,
   the activation threshold should be carefully chosen to avoid false
   positives.

   Parser objects usually have a maximum amplification factor of 100,
   but the actual default value depends on the underlying Expat
   library.

   An "ExpatError" is raised if this method is called on a non-root
   parser or if *max_factor* is outside the valid range. The
   corresponding "lineno" and "offset" should not be used as they may
   have no special meaning.

   Nota:

     The maximum amplification factor is only considered if the
     threshold that can be adjusted by
     "SetBillionLaughsAttackProtectionActivationThreshold()" is
     exceeded.

   Added in version 3.14.6.

xmlparser.SetAllocTrackerActivationThreshold(threshold, /)

   Sets the number of allocated bytes of dynamic memory needed to
   activate protection against disproportionate use of RAM.

   Parser objects usually have an allocation activation threshold of
   64 MiB, but the actual default value depends on the underlying
   Expat library.

   An "ExpatError" is raised if this method is called on a non-root
   parser. The corresponding "lineno" and "offset" should not be used
   as they may have no special meaning.

   Added in version 3.14.1.

xmlparser.SetAllocTrackerMaximumAmplification(max_factor, /)

   Sets the maximum amplification factor between direct input and
   bytes of dynamic memory allocated.

   The amplification factor is calculated as "allocated / direct"
   while parsing, where "direct" is the number of bytes read from the
   primary document in parsing and "allocated" is the number of bytes
   of dynamic memory allocated in the parser hierarchy.

   The *max_factor* value must be a non-NaN "float" value greater than
   or equal to 1.0. Amplification factors greater than 100.0 can be
   observed near the start of parsing even with benign files in
   practice. In particular, the activation threshold should be
   carefully chosen to avoid false positives.

   Parser objects usually have a maximum amplification factor of 100,
   but the actual default value depends on the underlying Expat
   library.

   An "ExpatError" is raised if this method is called on a non-root
   parser or if *max_factor* is outside the valid range. The
   corresponding "lineno" and "offset" should not be used as they may
   have no special meaning.

   Nota:

     The maximum amplification factor is only considered if the
     threshold that can be adjusted by
     "SetAllocTrackerActivationThreshold()" is exceeded.

   Added in version 3.14.1.

"xmlparser" los objetos tienen los siguientes atributos:

xmlparser.buffer_size

   El tamaño del búfer usado cuando "buffer_text" es verdadero. Se
   puede establecer un nuevo tamaño de búfer asignando un nuevo valor
   entero a este atributo. Cuando se cambia el tamaño, el búfer se
   vaciará.

xmlparser.buffer_text

   Setting this to true causes the "xmlparser" object to buffer
   textual content returned by Expat to avoid multiple calls to the
   "CharacterDataHandler()" callback whenever possible.  This can
   improve performance substantially since Expat normally breaks
   character data into chunks at every line ending.  This attribute is
   false by default, and may be changed at any time. Note that when it
   is false, data that does not contain newlines may be chunked too.

xmlparser.buffer_used

   Si "buffer_text" está habilitado, el número de bytes almacenados en
   el búfer. Estos bytes representan texto codificado en UTF-8.  Este
   atributo no tiene una interpretación significativa cuando
   "buffer_text" es falso.

xmlparser.ordered_attributes

   Establecer este atributo en un número entero distinto de cero hace
   que los atributos se informen como una lista en lugar de un
   diccionario.  Los atributos se presentan en el orden que se
   encuentran en el texto del documento.  Para cada atributo, se
   presentan dos entradas de lista: el nombre del atributo y el valor
   del atributo. (Las versiones anteriores de este módulo también
   usaban este formato). De forma predeterminada, este atributo es
   falso; se puede cambiar en cualquier momento.

xmlparser.specified_attributes

   Si se establece en un número entero distinto de cero, el analizador
   informará solo los atributos que se especificaron en la instancia
   del documento y no los que se derivaron de declaraciones de
   atributos.  Las aplicaciones que establecen esto deben tener
   especial cuidado al utilizar la información adicional disponible en
   las declaraciones según sea necesario para cumplir con los
   estándares para el comportamiento de los procesadores XML.  De
   forma predeterminada, este atributo es falso; se puede cambiar en
   cualquier momento.

Los siguientes atributos contienen valores relacionados con el error
más reciente encontrado por un objeto "xmlparser", y solo tendrán los
valores correctos una vez que una llamada a "Parse()" o "ParseFile()"
haya lanzado una excepción "xml.parsers.expat.ExpatError".

xmlparser.ErrorByteIndex

   Índice de bytes en el que se produjo un error.

xmlparser.ErrorCode

   Código numérico que especifica el problema.  Este valor puede
   pasarse a la función "ErrorString()", o compararse con una de las
   constantes definidas en el objeto "errors".

xmlparser.ErrorColumnNumber

   Número de columna en la que se produjo un error.

xmlparser.ErrorLineNumber

   Número de línea en la que ocurrió un error.

Los siguientes atributos contienen valores relacionados con la
ubicación actual del análisis en un objeto "xmlparser".  Durante una
devolución de llamada que informa un evento de análisis, indican la
ubicación del primero de la secuencia de caracteres que generó el
evento. Cuando se llama fuera de una devolución de llamada, la
posición indicada estará justo después del último evento de análisis
(independientemente de si hubo una devolución de llamada asociada).

xmlparser.CurrentByteIndex

   Índice de bytes actual en la entrada del analizador.

xmlparser.CurrentColumnNumber

   Número de columna actual en la entrada del analizador.

xmlparser.CurrentLineNumber

   Número de línea actual en la entrada del analizador.

Aquí está la lista de controladores que se pueden configurar.  Para
configurar un controlador en un objeto "xmlparser" *o*, use
"o.handlername = func".  *handlername* debe tomarse de la siguiente
lista, y *func* debe ser un objeto invocable que acepte el número
correcto de argumentos.  Los argumentos son todos cadenas, a menos que
se indique lo contrario.

xmlparser.XmlDeclHandler(version, encoding, standalone)

   Se llama cuando se analiza la declaración XML.  La declaración XML
   es la declaración (opcional) de la versión aplicable de la
   recomendación XML, la codificación del texto del documento y una
   declaración "independiente" opcional. *version* y *encoding* serán
   cadenas, y *standalone* será "1" si el documento se declara
   independiente, "0" si se declara no independiente o "-1" si se
   omitió la cláusula independiente. Esto solo está disponible con la
   versión Expat 1.95.0 o más reciente.

xmlparser.StartDoctypeDeclHandler(doctypeName, systemId, publicId, has_internal_subset)

   Called when Expat begins parsing the document type declaration
   ("<!DOCTYPE ...").  The *doctypeName* is provided exactly as
   presented.  The *systemId* and *publicId* parameters give the
   system and public identifiers if specified, or "None" if omitted.
   *has_internal_subset* will be true if the document contains an
   internal document declaration subset. This requires Expat version
   1.2 or newer.

xmlparser.EndDoctypeDeclHandler()

   Se llama cuando Expat termina de analizar la declaración del tipo
   de documento. Esto requiere Expat versión 1.2 o más reciente.

xmlparser.ElementDeclHandler(name, model)

   Se llama una vez para cada declaración de tipo de elemento.  *name*
   es el nombre del tipo de elemento y *model* es una representación
   del modelo de contenido.

xmlparser.AttlistDeclHandler(elname, attname, type, default, required)

   Se llama para cada atributo declarado para un tipo de elemento.  Si
   una declaración de lista de atributos declara tres atributos, este
   controlador se llama tres veces, una para cada atributo.  *elname*
   es el nombre del elemento al que se aplica la declaración y
   *attname* es el nombre del atributo declarado.  El tipo de atributo
   es una cadena pasada como *type*; los valores posibles son
   "'CDATA'", "'ID'", "'IDREF'", ... *default* da el valor
   predeterminado para el atributo utilizado cuando el atributo no
   está especificado por el instancia de documento, o "None" si no hay
   un valor predeterminado (valores "#IMPLIED"). Si se requiere que el
   atributo se proporcione en la instancia del documento, *required*
   será verdadero. Esto requiere la versión Expat 1.95.0 o más
   reciente.

xmlparser.StartElementHandler(name, attributes)

   Llamado para el inicio de cada elemento.  *name* es una cadena que
   contiene el nombre del elemento, y *attributes* son los atributos
   del elemento. Si "order_attributes" es verdadero, esta es una lista
   (ver "order_attributes" para una descripción completa). De lo
   contrario, es un diccionario que asigna nombres a valores.

xmlparser.EndElementHandler(name)

   Llamado al final de cada elemento.

xmlparser.ProcessingInstructionHandler(target, data)

   Llamado para cada instrucción de procesamiento.

xmlparser.CharacterDataHandler(data)

   Called for character data.  This will be called for normal
   character data, CDATA marked content, and ignorable whitespace.
   Applications which must distinguish these cases can use the
   "StartCdataSectionHandler", "EndCdataSectionHandler", and
   "ElementDeclHandler" callbacks to collect the required information.
   Note that the character data may be chunked even if it is short and
   so you may receive more than one call to "CharacterDataHandler()".
   Set the "buffer_text" instance attribute to "True" to avoid that.

xmlparser.UnparsedEntityDeclHandler(entityName, base, systemId, publicId, notationName)

   Se llama para declaraciones de entidad sin analizar (NDATA).  Esto
   solo está presente para la versión 1.2 de la biblioteca Expat; para
   versiones más recientes, use "EntityDeclHandler" en su lugar.  (La
   función subyacente en la biblioteca Expat se ha declarado
   obsoleta).

xmlparser.EntityDeclHandler(entityName, is_parameter_entity, value, base, systemId, publicId, notationName)

   Llamado para todas las declaraciones de entidad.  Para parámetros y
   entidades internas, *value* será una cadena que proporciona el
   contenido declarado de la entidad; esto será "None" para entidades
   externas.  El parámetro *notationName* será "None" para las
   entidades analizadas y el nombre de la notación para las entidades
   no analizadas. *is_parameter_entity* será verdadero si la entidad
   es una entidad de parámetro o falso para las entidades generales
   (la mayoría de las aplicaciones solo deben preocuparse por las
   entidades generales). Esto solo está disponible a partir de la
   versión 1.95.0 de la biblioteca Expat.

xmlparser.NotationDeclHandler(notationName, base, systemId, publicId)

   Se llama para declaraciones de notación.  *notationName*, *base* y
   *systemId* y *publicId* son cadenas si se dan.  Si se omite el
   identificador público, *publicId* será "None".

xmlparser.StartNamespaceDeclHandler(prefix, uri)

   Se llama cuando un elemento contiene una declaración de espacio de
   nombres.  Las declaraciones de espacio de nombres se procesan antes
   de que se llame a "StartElementHandler" para el elemento en el que
   se colocan las declaraciones.

xmlparser.EndNamespaceDeclHandler(prefix)

   Se llama cuando se alcanza la etiqueta de cierre para un elemento
   que contiene una declaración de espacio de nombres.  Esto se llama
   una vez para cada declaración de espacio de nombres en el elemento
   en el orden inverso al que se llamó "StartNamespaceDeclHandler"
   para indicar el inicio del alcance de cada declaración de espacio
   de nombres.  Las llamadas a este controlador se realizan después
   del correspondiente "EndElementHandler" para el final del elemento.

xmlparser.CommentHandler(data)

   Llamado para comentarios.  *data* es el texto del comentario,
   excluyendo el "'<!-""-'" inicial y el final "'-""->'".

xmlparser.StartCdataSectionHandler()

   Llamado al comienzo de una sección CDATA.  Esto y
   "EndCdataSectionHandler" son necesarios para poder identificar el
   inicio sintáctico y el final de las secciones CDATA.

xmlparser.EndCdataSectionHandler()

   Llamado al final de una sección CDATA.

xmlparser.DefaultHandler(data)

   Se invoca por cualquier carácter del documento XML para el que no
   se ha especificado ningún controlador aplicable.  Esto significa
   caracteres que forman parte de una construcción que se podría
   informar, pero para los que no se ha proporcionado ningún
   controlador.

xmlparser.DefaultHandlerExpand(data)

   Es lo mismo que "DefaultHandler()", pero no inhibe la expansión de
   entidades internas. La referencia de la entidad no se pasará al
   controlador predeterminado.

xmlparser.NotStandaloneHandler()

   Se llama si el documento XML no se ha declarado como un documento
   independiente. Esto sucede cuando hay un subconjunto externo o una
   referencia a una entidad de parámetro, pero la declaración XML no
   establece independiente en "yes" en una declaración XML.  Si este
   controlador retorna "0", el analizador lanzará un error
   "XML_ERROR_NOT_STANDALONE".  Si este controlador no está
   configurado, el analizador no lanza ninguna excepción para esta
   condición.

xmlparser.ExternalEntityRefHandler(context, base, systemId, publicId)

   Advertencia:

     Implementing a handler that accesses local files and/or the
     network may create a vulnerability to external entity attacks if
     "xmlparser" is used with user-provided XML content. Please
     reflect on your threat model before implementing this handler.

   Llamado para referencias a entidades externas.  *base* es la base
   actual, según lo establecido por una llamada anterior a
   "SetBase()".  Los identificadores público y del sistema, *systemId*
   y *publicId*, son cadenas si se dan; si no se proporciona el
   identificador público, *publicId* será "None".  El valor *context*
   es opaco y solo debe usarse como se describe a continuación.

   Para que se analicen las entidades externas, se debe implementar
   este controlador. Es responsable de crear el sub-analizador usando
   "ExternalEntityParserCreate(context)", inicializándolo con las
   devoluciones de llamada apropiadas y analizando la entidad.  Este
   controlador debería devolver un número entero; si retorna "0", el
   analizador lanzará un error "XML_ERROR_EXTERNAL_ENTITY_HANDLING";
   de lo contrario, el análisis continuará.

   Si no se proporciona este controlador, las entidades externas se
   informan mediante la devolución de llamada "DefaultHandler", si se
   proporciona.

## Excepciones de ExpatError

Las excepciones "ExpatError" tienen una serie de atributos
interesantes:

ExpatError.code

   Número de error interno del expatriado para el error específico.
   El diccionario "errors.messages" asigna estos números de error a
   los mensajes de error de Expat.  Por ejemplo:

      from xml.parsers.expat import ParserCreate, ExpatError, errors

      p = ParserCreate()
      try:
          p.Parse(some_xml_document)
      except ExpatError as err:
          print("Error:", errors.messages[err.code])

   El módulo "errors" también proporciona constantes de mensajes de
   error y un diccionario "codes" mapeando estos mensajes a los
   códigos de error, ver más abajo.

ExpatError.lineno

   Número de línea en la que se detectó el error.  La primera línea
   está numerada como "1".

ExpatError.offset

   Carácter desplazado en la línea donde ocurrió el error.  La primera
   columna está numerada como "0".

## Ejemplo

El siguiente programa define tres controladores que simplemente
imprimen sus argumentos.

   import xml.parsers.expat

   # 3 handler functions
   def start_element(name, attrs):
       print('Start element:', name, attrs)
   def end_element(name):
       print('End element:', name)
   def char_data(data):
       print('Character data:', repr(data))

   p = xml.parsers.expat.ParserCreate()

   p.StartElementHandler = start_element
   p.EndElementHandler = end_element
   p.CharacterDataHandler = char_data

   p.Parse("""<?xml version="1.0"?>
   <parent id="top"><child1 name="paul">Text goes here</child1>
   <child2 name="fred">More text</child2>
   </parent>""", 1)

La salida de este programa es:

   Start element: parent {'id': 'top'}
   Start element: child1 {'name': 'paul'}
   Character data: 'Text goes here'
   End element: child1
   Character data: '\n'
   Start element: child2 {'name': 'fred'}
   Character data: 'More text'
   End element: child2
   Character data: '\n'
   End element: parent

## Descripciones del modelo de contenido

Los modelos de contenido se describen mediante tuplas anidadas.  Cada
tupla contiene cuatro valores: el tipo, el cuantificador, el nombre y
una tupla de niños.  Los niños son simplemente descripciones
adicionales del modelo de contenido.

The values of the first two fields are constants defined in the
"xml.parsers.expat.model" module.  These constants can be collected in
two groups: the model type group and the quantifier group.

Las constantes en el grupo de tipos de modelo son:

xml.parsers.expat.model.XML_CTYPE_ANY

   Se declaró que el elemento nombrado por el nombre del modelo tiene
   un modelo de contenido de "ANY".

xml.parsers.expat.model.XML_CTYPE_CHOICE

   El elemento nombrado permite elegir entre varias opciones; se
   utiliza para modelos de contenido como "(A | B | C)".

xml.parsers.expat.model.XML_CTYPE_EMPTY

   Los elementos que se declaran "EMPTY" tienen este tipo de modelo.

xml.parsers.expat.model.XML_CTYPE_MIXED

xml.parsers.expat.model.XML_CTYPE_NAME

xml.parsers.expat.model.XML_CTYPE_SEQ

   Los modelos que representan una serie de modelos que siguen uno
   tras otro se indican con este tipo de modelo.  Se utiliza para
   modelos como "(A, B, C)".

Las constantes en el grupo cuantificador son:

xml.parsers.expat.model.XML_CQUANT_NONE

   No se proporciona ningún modificador, por lo que puede aparecer
   exactamente una vez, como para "A".

xml.parsers.expat.model.XML_CQUANT_OPT

   El modelo es opcional: puede aparecer una vez o no aparecer, como
   para "A?".

xml.parsers.expat.model.XML_CQUANT_PLUS

   El modelo debe aparecer una o más veces (como "A+").

xml.parsers.expat.model.XML_CQUANT_REP

   El modelo debe aparecer cero o más veces, como en "A*".

## Constantes de error de expansión

The following constants are provided in the "xml.parsers.expat.errors"
module.  These constants are useful in interpreting some of the
attributes of the "ExpatError" exception objects raised when an error
has occurred. Since for backwards compatibility reasons, the
constants' value is the error *message* and not the numeric error
*code*, you do this by comparing its "code" attribute with
"errors.codes[errors.XML_ERROR_*CONSTANT_NAME*]".

El módulo "errors" tiene los siguientes atributos:

xml.parsers.expat.errors.codes

   Un diccionario que asigna descripciones de cadenas a sus códigos de
   error.

   Added in version 3.2.

xml.parsers.expat.errors.messages

   Un diccionario que asigna códigos de error numéricos a sus
   descripciones de cadenas.

   Added in version 3.2.

xml.parsers.expat.errors.XML_ERROR_ASYNC_ENTITY

xml.parsers.expat.errors.XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF

   Una referencia de entidad en un valor de atributo se refiere a una
   entidad externa en lugar de una entidad interna.

xml.parsers.expat.errors.XML_ERROR_BAD_CHAR_REF

   Una referencia de carácter se refiere a un carácter que es ilegal
   en XML (por ejemplo, carácter "0", o '"&#0;"').

xml.parsers.expat.errors.XML_ERROR_BINARY_ENTITY_REF

   Una referencia de entidad se refería a una entidad que se declaró
   con una notación, por lo que no se puede analizar.

xml.parsers.expat.errors.XML_ERROR_DUPLICATE_ATTRIBUTE

   Un atributo se utilizó más de una vez en una etiqueta de inicio.

xml.parsers.expat.errors.XML_ERROR_INCORRECT_ENCODING

xml.parsers.expat.errors.XML_ERROR_INVALID_TOKEN

   Se lanza cuando un byte de entrada no se puede asignar
   correctamente a un carácter; por ejemplo, un byte NUL (valor "0")
   en un flujo de entrada UTF-8.

xml.parsers.expat.errors.XML_ERROR_JUNK_AFTER_DOC_ELEMENT

   Se produjo algo diferente a los espacios en blanco después del
   elemento del documento.

xml.parsers.expat.errors.XML_ERROR_MISPLACED_XML_PI

   Se encontró una declaración XML en algún lugar que no sea el
   comienzo de los datos de entrada.

xml.parsers.expat.errors.XML_ERROR_NO_ELEMENTS

   El documento no contiene elementos (XML requiere que todos los
   documentos contengan exactamente un elemento de nivel superior)..

xml.parsers.expat.errors.XML_ERROR_NO_MEMORY

   Expat no pudo asignar memoria internamente.

xml.parsers.expat.errors.XML_ERROR_PARAM_ENTITY_REF

   Se encontró una referencia de entidad de parámetro donde no estaba
   permitida.

xml.parsers.expat.errors.XML_ERROR_PARTIAL_CHAR

   Se encontró un carácter incompleto en la entrada.

xml.parsers.expat.errors.XML_ERROR_RECURSIVE_ENTITY_REF

   Una referencia de entidad contenía otra referencia a la misma
   entidad; posiblemente a través de un nombre diferente, y
   posiblemente indirectamente.

xml.parsers.expat.errors.XML_ERROR_SYNTAX

   Se encontró algún error de sintaxis no especificado.

xml.parsers.expat.errors.XML_ERROR_TAG_MISMATCH

   Una etiqueta final no coincidía con la etiqueta inicial abierta más
   interna.

xml.parsers.expat.errors.XML_ERROR_UNCLOSED_TOKEN

   Algún token (como una etiqueta de inicio) no se cerró antes del
   final de la transmisión o se encontró el siguiente token.

xml.parsers.expat.errors.XML_ERROR_UNDEFINED_ENTITY

   Se hizo referencia a una entidad que no estaba definida.

xml.parsers.expat.errors.XML_ERROR_UNKNOWN_ENCODING

   La codificación del documento no es compatible con Expat.

xml.parsers.expat.errors.XML_ERROR_UNCLOSED_CDATA_SECTION

   No se cerró una sección marcada con CDATA.

xml.parsers.expat.errors.XML_ERROR_EXTERNAL_ENTITY_HANDLING

xml.parsers.expat.errors.XML_ERROR_NOT_STANDALONE

   El analizador determinó que el documento no era "independiente"
   aunque se declaró en la declaración XML, y el
   "NotStandaloneHandler" se estableció y devolvió "0".

xml.parsers.expat.errors.XML_ERROR_UNEXPECTED_STATE

xml.parsers.expat.errors.XML_ERROR_ENTITY_DECLARED_IN_PE

xml.parsers.expat.errors.XML_ERROR_FEATURE_REQUIRES_XML_DTD

   An operation was requested that requires DTD support to be compiled
   in, but Expat was configured without DTD support.  This should
   never be reported by a standard build of the "xml.parsers.expat"
   module.

xml.parsers.expat.errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING

   Se solicitó un cambio de comportamiento después de que comenzó el
   análisis que solo se puede cambiar antes de que haya comenzado el
   análisis.  Esto (actualmente) solo lanzado por "UseForeignDTD()".

xml.parsers.expat.errors.XML_ERROR_UNBOUND_PREFIX

   Se encontró un prefijo no declarado cuando se habilitó el
   procesamiento del espacio de nombres.

xml.parsers.expat.errors.XML_ERROR_UNDECLARING_PREFIX

   El documento intentó eliminar la declaración de espacio de nombres
   asociada con un prefijo.

xml.parsers.expat.errors.XML_ERROR_INCOMPLETE_PE

   El documento no contenía ningún elemento de documento.

xml.parsers.expat.errors.XML_ERROR_XML_DECL

   El documento no contenía ningún elemento de documento.

xml.parsers.expat.errors.XML_ERROR_TEXT_DECL

   Se produjo un error al analizar una declaración de texto en una
   entidad externa.

xml.parsers.expat.errors.XML_ERROR_PUBLICID

   Se encontraron caracteres en la identificación pública que no están
   permitidos.

xml.parsers.expat.errors.XML_ERROR_SUSPENDED

   La operación solicitada se realizó en un analizador suspendido,
   pero no está permitida.  Esto incluye intentos de proporcionar
   información adicional o detener el analizador.

xml.parsers.expat.errors.XML_ERROR_NOT_SUSPENDED

   Se realizó un intento de reanudar el analizador cuando no se había
   suspendido.

xml.parsers.expat.errors.XML_ERROR_ABORTED

   Esto no se debe informar a las aplicaciones Python.

xml.parsers.expat.errors.XML_ERROR_FINISHED

   La operación solicitada se realizó en un analizador que terminó de
   analizar la entrada, pero no está permitido.  Esto incluye intentos
   de proporcionar información adicional o detener el analizador.

xml.parsers.expat.errors.XML_ERROR_SUSPEND_PE

xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XML

   Se hizo un intento de declarar o remover el prefijo del namespace
   reservado "xml" o de enlazarlo con otro namespace URI.

xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XMLNS

   Se hizo un intento por declarar o remover el prefijo del namespace
   reservado "xmlns".

xml.parsers.expat.errors.XML_ERROR_RESERVED_NAMESPACE_URI

   Se hizo un intento de enlace entre la URI y uno de los prefijos del
   namespace reservado "xml" y "xmlns" a otro prefijo de namespace.

xml.parsers.expat.errors.XML_ERROR_INVALID_ARGUMENT

   Esto no se debe informar a las aplicaciones Python.

xml.parsers.expat.errors.XML_ERROR_NO_BUFFER

   Esto no se debe informar a las aplicaciones Python.

xml.parsers.expat.errors.XML_ERROR_AMPLIFICATION_LIMIT_BREACH

   El límite en el factor de amplificación de entrada (de DTD y
   entidades) ha sido sobrepasada.

xml.parsers.expat.errors.XML_ERROR_NOT_STARTED

   The parser was tried to be stopped or suspended before it started.

   Added in version 3.14.

-[ Notas al pie ]-

[1] La cadena de codificación incluida en la salida XML debe cumplir
    con los estándares apropiados. Por ejemplo, "UTF-8" es válido,
    pero "UTF8" no lo es. Consulte https://www.w3.org/TR/2006/REC-
    xml11-20060816/#NT-EncodingDecl y https://www.iana.org/assignments
    /character-sets/character-sets.xhtml.
