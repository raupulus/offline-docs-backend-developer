---
title: '"xml.sax" --- Support for SAX2 parsers'
source_url: https://docs.python.org/es/3
source_path: library/xml.sax.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4630
---

# "xml.sax" --- Support for SAX2 parsers

**Código fuente:** Lib/xml/sax/__init__.py

======================================================================

The "xml.sax" package provides a number of modules which implement the
Simple API for XML (SAX) interface for Python.  The package itself
provides the SAX exceptions and the convenience functions which will
be most used by users of the SAX API.

Nota:

  If you need to parse untrusted or unauthenticated data, see XML
  security.

Distinto en la versión 3.7.1: El analizador SAX ya no procesa
entidades generales externas por defecto para incrementar seguridad.
Antes, el analizador creaba conexiones de red para buscar archivos
remotos o archivos locales cargados del sistema de archivos para DTD y
entidades. La característica puede ser activadas de nuevo con el
método "setFeature()" en el objeto analizador y el argumento
"feature_external_ges".

Las funciones de conveniencia son:

xml.sax.make_parser(parser_list=[])

   Crea y retorna un objeto SAX "XMLReader".  El primer analizador
   encontrado será el que se use.  Si se provee *parser_list*, debe
   ser un iterable de cadenas de caracteres el cual nombra módulos que
   tienen una función llamada "créate_parser()".  Los módulos listados
   en *parser_list* serán usados antes de los módulos en la lista de
   analizadores por defecto.

   Distinto en la versión 3.8: El argumento *parser_list* puede ser
   cualquier iterable, no sólo una lista.

xml.sax.parse(filename_or_stream, handler, error_handler=handler.ErrorHandler())

   Crea un analizador SAD y úsalo para analizar un documento.  El
   documento, aprobado como *filename_or_steam*, puede ser un nombre
   de archivo o un objeto de archivo.  El parámetro *handler* necesita
   ser una instancia SAX "ContentHandler".  Si se da *error_handler*,
   debe ser una instancia "ErrorHandler" SAX; si es omitido, se
   lanzará "SAXParseException" en todos los errores. No hay valor
   retornado; toda tarea debe ser realizada por el *handler* aprobado.

xml.sax.parseString(string, handler, error_handler=handler.ErrorHandler())

   Similar a "parser()", pero analiza desde un búfer *string* recibido
   como un parámetro.  *string* debe ser una instancia "str" o un
   *bytes-like object*.

   Distinto en la versión 3.5: Agregado soporte de instancias "str".

Una aplicación SAX típica usa tres tipos de objetos: lectores,
gestores y fuentes de entrada.  "Lector" en este contexto es otro
término para analizador, por ejemplo, alguna pieza de código que lee
los bytes o caracteres de la fuente de entrada, y produce una
secuencia de eventos. Los eventos luego se distribuyen a los objetos
gestores, por ejemplo el lector invoca un método en el gestor.  Una
aplicación SAX debe por tanto obtener un objeto lector, crear o abrir
una fuente de entrada, crear los gestores, y conectar esos objetos
juntos.  Como paso final de preparación, el lector es llamado para
analizar la entrada. Durante el análisis, los métodos en los objetos
gestores son llamados basados en eventos estructurales y sintácticos
de los datos introducidos.

For these objects, only the interfaces are relevant; they are normally
not instantiated by the application itself.  Since Python does not
have an explicit notion of interface, they are formally introduced as
classes, but applications may use implementations which do not inherit
from the provided classes.  The "InputSource", "Locator",
"Attributes", "AttributesNS", and "XMLReader" interfaces are defined
in the module "xml.sax.xmlreader".  The handler interfaces are defined
in "xml.sax.handler".  For convenience, "InputSource" (which is often
instantiated directly) and the handler classes are also available from
"xml.sax".  These interfaces are described below.

In addition to these classes, "xml.sax" provides the following
exception classes.

exception xml.sax.SAXException(msg, exception=None)

   Encapsula un error XML o advertencia.  Esta clase puede contener
   errores básicos o información de advertencias ya sea para el
   analizador XML o la aplicación: esto puede ser heredado para
   proveer funcionalidad adicionar o para agregar localización.  Nota
   que a pesar de los analizadores definidos en la interfaz
   "ErrorHandler" recibe instancias de esta excepción, no es requerido
   para lanzar la excepción --- esto es algo útil como un contenedor
   para información.

   Cuando es instanciado, *msg* debería ser una descripción del error
   legible para humanos. El parámetro opcional *exception*, si es
   dado, debería ser "None" o una excepción que fue atrapada por el
   código analizador y se transmite como información.

   Esta es la clase base para las otras clases excepción SAX.

exception xml.sax.SAXParseException(msg, exception, locator)

   Subclase de "SAXException" levantada en errores de análisis. Las
   instancias de esta clase son pasadas a los métodos de las
   interfaces SAX "ErrorHandler" para proveer información sobre el
   error de análisis.  Esta clase soporta la interfaz SAX "Locator"
   así como la interfaz "SAXException".

exception xml.sax.SAXNotRecognizedException(msg, exception=None)

   Subclase de "SAXException" lanzada cuando una SAX "XMLReader" es
   confrontada con una propiedad o característica no reconocida.  Las
   aplicaciones SAX y extensiones pueden usar esta clase para
   propósitos similares.

exception xml.sax.SAXNotSupportedException(msg, exception=None)

   Las subclases de "SAXException" se lanzan cuando un SAX "sax" se
   pregunta para habilitar una característica que no tiene soporte, o
   para establecer una propiedad a un valor que la implementación no
   da soporte.  Las aplicaciones sAX y las extensiones pueden usar
   esta clase para propósitos similares.

Ver también:

  SAX: The Simple API for XML
     Este sitio es el punto focal para la definición de la API SAX.
     Provee una implementación Java y documentación en línea.  Los
     enlaces para implementaciones e información histórica también
     están disponibles.

  Módulo "xml.sax.handler"
     Definiciones de las interfaces para objetos proporcionados por
     aplicaciones.

  Módulo "xml.sax.saxutils"
     Funciones de conveniencia para usar en aplicaciones SAX.

  Módulo "xml.sax.xmlreader"
     Definiciones de las interfaces para objetos que proveen
     analizadores.

## Objetos SAXException

La clase de excepción "SAXException" da soporte a los siguientes
métodos:

SAXException.getMessage()

   Retorna un mensaje legible para humanos describiendo la condición
   de error.

SAXException.getException()

   Retorna un objeto excepción encapsulado, o "None".
