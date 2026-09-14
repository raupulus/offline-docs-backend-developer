---
title: Lidiar con errores
source_url: https://docs.python.org/es/3
source_path: bugs.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
order: 20
---

# Lidiar con errores

Python es un lenguaje de programación maduro que ha establecido una
reputación de estabilidad.  Con el fin de mantener esta reputación, a
los desarrolladores les gustaría conocer cualquier anomalía que
encuentre en Python.

It can be sometimes faster to fix bugs yourself and contribute patches
to Python as it streamlines the process and involves fewer people.
Learn how to contribute.

## Documentación de errores

If you find a bug in this documentation or would like to propose an
improvement, please submit a bug report on the issue tracker.  If you
have a suggestion on how to fix it, include that as well.

If the bug or suggested improvement concerns the translation of this
documentation, submit the report to the translation’s repository
instead.

También puede abrir una discusión en nuestro foro de Documentación de
Discourse.

If you find a bug in the theme (HTML / CSS / JavaScript) of the
documentation, please submit a bug report on the python-doc-theme
issue tracker.

Ver también:

  Documentación de errores
     Una lista de errores (*bugs*) que ha sido enviada al issue
     tracker (sistema de seguimiento de incidentes) de Python.

  Seguimiento de incidencias
     Resumen general del proceso necesario para reportar una mejora en
     el tracker.

  Ayudar con la documentación
     Guía detallada para gente interesada en contribuir a la
     documentación de Python.

  Documentation Translations
     Una lista de páginas de GitHub para la traducción de
     documentación y sus contactos principales.

## Utilizar el issue tracker de Python

Los informes de incidencias de Python deben enviarse a través del
gestor de incidencias de GitHub
(https://github.com/python/cpython/issues). El gestor de incidencias
de GitHub ofrece un formulario web que permite introducir la
información pertinente y enviarla a los desarrolladores.

El primer paso para completar un informe es determinar si el problema
ya ha sido descrito previamente.  La ventaja de hacer esto, aparte de
ahorrar tiempo a los desarrolladores, es que te permite aprender qué
cambios se han realizado para repararlo; puede que el problema se haya
reparado para la siguiente versión, o que sea necesaria información
adicional (en ese caso, ¡te invitamos a incluirla si puedes!). Para
hacerlo, busca en la base de datos de errores usando la zona de
búsqueda al principio de esta página.

Si el problema del que informa no está ya en la lista, inicie sesión
en GitHub. Si aún no tienes una cuenta en GitHub, crea una nueva a
través del enlace "Regístrate". No es posible enviar un informe de
error de forma anónima.

Ahora que has iniciado sesión, puedes enviar un informe de error. Haz
clic en el botón "New issue" de la barra superior para notificar un
nuevo informe de error.

El formulario de envío tiene dos campos: "Title" y "Comment".

En el campo "Title", introduzca una descripción *muy* breve del
problema; menos de diez palabras es suficiente.

En el campo "Comment", describe el problema con detalle, incluyendo
qué esperabas que ocurriera y que ha sucedido en realidad. Asegúrate
de incluir si cualquier módulo de extensión está involucrado, y qué
plataformas de hardware y software estás usando (incluyendo las
versiones correspondientes).

Cada informe de error será asignado a un desarrollador que determinará
qué es necesario hacer para corregir el problema. Recibirás una
actualización cada vez que se tome una medida al respecto.

Ver también:

  Cómo informar de errores de manera efectiva
     Artículo que detalla cómo crear un informe de errores útil.
     Describe qué tipo de información es útil y por qué lo es.

  Bug Writing Guidelines
     Información sobre cómo escribir un buen informe de errores. Parte
     de esta información es específica al proyecto Mozilla, pero en
     general describe buenas prácticas.

## Para empezar a contribuir en Python

Más allá de informar de los errores que puedas encontrar, te damos la
bienvenida a enviar parches para corregirlos.  Puedes encontrar más
información en cómo empezar parcheando Python  en la Python
Developer's Guide. Si tienes preguntas, el core-mentorship mailing
list es un agradable lugar para obtener respuestas a cualquiera y a
todas las preguntas pertenecientes al proceso de corrección de
problemas en Python.
