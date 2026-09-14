---
title: Collator::compare
description: Comparar dos strings Unicode
source_url: https://www.php.net/manual/es/collator.compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39370
---

Collator::compare

collator_compare

Comparar dos strings Unicode

## Descripción

Estilo orientado a objetos

```php
public Collator::compare(string $string1, string $string2): int
```php

Estilo procedimental

```php
collator_compare(Collator $object, string $string1, string $string2): int
```

Comparar dos strings Unicode según las reglas de collation.

## Parámetros

`object`  
Objeto `Collator`.

`string1`  
El primer string a comparar.

`string2`  
El segundo string a comparar.

## Valores devueltos

Resultados de comparación

- 1 si `string1` es *mayor* que `string2`;

- 0 si `string1` es *igual* a `string2`;

- -1 si `string1` es *menor* que `string2`.

Retorna `false` en caso de fallo.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Ejemplo con `collator_compare`

```php
<?php
$s1 = 'Hello';
$s2 = 'hello';

$coll = collator_create( 'en_US' );
$res  = collator_compare( $coll, $s1, $s2 );

if ($res === false) {
    echo collator_get_error_message( $coll );
} else if( $res > 0 ) {
    echo "s1 es mayor que s2\n";
} else if( $res < 0 ) {
    echo "s1 es menor que s2\n";
} else {
    echo "s1 es igual a s2\n";
}
?>

    
```

El ejemplo anterior mostrará:

         s1 es mayor que s2

Comparar strings sin diacríticos o sensibilidad a mayúsculas/minúsculas

```php
     
<?php
$c = new Collator( 'en' );
$c->setStrength( Collator::PRIMARY );
if ( $c->compare( 'Séan', 'Sean' ) == 0 )
{
    echo "Iguales\n";
}

    
```

El ejemplo anterior mostrará:

         Iguales
        

Este ejemplo solicita al collator que compare solo teniendo en cuenta los caracteres base. La documentación para `Collator->setStrength` explica las diferentes fuerzas.

## Véase también

`collator_sort`
