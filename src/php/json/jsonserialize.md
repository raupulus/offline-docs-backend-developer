---
title: JsonSerializable::jsonSerialize
description: Especifica los datos que deben ser serializados en JSON
source_url: https://www.php.net/manual/es/jsonserializable.jsonserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/jsonserializable/jsonserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: false
translation_revision: 0a09554f3
order: 42890
---

JsonSerializable::jsonSerialize

Especifica los datos que deben ser serializados en JSON

## Descripción

```php
public JsonSerializable::jsonSerialize(): mixed
```php

Serializa el objeto en un valor que puede ser serializado nativamente por la función `json_encode`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los datos que pueden ser serializados por la función `json_encode`, que pueden ser valores de cualquier tipo excepto un `resource`.

## Ejemplos

Ejemplo con JsonSerializable::jsonSerialize devolviendo un `array`

```
<?php
class ArrayValue implements JsonSerializable {
    private $array;
    public function __construct(array $array) {
        $this->array = $array;
    }

    public function jsonSerialize(): mixed {
        return $this->array;
    }
}

$array = [1, 2, 3];
echo json_encode(new ArrayValue($array), JSON_PRETTY_PRINT);
?>

    
```php

El ejemplo anterior mostrará:

    [
        1,
        2,
        3
    ]

Ejemplo con JsonSerializable::jsonSerialize devolviendo un `array` asociativo

```
<?php
class ArrayValue implements JsonSerializable {
    private $array;
    public function __construct(array $array) {
        $this->array = $array;
    }

    public function jsonSerialize() {
        return $this->array;
    }
}

$array = ['foo' => 'bar', 'quux' => 'baz'];
echo json_encode(new ArrayValue($array), JSON_PRETTY_PRINT);
?>

    
```php

El ejemplo anterior mostrará:

    {
        "foo": "bar",
        "quux": "baz"
    }

Ejemplo con JsonSerializable::jsonSerialize devolviendo un `int`

```
<?php
class IntegerValue implements JsonSerializable {
    private $number;
    public function __construct($number) {
        $this->number = (int) $number;
    }

    public function jsonSerialize() {
        return $this->number;
    }
}

echo json_encode(new IntegerValue(1), JSON_PRETTY_PRINT);
?>

    
```php

El ejemplo anterior mostrará:

    1

Ejemplo con JsonSerializable::jsonSerialize devolviendo una `string`

```
<?php
class StringValue implements JsonSerializable {
    private $string;
    public function __construct($string) {
        $this->string = (string) $string;
    }

    public function jsonSerialize() {
        return $this->string;
    }
}

echo json_encode(new StringValue('Hello!'), JSON_PRETTY_PRINT);
?>

    
```php

El ejemplo anterior mostrará:

    "Hello!"
