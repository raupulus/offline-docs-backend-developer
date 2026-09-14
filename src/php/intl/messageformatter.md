---
title: La clase MessageFormatter
source_url: https://www.php.net/manual/es/class.messageformatter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 42130
---

## Introducción

`MessageFormatter` es una clase concreta que permite producir mensajes concatenados, independientes del idioma. Las métodos proporcionadas en esta clase se utilizan para construir mensajes que están destinados a los usuarios finales.

La clase `MessageFormatter` ensambla los mensajes a partir de diferentes fragmentos (textos, números y fechas), proporcionados por el programa. Gracias a la clase `MessageFormatter`, el programa no necesita conocer el orden de los fragmentos. La clase utiliza especificaciones de formato para ensamblar los fragmentos en un solo mensaje. Por ejemplo, `MessageFormatter` permite mostrar la frase `"Finalizado de imprimir x fichero sobre y..."` de una manera que permanece flexible para la traducción.

Anteriormente, un mensaje se creaba en forma de frase, y se gestionaba como un string. Este procedimiento generaba problemas para las traducciones, ya que la estructura de la frase, el orden de las palabras, el formato de los números, etc. era muy diferente de un idioma a otro. El enfoque de creación de mensajes, independiente del idioma, permite separar el mensaje y las variables. Con estas variables, `MessageFormatter` puede concatenar las diferentes partes del mensaje, formatearlas según las convenciones correctas, y proporcionar un mensaje bien formado.

`MessageFormatter` toma una serie de objetos, formatea los textos, y los inserta en los strings formateados en los emplazamientos correctos. Una amplia variedad de formatos puede ser utilizada en conjunción con `MessageFormatter` para gestionar el plural, los números, etc. Típicamente, el mensaje es proporcionado por un recurso, y los argumentos son preparados dinámicamente.

## Sinopsis de la clase

MessageFormatter

Métodos

## Véase también

[ Documentación de formato ICU ](https://unicode-org.github.io/icu/userguide/format_parse/), [ Descripción del formato de mensajes ICU ](https://unicode-org.github.io/icu/userguide/format_parse/messages/), [Formateadores de mensajes ICU](https://unicode-org.github.io/icu/userguide/format_parse/messages/), [Formateadores de elección ICU](https://unicode-org.github.io/icu-docs/apidoc/released/icu4c/classChoiceFormat.html)
