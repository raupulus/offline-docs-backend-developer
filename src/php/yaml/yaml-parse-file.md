---
title: yaml_parse_file
description: Analiza una secuencia de texto en formato YAML desde un fichero
source_url: https://www.php.net/manual/es/function.yaml-parse-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/functions/yaml-parse-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: 132d2a8d6
order: 107400
---

yaml_parse_file

Analiza una secuencia de texto en formato YAML desde un fichero

## Descripción

```php
yaml_parse_file(string $filename, [int $pos], [int $ndocs], [array $callbacks]): mixed
```php

Convierte toda o parte de una secuencia de texto en YAML a una variable en PHP.

## Parámetros

`filename`  
Ruta del nombre del fichero.

`pos`  
Documento YAML a extraer desde la secuencia de texto (`-1` para analizar todos los documentos, `0` solo para el primer documento, etc).

`ndocs`  
Si se facilita `ndocs`, se completará con el número de documentos encontrados en la secuencia de texto.

`callbacks`  
Controlador de contenido para los nodos YAML. Es un `array` asociativo de etiquetas YAML =\> asociando sus `callable` correspondientes. Ver [Analizar callbacks](#yaml.callbacks.parse) para más información.

## Valores devueltos

Devuelve el valor codificado de `filename` en el tipo apropiado de PHP.

En caso de error, se devuelve una cadena que contiene un mensaje de error.

Si `pos` es `-1`, se devolverá un `array` con una entrada por cada documento encontrado en el flujo.

## Notas

> [!WARNING]
> El procesamiento de las entradas de los usuarios no confiables con `yaml_parse_file` es peligroso si el uso de `unserialize` está habilitado para los nodos usando la etiqueta `!php/object`. Este comportamiento puede ser desactivado por el uso de el ajuste ini `yaml.decode_php`.

## Véase también

`yaml_parse`, `yaml_parse_url`, `yaml_emit`
