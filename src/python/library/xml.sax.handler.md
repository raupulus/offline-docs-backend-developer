---
title: '"xml.sax.handler" --- Base classes for SAX handlers'
source_url: https://docs.python.org/es/3
source_path: library/xml.sax.handler.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4610
---

# "xml.sax.handler" --- Base classes for SAX handlers

**Source code** Lib/xml/sax/handler.py

======================================================================

The SAX API defines five kinds of handlers: content handlers, DTD
handlers, error handlers, entity resolvers and lexical handlers.
Applications normally only need to implement those interfaces whose
events they are interested in; they can implement the interfaces in a
single object or in multiple objects. Handler implementations should
inherit from the base classes provided in the module
"xml.sax.handler", so that all methods get default implementations.

class xml.sax.handler.ContentHandler

   Esta es la principal interfaz de devolución de llamada en el SAX, y
   la más importante para las aplicaciones. El orden de los eventos en
   esta interfaz refleja el orden de la información en el documento.

class xml.sax.handler.DTDHandler

   Manejar eventos de DTD.

   Esta interfaz especifica solo los eventos DTD necesarios para el
   análisis básico (entidades y atributos no analizados).

class xml.sax.handler.EntityResolver

   Interfaz básica para resolver entidades. Si creas un objeto
   implementando esta interfaz, y luego registras el objeto con tu
   Parser, el parser (analizador) invocara al método en tu objeto para
   resolver todas las entidades externas.

class xml.sax.handler.ErrorHandler

   Interfaz utilizada por el parser para presentar mensajes de error y
   advertencia a la aplicación.  Los métodos de este objeto controlan
   si los errores se convierten inmediatamente en excepciones o se
   manejan de alguna otra manera.

class xml.sax.handler.LexicalHandler

   Interface usada por el parser para representar eventos de baja
   frecuencia que pueden no ser de interés para muchas aplicaciones.

In addition to these classes, "xml.sax.handler" provides symbolic
constants for the feature and property names.

xml.sax.handler.feature_namespaces

      value: ""http://xml.org/sax/features/namespaces""
      true: Realizar el procesamiento del Namespace (espacio de nombres).
      false: Opcionalmente no realizar el procesamiento del Namespace (espacio de nombres) (implica prefijos de espacio de nombres; por defecto).
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.feature_namespace_prefixes

      value: ""http://xml.org/sax/features/namespace-prefixes""
      true: Reporte de los nombres prefijados originales y los atributos utilizados para las declaraciones del Namespace (espacio de nombres).
      false: No informar de los atributos utilizados para las declaraciones del Namespace (espacio de nombres), y opcionalmente no informar de los nombres prefijados originales (por defecto).
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.feature_string_interning

      value: ""http://xml.org/sax/features/string-interning""
      true: Todos los nombres de elementos, prefijos, nombres de atributos, URIs del Namespace (espacio de nombres) y nombres locales son internados usando la función interna incorporada.
      false: Los nombres no están necesariamente internados, aunque pueden estarlo (por defecto).
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.feature_validation

      value: ""http://xml.org/sax/features/validation""
      true: Reportar de todos los errores de validación (implica entidades generales externas y entidades de parámetros externos).
      false: No informe de los errores de validación.
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.feature_external_ges

   Advertencia:

     Enabling opens a vulnerability to external entity attacks if the
     parser is used with user-provided XML content. Please reflect on
     your threat model before enabling this feature.

      value: ""http://xml.org/sax/features/external-parameter-entities""
      true: Incluye todas las entidades externas generales de texto (text).
      false: No incluya entidades generales externas.
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.feature_external_pes

      value: ""http://xml.org/sax/features/external-parameter-entities""
      true: Incluye todas las entidades paramétricas externas, incluyendo el subconjunto DTD externo.
      false: No incluya ninguna entidad paramétrica externa, ni siquiera el subconjunto DTD externo.
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.all_features

   Lista de todas las características.

xml.sax.handler.property_lexical_handler

      value: ""http://xml.org/sax/properties/lexical-handler""
      data type: xml.sax.sax2lib.LexicalHandler (no soportado en Python 2)
      descripción: Un  handler (manipulador) de extensión opcional para eventos léxicos como los comentarios.
      acceso: read/write (leer/escribir)

