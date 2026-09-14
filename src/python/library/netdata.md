---
title: Manejo de datos de internet
source_url: https://docs.python.org/es/3
source_path: library/netdata.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3300
---

# Manejo de datos de internet

Este capítulo describe los módulos que admiten el manejo de formatos
de datos comúnmente usados en Internet.

* "email" --- An email and MIME handling package

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

  * "email.message.Message": Representar un mensaje de correo
    electrónico usando la API "compat32"

  * "email.mime": Creating email and MIME objects from scratch

  * "email.header": Internationalized headers

  * "email.charset": Representing character sets

  * "email.encoders": Encoders

  * "email.utils": Miscellaneous utilities

  * "email.iterators": Iterators

* "json" --- JSON encoder and decoder

  * Uso básico

  * Codificadores y Decodificadores

  * Excepciones

  * Cumplimiento e interoperabilidad estándar

    * Codificaciones de caracteres

    * Valores de número infinito y NaN

    * Nombres repetidos dentro de un objeto

    * Valores de nivel superior No-Objeto , No-Arreglo

    * Limitaciones de la implementación

  * Command-line interface

    * Command-line options

* "mailbox" --- Manipulate mailboxes in various formats

  * "Mailbox" objects

    * "Maildir" objects

    * "mbox" objects

    * "MH" objects

    * "Babyl" objects

    * "MMDF" objects

  * "Message" objects

    * "MaildirMessage" objects

    * "mboxMessage" objects

    * "MHMessage" objects

    * "BabylMessage" objects

    * "MMDFMessage" objects

  * Excepciones

  * Ejemplos

* "mimetypes" --- Map filenames to MIME types

  * MimeTypes objects

  * Command-line usage

  * Command-line example

* "base64" --- Base16, Base32, Base64, Base85 Data Encodings

  * RFC 4648 Encodings

  * Base85 Encodings

  * Legacy Interface

  * Consideraciones de Seguridad

* "binascii" --- Convert between binary and ASCII

* "quopri" --- Encode and decode MIME quoted-printable data
