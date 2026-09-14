---
title: Módulos de procesamiento XML
source_url: https://docs.python.org/es/3
source_path: library/xml.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4650
---

# Módulos de procesamiento XML

**Código fuente:** Lib/xml/

======================================================================

Las interfaces de Python para procesar XML están agrupadas en el
paquete "xml".

Nota:

  If you need to parse untrusted or unauthenticated data, see XML
  security.

It is important to note that modules in the "xml" package require that
there be at least one SAX-compliant XML parser available. The Expat
parser is included with Python, so the "xml.parsers.expat" module will
always be available.

La documentación de los paquetes "xml.dom" y "xml.sax" es la
definición de los enlaces de Python para las interfaces DOM y SAX.

Los submódulos de manejo de XML son:

* "xml.etree.ElementTree": la API ElementTree, un procesador de XML
  simple y ligero

* "xml.dom": la definición de la API DOM

* "xml.dom.minidom": una implementación mínima de DOM

* "xml.dom.pulldom": soporte para la construcción de árboles DOM
  parciales

* "xml.sax": clases base SAX2 y funciones de conveniencia

* "xml.parsers.expat": el enlace del analizador Expat

## XML security

An attacker can abuse XML features to carry out denial of service
attacks, access local files, generate network connections to other
machines, or circumvent firewalls when attacker-controlled XML is
being parsed, in Python or elsewhere.

The built-in XML parsers of Python rely on the library libexpat,
commonly called Expat, for parsing XML.

By default, Expat itself does not access local files or create network
connections.

Expat versions lower than 2.7.2 may be vulnerable to the "billion
laughs", "quadratic blowup" and "large tokens" vulnerabilities, or to
disproportional use of dynamic memory. Python bundles a copy of Expat,
and whether Python uses the bundled or a system-wide Expat, depends on
how the Python interpreter "has been configured" in your environment.
Python may be vulnerable if it uses such older versions of Expat.
Check "pyexpat.EXPAT_VERSION".

"xmlrpc" is **vulnerable** to the "decompression bomb" attack.

mil millones de risas / expansión exponencial de entidad
   El ataque Billion Laughs, también conocido como expansión
   exponencial de entidades, utiliza varios niveles de entidades
   anidadas. Cada entidad hace referencia a otra entidad varias veces
   y la definición de entidad final contiene una cadena pequeña. La
   expansión exponencial da como resultado varios gigabytes de texto y
   consume mucha memoria y tiempo de CPU.

expansión de entidad de explosión cuadrática
   Un ataque de explosión cuadrática es similar a un ataque de Billion
   Laughs; también abusa de la expansión de entidad. En lugar de
   entidades anidadas, repite una entidad grande con un par de miles
   de caracteres una y otra vez. El ataque no es tan eficaz como el
   caso exponencial, pero evita desencadenar contramedidas del
   analizador que prohíben entidades profundamente anidadas.

bomba de descompresión
   Las bombas de descompresión (también conocidas como ZIP bomb) se
   aplican a todas las bibliotecas XML que pueden analizar secuencias
   XML comprimidas, como secuencias HTTP comprimidas con gzip o
   archivos comprimidos por LZMA. Para un atacante puede reducir la
   cantidad de datos transmitidos en magnitudes de tres o más.

large tokens
   Expat needs to re-parse unfinished tokens; without the protection
   introduced in Expat 2.6.0, this can lead to quadratic runtime that
   can be used to cause denial of service in the application parsing
   XML. The issue is known as **CVE 2023-52425**.
