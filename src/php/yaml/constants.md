---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/yaml.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: 86e6094e8
order: 107360
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`YAML_ANY_SCALAR_STYLE` (`int`)  

`YAML_PLAIN_SCALAR_STYLE` (`int`)  

`YAML_SINGLE_QUOTED_SCALAR_STYLE` (`int`)  

`YAML_DOUBLE_QUOTED_SCALAR_STYLE` (`int`)  

`YAML_LITERAL_SCALAR_STYLE` (`int`)  

`YAML_FOLDED_SCALAR_STYLE` (`int`)  

<!-- -->

`YAML_NULL_TAG` (`string`)  
"tag:yaml.org,2002:null"

`YAML_BOOL_TAG` (`string`)  
"tag:yaml.org,2002:bool"

`YAML_STR_TAG` (`string`)  
"tag:yaml.org,2002:str"

`YAML_INT_TAG` (`string`)  
"tag:yaml.org,2002:int"

`YAML_FLOAT_TAG` (`string`)  
"tag:yaml.org,2002:float"

`YAML_TIMESTAMP_TAG` (`string`)  
"tag:yaml.org,2002:timestamp"

`YAML_SEQ_TAG` (`string`)  
"tag:yaml.org,2002:seq"

`YAML_MAP_TAG` (`string`)  
"tag:yaml.org,2002:map"

`YAML_PHP_TAG` (`string`)  
"!php/object"

<!-- -->

`YAML_ANY_ENCODING` (`int`)  
Dejar que el emisor elija una codificación.

`YAML_UTF8_ENCODING` (`int`)  
Codificar como UTF8.

`YAML_UTF16LE_ENCODING` (`int`)  
Codificar como UTF16LE.

`YAML_UTF16BE_ENCODING` (`int`)  
Codificar como UTF16BE.

<!-- -->

`YAML_ANY_BREAK` (`int`)  
Dejar que el emisor elija el carácter de salto de línea.

`YAML_CR_BREAK` (`int`)  
Usar `\r` como carácter de salto (al estilo de Mac).

`YAML_LN_BREAK` (`int`)  
Usar `\n` como carácter de salto (al estilo de Unix).

`YAML_CRLN_BREAK` (`int`)  
Usar `\r\n` como cáracter de salto (al estilo de DOS).
