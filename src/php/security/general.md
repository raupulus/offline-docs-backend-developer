---
title: Consideraciones generales
source_url: https://www.php.net/manual/es/security.general.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/general.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: 96c9d88ba
order: 109950
---

## Consideraciones generales

Un sistema completamente seguro es prácticamente un imposible, de modo que el enfoque usado con mayor frecuencia en la profesión de seguridad es uno que busque el balance adecuado entre riesgo y funcionalidad. Si cada variable enviada por un usuario requiriera de dos formas de validación biométrica (como rastreo de retinas y análisis dactilar), usted contaría con un nivel extremadamente alto de confiabilidad. También implicaría que llenar los datos de un formulario razonablemente complejo podría tomar media hora, cosa que podría incentivar a los usuarios a buscar métodos para esquivar los mecanismos de seguridad.

La mejor seguridad con frecuencia es lo suficientemente razonable como para suplir los requerimientos dados sin prevenir que el usuario realice su labor de forma natural, y sin sobrecargar al autor del código con una complejidad excesiva. De hecho, algunos ataques de seguridad son simples recursos que aprovechan las vulnerabilidades de este tipo de seguridad sobrecargada, que tiende a erosionarse con el tiempo.

Una frase que vale la pena recordar: Un sistema es apenas tan bueno como el eslabón más débil de una cadena. Si todas las transacciones son registradas copiosamente basándose en la fecha/hora, ubicación, tipo de transacción, etc. pero la verificación del usuario se realiza únicamente mediante una cookie sencilla, la validez de atar a los usuarios al registro de transacciones es mermada severamente.

Cuando realice pruebas, tenga en mente que no será capaz de probar todas las diferentes posibilidades, incluso para las páginas más simples. Los datos de entrada que usted puede esperar en sus aplicaciones no necesariamente tendrán relación alguna con el tipo de información que podría ingresar un empleado disgustado, un cracker con meses de tiempo entre sus manos, o un gato doméstico caminando sobre el teclado. Es por esto que es mejor observar el código desde una perspectiva lógica, para determinar en dónde podrían introducirse datos inesperados, y luego hacer un seguimiento de cómo esta información es modificada, reducida o amplificada.

Internet está repleto de personas que tratan de crearse fama al romper la seguridad de su código, bloquear su sitio, publicar contenido inapropiado, y por lo demás haciendo que sus días sean más interesantes. No importa si usted administra un sitio pequeño o grande, usted es un objetivo por el simple hecho de estar en línea, por tener un servidor al cual es posible conectarse. Muchas aplicaciones de cracking no hacen distinciones por tamaños, simplemente recorren bloques masivos de direcciones IP en busca de víctimas. Trate de no convertirse en una.
