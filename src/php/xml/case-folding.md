---
title: Case Folding
source_url: https://www.php.net/manual/es/xml.case-folding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/case-folding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_revision: af4410a7e
order: 102600
---

Las funciones manejadoras de elementos pueden obtener sus nombres de elementos "case-folded". Case folding se define como "un proceso aplicado a una secuencia de caracteres", en el cual aquellos que son identificados como no-mayúsculas son reemplazados por sus equivalentes en mayúsculas". En otras palabras, cuando se trata de XML, case folding simplemente significa poner en mayúsculas.

Por defecto, todos los nombres de elementos que son pasados al manejador de funciones son pasados a mayúsculas. Este comportamiento puede ser consultado y controlado por el intérprete XML mediante las funciones `xml_parser_get_option` y `xml_parser_set_option` respectivamente.
