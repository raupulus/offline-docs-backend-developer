---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/intl.locale-constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale-constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1f68eecaa
order: 42010
---

## Constantes predefinidas

Estas constantes definen el comportamiento de Locale

`Locale::DEFAULT_LOCALE` `null`  
Utilizada como argumento de configuración local con los métodos de las diferentes clases afectadas, tales como `NumberFormatter`. Esta constante hace que se utilicen los valores por omisión.

Estas constantes describen la elección de la configuración local para el método getLocale de diferentes clases.

`Locale::ACTUAL_LOCALE` `int`  
La configuración local utilizada por los datos entrantes.

`Locale::VALID_LOCALE` `int`  
Esta es la configuración local más específica soportada por ICU.

## Subetiqueta de idioma

Estas constantes definen cómo se analizan o componen las configuraciones locales. Deben ser utilizadas como claves en un array de argumentos pasado a `locale_compose` y son devueltas por `locale_parse` como claves de un `array` asociativo.

`Locale::LANG_TAG` `string`  
Subetiqueta de idioma

`Locale::EXTLANG_TAG` `string`  
Subetiqueta de idioma extendido

`Locale::SCRIPT_TAG` `string`  
Subetiqueta de script

`Locale::REGION_TAG` `string`  
Subetiqueta de región

`Locale::VARIANT_TAG` `string`  
Subetiqueta de variante

`Locale::GRANDFATHERED_LANG_TAG` `string`  
Subetiqueta de idioma heredado

`Locale::PRIVATE_TAG` `string`  
Subetiqueta privada