xml.sax.handler.property_declaration_handler

      value: ""http://xml.org/sax/properties/declaration-handler""
      data type: xml.sax.sax2lib.DeclHandler (no soportado en Python 2)
      description: Un gestor de extensión opcional para eventos relacionados con la DTD que no sean anotaciones y entidades no preparadas.
      acceso: read/write (leer/escribir)

xml.sax.handler.property_dom_node

      value: ""http://xml.org/sax/properties/dom-node""
      data type: org.w3c.dom.Node (not supported in Python 2)
      descripción: Cuando se analiza, el nodo DOM actual que se visita si se trata de un iterador DOM; cuando no se analiza, el nodo DOM raíz para la iteración.
      acceso: (parsing) solo de lectura; (not parsing) lectura/escritura

xml.sax.handler.property_xml_string

      value: ""http://xml.org/sax/properties/xml-string""
      tipo de datos: Bytes
      description: La cadena literal de caracteres que fue la fuente del evento actual.
      acceso: solo-lectura

xml.sax.handler.all_properties

   Lista de todos los nombres de propiedades conocidas.

## Objetos ContentHandler

Se espera que los usuarios subclasifiquen "ContentHandler" para apoyar
su aplicación.  Los siguientes métodos son llamados por el analizador
en los eventos apropiados en el documento de entrada:

ContentHandler.setDocumentLocator(locator)

   Invocado por el parser (analizador) para dar a la aplicación un
   localizador para determinar el origen de los eventos del documento.

   Se recomienda encarecidamente a los parsers (analizadores) SAX
   (aunque no es absolutamente necesario) que proporcionen un
   localizador: si lo hace, debe proporcionar el localizador a la
   aplicación invocando este método antes de invocar cualquiera de los
   otros métodos de la interfaz DocumentHandler.

   El localizador permite a la aplicación determinar la posición final
   de cualquier evento relacionado con el documento, incluso si el
   analizador no informa de un error. Normalmente, la aplicación
   utilizará esta información para informar de sus propios errores
   (como el contenido de los caracteres que no coinciden con las
   reglas de negocio de la aplicación). Es probable que la información
   retornada por el localizador no sea suficiente para su uso con un
   motor de búsqueda.

   Tenga en cuenta que el localizador retornará la información
   correcta solo durante la invocación de los eventos en esta
   interfaz. La aplicación no debe intentar utilizarlo en ningún otro
   momento.

ContentHandler.startDocument()

   Recibir la notificación del inicio de un documento.

   El parser (analizador) SAX invocará este método solo una vez, antes
   que cualquier otro método en esta interfaz o en DTDHandler (excepto
   "setDocumentLocator()").

ContentHandler.endDocument()

   Recibir una notificación del final de un documento.

   El analizador (parser) SAX invocará este método solo una vez, y
   será el último método invocado durante el análisis. El analizador
   no invocará este método hasta que no haya abandonado el análisis
   sintáctico (debido a un error irrecuperable) o haya llegado al
   final de la entrada.

ContentHandler.startPrefixMapping(prefix, uri)

   Comienza el alcance de un mapeo del prefijo-URI Namespace.

   La información de este evento no es necesaria para el procesamiento
   normal del Namespace (espacio de nombres): el lector de XML SAX
   sustituirá automáticamente los prefijos de los nombres de elementos
   y atributos cuando se active la función "feature_namespaces"
   default (el valor por defecto).

   Sin embargo, hay casos en que las aplicaciones necesitan utilizar
   prefijos en los datos de los caracteres o en los valores de los
   atributos, en los que no se pueden expandir automáticamente de
   forma segura; los eventos "startPrefixMapping()" y
   "endPrefixMapping()" suministran la información a la aplicación
   para expandir los prefijos en esos contextos por sí mismos, si es
   necesario.

   Note que los eventos "startPrefixMapping()" y "endPrefixMapping()"
   no están garantizados de estar apropiadamente anidados en relación
   a cada uno: todos los eventos "startPrefixMapping()" ocurrirán
   antes del correspondiente evento "startElement()", y todos los
   eventos "endPrefixMapping()" ocurrirán después del correspondiente
   evento "endElement()", pero su orden no está garantizado.

