---
title: yaz_itemorder
description: Prepara para la solicitud Z39.50 Item Order con el paquete ILL-Request
source_url: https://www.php.net/manual/es/function.yaz-itemorder.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-itemorder.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 107870
---

yaz_itemorder

Prepara para la solicitud Z39.50 Item Order con el paquete ILL-Request

## Descripción

```php
yaz_itemorder(resource $id, array $args): void
```php

Esta función prepara para una petición de tipo "Extended Services" utilizando el "Profile" para "Use of Z39.50 Item Order Extended Service to Transport ILL (Profile/1)". Ver [aquí](http://www.collectionscanada.ca/iso/ill/stanprf.htm) y la [especificación](http://www.collectionscanada.ca/iso/ill/document/standard/z-ill-1a.pdf).

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`args`  
Debe ser un array asociativo con información sobre la solicitud de los elementos que serán enviados. La clave de la tabla hash es el nombre del camino de acceso ASN.1 correspondiente. Por ejemplo, el ISBN bajo el Item-ID tiene la clave item-id,ISBN.

Los parámetros de la petición ILL son:

\
protocol-version-num\
transaction-id,initial-requester-id,person-or-institution-symbol,person\
transaction-id,initial-requester-id,person-or-institution-symbol,institution\
transaction-id,initial-requester-id,name-of-person-or-institution,name-of-person\
transaction-id,initial-requester-id,name-of-person-or-institution,name-of-institution\
transaction-id,transaction-group-qualifier\
transaction-id,transaction-qualifier\
transaction-id,sub-transaction-qualifier\
service-date-time,this,date\
service-date-time,this,time\
service-date-time,original,date\
service-date-time,original,time\
requester-id,person-or-institution-symbol,person\
requester-id,person-or-institution-symbol,institution\
requester-id,name-of-person-or-institution,name-of-person\
requester-id,name-of-person-or-institution,name-of-institution\
responder-id,person-or-institution-symbol,person\
responder-id,person-or-institution-symbol,institution\
responder-id,name-of-person-or-institution,name-of-person\
responder-id,name-of-person-or-institution,name-of-institution\
transaction-type\
delivery-address,postal-address,name-of-person-or-institution,name-of-person\
delivery-address,postal-address,name-of-person-or-institution,name-of-institution\
delivery-address,postal-address,extended-postal-delivery-address\
delivery-address,postal-address,street-and-number\
delivery-address,postal-address,post-office-box\
delivery-address,postal-address,city\
delivery-address,postal-address,region\
delivery-address,postal-address,country\
delivery-address,postal-address,postal-code\
delivery-address,electronic-address,telecom-service-identifier\
delivery-address,electronic-address,telecom-service-addreess\
billing-address,postal-address,name-of-person-or-institution,name-of-person\
billing-address,postal-address,name-of-person-or-institution,name-of-institution\
billing-address,postal-address,extended-postal-delivery-address\
billing-address,postal-address,street-and-number\
billing-address,postal-address,post-office-box\
billing-address,postal-address,city\
billing-address,postal-address,region\
billing-address,postal-address,country\
billing-address,postal-address,postal-code\
billing-address,electronic-address,telecom-service-identifier\
billing-address,electronic-address,telecom-service-addreess\
ill-service-type\
requester-optional-messages,can-send-RECEIVED\
requester-optional-messages,can-send-RETURNED\
requester-optional-messages,requester-SHIPPED\
requester-optional-messages,requester-CHECKED-IN\
search-type,level-of-service\
search-type,need-before-date\
search-type,expiry-date\
search-type,expiry-flag\
place-on-hold\
client-id,client-name\
client-id,client-status\
client-id,client-identifier\
item-id,item-type\
item-id,call-number\
item-id,author\
item-id,title\
item-id,sub-title\
item-id,sponsoring-body\
item-id,place-of-publication\
item-id,publisher\
item-id,series-title-number\
item-id,volume-issue\
item-id,edition\
item-id,publication-date\
item-id,publication-date-of-component\
item-id,author-of-article\
item-id,title-of-article\
item-id,pagination\
item-id,ISBN\
item-id,ISSN\
item-id,additional-no-letters\
item-id,verification-reference-source\
copyright-complicance\
retry-flag\
forward-flag\
requester-note\
forward-note\
      

También hay unos pocos parámetros que son parte del Paquete de Solicitud de Servicios Extendidos y el paquete ItemOrder:

\
package-name\
user-id\
contact-name\
contact-phone\
contact-email\
itemorder-item\
      

## Valores devueltos

No se retorna ningún valor.
