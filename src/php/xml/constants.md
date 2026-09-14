---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/xml.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xml/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xml
translation_status: ready
translation_reviewed: true
translation_revision: 9acfa1897
order: 102620
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`XML_ERROR_NONE` (`int`)  

`XML_ERROR_NO_MEMORY` (`int`)  

`XML_ERROR_SYNTAX` (`int`)  

`XML_ERROR_NO_ELEMENTS` (`int`)  

`XML_ERROR_INVALID_TOKEN` (`int`)  

`XML_ERROR_UNCLOSED_TOKEN` (`int`)  

`XML_ERROR_PARTIAL_CHAR` (`int`)  

`XML_ERROR_TAG_MISMATCH` (`int`)  

`XML_ERROR_DUPLICATE_ATTRIBUTE` (`int`)  

`XML_ERROR_JUNK_AFTER_DOC_ELEMENT` (`int`)  

`XML_ERROR_PARAM_ENTITY_REF` (`int`)  

`XML_ERROR_UNDEFINED_ENTITY` (`int`)  

`XML_ERROR_RECURSIVE_ENTITY_REF` (`int`)  

`XML_ERROR_ASYNC_ENTITY` (`int`)  

`XML_ERROR_BAD_CHAR_REF` (`int`)  

`XML_ERROR_BINARY_ENTITY_REF` (`int`)  

`XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF` (`int`)  

`XML_ERROR_MISPLACED_XML_PI` (`int`)  

`XML_ERROR_UNKNOWN_ENCODING` (`int`)  

`XML_ERROR_INCORRECT_ENCODING` (`int`)  

`XML_ERROR_UNCLOSED_CDATA_SECTION` (`int`)  

`XML_ERROR_EXTERNAL_ENTITY_HANDLING` (`int`)  

`XML_OPTION_CASE_FOLDING` (`int`)  

`XML_OPTION_PARSE_HUGE` (`int`)  
Disponible a partir de PHP 8.4.0. Cuando se utiliza libxml2 \< 2.7.0 (por ejemplo en PHP 7.x), esta opción está activada por omisión y no puede ser desactivada.

`XML_OPTION_TARGET_ENCODING` (`int`)  

`XML_OPTION_SKIP_TAGSTART` (`int`)  

`XML_OPTION_SKIP_WHITE` (`int`)  

`XML_SAX_IMPL` (`string`)  
Indica el método de implementación de SAX. Puede ser `libxml` o `expat`.
