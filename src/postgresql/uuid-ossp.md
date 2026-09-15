---
title: uuid-ossp — a UUID generator
source_url: https://www.postgresql.org/docs/17/uuid-ossp.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: uuid-ossp.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3730
---

## uuid-ossp a UUID generator

uuid-ossp

The `uuid-ossp` module provides functions to generate universally unique identifiers (UUIDs) using one of several standard algorithms. There are also functions to produce certain special UUID constants. This module is only necessary for special requirements beyond what is available in core PostgreSQL. See [???](#functions-uuid) for built-in ways to generate UUIDs.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

## `uuid-ossp` Functions

[Functions for UUID Generation](#uuid-ossp-functions) shows the functions available to generate UUIDs. The relevant standards ITU-T Rec. X.667, ISO/IEC 9834-8:2005, and [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122) specify four algorithms for generating UUIDs, identified by the version numbers 1, 3, 4, and 5. (There is no version 2 algorithm.) Each of these algorithms could be suitable for a different set of applications.

<table id="uuid-ossp-functions">
<caption>Functions for UUID Generation</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>uuid_generate_v1</code> () uuid</p>
<p>Generates a version 1 UUID. This involves the MAC address of the computer and a time stamp. Note that UUIDs of this kind reveal the identity of the computer that created the identifier and the time at which it did so, which might make it unsuitable for certain security-sensitive applications.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>uuid_generate_v1mc</code> () uuid</p>
<p>Generates a version 1 UUID, but uses a random multicast MAC address instead of the real MAC address of the computer.</p></td>
</tr>
<tr>
<td><p role="func_signature"><span class="indexterm"></span> <code>uuid_generate_v3</code> ( <code>namespace</code> <code>uuid</code>, <code>name</code> <code>text</code> ) uuid</p>
<p>Generates a version 3 UUID in the given namespace using the specified input name. The namespace should be one of the special constants produced by the <code>uuid_ns_*()</code> functions shown in <a href="#uuid-ossp-constants">Functions Returning UUID Constants</a>. (It could be any UUID in theory.) The name is an identifier in the selected namespace.</p>
<p>For example:</p>
<pre><code>SELECT uuid_generate_v3(uuid_ns_url(), &#39;http://www.postgresql.org&#39;);</code></pre>
<p>The name parameter will be MD5-hashed, so the cleartext cannot be derived from the generated UUID. The generation of UUIDs by this method has no random or environment-dependent element and is therefore reproducible.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>uuid_generate_v4</code> () uuid</p>
<p>Generates a version 4 UUID, which is derived entirely from random numbers.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>uuid_generate_v5</code> ( <code>namespace</code> <code>uuid</code>, <code>name</code> <code>text</code> ) uuid</p>
<p>Generates a version 5 UUID, which works like a version 3 UUID except that SHA-1 is used as a hashing method. Version 5 should be preferred over version 3 because SHA-1 is thought to be more secure than MD5.</p></td>
</tr>
</tbody>
</table>

<table id="uuid-ossp-constants">
<caption>Functions Returning UUID Constants</caption>
<thead>
<tr>
<th><p role="func_signature">Function</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p role="func_signature"><code>uuid_nil</code> () uuid</p>
<p>Returns a “nil” UUID constant, which does not occur as a real UUID.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>uuid_ns_dns</code> () uuid</p>
<p>Returns a constant designating the DNS namespace for UUIDs.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>uuid_ns_url</code> () uuid</p>
<p>Returns a constant designating the URL namespace for UUIDs.</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>uuid_ns_oid</code> () uuid</p>
<p>Returns a constant designating the ISO object identifier (OID) namespace for UUIDs. (This pertains to ASN.1 OIDs, which are unrelated to the OIDs used in PostgreSQL.)</p></td>
</tr>
<tr>
<td><p role="func_signature"><code>uuid_ns_x500</code> () uuid</p>
<p>Returns a constant designating the X.500 distinguished name (DN) namespace for UUIDs.</p></td>
</tr>
</tbody>
</table>

## Building `uuid-ossp`

Historically this module depended on the OSSP UUID library, which accounts for the module's name. While the OSSP UUID library can still be found at [](http://www.ossp.org/pkg/lib/uuid/), it is not well maintained, and is becoming increasingly difficult to port to newer platforms. `uuid-ossp` can now be built without the OSSP library on some platforms. On FreeBSD and some other BSD-derived platforms, suitable UUID creation functions are included in the core `libc` library. On Linux, macOS, and some other platforms, suitable functions are provided in the `libuuid` library, which originally came from the `e2fsprogs` project (though on modern Linux it is considered part of `util-linux-ng`). When invoking `configure`, specify `--with-uuid=bsd` to use the BSD functions, or `--with-uuid=e2fs` to use `e2fsprogs`' `libuuid`, or `--with-uuid=ossp` to use the OSSP UUID library. More than one of these libraries might be available on a particular machine, so `configure` does not automatically choose one.

## Author

Peter Eisentraut <peter_e@gmx.net>
