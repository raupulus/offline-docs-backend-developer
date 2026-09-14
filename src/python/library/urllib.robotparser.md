---
title: '"urllib.robotparser" ---  Parser for robots.txt'
source_url: https://docs.python.org/es/3
source_path: library/urllib.robotparser.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4430
---

# "urllib.robotparser" ---  Parser for robots.txt

**Código fuente:** Lib/urllib/robotparser.py

======================================================================

This module provides a single class, "RobotFileParser", which answers
questions about whether or not a particular user agent can fetch a URL
on the website that published the "robots.txt" file.  For more details
on the structure of "robots.txt" files, see **RFC 9309**.

class urllib.robotparser.RobotFileParser(url='')

   Esta clase proporciona métodos para leer, analizar y responder
   preguntas acerca de "robots.txt"

   set_url(url)

      Establece la URL que hace referencia a un archivo "robots.txt".

   read()

      Lee la URL "robots.txt" y la envía al analizador.

   parse(lines)

      Analiza el argumento *lines*.

   can_fetch(useragent, url)

      Retorna "True" si el *useragent* tiene permiso para buscar la
      *url* de acuerdo con las reglas contenidas en el archivo
      "robots.txt" analizado.

   mtime()

      Retorna la hora en que se recuperó por última vez el archivo
      "robots.txt". Esto es útil para arañas web de larga duración que
      necesitan buscar nuevos archivos "robots.txt" periódicamente.

   modified()

      Establece la hora a la que se recuperó por última vez el archivo
      "robots.txt" hasta la hora actual.

   crawl_delay(useragent)

      Retorna el valor del parámetro "Crawl-delay" de "robots.txt"
      para el *useragent* en cuestión. Si no existe tal parámetro o no
      se aplica al *useragent* especificado o la entrada "robots.txt"
      para este parámetro tiene una sintaxis no válida, devuelve
      "None".

      Added in version 3.6.

   request_rate(useragent)

      Retorna el contenido del parámetro "Request-rate" de
      "robots.txt" como una *tupla nombrada* "RequestRate(requests,
      seconds)". Si no existe tal parámetro o no se aplica al
      *useragent* especificado o la entrada "robots.txt" para este
      parámetro tiene una sintaxis no válida, devuelve "None".

      Added in version 3.6.

   site_maps()

      Retorna el contenido del parámetro "Sitemap" de "robots.txt" en
      forma de "list()". Si no existe tal parámetro o la entrada
      "robots.txt" para este parámetro tiene una sintaxis no válida,
      devuelve "None".

      Added in version 3.8.

El siguiente ejemplo demuestra el uso básico de la clase
"RobotFileParser":

   >>> import urllib.robotparser
   >>> rp = urllib.robotparser.RobotFileParser()
   >>> rp.set_url("http://www.pythontest.net/robots.txt")
   >>> rp.read()
   >>> rrate = rp.request_rate("*")
   >>> rrate.requests
   1
   >>> rrate.seconds
   1
   >>> rp.crawl_delay("*")
   6
   >>> rp.can_fetch("*", "http://www.pythontest.net/")
   True
   >>> rp.can_fetch("*", "http://www.pythontest.net/no-robots-here/")
   False
