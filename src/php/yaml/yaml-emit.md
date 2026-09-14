---
title: yaml_emit
description: Devuelve la representación de un valor YAML
source_url: https://www.php.net/manual/es/function.yaml-emit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/functions/yaml-emit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: af5f2f87b
order: 107390
---

yaml_emit

Devuelve la representación de un valor YAML

## Descripción

```php
yaml_emit(mixed $data, [int $encoding], [int $linebreak], [array $callbacks]): string
```php

Genera una representación YAML de los datos en `data` proporcionados.

## Parámetros

`data`  
La `data` se codifica. Puede ser de cualquier tipo excepto un `resource`.

`encoding`  
Salida de codificación de caracteres elegidos desde `YAML_ANY_ENCODING`, `YAML_UTF8_ENCODING`, `YAML_UTF16LE_ENCODING`, `YAML_UTF16BE_ENCODING`.

`linebreak`  
Estilo de salida de línea de salto desde: `YAML_ANY_BREAK`, `YAML_CR_BREAK`, `YAML_LN_BREAK`, `YAML_CRLN_BREAK`.

`callbacks`  
Gestores de contenido para emitir nodos YAML. `array` asociativo de referenciaciones de nombres de clase =\> `callable`. Véase [emitir llamadas de retorno](#yaml.callbacks.emit) para más detalles.

## Valores devueltos

Devuelve un `string` de YAML codificado si es correcto.

## Historial de cambios

| Versión         | Descripción                         |
|-----------------|-------------------------------------|
| PECL yaml 1.1.0 | Se añadió el parámetro `callbacks`. |

## Ejemplos

Ejemplo de `yaml_emit`

```
<?php
$addr = array(
    "given" => "Chris",
    "family"=> "Dumars",
    "address"=> array(
        "lines"=> "458 Walkman Dr.
        Suite #292",
        "city"=> "Royal Oak",
        "state"=> "MI",
        "postal"=> 48046,
      ),
  );
$invoice = array (
    "invoice"=> 34843,
    "date"=> 980208000,
    "bill-to"=> $addr,
    "ship-to"=> $addr,
    "product"=> array(
        array(
            "sku"=> "BL394D",
            "quantity"=> 4,
            "description"=> "Basketball",
            "price"=> 450,
          ),
        array(
            "sku"=> "BL4438H",
            "quantity"=> 1,
            "description"=> "Super Hoop",
            "price"=> 2392,
          ),
      ),
    "tax"=> 251.42,
    "total"=> 4443.52,
    "comments"=> "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338.",
  );
var_dump(yaml_emit($invoice));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(628) "---
    invoice: 34843
    date: 980208000
    bill-to:
      given: Chris
      family: Dumars
      address:
        lines: |-
          458 Walkman Dr.
                  Suite #292
        city: Royal Oak
        state: MI
        postal: 48046
    ship-to:
      given: Chris
      family: Dumars
      address:
        lines: |-
          458 Walkman Dr.
                  Suite #292
        city: Royal Oak
        state: MI
        postal: 48046
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
    "

## Véase también

`yaml_emit_file`, `yaml_parse`
