---
title: yaml_parse
description: Analiza una secuencia de texto en formato YAML
source_url: https://www.php.net/manual/es/function.yaml-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/functions/yaml-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: b8758b060
order: 107420
---

yaml_parse

Analiza una secuencia de texto en formato YAML

## Descripción

```php
yaml_parse(string $input, [int $pos], [int $ndocs], [array $callbacks]): mixed
```php

Convierte toda o parte de una secuencia de texto en YAML a una variable en PHP.

## Parámetros

`input`  
La secuencia de texto (`string`) a analizar en formato YAML.

`pos`  
Documento YAML a extraer desde la secuencia de texto (`-1` para analizar todos los documentos, `0` solo para el primer documento, etc).

`ndocs`  
Si se facilita `ndocs`, se completará con el número de documentos encontrados en la secuencia de texto.

`callbacks`  
Controlador de contenido para los nodos YAML. Es un `array` asociativo de etiquetas YAML =\> asociando sus `callable` correspondientes. Ver [Analizar callbacks](#yaml.callbacks.parse) para más información.

## Valores devueltos

Devuelve el valor codificado de `input` en el formato apropiado de PHP o `false` si ocurre un error. Si el valor de `pos` es `-1` devolverá un `array` con una entrada por cada documento encontrado en el texto.

## Ejemplos

Ejemplo de `yaml_parse`

```
<?php
$yaml = <<<EOD
---
invoice: 34843
date: "2001-01-23"
bill-to: &id001
  given: Chris
  family: Dumars
  address:
    lines: |-
      458 Walkman Dr.
              Suite #292
    city: Royal Oak
    state: MI
    postal: 48046
ship-to: *id001
product:
- sku: BL394D
  quantity: 4
  description: Basketball
  price: 450
- sku: BL4438H
  quantity: 1
  description: Super Hoop
  price: 2392
tax: 251.420000
total: 4443.520000
comments: Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338.
...
EOD;

$parsed = yaml_parse($yaml);
var_dump($parsed);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(8) {
      ["invoice"]=>
      int(34843)
      ["date"]=>
      string(10) "2001-01-23"
      ["bill-to"]=>
      &array(3) {
        ["given"]=>
        string(5) "Chris"
        ["family"]=>
        string(6) "Dumars"
        ["address"]=>
        array(4) {
          ["lines"]=>
          string(34) "458 Walkman Dr.
            Suite #292"
          ["city"]=>
          string(9) "Royal Oak"
          ["state"]=>
          string(2) "MI"
          ["postal"]=>
          int(48046)
        }
      }
      ["ship-to"]=>
      &array(3) {
        ["given"]=>
        string(5) "Chris"
        ["family"]=>
        string(6) "Dumars"
        ["address"]=>
        array(4) {
          ["lines"]=>
          string(34) "458 Walkman Dr.
            Suite #292"
          ["city"]=>
          string(9) "Royal Oak"
          ["state"]=>
          string(2) "MI"
          ["postal"]=>
          int(48046)
        }
      }
      ["product"]=>
      array(2) {
        [0]=>
        array(4) {
          ["sku"]=>
          string(6) "BL394D"
          ["quantity"]=>
          int(4)
          ["description"]=>
          string(10) "Basketball"
          ["price"]=>
          int(450)
        }
        [1]=>
        array(4) {
          ["sku"]=>
          string(7) "BL4438H"
          ["quantity"]=>
          int(1)
          ["description"]=>
          string(10) "Super Hoop"
          ["price"]=>
          int(2392)
        }
      }
      ["tax"]=>
      float(251.42)
      ["total"]=>
      float(4443.52)
      ["comments"]=>
      string(68) "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338."
    }

## Notas

> [!WARNING]
> El procesamiento de las entradas de los usuarios no confiables con `yaml_parse` es peligroso si el uso de `unserialize` está habilitado para los nodos usando la etiqueta `!php/object`. Este comportamiento puede ser desactivado por el uso de el ajuste ini `yaml.decode_php`.

## Véase también

`yaml_parse_file`, `yaml_parse_url`, `yaml_emit`
