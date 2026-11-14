# Data processing notice · KVA Hackathon platform

> Verbatim copy of the privacy notice shown by the KVA Hackathon platform (participants' dashboard), version 2026-11-04, saved 2026-11-14. Useful also as a reference: it is how KVA itself describes an "AI brain" platform (GDPR basis, AI confirmation rule, provider list).

KVA · version 2026-11-04 · please confirm you have read it before continuing.

## 1. Who processes your data
The data controller is KVA. KVA uses KVA Hackathon, a platform provided by Kakashi Ventures S.r.l., which processes data on its behalf as a data processor (GDPR art. 28). For any request about your data, contact your organisation's privacy contact.

## 2. What we process
- **Identifiers:** name, work email, role, team.
- **Recorded work:** activities, goals, issues, documents and comments that you or your colleagues enter.
- The questions you ask the assistant and its answers, kept so that you can find them again.
- **Security records:** sign-ins and changes, with author and date.

## 3. What we do NOT process
Screen recordings, webcam, content from applications that are not connected, personal communications, biometric or special-category data. The platform does not score people.

## 4. Why, and on what basis
Organising and carrying out the work: performance of the contract (GDPR art. 6.1.b). Coordinating projects and keeping the organisation's knowledge: the controller's legitimate interest (GDPR art. 6.1.f), balanced by the safeguards in this notice. The platform is a work tool (art. 4(2), Law 300/1970) and is not used to assess individual performance or for decisions about your employment. We do not rely on your consent, which would not be free in an employment relationship. This confirmation is an acknowledgement.

## 5. Artificial intelligence
The platform uses AI models to summarise, answer questions and propose activities. A proposal takes effect only when a person confirms it, with one declared exception: a model may link recorded work to activities and mark an activity closed when that work proves it, and the closure can be reopened. No decision about you is made automatically.

## 6. Who sees the data
Internally: authorised people according to the roles and access decided by KVA; restricted areas only to those with an explicit grant. Externally: Kakashi Ventures and the providers below, limited to those of the services active for KVA. Each shows its region: those in the United States involve a transfer outside the EU, governed by the clauses of the contract with the provider.

| Provider | Region | Purpose | Data |
|---|---|---|---|
| Supabase (Postgres) | EU (the project's region) | the platform database and the storage for uploaded files | all working data: projects, activity, goals, criticalities, documents, communications, profiles |
| Vercel | EU (the function's region) · logs in the USA | application hosting and, from Phase 3, the per-organisation domains | application traffic and runtime logs; no persistent copy of the database |
| Anthropic | USA (under standard contractual clauses) | the texts the platform generates: summaries, dossiers, answers from «8», judgements | the corpus fragments sent in a single request (task_log, wiki, communications) and the question asked. No training on our data. |
| Resend | USA | outbound mail of an instance without the ctrl8@ mailbox (today the hackathon one): the sign-in code and transactional mail | the recipient's email address and the text of the mail (for sign-in: the six-digit code). No attachments. Where the ctrl8@ Gmail mailbox is configured, Resend receives nothing. |
| Google (Gmail · Calendar · Drive) | EU/USA (Google Workspace, standard contractual clauses) | the ctrl8@ service mailbox, the calendar as planning capacity, the linked documents, the Meet rooms of an event created by the organiser | mail sent from and received by the service mailbox; event titles and times; the Drive files explicitly linked. `apis.google.com` is the Drive picker script, loaded by the person's BROWSER: it does not go through our server, but it does make that visit known to Google — so it belongs here and not among the non-processing entries. |
| Microsoft (Entra ID · Graph · SharePoint · OneDrive) | EU/USA (Microsoft 365, standard contractual clauses) | reading, with the administrator's or the person's consent, the SharePoint and OneDrive documents chosen for the genesis corpus | the text of files in the selected folders and sites (read-only); for personal OneDrive, the person's delegated token |
| Luma | USA — check Luma's DPA at activation | registrations for camp events published on Luma (e.g. the hackathon) | READ only: name, email, form answers and status of people who register for a KVA event on Luma, which Luma collects on KVA's behalf. KVA Hackathon receives them through the signed webhook and re-reads them with the calendar API key; it sends nothing to Luma. |
| Eventbrite | USA — check Eventbrite's DPA at activation | registrations for camp events published on Eventbrite (e.g. the hackathon) | READ only: name, email, order-form answers and ticket status of people who register for a KVA event on Eventbrite. The notification is only a pointer: KVA Hackathon re-reads the order with the account's private token; it sends nothing to Eventbrite. |
| Open-Meteo | EU (Germany) · no account, no key | the weather on the desk (the eyebrow of `/me`) | the COORDINATES of the declared location, rounded to two decimals (~1 km) by the code that composes the request. No personal identifier, no working data. |

## 7. Retention
Data stays as long as the work requires it and according to the rules of KVA. When your employment ends your account is deactivated. The record of acknowledgements is kept to show that this notice was given.

## 8. Your rights
Access, rectification, erasure, restriction, objection and portability: from /me/privacy or by writing to the privacy contact. You can lodge a complaint with the Italian data protection authority (garanteprivacy.it).

## 9. Changes
We give at least 7 days' notice before a substantial change.