ContentHandler.endPrefixMapping(prefix)

   Terminar con el alcance de un mapeo de prefijos-URI.

   Ver "startPrefixMapping()" para más detalles. Este evento siempre
   ocurrirá después del correspondiente evento "endElement()", pero el
   orden de los eventos "endPrefixMapping()" no está garantizado.

ContentHandler.startElement(name, attrs)

   Señala el inicio de un elemento en modo no espacial.

   The *name* parameter contains the raw XML 1.0 name of the element
   type as a string and the *attrs* parameter holds an object of the
   Attributes interface containing the attributes of the element.  The
   object passed as *attrs* may be re-used by the parser; holding on
   to a reference to it is not a reliable way to keep a copy of the
   attributes. To keep a copy of the attributes, use the "copy()"
   method of the *attrs* object.

ContentHandler.endElement(name)

   Señala el final de un elemento en modo no espacial.

   El parámetro *name* contiene el nombre del tipo de elemento, al
   igual que con el evento "startElement()".

ContentHandler.startElementNS(name, qname, attrs)

   Señala el inicio de un elemento en el modo de Namespace (espacio de
   nombres).

   The *name* parameter contains the name of the element type as a
   "(uri, localname)" tuple, the *qname* parameter contains the raw
   XML 1.0 name used in the source document, and the *attrs* parameter
   holds an instance of the AttributesNS interface containing the
   attributes of the element.  If no namespace is associated with the
   element, the *uri* component of *name* will be "None".  The object
   passed as *attrs* may be re-used by the parser; holding on to a
   reference to it is not a reliable way to keep a copy of the
   attributes.  To keep a copy of the attributes, use the "copy()"
   method of the *attrs* object.

   Los parsers (analizadores) pueden establecer el parámetro *qname*
   como "None", a menos que se active la función
   "feature_namespace_prefixes".

ContentHandler.endElementNS(name, qname)

   Señala el final de un elemento en el modo de namespace.

   El parámetro *name* contiene el nombre del tipo de elemento, al
   igual que con el método "startElementNS()", así como el parámetro
   *qname*.

ContentHandler.characters(content)

   Recibir la notificación de los datos de los caracteres.

   El Parser (analizador) llamará a este método para informar de cada
   dato de carácter. Los parsers (analizadores) SAX pueden retornar
   todos los datos de caracteres contiguos en un solo trozo, o pueden
   dividirlos en varios trozos; sin embargo, todos los caracteres de
   un mismo evento deben provenir de la misma entidad externa para que
   el Localizador proporcione información útil.

   **content**  puede ser una cadena o una instancia de bytes; el
   módulo lector de "Expat" siempre produce cadenas.

   Nota:

     La anterior interfaz SAX 1 proporcionada por el Grupo de Interés
     Especial de Python XML utilizaba una interfaz más parecida a Java
     para este método.  Dado que la mayoría de los parsers
     (analizadores) utilizados de Python no aprovecharon la interfaz
     más antigua, se eligió la firma más simple para reemplazarla.
     Para convertir el código antiguo en la nueva interfaz, se utilizó
     *content* en lugar de cortar el contenido con los antiguos
     parámetros *offset* y *length*.

ContentHandler.ignorableWhitespace(whitespace)

   Recibir notificación de espacios en blanco ignorables en el
   contenido de los elementos.

   Los parsers  validadores deben utilizar este método para informar
   de cada trozo de espacio en blanco desconocido (véase la
   recomendación W3C XML 1.0, sección 2.10): los analizadores no
   validadores también pueden utilizar este método si son capaces de
   analizar y utilizar modelos de contenido.

   Los parsers (analizadores) SAX pueden retornar todos los espacios
   blancos contiguos en un solo trozo, o pueden dividirlo en varios
   trozos; sin embargo, todos los caracteres de un mismo evento deben
   provenir de la misma entidad externa, para que el Localizador
   proporcione información útil.

