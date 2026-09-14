---
title: Collator::setStrength
description: Establecer la fuerza de la ordenación
source_url: https://www.php.net/manual/es/collator.setstrength.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/set-strength.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: e290572f2
order: 39470
---

Collator::setStrength

collator_set_strength

Establecer la fuerza de la ordenación

## Descripción

Estilo orientado a objetos

```php
public Collator::setStrength(int $strength): true
```php

Estilo procedimental

```php
collator_set_strength(Collator $object, int $strength): true
```

El [Servicio de Ordenación ICU](https://icu.unicode.org/) admite muchos niveles de comparación (denominados "Niveles", pero también conocidos como "Fuerzas"). Al permitir que estas categorías puedan emplearse de forma selectiva, la búsqueda de una cadena en un texto puede realizarse con diversas condiciones de coincidencia.

1.  *Nivel Primario*: Normalmente, se utiliza para denotar diferencias entre caracteres base (por ejemplo, "a" \< "b"). Es la diferencia más fuerte. Por ejemplo, los diccionarios se dividen en diferentes secciones según el carácter base. También se conoce como `fuerza nivel 1`.

2.  *Nivel Secundario*: Las tildes en los caracteres se consideran diferencias secundarias (por ejemplo, "as" \< "às" \< "at"). Otras diferencias entre letras también pueden considerarse diferencias secundarias, dependiendo del idioma. Una diferencia secundaria se ignora cuando existe una diferencia primaria en cualquier parte de las cadenas. También se conoce como `fuerza nivel 2`.

    > [!NOTE]
    > Nota: En algunos idiomas (como el danés), ciertas letras acentuadas se consideran caracteres base separados. Sin embargo, en la mayoría de los idiomas, una letra acentuada solo tiene una diferencia secundaria respecto a la versión sin acentuar de esa letra.

3.  *Nivel Terciario*: Las diferencias entre mayúsculas y minúsculas en los caracteres se distinguen en el nivel terciario (por ejemplo, "ao" \< "Ao" \< "aò"). Además, una variante de una letra difiere de la forma base en el nivel terciario (como "a" y "𝒶"). Otro ejemplo es la diferencia entre Kana grande y pequeña. Una diferencia terciaria se ignora cuando existe una diferencia primaria o secundaria en cualquier parte de las cadenas. También se conoce como `fuerza nivel 3`.

4.  *Nivel Cuaternario*: Cuando la puntuación se ignora (consulte Ignorar puntuaciones) en los niveles 1-3, puede utilizarse un nivel adicional para distinguir palabras con y sin puntuación (por ejemplo, "ab" \< "a-b" \< "aB"). Esta diferencia se ignora cuando existe una diferencia primaria, secundaria o terciaria. También se conoce como `fuerza nivel 4`. El nivel cuaternario solo debe utilizarse si se requiere ignorar la puntuación o al procesar texto en japonés (consulte Procesamiento de Hiragana).

5.  *Nivel Idéntico*: Cuando todos los demás niveles son iguales, el nivel idéntico se utiliza como desempate. Los valores de punto de código Unicode de la forma NFD de cada cadena se comparan en este nivel, por si no hubiera diferencias en los niveles 1-4. Por ejemplo, los signos de entonación hebreos solo se distinguen en este nivel. Este nivel debe utilizarse con moderación, ya que la diferencia de valores de punto de código entre dos cadenas es un suceso extremadamente raro. El uso de este nivel reduce considerablemente el rendimiento tanto para la comparación incremental como para la generación de claves de ordenación (además de aumentar la longitud de la clave de ordenación). También se conoce como `fuerza nivel 5`.

Por ejemplo, las personas pueden optar por ignorar las tildes o ignorar las tildes y las mayúsculas/minúsculas al buscar texto. Casi todos los caracteres se distinguen por los tres primeros niveles, y en la mayoría de los entornos regionales el valor por omisión es, por tanto, el Terciario. Sin embargo, si Alternate se establece en Shifted, entonces la fuerza Cuaternaria puede utilizarse para desempatar entre espacios en blanco, puntuaciones y símbolos que, de otro modo, se ignorarían. Si se requieren distinciones muy finas entre caracteres, puede utilizarse la fuerza Idéntica (por ejemplo, la fuerza Idéntica distingue entre la A pequeña negrita matemática y la A pequeña cursiva matemática). No obstante, el uso de niveles superiores al Terciario o la fuerza Idéntica genera claves de ordenación significativamente más largas y un rendimiento más lento en la comparación de cadenas iguales.

## Parámetros

`object`  
Objeto `Collator`.

`strength`  
Fuerza a establecer.

Los valores posibles son:

- `Collator::PRIMARY`

- `Collator::SECONDARY`

- `Collator::TERTIARY`

- `Collator::QUATERNARY`

- `Collator::IDENTICAL`

- `Collator::DEFAULT_STRENGTH`

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo de `collator_set_strength`

```php
<?php
$arr  = array( 'aò', 'Ao', 'ao' );
$coll = collator_create( 'en_US' );

// Ordenar el array usando la fuerza por omisión.
collator_sort( $coll, $arr );
var_export( $arr );

// Ordenar el array usando la fuerza primaria.
collator_set_strength( $coll, Collator::PRIMARY );
collator_sort( $coll, $arr );
var_export( $arr );
?>

    
```

El ejemplo anterior mostrará:

    array (
      0 => 'ao',
      1 => 'Ao',
      2 => 'aò',
    )
    array (
      0 => 'aò',
      1 => 'Ao',
      2 => 'ao',
    )

## Véase también

[Constantes de Collator](#intl.collator-constants), `collator_get_strength`
