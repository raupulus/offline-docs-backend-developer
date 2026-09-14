---
title: Ejemplos
source_url: https://www.php.net/manual/es/gender.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gender/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gender
translation_status: ready
translation_revision: 1742a682c
order: 26000
---

## Ejemplos

## Ejemplo de uso.

Ejemplo de uso de la clase Gender.

Ejemplo de uso.

```php
<?php

namespace Gender;

$género = new Gender;

$nombre = "Milene";
$país = Gender::FRANCE;

$resultado = $género->get($nombre, $país);

$datos = $género->country($país);

switch($resultado) {
    case Gender::IS_FEMALE:
        printf("El nombre %s es femenino en %s\n", $nombre, $datos['country']);
    break;

    case Gender::IS_MOSTLY_FEMALE:
        printf("El nombre %s es habitualmente femenino en %s\n", $nombre, $datos['country']);
    break;

    case Gender::IS_MALE:
        printf("El nombre %s es masculino en %s\n", $nombre, $datos['country']);
    break;

    case Gender::IS_MOSTLY_MALE:
        printf("El nombre %s es habitualmente masculino en %s\n", $nombre, $datos['country']);
    break;

    case Gender::IS_UNISEX_NAME:
        printf("El nombre %s es unisex en %s\n", $nombre, $datos['country']);
    break;

    case Gender::IS_A_COUPLE:
        printf("El nombre %s es masculino y femenino en %s\n", $nombre, $datos['country']);
    break;

    case Gender::NAME_NOT_FOUND:
        printf("El nombre %s no se encontró en %s\n", $nombre, $datos['country']);
    break;

    case Gender::ERROR_IN_NAME:
        echo "¡Hay un error con el nombre proporcionado!\n";
    break;

    default:
        echo "¡Ocurrió un error!\n";
    break;

}

   
```
