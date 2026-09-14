---
title: Codificación de caracteres
source_url: https://www.php.net/manual/es/xml.encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_revision: af4410a7e
order: 102630
---

La extensión de PHP XML es compatible con el conjunto de caracteres [Unicode](http://www.unicode.org/) a través de diferentes codificaciones de caracteres. Hay dos tipos de codificaciones de caracteres: la codificación fuente y la codificación de destino. La representación interna de PHP del documento está siempre codificada con `UTF-8`.

La codificación fuente se hace cuando un documento XML es [analizado](#function.xml-parse). Una vez [creado un intérprete XML](#function.xml-parser-create), la codificación fuente puede ser especificada (esta codificación no puede ser cambiada más adelante en la vida del intérprete XML). Las codificaciones fuente soportadas son `ISO-8859-1`, `US-ASCII` y `UTF-8`. Las dos primeras son codificaciones de un solo byte, lo cual significa que cada caracter se representa por un solo byte. `UTF-8` puede codificar caracteres compuestos por un número variable de bits (hasta 21) de uno a cuatro bytes. La codificación fuente por defecto usada por PHP es `ISO-8859-1`.

La codificación de destino se hace cuando PHP pasa datos al controlador XML de funciones. Cuando un intérprete XML se ha creado, la codificación de destino se establece igual que la que tenga la codificación fuente, pero esta puede ser cambiada en cualquier punto. La codificación de destino afectará a los caracteres de los datos como también a los nombres de etiquetas y las intrucciones de procesamiento de destino.

Si el intérprete XML encuentra caracteres fuera de rango que su codificación fuente es capaz de representar, devolverá un error.

Si PHP encuentra caracteres en el documento XML analizado que no pueden ser representados en la codificación de destino escogida, los caracteres problemáticos seran "degradados". Actualmente esto significa que tales caracteres seran reemplazados por un signo de interrogación.
