---
title: Herramientas Para Procesar Formatos de Marcado Estructurado
source_url: https://docs.python.org/es/3
source_path: library/markup.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3180
---

# Herramientas Para Procesar Formatos de Marcado Estructurado

Python soporta una variedad de módulos para trabajar con varias formas
de almacenar datos de forma estructurada. Esto incluye módulos para
trabajar con el Lenguaje de Marcado Estructurado General (SGML) y el
Lenguaje de de Marcado de Hipertexto (HTML), y varias interfaces para
trabajar con el Lenguaje de Marcado Estructurado Extensible (XML).

* "html" --- HyperText Markup Language support

* "html.parser" --- Simple HTML and XHTML parser

  * Aplicación ejemplo de un analizador sintáctico (*parser*) de HTML

  * Métodos "HTMLParser"

  * Ejemplos

* "html.entities" --- Definitions of HTML general entities

* Módulos de procesamiento XML

  * XML security

* "xml.etree.ElementTree" --- The ElementTree XML API

  * Tutorial

    * Árbol y elementos XML

    * Procesando XML

    * API de consulta para un procesamiento no bloqueante

    * Encontrando elementos interesantes

    * Modificando un archivo XML

    * Construyendo documentos XML

    * Procesando XML con espacio de nombres

  * Soporte de XPath

    * Ejemplo

    * Sintaxis XPath soportada

  * Referencia

    * Funciones

  * Soporte de XInclude

    * Ejemplo

  * Referencia

    * Funciones

    * Objetos Element

    * Objetos ElementTree

    * Objetos QName

    * Objetos TreeBuilder

    * Objetos XMLParser

    * Objetos XMLPullParser

    * Excepciones

* "xml.dom" --- The Document Object Model API

  * Contenido del módulo

  * Objetos en el DOM

    * Objetos *DOMImplementation*

    * Objetos nodo

    * Objetos *NodeList*

    * Objetos *DocumentType*

    * Objetos documento

    * Objetos elemento

    * Objetos atributo

    * Objetos *NamedNodeMap*

    * Objetos comentario

    * Objetos Texto y *CDATASection*

    * Objetos *ProcessingInstruction*

    * Excepciones

  * Conformidad

    * Mapeo de tipos

    * Métodos de acceso (*accessor*)

* "xml.dom.minidom" --- Minimal DOM implementation

  * Objetos del DOM

  * Ejemplo de DOM

  * minidom y el estándar DOM

* "xml.dom.pulldom" --- Support for building partial DOM trees

  * Objetos DOMEventStream

* "xml.sax" --- Support for SAX2 parsers

  * Objetos SAXException

* "xml.sax.handler" --- Base classes for SAX handlers

  * Objetos ContentHandler

  * Objetos DTDHandler

  * Objetos EntityResolver

  * Objetos ErrorHandler

  * Objetos DTDHandler

* "xml.sax.saxutils" --- SAX Utilities

* "xml.sax.xmlreader" --- Interface for XML parsers

  * Objetos XMLReader

  * Objetos IncrementalParser

  * Objetos localizadores

  * Objetos InputSource

  * La Interfaz "Attributes"

  * La Interfaz "AttributesNS"

* "xml.parsers.expat" --- Fast XML parsing using Expat

  * Objetos XMLParser

  * Excepciones de ExpatError

  * Ejemplo

  * Descripciones del modelo de contenido

  * Constantes de error de expansión
