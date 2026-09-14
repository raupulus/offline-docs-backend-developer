---
title: yaml_emit_file
description: Enviar la representación YAML de un valor a un fichero
source_url: https://www.php.net/manual/es/function.yaml-emit-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/functions/yaml-emit-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: af5f2f87b
order: 107380
---

yaml_emit_file

Enviar la representación YAML de un valor a un fichero

## Descripción

```php
yaml_emit_file(string $filename, mixed $data, [int $encoding], [int $linebreak], [array $callbacks]): bool
```php

Genera una representación YAML de `data` proporcionada en el `filename`.

## Parámetros

`filename`  
Ruta a el fichero.

`data`  
La `data` se codifica. Puede ser de cualquier tipo excepto un `resource`.

`encoding`  
Salida de codificación de caracteres seleccionando entre `YAML_ANY_ENCODING`, `YAML_UTF8_ENCODING`, `YAML_UTF16LE_ENCODING`, `YAML_UTF16BE_ENCODING`.

`linebreak`  
Salida del estilo de salto de línea seleccionando entre `YAML_ANY_BREAK`, `YAML_CR_BREAK`, `YAML_LN_BREAK`, `YAML_CRLN_BREAK`.

`callbacks`  
Manejadores de contenido para emitir nodos YAML. `array` asociativo de nombre de clase de asignaciones =\> `callable`. Véase [emitir llamadas de retorno](#yaml.callbacks.emit) para más detalles.

## Valores devueltos

Devuelve `true` en caso de éxito.

## Historial de cambios

| Versión         | Descripción                           |
|-----------------|---------------------------------------|
| PECL yaml 1.1.0 | El parámetro `callbacks` fue añadido. |

## Véase también

`yaml_emit`, `yaml_parse`
