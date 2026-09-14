---
title: '"xml.sax.xmlreader" --- Interface for XML parsers'
source_url: https://docs.python.org/es/3
source_path: library/xml.sax.reader.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4620
---

# "xml.sax.xmlreader" --- Interface for XML parsers

**Código fuente:** Lib/xml/sax/xmlreader.py

======================================================================

Los analizadores SAX implementan la interfaz "XMLReader". Están
implementados en un módulo Python, que debe proveer una función
"create_parser()". Esta función es invocada por
"xml.sax.make_parser()" sin argumentos para crear un nuevo objeto
analizador.

class xml.sax.xmlreader.XMLReader

   Clase base que puede ser heredada por analizadores SAX.

class xml.sax.xmlreader.IncrementalParser

   En algunos casos, es deseable no analizar una fuente de entrada a
   la vez, si no alimentar partes del documento a medida que estén
   disponibles. Tenga en cuenta que el lector normalmente no leerá el
   fichero completo, si no que también lo leerá por partes, aún así
   "parse()" no retornará hasta que el documento por completo es
   procesado. Por lo tanto, estas interfaces deben utilizarse si el
   comportamiento de bloqueo "parse()" no es deseable.

   Cuando se crea una instancia del analizador, está listo para
   comenzar a aceptar información desde el método de alimentación
   inmediatamente. Después de que el análisis ha finalizado con una
   llamada para cerrar, se debe llamar al método de reinicio para que
   el analizador esté listo para aceptar información nueva, ya sea de
   la fuente o utilizando el método de análisis.

   Tenga en cuenta que estos métodos *no* deben ser llamados durante
   el análisis, es decir, después de que el análisis ha sido llamado y
   antes de que regrese.

   Por defecto, la clase también implementa el método de análisis de
   la interfaz XMLReader utilizando los métodos de alimentación,
   cierre y reinicio de la interfaz IncrementalParser en conveniencia
   a los escritores de controlador SAX 2.0.

class xml.sax.xmlreader.Locator

   La interfaz para asociar un evento SAX con una ubicación del
   documento. Un objeto localizador retornará resultados válidos sólo
   durante llamadas a métodos DocumentHandler; en cualquier otro
   momento, los resultados son impredecibles. Si la información no
   está disponible, los métodos pueden retornar "None".

class xml.sax.xmlreader.InputSource(system_id=None)

   La encapsulación de la información necesaria por el "XMLReader"
   para leer entidades.

   Esta clase puede incluir información sobre el identificador
   público, identificador del sistema, flujo de bytes (posiblemente
   con la información de codificación de caracteres) y/o el flujo de
   caracteres de una entidad.

   Las aplicaciones crearán objetos de esta clase para uso en el
   método "XMLReader.parse()" y para retornar desde
   EntityResolver.resolveEntity.

   Una "InputSource" pertenece a la aplicación, el "XMLReader" no
   tiene permitido modificar objetos "InputSource" pasados desde la
   aplicación, a pesar de que puede hacer copias y modificarlas.

class xml.sax.xmlreader.AttributesImpl(attrs)

   Esta es una implementación de la interfaz "Attributes" (vea la
   sección La Interfaz Attributes). Este es un objeto de tipo
   diccionario que representa los atributos de elemento en una llamada
   "startElement()". En adición a las operaciones de diccionario más
   útiles, soporta una serie de otros métodos como se describe en la
   interfaz. Los lectores deben crear una instancia de los objetos de
   esta clase; *attrs* debe ser un objeto de tipo diccionario que
   contenga un mapeo de nombres de atributo a valores de atributo.

class xml.sax.xmlreader.AttributesNSImpl(attrs, qnames)

   Variante consciente del espacio de nombres de "AttributesImpl", que
   se pasará a "startElementNS()". Es derivada de "AttributesImpl",
   pero entiende nombres de atributo como dos tuplas de *namespaceURI*
   y *localname*. En adición, provee una serie de métodos esperando
   nombres calificados como aparecen en el documento original. Esta
   clase implementa la interfaz "AttributesNS" (vea la sección La
   Interfaz AttributesNS).

