---
title: Ejemplos
source_url: https://www.php.net/manual/es/yaml.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: bd4e76401
order: 107370
---

## Ejemplos

Ejemplo de Yaml

```php
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
    "date"=> "2001-01-23",
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

// genera un representación de la factura en YAML
$yaml = yaml_emit($invoice);
var_dump($yaml);

// convierte lo anterior en YAML a una variable PHP
$parsed = yaml_parse($yaml);

// verifica que la comprobación de ida y vuelta a una extructura equivalente
var_dump($parsed == $invoice);
?>

  
```

Resultado del ejemplo anterior es similar a:

    string(631) "---
    invoice: 34843
    date: "2001-01-23"
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
    bool(true)
