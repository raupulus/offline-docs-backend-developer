---
title: La interface Hashable
source_url: https://www.php.net/manual/es/class.ds-hashable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds.hashable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_revision: dfd68fd22
order: 16540
---

## Introducción

Hashable es una interface que permite a los objetos ser usados como claves. Esta es una alternativa a `spl_object_hash`, la cual determina el hash de un objeto basado en su gestor: estos significa que dos objetos que son considerados iguales por una implícita definición no serán tratados como iguales debido a que no son la misma instancia.

`hash` es utilizada para devolver un valor escalar para ser usado como el valor hash del objeto, el cual determina donde este va en la tabla hash. Aunque este valor no tiene que ser único, los objetos los cuales son iguales deben tener el mismo valor hash.

`equals` es utilizada para determinar si dos objetos son iguales. Está garantizado que el objeto de comparación será una instancia de la misma clase que el sujeto.

## Sinopsis de la interfaz

Ds\Hashable

Métodos