## Objetos XMLReader

La interfaz "XMLReader" soporta los siguientes métodos:

XMLReader.parse(source)

   Procesa una fuente de entrada, produciendo eventos SAX. El objeto
   *source* puede ser un identificador de sistema (una cadena
   identificando la fuente de entrada -- típicamente un nombre de
   fichero o una URL), un "pathlib.Path" o un objeto *path-like*, o un
   objeto "InputSource". Cuando "parse()" retorna, la entrada es
   procesada completamente, y el objeto analizador puede ser
   descartado o reiniciado.

   Distinto en la versión 3.5: Agregado soporte de flujo de
   caracteres.

   Distinto en la versión 3.8: Agregado soporte de objetos path-like.

XMLReader.getContentHandler()

   Retorna el "ContentHandler" actual.

XMLReader.setContentHandler(handler)

   Establece el "ContentHandler" actual. Si ningún "ContentHandler" es
   establecido, los eventos de contenido serán descartados.

XMLReader.getDTDHandler()

   Retorna el "DTDHandler" actual.

XMLReader.setDTDHandler(handler)

   Establece el "DTDHandler" actual. Si ningún "DTDHandler" es
   establecido, los eventos DTD serán descartados.

XMLReader.getEntityResolver()

   Retorna el "EntityResolver" actual.

XMLReader.setEntityResolver(handler)

   Establece el "EntityResolver" actual. Si ningún "EntityResolver" es
   establecido, los intentos de resolver una entidad externa
   resultarán en la apertura del identificador de sistema para la
   entidad, y un error si no está disponible.

XMLReader.getErrorHandler()

   Retorna el "ErrorHandler" actual.

XMLReader.setErrorHandler(handler)

   Establece el manejador de errores actual. Si ningún "ErrorHandler"
   es establecido, se lanzarán errores como excepciones, y se
   imprimirán alertas.

XMLReader.setLocale(locale)

   Permite a una aplicación establecer la configuración local para
   errores y alertas.

   Analizadores SAX no son requeridos para proveer localización para
   errores y alertas; si no pueden soportar la configuración local
   solicitada, de cualquier forma, lanzarán una excepción SAX. Las
   aplicaciones pueden solicitar un cambio local en medio del
   análisis.

XMLReader.getFeature(featurename)

   Retorna la configuración actual para la característica
   *featurename*. Si la característica no es reconocida,
   "SAXNotRecognizedException" es lanzada. Los bien conocidos
   featurenames son listados en el módulo "xml.sax.handler".

XMLReader.setFeature(featurename, value)

   Establece el *featurename* a *value*. Si la característica no es
   reconocida, "SAXNotRecognizedException" es lanzada. Si la
   característica o su configuración no es soportada por el
   analizador, *SAXNotSupportedException* es lanzada.

XMLReader.getProperty(propertyname)

   Retorna la configuración actual para la propiedad *propertyname*.
   Si la configuración no es reconocida, una
   "SAXNotRecognizedException" es lanzada. Las bien conocidas
   propertynames son listadas en el módulo  "xml.sax.handler".

XMLReader.setProperty(propertyname, value)

   Establece el *propertyname* a *value*. Si la propiedad no es
   reconocida, "SAXNotRecognizedException" es lanzada. Si la propiedad
   o su configuración no es soportada por el analizador,
   *SAXNotSupportedException* es lanzada.

## Objetos IncrementalParser

Las instancias de "IncrementalParser" ofrecen los siguientes métodos
adicionales:

IncrementalParser.feed(data)

   Procesa una parte de *data*.

