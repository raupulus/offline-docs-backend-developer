---
title: La interfaz Stringable
source_url: https://www.php.net/manual/es/class.stringable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/stringable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 3950
---

## Introducción

La interfaz Stringable designa una clase que posee un método [\_\_toString()](#object.tostring). A diferencia de la mayoría de las interfaces, Stringable está implícitamente presente en cualquier clase para la cual el método mágico [\_\_toString()](#object.tostring) está definido, aunque puede y debe ser declarada explícitamente.

Su valor principal es permitir a las funciones verificar el tipo en comparación con el tipo de unión `string|Stringable` para aceptar ya sea un string primitivo, ya sea un objeto que pueda ser convertido a string.

## Sinopsis de la interfaz

Stringable

Métodos

## Ejemplos de Stringable

Ejemplo simple

Esto utiliza la [promoción de propiedades del constructor](#language.oop5.decon.constructor.promotion).

```php
<?php
class IPv4Address implements Stringable {
    public function __construct(
        private string $oct1,
        private string $oct2,
        private string $oct3,
        private string $oct4,
    ) {}

    public function __toString(): string {
        return "$this->oct1.$this->oct2.$this->oct3.$this->oct4";
    }
}

function showStuff(string|Stringable $value) {
    // Para un Stringable, esto llamará implícitamente a __toString().
    print $value;
}

$ip = new IPv4Address('123', '234', '42', '9');

showStuff($ip);
?>

     
```

Resultado del ejemplo anterior es similar a:

    123.234.42.9