ContentHandler.processingInstruction(target, data)

   Recibir la notificación de una instrucción de procesamiento.

   El Parser (analizador) invocará este método una vez por cada
   instrucción de procesamiento encontrada: nótese que las
   instrucciones de procesamiento pueden ocurrir antes o después del
   elemento principal del documento.

   Un parser (analizador) SAX nunca debe informar de una declaración
   XML (XML 1.0, sección 2.8) o una declaración de texto (XML 1.0,
   sección 4.3.1) utilizando este método.

ContentHandler.skippedEntity(name)

   Recibir la notificación de una entidad salteada.

   El Parser invocará este método una vez por cada entidad omitida.
   Los procesos no validadores pueden omitir entidades si no han visto
   las declaraciones (porque, por ejemplo, la entidad fue declarada en
   un subconjunto DTD externo). Todos los procesos pueden omitir
   entidades externas, dependiendo de los valores de las propiedades
   "feature_external_ges" y "feature_external_pes".

## Objetos DTDHandler

"DTDHandler" la instancia provee los siguientes métodos:

DTDHandler.notationDecl(name, publicId, systemId)

   Manejar un evento de declaración de anotación.

DTDHandler.unparsedEntityDecl(name, publicId, systemId, ndata)

   Manejar un evento de declaración de entidad no preparada.

## Objetos EntityResolver

EntityResolver.resolveEntity(publicId, systemId)

   Resolver el identificador de sistema de una entidad y retornar ya
   sea el identificador de sistema para leerlo como una cadena, o una
   fuente de entrada para leerlo. La implementación por defecto
   retorna *systemId*.

## Objetos ErrorHandler

Los objetos con esta interfaz se usan para recibir información de
error y advertencia del "XMLReader".  Si creas un objeto que
implemente esta interfaz, y luego registras el objeto con tu
"XMLReader", el parser (analizador) invocará a los métodos de tu
objeto para informar de todas las advertencias y errores. Hay tres
niveles de errores disponibles: advertencias, errores (posiblemente)
recuperables y errores no recuperables.  Todos los métodos toman un
"SAXParseException" como único parámetro.  Los errores y advertencias
pueden ser convertidos en una excepción lanzando el objeto de
excepción pasado.

ErrorHandler.error(exception)

   Invocación cuando el parser (analizador) encuentra un error
   recuperable.  Si este método no lanza una excepción, el análisis
   sintáctico puede continuar, pero la aplicación no debe esperar más
   información del documento.  Permitir que el parser (analizador)
   continúe puede permitir que se descubran errores adicionales en el
   documento de entrada.

ErrorHandler.fatalError(exception)

   Invocación cuando el parser (analizador) encuentra un error del que
   no puede recuperarse; se espera que el análisis sintáctico termine
   cuando vuelva este método.

ErrorHandler.warning(exception)

   Invocación cuando el parser (analizador) presenta información de
   advertencia menor a la aplicación. Se espera que el análisis
   sintáctico continúe cuando vuelva este método, y la información del
   documento seguirá pasando a la aplicación. Si se lanza una
   excepción con este método, el análisis sintáctico terminará.

## Objetos DTDHandler

Handler (manipulador) de extensión opcional para eventos léxicos SAX2.

Este handler se usa para obtener información léxica de un documento
XML. La información léxica incluye información que describe la
codificación del documento usado u los comentarios XML embebidos en el
documento, como también una sección para el DTD y para cada sección
CDTA. Estos manipuladores léxicos son usado de la misma forma que los
manipuladores de contenido (content handlers).

Configurar el LexicalHandlerde un XMLReader usando el método
setProperty con la propiedad identificadora
"'http://xml.org/sax/properties/lexical-handler'".

LexicalHandler.comment(content)

   Reporta un comentario en cualquier lugar en el documento
   (incluyendo el DTD y elementos por fuera del documento).

LexicalHandler.startDTD(name, public_id, system_id)

   Reporta el estado de las declaraciones del DTD en caso de tenga
   asociado un DTD.

LexicalHandler.endDTD()

   Reporta el fin de la declaración del DTD.

LexicalHandler.startCDATA()

   Reporta el inicio de la sección CDATA marcada.

   El contenido de la sección marcada del CDATA se reportará a través
   de manipulador de caracteres.

LexicalHandler.endCDATA()

   Reporta el final de la sección marcada del CDATA.