IncrementalParser.close()

   Asume el fin del documento. Eso verificará las condiciones bien
   formadas que pueden ser verificadas sólo al final, invocar
   manejadores, y puede limpiar los recursos asignados durante el
   análisis.

IncrementalParser.reset()

   Este método es llamado después de que el cierre ha sido llamado
   para restablecer el analizador, de forma que esté listo para
   analizar nuevos documentos. Los resultados de llamar parse o feed
   después del cierre sin llamar a reset son indefinidos.

## Objetos localizadores

Las instancias de "Locator" proveen estos métodos:

Locator.getColumnNumber()

   Retorna el número de columna donde el evento actual comienza.

Locator.getLineNumber()

   Retorna el número de línea donde el evento actual comienza.

Locator.getPublicId()

   Retorna el identificador público para el evento actual.

Locator.getSystemId()

   Retorna el identificador de sistema para el evento actual.

## Objetos InputSource

InputSource.setPublicId(id)

   Establece el identificador público de esta "InputSource".

InputSource.getPublicId()

   Retorna el identificador público para esta "InputSource".

InputSource.setSystemId(id)

   Establece el identificador de sistema de esta "InputSource".

InputSource.getSystemId()

   Retorna el identificador de sistema para esta "InputSource".

InputSource.setEncoding(encoding)

   Establece la codificación de caracteres para esta "InputSource".

   La codificación debe ser una cadena aceptable para una declaración
   de codificación XML (vea la sección 4.3.3 de la recomendación XML).

   El atributo de codificación de la "InputSource" es ignorado si la
   "InputSource" contiene también un flujo de caracteres.

InputSource.getEncoding()

   Obtiene la codificación de caracteres de esta InputSource.

InputSource.setByteStream(bytefile)

   Establece el flujo de bytes (un *binary file*) para esta fuente de
   entrada.

   El analizador SAX ignorará esto si existe también un flujo de
   caracteres especificado, pero utilizará un flujo de bytes en
   preferencia para abrir una conexión URI en sí.

   Si la aplicación conoce la codificación de caracteres del flujo de
   bytes, debería establecerla con el método setEncoding.

InputSource.getByteStream()

   Obtiene el flujo de bytes para esta fuente de entrada.

   El método getEncoding retornará la codificación de caracteres para
   este flujo de bytes, o "None" si se desconoce.

InputSource.setCharacterStream(charfile)

   Establece el flujo de caracteres (un *text file*) para esta fuente
   de entrada.

   Si existe un flujo de caracteres especificado, el analizador SAX
   ignorará cualquier flujo de bytes y no intentará abrir una conexión
   URI al identificador de sistema.

InputSource.getCharacterStream()

   Obtiene el flujo de caracteres para esta fuente de entrada.

## La Interfaz "Attributes"

Los objetos "Attributes" implementa una porción del *mapping
protocol*, incluyendo los métodos "copy()", "get()", "__contains__()",
"items()", "keys()", y "values()".  Los siguientes métodos también son
provistos:

Attributes.getLength()

   Retorna el número de atributos.

Attributes.getNames()

   Retorna los nombres de los atributos.

Attributes.getType(name)

   Retorna el tipo del atributo *name*, que es normalmente "'CDATA'".

Attributes.getValue(name)

   Retorna el valor del atributo *name*.

## La Interfaz "AttributesNS"

Esta interfaz es un subtipo de la interfaz "Attributes" (vea la
sección La Interfaz Attributes). Todos los métodos soportados por la
interfaz están también disponibles en los objetos "AttributesNS".

Los siguientes métodos están también disponibles:

AttributesNS.getValueByQName(name)

   Retorna el valor para un nombre cualificado.

AttributesNS.getNameByQName(name)

   Retorna el par "(namespace, localname)" para un *name* cualificado.

AttributesNS.getQNameByName(name)

   Retorna el nombre cualificado para un par "(namespace, localname)".

AttributesNS.getQNames()

   Retorna los nombres cualificados para todos los atributos.
