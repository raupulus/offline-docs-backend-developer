---
title: Collator::getSortKey
description: Obtiene la clave de ordenación para una cadena
source_url: https://www.php.net/manual/es/collator.getsortkey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/get-sort-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: 743f97dd0
order: 39440
---

Collator::getSortKey

collator_get_sort_key

Obtiene la clave de ordenación para una cadena

## Descripción

Estilo orientado a objetos

```php
public Collator::getSortKey(string $string): string
```php

Estilo procedimental

```php
collator_get_sort_key(Collator $object, string $string): string
```

Devuelve la clave de collation para una cadena. Las claves de collation pueden compararse directamente en lugar de cadenas, no obstante son específicas de la implementación y pueden cambiar entre versiones de la biblioteca ICU. Las claves de ordenación son generalmente útiles solo en bases de datos u otras circunstancias donde las llamadas a funciones son extremadamente costosas.

## Parámetros

`object`  
Objeto `Collator`.

`string`  
La cadena desde la cual producir la clave.

## Valores devueltos

Devuelve la clave de collation para la cadena, o `false` si ocurre un error.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Ejemplo `collator_get_sort_key`

```php
<?php

$s1 = 'Hello';

$coll = collator_create('en_US');
$res  = collator_get_sort_key($coll, $s1);

echo bin2hex($res);
?>

    
```

Resultado del ejemplo anterior es similar a:

         3832404046010901dc08

`Collator::getSortKey` : ejemplo con `usort`

```php
<?php

$data = [
    [ 'name' => '🇳🇱 Derick Rethans', 'linked_account' => 'https://phpc.social/users/derickr' ],
    [ 'name' => 'Elephpant', 'linked_account' => 'https://phpc.social/phpc' ],
    [ 'name' => '🇫🇷 Marcus Bointon', 'linked_account' => 'https://phpc.social/users/Synchro' ],
];

/* Crear el collator */
$col = new Collator('en');

/* Ordenar letras mayúsculas antes que minúsculas */
$col->setAttribute(Collator::CASE_FIRST, Collator::UPPER_FIRST);

/* Utilizar una función definida por el usuario con sort, que elimina los emojis */
usort(
    $data,
    function($a, $b) use ($col) {
        /* Eliminar la clase de caracteres 'S' (Símbolos) y los espacios
         * (con trim) */
        $aName = trim(preg_replace('/\p{S}+/u', '', $a['name']));
        $bName = trim(preg_replace('/\p{S}+/u', '', $b['name']));

        /* Crear la clave de ordenación */
        $aKey = $col->getSortKey($aName);
        $bKey = $col->getSortKey($bName);

        /* Utilizar la clave de ordenación para determinar el orden de los elementos */
        return $aKey <=> $bKey;
    }
);

var_dump($data);
?>

    
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0] =>
      array(2) {
        'name' =>
        string(25) "🇳🇱 Derick Rethans"
        'linked_account' =>
        string(33) "https://phpc.social/users/derickr"
      }
      [1] =>
      array(2) {
        'name' =>
        string(9) "Elephpant"
        'linked_account' =>
        string(24) "https://phpc.social/phpc"
      }
      [2] =>
      array(2) {
        'name' =>
        string(25) "🇫🇷 Marcus Bointon"
        'linked_account' =>
        string(33) "https://phpc.social/users/Synchro"
      }
    }

## Véase también

`collator_sort`, `collator_sort_with_sort_keys`
