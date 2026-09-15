---
title: Network applications
source_url: https://www.debian.org/doc/manuals/debian-reference/_network_applications
source_repo: https://salsa.debian.org/debian/debian-reference.git
source_ref: master
source_commit: b7239e647
source_path: 06_network_applications.rawxml
technology: debian
version: 12 (Bookworm)
license: GPL-2.0-or-later
retrieved_at: '2026-09-15'
order: 70
---

## Network applications

After establishing network connectivity (see [???](#_network_setup)), you can run various network applications.

> [!TIP]
> For modern Debian specific guide to the network infrastructure, read [The Debian Administrator's Handbook — Network Infrastructure](https://www.debian.org/doc/manuals/debian-handbook/network-infrastructure).

> [!TIP]
> If you enabled "2-Step Verification" with some ISP, you need to obtain an application password to access POP and SMTP services from your program. You may need to approve your host IP in advance.

## Web browsers

There are many [web browser](https://en.wikipedia.org/wiki/Web_Browsers) packages to access remote contents with [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (HTTP).

| package | popcon | size | type | description of web browser |
|:---|:---|:---|:---|:---|
| `chromium` | @-@popcon1@-@ | @-@psize1@-@ | X | [Chromium](https://en.wikipedia.org/wiki/Chromium_(web_browser)), (open-source browser from Google) |
| `firefox` | @-@popcon1@-@ | @-@psize1@-@ | , , | [Firefox](https://en.wikipedia.org/wiki/Firefox), (open-source browser from Mozilla, only available in Debian Unstable) |
| `firefox-esr` | @-@popcon1@-@ | @-@psize1@-@ | , , | [Firefox ESR](https://en.wikipedia.org/wiki/Firefox#Extended_Support_Release), (Firefox Extended Support Release) |
| `epiphany-browser` | @-@popcon1@-@ | @-@psize1@-@ | , , | [GNOME](https://en.wikipedia.org/wiki/GNOME), [HIG](https://en.wikipedia.org/wiki/Human_interface_guidelines) compliant, [Epiphany](https://en.wikipedia.org/wiki/Epiphany_(browser)) |
| `konqueror` | @-@popcon1@-@ | @-@psize1@-@ | , , | [KDE](https://en.wikipedia.org/wiki/KDE), [Konqueror](https://en.wikipedia.org/wiki/Konqueror) |
| `dillo` | @-@popcon1@-@ | @-@psize1@-@ | , , | [Dillo](https://en.wikipedia.org/wiki/Dillo), (light weight browser, [FLTK](https://en.wikipedia.org/wiki/FLTK) based) |
| `w3m` | @-@popcon1@-@ | @-@psize1@-@ | text | [w3m](https://en.wikipedia.org/wiki/W3m) |
| `lynx` | @-@popcon1@-@ | @-@psize1@-@ | , , | [Lynx](https://en.wikipedia.org/wiki/Lynx_(web_browser)) |
| `elinks` | @-@popcon1@-@ | @-@psize1@-@ | , , | [ELinks](https://en.wikipedia.org/wiki/ELinks) |
| `links` | @-@popcon1@-@ | @-@psize1@-@ | , , | [Links](https://en.wikipedia.org/wiki/Links_(web_browser)) (text only) |
| `links2` | @-@popcon1@-@ | @-@psize1@-@ | graphics | [Links](https://en.wikipedia.org/wiki/Links_(web_browser)) (console graphics without X) |

List of web browsers

### Browser configuration

You may be able to use following special URL strings for some browsers to confirm their settings.

- "`about:`"

- "`about:config`"

- "`about:plugins`"

Debian offers many free browser plugin packages in the main archive area which can handle not only [Java (software platform)](https://en.wikipedia.org/wiki/Java_(software_platform)) and [Flash](https://en.wikipedia.org/wiki/Adobe_Flash) but also [MPEG](https://en.wikipedia.org/wiki/MPEG-1), [MPEG2](https://en.wikipedia.org/wiki/MPEG-2), [MPEG4](https://en.wikipedia.org/wiki/MPEG-4), [DivX](https://en.wikipedia.org/wiki/DivX), [Windows Media Video (.wmv)](https://en.wikipedia.org/wiki/Windows_Media_Video), [QuickTime (.mov)](https://en.wikipedia.org/wiki/QuickTime), [MP3 (.mp3)](https://en.wikipedia.org/wiki/MP3), [Ogg/Vorbis](https://en.wikipedia.org/wiki/Vorbis) files, DVDs, VCDs, etc. Debian also offers helper programs to install non-free browser plugin packages as contrib or non-free archive area.

| package | popcon | size | area | description |
|:---|:---|:---|:---|:---|
| `pepperflashplugin-nonfree` | @-@popcon1@-@ | @-@psize1@-@ | contrib | Pepper Flash Player - browser plugin |
| `browser-plugin-freshplayer-pepperflash` | @-@popcon1@-@ | @-@psize1@-@ | contrib | PPAPI-host NPAPI-plugin adapter for pepperflash |

List of browser plugin packages

> [!TIP]
> Although use of above Debian packages are much easier, browser plugins can be still manually enabled by installing "\*.so" into plugin directories (e.g., "`/usr/lib/iceweasel/plugins/`") and restarting browsers.

Some web sites refuse to be connected based on the user-agent string of your browser. You can work around this situation by [spoofing the user-agent string](http://www.mozilla.org/unix/customizing.html#prefs). For example, you can do this by adding following line into user configuration files such as "`~/.gnome2/epiphany/mozilla/epiphany/user.js`" or "`~/.mozilla/firefox/*.default/user.js`".

    user_pref{"general.useragent.override","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"};

Alternatively, you can add and reset this variable by typing "`about:config`" into URL and right clicking its display contents.

> [!CAUTION]
> Spoofed user-agent string may cause [bad side effects with Java](https://bugzilla.mozilla.org/show_bug.cgi?id=83376).

## The mail system

> [!CAUTION]
> If you are to set up the mail server to exchange mail directly with the Internet, you should be better than reading this elementary document.

The mail system involves many server programs and many client programs running on multiple hosts. From the functionality, there are 3 types of mail agent programs:

- The mail transport agent ([MTA](https://en.wikipedia.org/wiki/Message_transfer_agent), see [Mail transport agent (MTA)](#_mail_transport_agent_mta)) is a program for transferring mails between different hosts.

- The mail delivery agent ([MDA](https://en.wikipedia.org/wiki/Mail_delivery_agent), see [Mail delivery agent (MDA) with filter](#_mail_delivery_agent_mda_with_filter)) is a program for delivering messages to the users' mailboxes within a host.

- The mail user agent (MUA, also known as [email client](https://en.wikipedia.org/wiki/Email_client), see [Mail user agent (MUA)](#_mail_user_agent_mua)) is the program to generate messages and to access delivered messages.

> [!NOTE]
> The following configuration examples are only valid for the typical mobile workstation on consumer grade Internet connections.

### Email basics

An [email](https://en.wikipedia.org/wiki/Email) message consists of three components, the message envelope, the message header, and the message body.

The "To" and "From" information in the message envelope is used by the [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) to deliver the email. (The "From" information in the message envelope is also called [bounce address](https://en.wikipedia.org/wiki/Bounce_address), From\_, etc.).

The "To" and "From" information in the message header is displayed by the [email client](https://en.wikipedia.org/wiki/Email_client). (While it is most common for these to be the same as ones in the message envelope, such is not always the case.)

The [email client](https://en.wikipedia.org/wiki/Email_client) (MUA) needs to interpret the message header and body data using [Multipurpose Internet Mail Extensions (MIME)](https://en.wikipedia.org/wiki/MIME) to deal the content data type and encoding.

### Modern mail service basics

In order to minimize exposure to the spam (unwanted and unsolicited email) problems, many ISPs which provide consumer grade Internet connections are implementing counter measures.

- The smarthost service for their customers to send message uses the message submission port (587) specified in [rfc4409](http://tools.ietf.org/html/rfc4409) with the password ([SMTP AUTH](https://en.wikipedia.org/wiki/SMTP-AUTH) service) specified in [rfc4954](http://tools.ietf.org/html/rfc4954).

- The [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) port (25) connection from their internal network hosts (except ISP's own outgoing mail server) to the Internet are blocked.

- The [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) port (25) connection to the ISP's incoming mail server from some suspicious external network hosts are blocked. (The connection from hosts on the dynamic IP address range used by the dial-up and other consumer grade Internet connections are the first ones to be blocked.)

- [Anti-spam techniques](https://en.wikipedia.org/wiki/Anti-spam_techniques) such as [DomainKeys Identified Mail (DKIM)](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), [Sender_Policy_Framework (SPF)](https://en.wikipedia.org/wiki/Sender_Policy_Framework), and [Domain-based Message Authentication, Reporting and Conformance (DMARC)](https://en.wikipedia.org/wiki/DMARC) are widely used for the [email filtering](https://en.wikipedia.org/wiki/Email_filtering).

- The [DomainKeys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) service may be provided for your mail sent through the smarthost.

- The smarthost may rewrite the source mail address to your mail account on the smarthost.

When configuring your mail system or resolving mail delivery problems, you must consider these new limitations.

> [!CAUTION]
> It is not realistic to run SMTP server on consumer grade network to send mail directly to the remote host reliably.

> [!CAUTION]
> It is not realistic to expect a single smarthost to send mails of unrelated source mail addresses to the remote host reliably.

> [!CAUTION]
> A mail may be rejected by any host en route to the destination quietly. Making your mail to appear as authentic as possible is the only way to send a mail to the remote host reliably.

In light of these hostile Internet situation and limitations, some independent Internet mail ISPs such as Yahoo.com and Gmail.com offer the secure mail service which can be connected from anywhere on the Internet using [Transport Layer Security (TLS) and its predecessor, Secure Sockets Layer (SSL)](https://en.wikipedia.org/wiki/Transport_Layer_Security).

- The smarthost service on port 465 with the deprecated SMTP over SSL ([SMTPS](https://en.wikipedia.org/wiki/SMTPS) protocol).

- The smarthost service on port 587 with the [STARTTLS](https://en.wikipedia.org/wiki/STARTTLS).

- The incoming mail is accessible at the TLS/POP3 port (995) with [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol).

For the simplicity, I assume that the smarthost is located at "`smtp.hostname.dom`", requires [SMTP Authentication](https://en.wikipedia.org/wiki/SMTP_Authentication), and uses the message submission port (587) with the [STARTTLS](https://en.wikipedia.org/wiki/STARTTLS) in the following text.

### The mail configuration strategy for workstation

The most simple mail configuration is that the mail is sent to the ISP's smarthost and received from ISP's POP3 server by the MUA (see [Mail user agent (MUA)](#_mail_user_agent_mua)) itself. This type of configuration is popular with full featured GUI based MUA such as `icedove(1)`, `evolution(1)`, etc. If you need to filter mail by their types, you use MUA's filtering function. For this case, the local MTA (see [Mail transport agent (MTA)](#_mail_transport_agent_mta)) need to do local delivery only (when sender and receiver are on the same host).

Please note that the Debian system is the multiuser system. Even if you are the only user, there are many programs running as root and they may send you a mail.

The alternative mail configuration is that the mail is sent via local MTA to the ISP's smarthost and received from ISP's POP3 by the mail retriever (see [The remote mail retrieval and forward utility](#_the_remote_mail_retrieval_and_forward_utility)) to the local mailbox. If you need to filter mail by their types, you use MDA with filter (see [Mail delivery agent (MDA) with filter](#_mail_delivery_agent_mda_with_filter)) to filter mail into separate mailboxes. This type of configuration is popular with simple console based MUA such as `mutt(1)`, `mew(1)`, etc., although this is possible with any MUAs (see [Mail user agent (MUA)](#_mail_user_agent_mua)). For this case, the local MTA (see [Mail transport agent (MTA)](#_mail_transport_agent_mta)) need to do both smarthost delivery and local delivery. Since mobile workstation does not have valid FQDN, you must configure the local MTA to hide and spoof the real local mail name in outgoing mail to avoid mail delivery errors (see [The mail address configuration](#_the_mail_address_configuration)).

> [!TIP]
> You may wish to configure MUA/MDA to use [Maildir](https://en.wikipedia.org/wiki/Maildir) for storing email messages somewhere under your home directory.

## Mail transport agent (MTA)

For normal workstation, the popular choice for Mail transport agent (MTA) is either `exim4-*` or `postfix` packages. It is really up to you.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `exim4-daemon-light` | @-@popcon1@-@ | @-@psize1@-@ | Exim4 mail transport agent (MTA: Debian default) |
| `exim4-base` | @-@popcon1@-@ | @-@psize1@-@ | Exim4 documentation (text) and common files |
| `exim4-doc-html` | @-@popcon1@-@ | @-@psize1@-@ | Exim4 documentation (html) |
| `exim4-doc-info` | @-@popcon1@-@ | @-@psize1@-@ | Exim4 documentation (info) |
| `postfix` | @-@popcon1@-@ | @-@psize1@-@ | Postfix mail transport agent (MTA: alternative) |
| `postfix-doc` | @-@popcon1@-@ | @-@psize1@-@ | Postfix documentation (html+text) |
| `sasl2-bin` | @-@popcon1@-@ | @-@psize1@-@ | Cyrus SASL API implementation (supplement postfix for SMTP AUTH) |
| `cyrus-sasl2-doc` | @-@popcon1@-@ | @-@psize1@-@ | Cyrus SASL - documentation |

List of basic mail transport agent related packages for workstation

Although the popcon vote count of `exim4-*` looks several times popular than that of `postfix`, this does not mean `postfix` is not popular with Debian developers. The Debian server system uses both `exim4` and `postfix`. The [mail header analysis](http://wiki.debian.org/DefaultMTA) of mailing list postings from prominent Debian developers also indicate both of these MTAs are as popular.

The `exim4-*` packages are known to have very small memory consumption and very flexible for its configuration. The `postfix` package is known to be compact, fast, simple, and secure. Both come with ample documentation and are as good in quality and license.

There are many choices for mail transport agent (MTA) packages with different capability and focus in Debian archive.

| package | popcon | size | capability and focus |
|:---|:---|:---|:---|
| `exim4-daemon-light` | @-@popcon1@-@ | @-@psize1@-@ | full |
| `postfix` | @-@popcon1@-@ | @-@psize1@-@ | full (security) |
| `exim4-daemon-heavy` | @-@popcon1@-@ | @-@psize1@-@ | full (flexible) |
| `sendmail-bin` | @-@popcon1@-@ | @-@psize1@-@ | full (only if you are already familiar) |
| `nullmailer` | @-@popcon1@-@ | @-@psize1@-@ | strip down, no local mail |
| `ssmtp` | @-@popcon1@-@ | @-@psize1@-@ | strip down, no local mail |
| `courier-mta` | @-@popcon1@-@ | @-@psize1@-@ | very full (web interface etc.) |
| `masqmail` | @-@popcon1@-@ | @-@psize1@-@ | light |
| `esmtp` | @-@popcon1@-@ | @-@psize1@-@ | light |
| `esmtp-run` | @-@popcon1@-@ | @-@psize1@-@ | light (sendmail compatibility extension to `esmtp`) |
| `msmtp` | @-@popcon1@-@ | @-@psize1@-@ | light |
| `msmtp-mta` | @-@popcon1@-@ | @-@psize1@-@ | light (sendmail compatibility extension to `msmtp`) |

List of choices for mail transport agent (MTA) packages in Debian archive

### The configuration of exim4

> [!CAUTION]
> Configuring `exim4` to send the Internet mail via multiple corresponding smarthosts for multiple source email addresses is non-trivial. Please set up `exim4` only for a single email address for the system programs such as `popcon` and `cron` and set up `msmtp` for multiple source email addresses for the user programs such as `mutt`.

For the Internet mail via smarthost, you (re)configure `exim4-*` packages as the following.

    $ sudo /etc/init.d/exim4 stop
    $ sudo dpkg-reconfigure exim4-config

Select "mail sent by smarthost; received via SMTP or fetchmail" for "General type of mail configuration".

Set "System mail name:" to its default as the FQDN (see [???](#_the_hostname_resolution)).

Set "IP-addresses to listen on for incoming SMTP connections:" to its default as "127.0.0.1 ; ::1".

Unset contents of "Other destinations for which mail is accepted:".

Unset contents of "Machines to relay mail for:".

Set "IP address or host name of the outgoing smarthost:" to "smtp.hostname.dom:587".

Select "\<No\>" for "Hide local mail name in outgoing mail?". (Use "`/etc/email-addresses`" as in [The mail address configuration](#_the_mail_address_configuration), instead.)

Reply to "Keep number of DNS-queries minimal (Dial-on-Demand)?" as one of the following.

- "No" if the system is connected to the Internet while booting.

- "Yes" if the system is **not** connected to the Internet while booting.

Set "Delivery method for local mail:" to "mbox format in /var/mail/".

Select "\<Yes\>" for "Split configuration into small files?:".

Create password entries for the smarthost by editing "`/etc/exim4/passwd.client`".

    $ sudo vim /etc/exim4/passwd.client
     ...
    $ cat /etc/exim4/passwd.client
    ^smtp.*\.hostname\.dom:username@hostname.dom:password

Start `exim4` by the following.

    $ sudo /etc/init.d/exim4 start

The host name in "`/etc/exim4/passwd.client`" should not be the alias. You check the real host name with the following.

    $ host smtp.hostname.dom
    smtp.hostname.dom is an alias for smtp99.hostname.dom.
    smtp99.hostname.dom has address 123.234.123.89

I use regex in "`/etc/exim4/passwd.client`" to work around the alias issue. SMTP AUTH probably works even if the ISP moves host pointed by the alias.

You can manually update `exim4` configuration by the following:

- Update `exim4` configuration files in "`/etc/exim4/`".

  - creating "`/etc/exim4/exim4.conf.localmacros`" to set MACROs and editing "`/etc/exim4/exim4.conf.template`". (non-split configuration)

  - creating new files or editing existing files in the "`/etc/exim4/exim4.conf.d`" subdirectories. (split configuration)

- Run "`invoke-rc.d exim4 reload`".

Please read the official guide at: "`/usr/share/doc/exim4-base/README.Debian.gz`" and `update-exim4.conf(8)`.

> [!CAUTION]
> Starting `exim4` takes long time if "No" (default value) was chosen for the debconf query of "Keep number of DNS-queries minimal (Dial-on-Demand)?" and the system is **not** connected to the Internet while booting.

> [!WARNING]
> It is insecure to use plain text password without encryption even if your ISP allows it.

> [!TIP]
> Although use of [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) with [STARTTLS](https://en.wikipedia.org/wiki/STARTTLS) on port 587 is recommended, some ISPs still use deprecated [SMTPS](https://en.wikipedia.org/wiki/SMTPS) (SSL on port 465). Exim4 after 4.77 supports this deprecated SMTPS protocol for both as client and as server.

> [!TIP]
> If you are looking for a light weight MTA that respects "`/etc/aliases`" for your laptop PC, you should consider to configure `exim4(8)` with "`QUEUERUNNER='queueonly'`", "`QUEUERUNNER='nodaemon'`", etc. in "`/etc/default/exim4`".

### The configuration of postfix with SASL

For the Internet mail via smarthost, you should first read [postfix documentation](http://www.postfix.org/documentation.html) and key manual pages.

| command        | function                           |
|:---------------|:-----------------------------------|
| `postfix(1)`   | Postfix control program            |
| `postconf(1)`  | Postfix configuration utility      |
| `postconf(5)`  | Postfix configuration parameters   |
| `postmap(1)`   | Postfix lookup table maintenance   |
| `postalias(1)` | Postfix alias database maintenance |

List of important postfix manual pages

You (re)configure `postfix` and `sasl2-bin` packages as follows.

    $ sudo /etc/init.d/postfix stop
    $ sudo dpkg-reconfigure postfix

Chose "Internet with smarthost".

Set "SMTP relay host (blank for none):" to "`[smtp.hostname.dom]:587`" and configure it by the following.

    $ sudo postconf -e 'smtp_sender_dependent_authentication = yes'
    $ sudo postconf -e 'smtp_sasl_auth_enable = yes'
    $ sudo postconf -e 'smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd'
    $ sudo postconf -e 'smtp_sasl_type = cyrus'
    $ sudo vim /etc/postfix/sasl_passwd

Create password entries for the smarthost.

    $ cat /etc/postfix/sasl_passwd
    [smtp.hostname.dom]:587     username:password
    $ sudo postmap hush:/etc/postfix/sasl_passwd

Start the `postfix` by the following.

    $ sudo /etc/init.d/postfix start

Here the use of "`[`" and "`]`" in the `dpkg-reconfigure` dialog and "`/etc/postfix/sasl_passwd`" ensures not to check MX record but directly use exact hostname specified. See "Enabling SASL authentication in the Postfix SMTP client" in "`/usr/share/doc/postfix/html/SASL_README.html`".

### The mail address configuration

There are a few [mail address configuration files for mail transport, delivery and user agents](https://www.debian.org/doc/debian-policy/ch-customized-programs#s-mail-transport-agents).

| file | function | application |
|:---|:---|:---|
| `/etc/mailname` | default host name for (outgoing) mail | Debian specific, `mailname(5)` |
| `/etc/email-addresses` | host name spoofing for outgoing mail | `exim(8)` specific, `exim4-config_files(5)` |
| `/etc/postfix/generic` | host name spoofing for outgoing mail | `postfix(1)` specific, activated after `postmap(1)` command execution. |
| `/etc/aliases` | account name alias for incoming mail | general, activated after `newaliases(1)` command execution. |

List of mail address related configuration files

The **mailname** in the "`/etc/mailname`" file is usually a fully qualified domain name (FQDN) that resolves to one of the host's IP addresses. For the mobile workstation which does not have a hostname with resolvable IP address, set this **mailname** to the value of "`hostname -f`". (This is safe choice and works for both `exim4-*` and `postfix`.)

> [!TIP]
> The contents of "`/etc/mailname`" is used by many non-MTA programs for their default behavior. For `mutt`, set "`hostname`" and "`from`" variables in `~/muttrc` file to override the **mailname** value. For programs in the `devscripts` package, such as `bts(1)` and `dch(1)`, export environment variables "`$DEBFULLNAME`" and "`$DEBEMAIL`" to override it.

> [!TIP]
> The `popularity-contest` package normally send mail from root account with FQDN. You need to set `MAILFROM` in `/etc/popularity-contest.conf` as described in the `/usr/share/popularity-contest/default.conf` file. Otherwise, your mail will be rejected by the smarthost SMTP server. Although this is tedious, this approach is safer than rewriting the source address for all mails from root by MTA and should be used for other daemons and cron scripts.

When setting the **mailname** to "`hostname -f`", the spoofing of the source mail address via MTA can be realized by the following.

- "`/etc/email-addresses`" file for `exim4(8)` as explained in the `exim4-config_files(5)`

- "`/etc/postfix/generic`" file for `postfix(1)` as explained in the `generic(5)`

For `postfix`, the following extra steps are needed.

    # postmap hash:/etc/postfix/generic
    # postconf -e 'smtp_generic_maps = hash:/etc/postfix/generic'
    # postfix reload

You can test mail address configuration using the following.

- `exim(8)` with `-brw, -bf, -bF, -bV, …` options

- `postmap(1)` with `-q` option.

> [!TIP]
> Exim comes with several utility programs such as `exiqgrep(8)` and `exipick(8)`. See "`dpkg -L exim4-base|grep man8/`" for available commands.

### Basic MTA operations

There are several basic MTA operations. Some may be performed via `sendmail(1)` compatibility interface.

| exim command | postfix command | description |
|:---|:---|:---|
| `sendmail` | `sendmail` | read mails from standard input and arrange for delivery (`-bm`) |
| `mailq` | `mailq` | list the mail queue with status and queue ID (`-bp`) |
| `newaliases` | `newaliases` | initialize alias database (`-I`) |
| `exim4 -q` | `postqueue -f` | flush waiting mails (`-q`) |
| `exim4 -qf` | `postsuper -r ALL deferred; postqueue -f` | flush all mails |
| `exim4 -qff` | `postsuper -r ALL; postqueue -f` | flush even frozen mails |
| `exim4 -Mg queue_id` | `postsuper -h queue_id` | freeze one message by its queue ID |
| `exim4 -Mrm queue_id` | `postsuper -d queue_id` | remove one message by its queue ID |
| N/A | `postsuper -d ALL` | remove all messages |

List of basic MTA operation

> [!TIP]
> It may be a good idea to flush all mails by a script in "`/etc/ppp/ip-up.d/*`".

## Mail user agent (MUA)

If you subscribe to Debian related mailing list, it may be a good idea to use such MUA as `mutt` and `mew` which are the de facto standard for the participant and known to behave as expected.

| package | popcon | size | type |
|:---|:---|:---|:---|
| `evolution` | @-@popcon1@-@ | @-@psize1@-@ | X GUI program (GNOME3, groupware suite) |
| `thunderbird` | @-@popcon1@-@ | @-@psize1@-@ | X GUI program (GNOME2, [unbranded](https://en.wikipedia.org/wiki/Mozilla_Corporation_software_rebranded_by_the_Debian_project) [Mozilla Thunderbird](https://en.wikipedia.org/wiki/Mozilla_Thunderbird)) |
| `kmail` | @-@popcon1@-@ | @-@psize1@-@ | X GUI program (KDE) |
| `mutt` | @-@popcon1@-@ | @-@psize1@-@ | character terminal program probably used with `vim` |
| `mew` | @-@popcon1@-@ | @-@psize1@-@ | character terminal program under `(x)emacs` |

List of mail user agent (MUA)

### Basic MUA — Mutt

Customize "`~/.muttrc`" as the following to use `mutt` as the mail user agent (MUA) in combination with `vim`.

    #
    # User configuration file to override /etc/Muttrc
    #
    # spoof source mail address
    set use_from
    set hostname=example.dom
    set from="Name Surname <username@example.dom>"
    set signature="~/.signature"

    # vim: "gq" to reformat quotes
    set editor="vim -c 'set tw=72 et ft=mail'"

    # "mutt" goes to Inbox, while "mutt -y" lists mailboxes
    set mbox_type=Maildir           # use qmail Maildir format for creating mbox
    set mbox=~/Mail                 # keep all mail boxes in $HOME/Mail/
    set spoolfile=+Inbox            # mail delivered to $HOME/Mail/Inbox
    set record=+Outbox              # save fcc mail to $HOME/Mail/Outbox
    set postponed=+Postponed        # keep postponed in $HOME/Mail/postponed
    set move=no                     # do not move Inbox items to mbox
    set quit=ask-yes                # do not quit by "q" only
    set delete=yes                  # always delete w/o asking while exiting
    set fcc_clear                   # store fcc as non encrypted

    # Mailboxes in Maildir (automatic update)
    mailboxes `cd ~/Mail; /bin/ls -1|sed -e 's/^/+/' | tr "\n" " "`
    unmailboxes Maillog *.ev-summary

    ## Default
    #set index_format="%4C %Z %{%b %d} %-15.15L (%4l) %s"
    ## Thread index with senders (collapse)
    set index_format="%4C %Z %{%b %d} %-15.15n %?M?(#%03M)&(%4l)? %s"

    ## Default
    #set folder_format="%2C %t %N %F %2l %-8.8u %-8.8g %8s %d %f"
    ## just folder names
    set folder_format="%2C %t %N %f"

Add the following to "`/etc/mailcap`" or "`~/.mailcap`" to display HTML mail and MS Word attachments inline.

    text/html; lynx -force_html %s; needsterminal;
    application/msword; /usr/bin/antiword '%s'; copiousoutput; description="Microsoft Word Text"; nametemplate=%s.doc

> [!TIP]
> Mutt can be used as the [IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol) client and the mailbox format converter. You can tag messages with "`t`", "`T`", etc. These tagged messages can be copied with "`;C`" between different mailboxes and deleted with "`;d`" in one action.

### Advanced MUA — Mutt + msmtp

Mutt can be configured to use multiple source email addresses with multiple corresponding smarthosts using [msmtp](http://msmtp.sourceforge.net/).

> [!TIP]
> Msmtp is a sendmail emulator which allows to be installed along another sendmail emulator which provides the `/usr/sbin/sendmail` command. So you can leave your system mail to be `exim4` or `postfix`.

Let's think about supporting 3 email addresses as an example:

- "My Name1 \<<myaccount1@gmail.com>\>"

- "My Name2 \<<myaccount2@gmail.com>\>"

- "My Name3 \<<myaccount3@example.org>\>"

Here is an example of `~/.muttrc` customization supporting 3 smarthosts for 3 different source email addresses.

    set use_from
    set from="My Name3 <myaccount3@example.org>"
    set reverse_name
    alternates myaccount1@gmail\.com|myaccount1@gmail\.com|myaccount3@example\.org

    # ...

    # MACRO
    macro compose "1" "<edit-from>^UMy Name1 \<myaccount1@gmail.com\>\n"
    macro compose "2" "<edit-from>^UMy Name2 \<myaccount2@gmail.com\>\n"
    macro compose "3" "<edit-from>^UMy Name3 \<myaccount3@example.org\>\n"

    send2-hook '~f myaccount1@gmail.com' "set sendmail = '/usr/bin/msmtp --read-envelope-from'"
    send2-hook '~f myaccount2@gmail.com' "set sendmail = '/usr/bin/msmtp --read-envelope-from'"
    send2-hook '~f myaccount3@example.org' "set sendmail = '/usr/bin/msmtp --read-envelope-from'"

    # ...

Let's install `msmtp-gnome` and set `~/.msmtprc` as follows.

    defaults
    logfile ~/.msmtp.log
    domain myhostname.example.org
    tls on
    tls_starttls on
    tls_certcheck on
    tls_trust_file /etc/ssl/certs/ca-certificates.crt
    auth on
    port 587
    auto_from

    account myaccount1@gmail.com
    host smtp.gmail.com
    from  myaccount1@gmail.com
    user  myaccount1@gmail.com

    account myaccount2@gmail.com
    host smtp.gmail.com
    from  myaccount2@gmail.com
    user  myaccount2@gmail.com

    account myaccount3@example.org
    host mail.example.org
    from  myaccount3@example.org
    user  myaccount3@example.org

    account default : myaccount3@example.org

Then, add password data into the Gnome key ring. For example:

     $ secret-tool store --label=msmtp \
         host smtp.gmail.com \
         service smtp \
         user myaccount1@gmail.com
     ...

> [!TIP]
> If you don't wish to use the Gnome key ring, you can install `msmtp` package instead and add an entry such as "`password secret123`" to each account in `~/.msmtprc`. See [memtp documentation](http://msmtp.sourceforge.net/doc/msmtp.html) for more.

## The remote mail retrieval and forward utility

Instead of running a MUA to access remote mails and to process them manually, you may wish to automate such process to have all the mails delivered to the local host. The remote mail retrieval and forward utility is the tool for you.

Although `fetchmail(1)` has been de facto standard for the remote mail retrieval on GNU/Linux, the author likes `getmail(1)` now. If you want to reject mail before downloading to save bandwidth, `mailfilter` or `mpop` may be useful. Whichever mail retriever utilities are used, it is a good idea to configure system to deliver retrieved mails to MDA, such as `maildrop`, via pipe.

| package | popcon | size | description |
|:---|:---|:---|:---|
| `fetchmail` | @-@popcon1@-@ | @-@psize1@-@ | mail retriever (POP3, APOP, IMAP) (old) |
| `getmail` | @-@popcon1@-@ | @-@psize1@-@ | mail retriever (POP3, IMAP4, and SDPS) (simple, secure, and reliable) |
| `mailfilter` | @-@popcon1@-@ | @-@psize1@-@ | mail retriever (POP3) with with regex filtering capability |
| `mpop` | @-@popcon1@-@ | @-@psize1@-@ | mail retriever (POP3) and MDA with filtering capability |

List of remote mail retrieval and forward utilities

### getmail configuration

`getmail(1)` configuration is described in [getmail documentation](http://pyropus.ca/software/getmail/documentation.html). Here is my set up to access multiple POP3 accounts as user.

Create "`/usr/local/bin/getmails`" as the following.

    #!/bin/sh
    set -e
    if [ -f $HOME/.getmail/running ]; then
      echo "getmail is already running ... (if not, remove $HOME/.getmail/running)" >&2
      pgrep -l "getmai[l]"
      exit 1
    else
      echo "getmail has not been running ... " >&2
    fi
    if [ -f $HOME/.getmail/stop ]; then
      echo "do not run getmail ... (if not, remove $HOME/.getmail/stop)" >&2
      exit
    fi
    if [ "x$1" = "x-l" ]; then
      exit
    fi
    rcfiles="/usr/bin/getmail"
    for file in $HOME/.getmail/config/* ; do
      rcfiles="$rcfiles --rcfile $file"
    done
    date -u > $HOME/.getmail/running
    eval "$rcfiles $@"
    rm $HOME/.getmail/running

Configure it as the following.

    $ sudo chmod 755 /usr/local/bin/getmails
    $ mkdir -m 0700 $HOME/.getmail
    $ mkdir -m 0700 $HOME/.getmail/config
    $ mkdir -m 0700 $HOME/.getmail/log

Create configuration files "`$HOME/.getmail/config/pop3_name`" for each POP3 accounts as the following.

    [retriever]
    type = SimplePOP3SSLRetriever
    server = pop.example.com
    username =  pop3_name@example.com
    password = <your-password>

    [destination]
    type = MDA_external
    path = /usr/bin/maildrop
    unixfrom = True

    [options]
    verbose = 0
    delete = True
    delivered_to = False
    message_log = ~/.getmail/log/pop3_name.log

Configure it as the following.

    $ chmod 0600 $HOME/.getmail/config/*

Schedule "`/usr/local/bin/getmails`" to run every 15 minutes with `cron(8)` by executing "`sudo crontab -e -u <user_name>`" and adding following to user's cron entry.

    5,20,35,50 * * * * /usr/local/bin/getmails --quiet

> [!TIP]
> Problems of POP3 access may not come from `getmail`. Some popular free POP3 services may be violating the POP3 protocol and their SPAM filter may not be perfect. For example, they may delete messages just after receiving RETR command before receiving DELE command and may quarantined messages into Spam mailbox. You should minimize damages by configuring them to archive accessed messages and not to delete them. See also ["Some mail was not downloaded"](http://mail.google.com/support/bin/answer.py?answer=13291&topic=1555).

### fetchmail configuration

`fetchmail(1)` configuration is set by "`/etc/default/fetchmail`", "`/etc/fetchmailrc`" and "`$HOME/.fetchmailrc`". See its example in "`/usr/share/doc/fetchmail/examples/fetchmailrc.example`".

## Mail delivery agent (MDA) with filter

Most MTA programs, such as `postfix` and `exim4`, function as MDA (mail delivery agent). There are specialized MDA with filtering capabilities.

Although `procmail(1)` has been de facto standard for MDA with filter on GNU/Linux, author likes `maildrop(1)` now. Whichever filtering utilities are used, it is a good idea to configure system to deliver filtered mails to a [qmail-style Maildir](https://en.wikipedia.org/wiki/Maildir).

| package | popcon | size | description |
|:---|:---|:---|:---|
| `procmail` | @-@popcon1@-@ | @-@psize1@-@ | MDA with filter (old) |
| `mailagent` | @-@popcon1@-@ | @-@psize1@-@ | MDA with Perl filter |
| `maildrop` | @-@popcon1@-@ | @-@psize1@-@ | MDA with structured filtering language |

List of MDA with filter

### maildrop configuration

`maildrop(1)` configuration is described in [maildropfilter documentation](http://www.courier-mta.org/maildrop/maildropfilter.html). Here is a configuration example for "`$HOME/.mailfilter`".

    # Local configuration
    MAILROOT="$HOME/Mail"
    # set this to /etc/mailname contents
    MAILHOST="example.dom"
    logfile $HOME/.maildroplog

    # rules are made to override the earlier value by the later one.

    # mailing list mails ?
    if (     /^Precedence:.*list/:h || /^Precedence:.*bulk/:h )
    {
        # rules for mailing list mails
        # default mailbox for mails from mailing list
        MAILBOX="Inbox-list"
        # default mailbox for mails from debian.org
        if ( /^(Sender|Resent-From|Resent-Sender): .*debian.org/:h )
        {
            MAILBOX="service.debian.org"
        }
        # default mailbox for mails from bugs.debian.org (BTS)
        if ( /^(Sender|Resent-From|Resent-sender): .*@bugs.debian.org/:h )
        {
            MAILBOX="bugs.debian.org"
        }
        # mailbox for each properly maintained mailing list with "List-Id: foo" or "List-Id: ...<foo.bar>"
        if ( /^List-Id: ([^<]*<)?([^<>]*)>?/:h )
        {
            MAILBOX="$MATCH2"
        }
    }
    else
    {
        # rules for non-mailing list mails
        # default incoming box
        MAILBOX="Inbox-unusual"
        # local mails
        if ( /Envelope-to: .*@$MAILHOST/:h )
        {
            MAILBOX="Inbox-local"
        }
        # html mails (99% spams)
        if ( /DOCTYPE html/:b ||\
             /^Content-Type: text\/html/ )
        {
            MAILBOX="Inbox-html"
        }
        # blacklist rule for spams
        if ( /^X-Advertisement/:h ||\
             /^Subject:.*BUSINESS PROPOSAL/:h ||\
             /^Subject:.*URGENT.*ASISSTANCE/:h ||\
             /^Subject: *I NEED YOUR ASSISTANCE/:h )
        {
            MAILBOX="Inbox-trash"
        }
        # whitelist rule for normal mails
        if ( /^From: .*@debian.org/:h ||\
             /^(Sender|Resent-From|Resent-Sender): .*debian.org/:h ||\
             /^Subject: .*(debian|bug|PATCH)/:h )
        {
            MAILBOX="Inbox"
        }
        # whiltelist rule for BTS related mails
        if ( /^Subject: .*Bug#.*/:h ||\
             /^(To|Cc): .*@bugs.debian.org/:h )
        {
            MAILBOX="bugs.debian.org"
        }
        # whitelist rule for getmails cron mails
        if ( /^Subject: Cron .*getmails/:h )
        {
            MAILBOX="Inbox-getmails"
        }
    }

    # check existance of $MAILBOX
    `test -d $MAILROOT/$MAILBOX`
    if ( $RETURNCODE == 1 )
    {
        # create maildir mailbox for $MAILBOX
        `maildirmake $MAILROOT/$MAILBOX`
    }
    # deliver to maildir $MAILBOX
    to "$MAILROOT/$MAILBOX/"
    exit

> [!WARNING]
> Unlike `procmail`, `maildrop` does not create missing maildir directories automatically. You must create them manually using `maildirmake(1)` in advance as in the example "`$HOME/.mailfilter`".

### procmail configuration

Here is a similar configuration with "`$HOME/.procmailrc`" for `procmail(1)`.

    MAILDIR=$HOME/Maildir
    DEFAULT=$MAILDIR/Inbox/
    LOGFILE=$MAILDIR/Maillog
    # clearly bad looking mails: drop them into X-trash and exit
    :0
    * 1^0 ^X-Advertisement
    * 1^0 ^Subject:.*BUSINESS PROPOSAL
    * 1^0 ^Subject:.*URGENT.*ASISSTANCE
    * 1^0 ^Subject: *I NEED YOUR ASSISTANCE
    X-trash/

    # Delivering mailinglist messages
    :0
    * 1^0 ^Precedence:.*list
    * 1^0 ^Precedence:.*bulk
    * 1^0 ^List-
    * 1^0 ^X-Distribution:.*bulk
    {
    :0
    * 1^0 ^Return-path:.*debian-devel-admin@debian.or.jp
    jp-debian-devel/

    :0
    * ^Resent-Sender.*debian-user-request@lists.debian.org
    debian-user/

    :0
    * ^Resent-Sender.*debian-devel-request@lists.debian.org
    debian-devel/

    :0
    * ^Resent-Sender.*debian-announce-request@lists.debian.org
    debian-announce

    :0
    mailing-list/
    }

    :0
    Inbox/

### Redeliver mbox contents

You need to manually deliver mails to the sorted mailboxes in your home directory from "`/var/mail/<username>`" if your home directory became full and `procmail(1)` failed. After making disk space in the home directory, run the following.

    # /etc/init.d/${MAILDAEMON} stop
    # formail -s procmail </var/mail/<username>
    # /etc/init.d/${MAILDAEMON} start

## POP3/IMAP4 server

If you are to run a private server on LAN, you may consider to run [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) / [IMAP4](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol) server for delivering mail to LAN clients.

| package | popcon | size | type | description |
|:---|:---|:---|:---|:---|
| `courier-pop` | @-@popcon1@-@ | @-@psize1@-@ | POP3 | Courier mail server - POP3 server (maildir format only) |
| `cyrus-pop3d` | @-@popcon1@-@ | @-@psize1@-@ | POP3 | Cyrus mail system (POP3 support) |
| `courier-imap` | @-@popcon1@-@ | @-@psize1@-@ | IMAP | Courier mail server - IMAP server (maildir format only) |
| `cyrus-imapd` | @-@popcon1@-@ | @-@psize1@-@ | IMAP | Cyrus mail system (IMAP support) |

List of POP3/IMAP4 servers

## The print server and utilities

In the old Unix-like system, the BSD [Line printer daemon (lpd)](https://en.wikipedia.org/wiki/Line_Printer_Daemon_protocol) was the standard and the standard print out format of the classic free software was [PostScript (PS)](https://en.wikipedia.org/wiki/PostScript). Some filter system was used along with [Ghostscript](https://en.wikipedia.org/wiki/Ghostscript) to enable printing to the non-PostScript printer. See [???](#_ghostscript).

In the modern Debian system, the [Common UNIX Printing System](https://en.wikipedia.org/wiki/Common_Unix_Printing_System) (CUPS) is the de facto standard and the standard print out format of the modern free software is [Portable Document Format (PDF)](https://en.wikipedia.org/wiki/PDF).

The CUPS uses [Internet Printing Protocol](https://en.wikipedia.org/wiki/Internet_Printing_Protocol) (IPP). The IPP is now supported by other OSs such as Windows XP and Mac OS X and has became new cross-platform de facto standard for remote printing with bi-directional communication capability.

Thanks to the file format dependent auto-conversion feature of the CUPS system, simply feeding any data to the `lpr` command should generate the expected print output. (In CUPS, `lpr` can be enabled by installing the `cups-bsd` package.)

The Debian system has some notable packages for the print servers and utilities.

| package | popcon | size | port | description |
|:---|:---|:---|:---|:---|
| `lpr` | @-@popcon1@-@ | @-@psize1@-@ | printer (515) | BSD lpr/lpd ([Line printer daemon](https://en.wikipedia.org/wiki/Line_Printer_Daemon_protocol)) |
| `lprng` | @-@popcon1@-@ | @-@psize1@-@ | , , | , , (Enhanced) |
| `cups` | @-@popcon1@-@ | @-@psize1@-@ | IPP (631) | Internet Printing CUPS server |
| `cups-client` | @-@popcon1@-@ | @-@psize1@-@ | , , | [System V printer commands](https://en.wikipedia.org/wiki/System_V_printing_system) for CUPS: `lp(1)`, `lpstat(1)`, `lpoptions(1)`, `cancel(1)`, `lpmove(8)`, `lpinfo(8)`, `lpadmin(8)`, … |
| `cups-bsd` | @-@popcon1@-@ | @-@psize1@-@ | , , | [BSD printer commands](https://en.wikipedia.org/wiki/Line_Printer_Daemon_protocol) for CUPS: `lpr(1)`, `lpq(1)`, `lprm(1)`, `lpc(8)` |
| `printer-driver-gutenprint` | @-@popcon1@-@ | @-@psize1@-@ | Not applicable | printer drivers for CUPS |

List of print servers and utilities

> [!TIP]
> You can configure CUPS system by pointing your web browser to "<http://localhost:631/>" .

## The remote access server and utilities (SSH)

The [Secure SHell](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) is the **secure** way to connect over the Internet. A free version of SSH called [OpenSSH](http://www.openssh.org/) is available as `openssh-client` and `openssh-server` packages in Debian.

| package | popcon | size | tool | description |
|:---|:---|:---|:---|:---|
| `openssh-client` | @-@popcon1@-@ | @-@psize1@-@ | `ssh(1)` | Secure shell client |
| `openssh-server` | @-@popcon1@-@ | @-@psize1@-@ | `sshd(8)` | Secure shell server |
| `ssh-askpass-fullscreen` | @-@popcon1@-@ | @-@psize1@-@ | `ssh-askpass-fullscreen(1)` | asks user for a pass phrase for ssh-add (GNOME2) |
| `ssh-askpass` | @-@popcon1@-@ | @-@psize1@-@ | `ssh-askpass(1)` | asks user for a pass phrase for ssh-add (plain X) |

List of remote access server and utilities

> [!CAUTION]
> See [???](#_extra_security_measures_for_the_internet) if your SSH is accessible from the Internet.

> [!TIP]
> Please use the `screen(1)` program to enable remote shell process to survive the interrupted connection (see [???](#_the_screen_program)).

### Basics of SSH

> [!WARNING]
> "`/etc/ssh/sshd_not_to_be_run`" must not be present if one wishes to run the OpenSSH server.

SSH has two authentication protocols.

| SSH protocol | SSH method | description |
|:---|:---|:---|
| SSH-1 | "`RSAAuthentication`" | RSA identity key based user authentication |
| , , | "`RhostsAuthentication`" | "`.rhosts`" based host authentication (insecure, disabled) |
| , , | "`RhostsRSAAuthentication`" | "`.rhosts`" based host authentication combined with RSA host key (disabled) |
| , , | "`ChallengeResponseAuthentication`" | RSA challenge-response authentication |
| , , | "`PasswordAuthentication`" | password based authentication |
| SSH-2 | "`PubkeyAuthentication`" | public key based user authentication |
| , , | "`HostbasedAuthentication`" | "`~/.rhosts`" or "`/etc/hosts.equiv`" based host authentication combined with public key client host authentication (disabled) |
| , , | "`ChallengeResponseAuthentication`" | challenge-response authentication |
| , , | "`PasswordAuthentication`" | password based authentication |

List of SSH authentication protocols and methods

> [!CAUTION]
> Be careful about these differences if you are using a non-Debian system.

See "`/usr/share/doc/ssh/README.Debian.gz`", `ssh(1)`, `sshd(8)`, `ssh-agent(1)`, and `ssh-keygen(1)` for details.

Following are the key configuration files.

| configuration file | description of configuration file |
|:---|:---|
| `/etc/ssh/ssh_config` | SSH client defaults, see `ssh_config(5)` |
| `/etc/ssh/sshd_config` | SSH server defaults, see `sshd_config(5)` |
| `~/.ssh/authorized_keys` | default public SSH keys that clients use to connect to this account on this SSH server |
| `~/.ssh/identity` | secret SSH-1 RSA key of the user |
| `~/.ssh/id_rsa` | secret SSH-2 RSA key of the user |
| `~/.ssh/id_dsa` | secret SSH-2 DSA key of the user |

List of SSH configuration files

> [!TIP]
> See `ssh-keygen(1)`, `ssh-add(1)` and `ssh-agent(1)` for how to use public and secret SSH keys.

> [!TIP]
> Make sure to verify settings by testing the connection. In case of any problem, use "`ssh -v`".

> [!TIP]
> You can change the pass phrase to encrypt local secret SSH keys later with "`ssh-keygen -p`".

> [!TIP]
> You can add options to the entries in "`~/.ssh/authorized_keys`" to limit hosts and to run specific commands. See `sshd(8)` for details.

The following starts an `ssh(1)` connection from a client.

| command | description |
|:---|:---|
| `ssh username@hostname.domain.ext` | connect with default mode |
| `ssh -v username@hostname.domain.ext` | connect with default mode with debugging messages |
| `ssh -1 username@hostname.domain.ext` | force to connect with SSH version 1 |
| `ssh -1 -o RSAAuthentication=no -l username hostname.domain.ext` | force to use password with SSH version 1 |
| `ssh -o PreferredAuthentications=password -l username hostname.domain.ext` | force to use password with SSH version 2 |

List of SSH client startup examples

If you use the same user name on the local and the remote host, you can eliminate typing "`username@`". Even if you use different user name on the local and the remote host, you can eliminate it using "`~/.ssh/config`". For [Debian Salsa service](https://salsa.debian.org/) with account name "`foo-guest`", you set "`~/.ssh/config`" to contain the following.

    Host salsa.debian.org people.debian.org
        User foo-guest

For the user, `ssh(1)` functions as a smarter and more secure `telnet(1)`. Unlike `telnet` command, `ssh` command does not stop on the `telnet` escape character (initial default CTRL-\]).

### Port forwarding for SMTP/POP3 tunneling

To establish a pipe to connect to port 25 of `remote-server` from port 4025 of `localhost`, and to port 110 of `remote-server` from port 4110 of `localhost` through `ssh`, execute on the local host as the following.

    # ssh -q -L 4025:remote-server:25 4110:remote-server:110 username@remote-server

This is a secure way to make connections to SMTP/POP3 servers over the Internet. Set the "`AllowTcpForwarding`" entry to "`yes`" in "`/etc/ssh/sshd_config`" of the remote host.

### Connecting without remote passwords

One can avoid having to remember passwords for remote systems by using "`RSAAuthentication`" (SSH-1 protocol) or "`PubkeyAuthentication`" (SSH-2 protocol).

On the remote system, set the respective entries, "`RSAAuthentication yes`" or "`PubkeyAuthentication yes`", in "`/etc/ssh/sshd_config`".

Generate authentication keys locally and install the public key on the remote system by the following.

- "`RSAAuthentication`": RSA key for SSH-1 (deprecated because it is superseded.)

<!-- -->

    $ ssh-keygen
    $ cat .ssh/identity.pub | ssh user1@remote "cat - >>.ssh/authorized_keys"

- "`PubkeyAuthentication`": RSA key for SSH-2

<!-- -->

    $ ssh-keygen -t rsa
    $ cat .ssh/id_rsa.pub | ssh user1@remote "cat - >>.ssh/authorized_keys"

- "`PubkeyAuthentication`": DSA key for SSH-2 (deprecated because it is slow.)

<!-- -->

    $ ssh-keygen -t dsa
    $ cat .ssh/id_dsa.pub | ssh user1@remote "cat - >>.ssh/authorized_keys"

> [!TIP]
> Use of DSA key for SSH-2 is deprecated because key is smaller and slow. There are no more reasons to work around RSA patent using DSA since it has been expired. DSA stands for [Digital Signature Algorithm](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm) and is slow. Also see [DSA-1571-1](https://www.debian.org/security/2008/dsa-1571).

> [!NOTE]
> For "`HostbasedAuthentication`" to work in SSH-2, you must adjust the settings of "`HostbasedAuthentication`" to "`yes`" in both "`/etc/ssh/sshd_config`" on the server host and "`/etc/ssh/ssh_config`" or "`~/.ssh/config`" on the client host.

### Dealing with alien SSH clients

There are some free [SSH](https://en.wikipedia.org/wiki/Secure_Shell) clients available for other platforms.

| environment | free SSH program |
|:---|:---|
| Windows | puTTY (<http://www.chiark.greenend.org.uk/~sgtatham/putty/>) (GPL) |
| Windows (cygwin) | SSH in cygwin (<http://www.cygwin.com/>) (GPL) |
| Macintosh Classic | macSSH (<http://www.macssh.com/>) (GPL) |
| Mac OS X | OpenSSH; use `ssh` in the Terminal application (GPL) |

List of free SSH clients for other platforms

### Setting up ssh-agent

It is safer to protect your SSH authentication secret keys with a pass phrase. If a pass phrase was not set, use "`ssh-keygen -p`" to set it.

Place your public SSH key (e.g. "`~/.ssh/id_rsa.pub`") into "`~/.ssh/authorized_keys`" on a remote host using a password-based connection to the remote host as described above.

    $ ssh-agent bash
    $ ssh-add ~/.ssh/id_rsa
    Enter passphrase for /home/<username>/.ssh/id_rsa:
    Identity added: /home/<username>/.ssh/id_rsa (/home/<username>/.ssh/id_rsa)

No remote password needed from here on for the next command.

    $ scp foo <username>@remote.host:foo

Press ^D to terminating ssh-agent session.

For the X server, the normal Debian startup script executes `ssh-agent` as the parent process. So you only need to execute `ssh-add` once. For more, read `ssh-agent(1)` and `ssh-add(1)`.

### How to shutdown the remote system on SSH

You need to protect the process doing "`shutdown -h now`" (see [???](#_how_to_shutdown_the_system)) from the termination of SSH using the `at(1)` command (see [???](#_scheduling_tasks_once)) by the following.

    # echo "shutdown -h now" | at now

Running "`shutdown -h now`" in `screen(1)` (see [???](#_the_screen_program)) session is another way to do the same.

### Troubleshooting SSH

If you have problems, check the permissions of configuration files and run `ssh` with the "`-v`" option.

Use the "`-p`" option if you are root and have trouble with a firewall; this avoids the use of server ports 1 — 1023.

If `ssh` connections to a remote site suddenly stop working, it may be the result of tinkering by the sysadmin, most likely a change in "`host_key`" during system maintenance. After making sure this is the case and nobody is trying to fake the remote host by some clever hack, one can regain a connection by removing the "`host_key`" entry from "`~/.ssh/known_hosts`" on the local host.

## Other network application servers

Here are other network application servers.

| package | popcon | size | protocol | description |
|:---|:---|:---|:---|:---|
| `telnetd` | @-@popcon1@-@ | @-@psize1@-@ | [TELNET](https://en.wikipedia.org/wiki/TELNET) | TELNET server |
| `telnetd-ssl` | @-@popcon1@-@ | @-@psize1@-@ | , , | , , (SSL support) |
| `nfs-kernel-server` | @-@popcon1@-@ | @-@psize1@-@ | [NFS](https://en.wikipedia.org/wiki/Network_File_System_(protocol)) | Unix file sharing |
| `samba` | @-@popcon1@-@ | @-@psize1@-@ | [SMB](https://en.wikipedia.org/wiki/Server_Message_Block) | Windows file and printer sharing |
| `netatalk` | @-@popcon1@-@ | @-@psize1@-@ | [ATP](https://en.wikipedia.org/wiki/AppleTalk) | Apple/Mac file and printer sharing (AppleTalk) |
| `proftpd-basic` | @-@popcon1@-@ | @-@psize1@-@ | [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) | General file download |
| `apache2` | @-@popcon1@-@ | @-@psize1@-@ | [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) | General web server |
| `squid` | @-@popcon1@-@ | @-@psize1@-@ | , , | General web [proxy server](https://en.wikipedia.org/wiki/Proxy_server) |
| `squid3` | @-@popcon1@-@ | @-@psize1@-@ | , , | , , |
| `bind9` | @-@popcon1@-@ | @-@psize1@-@ | [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) | IP address for other hosts |
| `isc-dhcp-server` | @-@popcon1@-@ | @-@psize1@-@ | [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) | IP address of client itself |

List of other network application servers

Common Internet File System Protocol (CIFS) is the same protocol as [Server Message Block (SMB)](https://en.wikipedia.org/wiki/Server_Message_Block) and is used widely by Microsoft Windows.

> [!TIP]
> See [???](#_the_modern_centralized_system_management) for integration of server systems.

> [!TIP]
> The hostname resolution is usually provided by the [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) server. For the host IP address dynamically assigned by [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol), [Dynamic DNS](https://en.wikipedia.org/wiki/Dynamic_DNS) can be set up for the hostname resolution using `bind9` and `isc-dhcp-server` as described in the [DDNS page on the Debian wiki](http://wiki.debian.org/DDNS).

> [!TIP]
> Use of proxy server such as `squid` is much more efficient for saving bandwidth than use of local mirror server with the full Debian archive contents.

## Other network application clients

Here are other network application clients.

| package | popcon | size | protocol | description |
|:---|:---|:---|:---|:---|
| `netcat` | @-@popcon1@-@ | @-@psize1@-@ | [TCP/IP](https://en.wikipedia.org/wiki/TCP/IP) | TCP/IP swiss army knife |
| `openssl` | @-@popcon1@-@ | @-@psize1@-@ | [SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security) | Secure Socket Layer (SSL) binary and related cryptographic tools |
| `stunnel4` | @-@popcon1@-@ | @-@psize1@-@ | , , | universal SSL Wrapper |
| `telnet` | @-@popcon1@-@ | @-@psize1@-@ | [TELNET](https://en.wikipedia.org/wiki/TELNET) | TELNET client |
| `telnet-ssl` | @-@popcon1@-@ | @-@psize1@-@ | , , | , , (SSL support) |
| `nfs-common` | @-@popcon1@-@ | @-@psize1@-@ | [NFS](https://en.wikipedia.org/wiki/Network_File_System_(protocol)) | Unix file sharing |
| `smbclient` | @-@popcon1@-@ | @-@psize1@-@ | [SMB](https://en.wikipedia.org/wiki/Server_Message_Block) | MS Windows file and printer sharing client |
| `cifs-utils` | @-@popcon1@-@ | @-@psize1@-@ | , , | mount and umount commands for remote MS Windows file |
| `ftp` | @-@popcon1@-@ | @-@psize1@-@ | [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) | FTP client |
| `lftp` | @-@popcon1@-@ | @-@psize1@-@ | , , | , , |
| `ncftp` | @-@popcon1@-@ | @-@psize1@-@ | , , | full screen FTP client |
| `wget` | @-@popcon1@-@ | @-@psize1@-@ | [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) and [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) | web downloader |
| `curl` | @-@popcon1@-@ | @-@psize1@-@ | , , | , , |
| `axel` | @-@popcon1@-@ | @-@psize1@-@ | , , | accelerated downloader |
| `aria2` | @-@popcon1@-@ | @-@psize1@-@ | , , | accelerated downloader with [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent_(protocol)) and [Metalink](https://en.wikipedia.org/wiki/Metalink) supports |
| `bind9-host` | @-@popcon1@-@ | @-@psize1@-@ | [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) | `host(1)` from bind9, "`Priority: standard`" |
| `dnsutils` | @-@popcon1@-@ | @-@psize1@-@ | , , | `dig(1)` from bind, "`Priority: standard`" |
| `isc-dhcp-client` | @-@popcon1@-@ | @-@psize1@-@ | [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) | obtain IP address |
| `ldap-utils` | @-@popcon1@-@ | @-@psize1@-@ | [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) | obtain data from LDAP server |

List of network application clients

## The diagnosis of the system daemons

The `telnet` program enables manual connection to the system daemons and its diagnosis.

For testing plain [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) service, try the following

    $ telnet mail.ispname.net pop3

For testing the [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)/SSL enabled [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) service by some ISPs, you need TLS/SSL enabled `telnet` client by the `telnet-ssl` or `openssl` packages.

    $ telnet -z ssl pop.gmail.com 995

    $ openssl s_client -connect pop.gmail.com:995

The following [RFCs](http://www.ietf.org/rfc.html) provide required knowledge to each system daemon.

| RFC | description |
|:---|:---|
| [rfc1939](http://tools.ietf.org/html/rfc1939) and [rfc2449](http://tools.ietf.org/html/rfc2449) | [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) service |
| [rfc3501](http://tools.ietf.org/html/rfc3501) | [IMAP4](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol) service |
| [rfc2821](http://tools.ietf.org/html/rfc2821) ([rfc821](http://tools.ietf.org/html/rfc821)) | [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) service |
| [rfc2822](http://tools.ietf.org/html/rfc2822) ([rfc822](http://tools.ietf.org/html/rfc822)) | Mail file format |
| [rfc2045](http://tools.ietf.org/html/rfc2045) | [Multipurpose Internet Mail Extensions (MIME)](https://en.wikipedia.org/wiki/MIME) |
| [rfc819](http://tools.ietf.org/html/rfc819) | [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) service |
| [rfc2616](http://tools.ietf.org/html/rfc2616) | [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) service |
| [rfc2396](http://tools.ietf.org/html/rfc2396) | [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) definition |

List of popular RFCs

The port usage is described in "`/etc/services`".
