---
title: '"email" --- An email and MIME handling package'
source_url: https://docs.python.org/es/3
source_path: library/email.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2520
---

# "email" --- An email and MIME handling package

**Código fuente** Lib/email/__init__.py

======================================================================

The "email" package is a library for managing email messages.  It is
specifically *not* designed to do any sending of email messages to
SMTP (**RFC 2821**), NNTP, or other servers; those are functions of
modules such as "smtplib".  The "email" package attempts to be as RFC-
compliant as possible, supporting **RFC 5322** and **RFC 6532**, as
well as such MIME-related RFCs as **RFC 2045**, **RFC 2046**, **RFC
2047**, **RFC 2183**, and **RFC 2231**.

La estructura general del paquete de correo electrónico se puede
dividir en tres componentes principales, más un cuarto componente que
controla el comportamiento de los otros componentes.

El componente central del paquete es un "modelo de objetos" que
representa los mensajes de correo electrónico. Una aplicación
interactúa con el paquete principalmente a través de la interfaz del
modelo de objetos definida en el submódulo "message". La aplicación
puede usar esta API para hacer preguntas sobre un correo electrónico
existente, para construir un nuevo correo electrónico o para agregar o
eliminar subcomponentes de correo electrónico que utilizan la misma
interfaz de modelo de objetos. Es decir, siguiendo la naturaleza de
los mensajes de correo electrónico y sus subcomponentes MIME, el
modelo de objetos de correo electrónico es una estructura de árbol de
objetos que proporcionan la API "EmailMessage".

Los otros dos componentes principales del paquete son "parser" y
"generator". El parser toma la versión serializada de un mensaje de
correo electrónico (una secuencia de bytes) Y la convierte en un árbol
de objetos "EmailMessage". El generador toma un "EmailMessage" y lo
convierte de nuevo en un flujo de bytes serializado. (El analizador y
el generador también manejan flujos de caracteres de texto, pero se
desaconseja este uso ya que es demasiado fácil terminar con mensajes
que no son válidos de una forma u otra).

El componente de control es el módulo de "policy". Cada "EmailMessage"
cada "generator", y cada "parser" tiene un objeto de "policy" asociado
que controla su comportamiento. Por lo general, una aplicación solo
necesita especificar la política cuando se crea un "EmailMessage" , ya
sea instanciando directamente un "EmailMessage" para crear un nuevo
correo electrónico o analizando un flujo de entrada con un "parser".
Pero la política se puede cambiar cuando el mensaje se serializa
mediante un "generator". Esto permite, por ejemplo, analizar un
mensaje de correo electrónico genérico desde el disco, pero
serializarlo utilizando la configuración estándar de SMTP al enviarlo
a un servidor de correo electrónico.

El paquete de correo electrónico hace todo lo posible para ocultar los
detalles de las diversas RFC que rigen de la aplicación.
Conceptualmente, la aplicación debería poder tratar el mensaje de
correo electrónico como un árbol estructurado de texto Unicode y
archivos adjuntos binarios, sin tener que preocuparse por cómo se
representan estos cuando se serializan. En la práctica, sin embargo, a
menudo es necesario conocer al menos algunas de las reglas que rigen
los mensajes MIME y su estructura, específicamente los nombres y la
naturaleza de los «tipos de contenido» MIME y cómo identifican los
documentos de varias partes. En su mayor parte, este conocimiento solo
debería ser necesario para aplicaciones más complejas, e incluso
entonces debería ser solo la estructura de alto nivel en cuestión, y
no los detalles de cómo se representan esas estructuras. Dado que los
tipos de contenido MIME se utilizan ampliamente en el software moderno
de Internet (no solo en el correo electrónico), este será un concepto
familiar para muchos programadores.

The following sections describe the functionality of the "email"
package. We start with the "message" object model, which is the
primary interface an application will use, and follow that with the
"parser" and "generator" components.  Then we cover the "policy"
controls, which completes the treatment of the main components of the
library.

Las siguientes tres secciones cubren las excepciones que puede generar
el paquete y los defectos (incumplimiento de las RFC) que el "parser"
puede detectar. Luego cubrimos los subcomponentes "headerregistry" y
"contentmanager", que proporcionan herramientas para realizar una
manipulación más detallada de los encabezados y cargas útiles,
respectivamente. Ambos componentes contienen características
relevantes para consumir y producir mensajes no triviales, pero
también documentan sus API de extensibilidad, que serán de interés
para aplicaciones avanzadas.

A continuación, se muestra un conjunto de ejemplos del uso de las
partes fundamentales de las API cubiertas en las secciones anteriores.

Lo anterior representa la API moderna (compatible con Unicode) del
paquete de correo electrónico. Las secciones restantes, comenzando con
la clase "Message", cubren la API "compat32" heredada que trata mucho
más directamente con los detalles de cómo se representan los mensajes
de correo electrónico. La API "compat32" no oculta los detalles de las
RFC de la aplicación, pero para las aplicaciones que necesitan operar
a ese nivel, pueden ser herramientas útiles. Esta documentación
también es relevante para las aplicaciones que todavía usan la API
"compat32" por razones de compatibilidad con versiones anteriores.

Distinto en la versión 3.6: Documentos reorganizados y reescritos para
promover la nueva API "EmailMessage"/"EmailPolicy".

Contents of the "email" package documentation:

* "email.message": Representing an email message

* "email.parser": Parsing email messages

  * API *FeedParser*

  * API *Parser*

  * Notas adicionales

* "email.generator": Generating MIME documents

* "email.policy": Policy Objects

* "email.errors": Exception and Defect classes

* "email.headerregistry": Custom Header Objects

* "email.contentmanager": Managing MIME Content

  * Instancias gestoras de contenido

* "email": Ejemplos

API heredada:

* "email.message.Message": Representar un mensaje de correo
  electrónico usando la API "compat32"

* "email.mime": Creating email and MIME objects from scratch

* "email.header": Internationalized headers

* "email.charset": Representing character sets

* "email.encoders": Encoders

* "email.utils": Miscellaneous utilities

* "email.iterators": Iterators

Ver también:

  Módulo "smtplib"
     Cliente SMTP (Protocolo simple de transporte de correo)

  Módulo "poplib"
     Cliente POP (Protocolo de oficina postal)

  Módulo "imaplib"
     Cliente IMAP (Protocolo de acceso a mensajes de Internet)

  Módulo "mailbox"
     Herramientas para crear, leer y administrar colecciones de
     mensajes en disco utilizando una variedad de formatos estándar.
