---
title: yaml_parse_url
description: Analiza una secuencia de texto Yaml desde una URL
source_url: https://www.php.net/manual/es/function.yaml-parse-url.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/functions/yaml-parse-url.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: 7c1cbb325
order: 107410
---

yaml_parse_url

Analiza una secuencia de texto Yaml desde una URL

## Descripción

```php
yaml_parse_url(string $url, [int $pos], [int $ndocs], [array $callbacks]): mixed
```php

Convierte toda o parte de una secuencia de texto en YAML a una variable en PHP.

## Parámetros

`url`  
La dirección `url` debe tener el formato "scheme://...". PHP buscará el controlador de protocolos (también conocido como wrapper) para el esquema especificado. Si no hay wrappers registrados para este protocolo, PHP lanzará un aviso para ayudar a indentificar posibles problemas con el script y continuar como si el nombre del fichero hiciera referencia a un fichero normal.

`pos`  
Documento YAML a extraer desde la secuencia de texto (`-1` para analizar todos los documentos, `0` solo para el primer documento, etc).

`ndocs`  
Si se facilita `ndocs`, se completará con el número de documentos encontrados en la secuencia de texto.

`callbacks`  
Controlador de contenido para los nodos YAML. Es un `array` asociativo de etiquetas YAML =\> asociando sus `callable` correspondientes. Ver [Analizar callbacks](#yaml.callbacks.parse) para más información

## Valores devueltos

Devuelve el valor codificado de `url` en el formato apropiado de PHP o `false` si ocurre un error. Si el valor de `pos` es `-1` devolverá un `array` con una entrada por cada documento encontrado en el texto.

## Notas

> [!WARNING]
> El procesamiento de entradas de usuario no confiables con `yaml_parse_url` es peligroso si el uso de `unserialize` está habilitado para nodos que utilizan la etiqueta `!php/object`. Este comportamiento puede ser deshabilitado utilizando la configuración ini `yaml.decode_php`.

## Véase también

`yaml_parse`, `yaml_parse_file`, `yaml_emit`
