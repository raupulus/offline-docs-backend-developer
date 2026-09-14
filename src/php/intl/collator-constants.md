---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/intl.collator-constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator-constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1f68eecaa
order: 39500
---

## Constantes predefinidas

`Collator::FRENCH_COLLATION` `int`  
Se ordenan los strings con diferentes acentos, al final de la cadena. Este atributo se configura automáticamente a *On* para las locales francesas, y algunas otras. Los usuarios no necesitan configurar explícitamente este atributo. Existe un coste de rendimiento al comparar strings cuando este atributo está a *On*, pero el tamaño de las claves de ordenación permanece inalterado. Los valores posibles son: `Collator::ON`, `Collator::OFF`(por omisión), `Collator::DEFAULT_VALUE`

Reglas de FRENCH_COLLATION

F=OFF cote \< coté \< côte \< côté, F=ON cote \< côte \< coté \< côté

`Collator::ALTERNATE_HANDLING`  
El atributo alterno se utiliza para controlar el manejo de caracteres variables de UCA: espacios en blanco, puntuación y símbolos. Si Alternate está configurado a *NonIgnorable* (N), entonces las diferencias entre estos caracteres tienen la misma importancia que las diferencias entre letras. Si Alternate está configurado a *Shifted* (S), entonces estos caracteres tendrán una importancia menor. El valor *Shifted* se utiliza a menudo conjuntamente con Quaternary que vale *Strength*. En este caso, los espacios en blanco, la puntuación y los símbolos se consideran durante la comparación, pero únicamente si los otros aspectos de la cadena (letras base, acentos y mayúsculas) son todos idénticos. Si Alternate no está configurado a Shifted, no hay entonces diferencia entre una Strength de 3 y una Strength de 4. Para más información y ejemplos, véase Variable_Weighting en [UCA](https://www.unicode.org/reports/tr10/). La razón por la que los valores de Alternate no son simplemente *On* y *Off* es que valores adicionales para Alternate podrían ser añadidos en el futuro. La opción UCA Blanked se expresa con un valor de Strength a 3, y Alternate configurado a Shifted. El valor por omisión para la mayoría de locales es NonIgnorable. Si Shifted es seleccionado, puede ser más lento si hay muchas cadenas que son idénticas, excepto por la puntuación: el tamaño de la clave de ordenación permanecerá inalterado, a menos que el nivel de Strength sea elevado.

Los valores posibles son: `Collator::NON_IGNORABLE`(por omisión), `Collator::SHIFTED`, `Collator::DEFAULT_VALUE`

Reglas ALTERNATE_HANDLING

S=3, A=N di Silva \< Di Silva \< diSilva \< U.S.A. \< USA, S=3, A=S di Silva = diSilva \< Di Silva \< U.S.A. = USA, S=4, A=S di Silva \< diSilva \< Di Silva \< U.S.A. \< USA

`Collator::CASE_FIRST` `int`  
El atributo Case_First se utiliza para controlar si las mayúsculas deben ser consideradas antes que las minúsculas, y viceversa, en ausencia de otros discriminantes. Los valores posibles son *Uppercase_First* (U) y *Lowercase_First* (L), más los valores estándar *Default* y *Off*. No hay casi diferencia entre Off y Lowercase_First en términos de resultados, por lo que los usuarios típicos no utilizarán Lowercase_First: únicamente Off o Uppercase_First. (Aquellos interesados en las diferencias entre X y L deberán consultar la sección `Collation Customization`). Especificar L o U no cambiará el rendimiento de comparación, pero afectará el tamaño de la clave de ordenación.

Los valores posibles son: `Collator::OFF`(por omisión), `Collator::LOWER_FIRST`, `Collator::UPPER_FIRST`, `Collator:DEFAULT`

Reglas CASE_FIRST

C=X or C=L "china" \< "China" \< "denmark" \< "Denmark", C=U "China" \< "china" \< "Denmark" \< "denmark"

`Collator::CASE_LEVEL` `int`  
El atributo Case_Level se utiliza para ignorar los acentos, pero no la casilla. En estas situaciones, póngase el atributo Strength a *Primary*, y Case_Level a *On*. En la mayoría de locales, este atributo está a Off por omisión. Existe un pequeño coste de rendimiento para la comparación de cadenas, e impacto en el tamaño de los índices de ordenación si este atributo está a *On*.

Los valores posibles son: `Collator::OFF`(por omisión), `Collator::ON`, `Collator::DEFAULT_VALUE`

Reglas CASE_LEVEL

S=1, E=X role = Role = rôle, S=1, E=O role = rôle \< Role

`Collator::NORMALIZATION_MODE` `int`  
El atributo Normalization determina si se debe normalizar totalmente el texto o no, para la comparación. Aunque este atributo esté a Off (que es el caso por omisión para muchas locales), los textos comparados para un uso ordinario serán correctos (para detalles, véase UTN \#5). Solo habrá un problema si las marcas de acento no son canónicas. Si este atributo está a *On*, entonces los mejores resultados están garantizados para todos los textos. Existe un coste de comparación medio si este atributo vale *On*, dependiendo de la frecuencia de las secuencias que requieren normalización. No hay efecto significativo en el tamaño de los índices de ordenación. Si el texto está en las formas de normalización NFD o NFKD, no es necesario activar la opción de Normalization.

Los valores posibles son: `Collator::OFF`(por omisión), `Collator::ON`, `Collator::DEFAULT_VALUE`

`Collator::STRENGTH` `int`  
El servicio de collation ICU soporta muchos niveles de comparación (llamados "Levels", pero también conocidos como "Strengths"). Con estas categorías, ICU puede ordenar strings con precisión, según las convenciones locales. Sin embargo, permitiendo el uso selectivo de los niveles, la búsqueda de un string en un texto puede ser realizada, a partir de diferentes condiciones. Para más información, véase el capítulo `collator_set_strength`.

Los valores posibles son: `Collator::PRIMARY`, `Collator::SECONDARY`, `Collator::TERTIARY`(por omisión), `Collator::QUATERNARY`, `Collator::IDENTICAL`, `Collator::DEFAULT_VALUE`

`Collator::HIRAGANA_QUATERNARY_MODE` `int`  
La compatibilidad con JIS x 4061 requiere la introducción de un nivel adicional para distinguir caracteres Hiragana y Katakana. Si la compatibilidad con el estándar es necesaria, entonces este atributo debe ser utilizado a *On*, y la Strength debe tomar el valor de Quaternary. Esto afectará el tamaño de los índices de ordenación, y el rendimiento de comparaciones de strings.

Los valores posibles son: `Collator::OFF`(por omisión), `Collator::ON`, `Collator::DEFAULT_VALUE`

`Collator::NUMERIC_COLLATION` `int`  
Cuando está activado, este atributo genera una clave de collation para los valores numéricos de sub-cadenas. Es un método para que '100' sea ordenado después de '2'.

Los valores posibles son: `Collator::OFF`(por omisión), `Collator::ON`, `Collator::DEFAULT_VALUE`

`Collator::DEFAULT_VALUE` `int`  

`Collator::PRIMARY` `int`  

`Collator::SECONDARY` `int`  

`Collator::TERTIARY` `int`  

`Collator::DEFAULT_STRENGTH` `int`  

`Collator::QUATERNARY` `int`  

`Collator::IDENTICAL` `int`  

`Collator::OFF` `int`  

`Collator::ON` `int`  

`Collator::SHIFTED` `int`  

`Collator::NON_IGNORABLE` `int`  

`Collator::LOWER_FIRST` `int`  

`Collator::UPPER_FIRST` `int`  

`Collator::SORT_REGULAR` `int`  

`Collator::SORT_STRING` `int`  

`Collator::SORT_NUMERIC` `int`
