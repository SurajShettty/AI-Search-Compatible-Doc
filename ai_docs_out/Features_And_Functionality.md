# Hostel Management Features and Functionality

**Module:** Hostel Management  
**Tags:** Hostel Management, Configuration, Admin Privileges, Student Allotment, Fee Payment, Infrastructure


## Overview

This document outlines the key features and functionalities of the Digii Hostel Management module. It covers administrative privileges, configuration settings for room allotment and fee payments, student self-registration options, and the setup of hostel policies and infrastructure.

## Prerequisites

- **Hostel Management Settings Super Admin Write** — "Hostel Management Settings Super Admin Write" admin privilege allows wardens to access and modify the hostel management configuration settings which includes payment and allotment type.
- **Hostel Management Settings Super Admin Read** — "Hostel Management Settings Super Admin Read" admin privilege allows wardens to only view and access the hostel management configuration settings which mainly includes payment and allotment type.
- **Admin Privileges (Infrastructure Management)** — The admin must first add hostel buildings, rooms, and beds in the Infrastructure Management section. This ensures that the necessary infrastructure is available for room allocation.
- **Hostel Management Settings** — The Hostel Management settings rights with appropriate read and write permissions should be given to admin, allowing to manage and update hostel-related data effectively.
- **Hostel Building Configuration** — Allows the Admin to add and manage hostel buildings within the platform under Infrastructure Management. The configuration includes specifying building details such as name, location, and available facilities.
- **Hostel Room Configuration** — Admins can add and manage hostel rooms under a specific building, detailing room numbers, capacities, and available amenities. This helps streamline room allotment based on student preferences and availability.
- **Hostel Bed Configuration** — Admins can assign and configure individual beds within hostel rooms, ensuring accurate bed assignments for students.

## Hostel Management Settings Super Admin Write Privilege

<!-- id: hostel-management-settings-super-admin-write-privilege | category: Admin Privileges -->

**What it does**

This admin privilege allows wardens to access and modify the hostel management configuration settings, including payment and allotment types.

**Why it matters**

It enables wardens to fully manage hostel settings, ensuring operational control over payment processing and room allocation policies.

**Questions this answers**

- What does 'Hostel Management Settings Super Admin Write' do?
- How can wardens change hostel settings?
- What permissions are needed to modify hostel payment types?
- Can a warden update allotment settings?
- What is the purpose of the Super Admin Write privilege for hostel management?

**Keywords:** hostel management, settings, super admin, write privilege, access, modify, configure, payment type, allotment type, warden, hostel admin, permissions, edit, update, change, admin rights, hostel configuration, manage settings, operational control

**Synonyms:** hostel settings write access, admin write privilege, modify hostel config, hostel management modification rights

**Related:** hostel-management-settings-super-admin-read-privilege

**Tags:** admin, privileges, access control, hostel management, configuration

---

## Hostel Management Settings Super Admin Read Privilege

<!-- id: hostel-management-settings-super-admin-read-privilege | category: Admin Privileges -->

**What it does**

This admin privilege allows wardens to only view and access the hostel management configuration settings, primarily payment and allotment types.

**Why it matters**

It provides necessary visibility into hostel settings without allowing modifications, which is useful for monitoring and reporting purposes.

**Questions this answers**

- What does 'Hostel Management Settings Super Admin Read' mean?
- How can wardens view hostel settings?
- What permissions are needed to see hostel payment types?
- Can a warden only view allotment settings?
- What is the purpose of the Super Admin Read privilege for hostel management?

**Keywords:** hostel management, settings, super admin, read privilege, access, view, configuration, payment type, allotment type, warden, hostel admin, permissions, monitor, check, see, admin rights, hostel configuration, view settings, reporting

**Synonyms:** hostel settings read access, admin read privilege, view hostel config, hostel management viewing rights

**Related:** hostel-management-settings-super-admin-write-privilege

**Tags:** admin, privileges, access control, hostel management, configuration

---

## Hostel Management Configuration

<!-- id: hostel-management-configuration | category: Hostel Management -->

**What it does**

This feature allows institutions to configure how hostel rooms are assigned to students and how fee payments are processed. It includes settings for Hostel Payment Mode (Dues Management or Offline Payment) and Hostel Allotment Type (Manual or Auto Allotment).

**Why it matters**

It streamlines the process of room allocation and fee payment tracking, ensuring operational efficiency and transparency. By offering flexibility in payment and allotment, it accommodates various preferences while maintaining financial accountability.

**Questions this answers**

- How do I configure hostel room assignments?
- What settings are available for hostel fee payments?
- Can I set up both manual and auto allotment for hostels?
- What is the Hostel Management Configuration feature?
- How does Digii handle hostel room and fee setup?
- Where can I define hostel payment and allotment types?

**Keywords:** hostel management, configuration, room assignment, fee payment, payment processing, dues management, offline payment, manual allotment, auto allotment, institutional policies, operational efficiency, transparency, financial accountability, hostel rooms, student allocation, setup hostel, hostel settings, configure rooms, configure fees

**Synonyms:** hostel setup, hostel settings, room allocation configuration, fee management setup, hostel module configuration

**Related:** hostel-payment-mode, hostel-allotment, enable-hostel-fee, allow-student-self-registration-for-hostel-allotments

**Tags:** hostel management, configuration, payments, allotment, administration

---

## Hostel Payment Mode

<!-- id: hostel-payment-mode | category: Hostel Management Configuration -->

**What it does**

This setting allows institutions to define how hostel fee payments are processed. Options include Dues Management (payments tracked within the platform) and Offline Payment (payments managed externally).

**Why it matters**

It is critical for ensuring smooth financial tracking and room allocation processes. By offering flexibility between Dues Management and Offline Payment, it accommodates various preferences while maintaining transparency in payment status.

**Examples**

- An institution chooses 'Dues Management' so students can pay hostel fees online and the system tracks their payment status automatically.
- A campus opts for 'Offline Payment' where students pay by cash at the admin office, and the hostel administrator updates the room allocation manually after confirming payment.

**Questions this answers**

- What are the options for hostel payment mode?
- How does Dues Management work for hostel fees?
- What is Offline Payment for hostels?
- Can I track hostel payments within the platform?
- How do I set up hostel payment methods?
- What's the difference between Dues Management and Offline Payment for hostels?

**Keywords:** hostel payment mode, fee payment, dues management, offline payment, payment tracking, financial tracking, hostel fees, payment status, room allocation, external payment, cash payment, cheque payment, online payment, payment options, configure payment, payment processing

**Synonyms:** hostel fee payment method, payment options, fee processing mode, hostel payment settings

**Related:** hostel-management-configuration, hostel-allotment

**Tags:** hostel management, payments, configuration, finance

---

## Hostel Allotment

<!-- id: hostel-allotment | category: Hostel Management Configuration -->

**What it does**

This configuration determines how hostel rooms are assigned to students. Institutions can choose between Manual Allotment (Hostel Administrators assign rooms) or Auto Allotment (rooms allocated based on payment status, applicable only with Dues Management).

**Why it matters**

It is crucial for ensuring a smooth and efficient room allocation process. It allows Hostel Administrators to manage room assignments based on payment methods and student preferences, ensuring fairness and transparency.

**Examples**

- With 'Manual Allotment' and 'Dues Management', a hostel administrator assigns a room to a student after their online payment is cleared.
- Using 'Auto Allotment' and 'Dues Management', a student selects a room, pays the dues, and the system automatically confirms their allocation.

**Questions this answers**

- What are the types of hostel allotment?
- How does Manual Allotment work for hostels?
- When can I use Auto Allotment for hostel rooms?
- Can students select their own rooms with auto allotment?
- How do I configure hostel room assignments?
- What happens if I choose Auto Allotment with Offline Payment?

**Keywords:** hostel allotment, room assignment, manual allotment, auto allotment, room allocation, student preferences, payment status, dues management, offline payment, hostel administrators, assign rooms, allocate rooms, room selection, configure allotment, hostel rooms, allotment type

**Synonyms:** room allocation type, hostel room assignment, allotment method, hostel room allocation

**Related:** hostel-management-configuration, hostel-payment-mode

**Tags:** hostel management, allotment, configuration, students

---

## Enable Hostel Fee

<!-- id: enable-hostel-fee | category: Consolidated Settings - Hostel Management -->

**What it does**

This feature allows institutions to collect hostel fees efficiently through an integrated system. When enabled under consolidated settings, students can view and pay hostel fees seamlessly alongside other dues via the 'Payments' option in their student account.

**Why it matters**

It simplifies fee collection, enhances transparency through consolidated payment records, reduces administrative workload, and offers students a convenient, single-point platform for managing all their payments.

**Examples**

- A student logs into their Digii account, navigates to 'Payments', and sees their hostel fees listed along with tuition and library dues, which they can pay in one go.

**Questions this answers**

- How do I enable hostel fee collection in Digii?
- Where can students pay hostel fees?
- Does Digii integrate hostel fees with other payments?
- What are the benefits of enabling hostel fees in consolidated settings?
- Can students see all their dues in one place?
- How does enabling hostel fees simplify administration?

**Keywords:** enable hostel fee, consolidated settings, fee collection, integrated system, student payments, payments option, unified interface, view fees, pay fees, administrative workload, financial operations, hostel dues, payment records, penalty enforcement, timely reminders, hostel fees, student account, payment management

**Synonyms:** activate hostel fee collection, hostel fee integration, unified fee payment, consolidated hostel payments

**Related:** hostel-payment-mode, allow-student-self-registration-for-hostel-allotments

**Tags:** hostel management, payments, fees, students, administration, consolidated settings

---

## Allow Student Self Registration for Hostel Allotments

<!-- id: allow-student-self-registration-for-hostel-allotments | category: Consolidated Settings - Hostel Management -->

**What it does**

This feature enables students to independently choose their hostel policy, building, and room using the 'Payments' option. Once activated, students can select preferred options and pay the associated fee to secure their allotment without administrative intervention.

**Why it matters**

It streamlines the registration process, reduces administrative burden, provides students with greater flexibility, and ensures payment compliance by linking allotments with the Dues Management module. This automates workflows and improves student satisfaction.

**Examples**

- At an institute, the Hostel department activates the "Allow Student Self Registration for Hostel" feature. Students can now access the 'Payments' section, where they see a list of available hostel policies, building and rooms under the Hostel option. Each student can select a convenient hostel policy, building and room based on their residence. After selecting, they proceed to pay the hostel allotment fee through various options available. Once payment is complete and verified by the system, the student's allotment to the selected hostel policy, building and room is confirmed automatically, without manual intervention by hostel warden. This streamlined system reduces delays and administrative load, allowing hostel wardens and administrators to focus on monitoring and support rather than processing registrations manually. It also empowers students with autonomy and clarity in managing their hostel needs, linked with hostel fee payment tracking.

**Questions this answers**

- Can students register for hostels themselves?
- How does student self-registration for hostels work?
- What are the benefits of allowing students to choose their own hostel rooms?
- Does self-registration link with hostel fee payment?
- How do I enable student self-service for hostel allotments?
- What happens after a student self-registers for a hostel?
- Can students select their preferred hostel building and room?

**Keywords:** student self-registration, hostel allotments, choose hostel, hostel policy, hostel building, hostel room, payments option, self-service, administrative intervention, payment compliance, dues management, automate registration, student satisfaction, operational efficiency, hostel management, student autonomy, secure allotment, online registration, reduce administrative workload, hostel signup

**Synonyms:** student hostel signup, self-allotment, student room selection, automated hostel registration, student-led hostel booking

**Related:** enable-hostel-fee, hostel-allotment, hostel-payment-mode

**Tags:** hostel management, students, self-service, registration, allotment, payments, administration, consolidated settings

---

## Hostel Policy

<!-- id: hostel-policy | category: Hostel Fee -->

**What it does**

This feature allows institutions to define specific policies by name and code for hostel management. Once created, a policy cannot be edited, archived, or deleted, ensuring consistency. Only one active policy is allowed at a time, configurable institution-wide or for specific academic years or semesters.

**Why it matters**

It is essential for ensuring consistency in hostel room allocation, aligning the process with academic schedules and institutional guidelines. This feature maintains a streamlined, standardized approach and prevents accidental modifications, ensuring organized and aligned room allocations.

**Examples**

- An institution creates a 'UG Hostel Policy 2024-25' for undergraduate students for the upcoming academic year, defining general rules for room sharing and fees. Once created, this policy cannot be changed to ensure consistency.

**Questions this answers**

- How do I define a hostel policy?
- Can I edit a hostel policy after creation?
- How many active hostel policies can there be?
- Can hostel policies be set for specific academic years?
- What is the purpose of a hostel policy?
- Why can't a hostel policy be edited once created?

**Keywords:** hostel policy, define policy, policy name, policy code, active policy, academic year, semester, institutional basis, room allocation, hostel management, consistency, guidelines, standardized approach, uneditable policy, policy options, hostel rules, accommodation policy, create policy

**Synonyms:** hostel rules, accommodation policy, room allocation policy, hostel guidelines

**Related:** hostel-policy-option

**Tags:** hostel management, policies, configuration, administration, fees

---

## Hostel Policy Option

<!-- id: hostel-policy-option | category: Hostel Fee -->

**What it does**

This feature allows defining specific criteria within a hostel policy, such as Option Name, Code, Fee Amount, Department, Programme, Batch Year, Quota, Gender, Room Type, and Allotment Start/End Dates. These options, once created, cannot be edited, archived, or deleted.

**Why it matters**

It is critical for ensuring room allocations align with institutional rules and student preferences. By providing flexibility in selecting criteria, it tailors assignments to administrative requirements and student needs, ensuring fairness, transparency, and an organized system.

**Examples**

- Within the 'UG Hostel Policy 2024-25', an option 'Double Sharing Male - Engineering' is created with a specific fee, applicable to male students from the Engineering department in the 2024 batch, for double-sharing rooms. This option has a defined allotment start and end date.

**Questions this answers**

- What details can I define in a hostel policy option?
- Can I set different fees for different hostel policy options?
- How do I specify gender-based rooms in a policy option?
- What happens if I select 'Dues Management' for the option fee?
- Can I edit a hostel policy option after it's created?
- How do I define room types within a hostel policy?
- What is the purpose of the allotment start and end dates?

**Keywords:** hostel policy option, option name, option code, option fee amount, department, programme, batch year, quota, gender, room type, allotment start date, allotment end date, allocation criteria, customized allocation, institutional rules, student preferences, room assignments, uneditable option, auto-generate code, policy criteria, hostel fees, room sharing

**Synonyms:** policy sub-option, hostel criteria, room allocation criteria, hostel policy details

**Related:** hostel-policy

**Tags:** hostel management, policies, configuration, administration, fees, students

---

## Admin Privileges (Infrastructure Management)

<!-- id: admin-privileges-infrastructure-management | category: Prerequisites - Hostel Management -->

**What it does**

This prerequisite requires the admin to first add hostel buildings, rooms, and beds in the Infrastructure Management section. This ensures that the necessary physical infrastructure is available for room allocation.

**Why it matters**

It is an essential foundational step to ensure that the physical hostel infrastructure (buildings, rooms, beds) is accurately recorded and available in the system before any allocation or management can occur.

**Questions this answers**

- What are the admin prerequisites for hostel management?
- Do I need to set up hostel buildings before allocating rooms?
- What is Infrastructure Management for hostels?
- How do I add hostel rooms and beds?
- What permissions are needed to manage hostel infrastructure?

**Keywords:** admin privileges, infrastructure management, hostel buildings, hostel rooms, hostel beds, add infrastructure, prerequisite, room allocation, physical infrastructure, manage buildings, manage rooms, manage beds, admin rights, hostel setup

**Synonyms:** infrastructure setup permissions, hostel infrastructure admin rights, hostel physical setup prerequisite

**Related:** hostel-building-configuration, hostel-room-configuration, hostel-bed-configuration

**Tags:** admin, privileges, infrastructure, hostel management, prerequisites

---

## Hostel Management Settings Rights

<!-- id: hostel-management-settings-rights | category: Prerequisites - Hostel Management -->

**What it does**

This prerequisite requires appropriate read and write permissions for Hostel Management settings to be given to the admin, allowing them to effectively manage and update hostel-related data.

**Why it matters**

It ensures that administrators have the necessary access levels to configure, manage, and update all hostel-related data and settings, which is crucial for effective hostel operations.

**Questions this answers**

- What permissions are needed for hostel management settings?
- How do I grant read/write access for hostel data?
- Is it a prerequisite to have hostel management settings rights?
- What data can be managed with these rights?
- Who needs hostel management settings permissions?

**Keywords:** hostel management settings, rights, read permissions, write permissions, admin access, manage hostel data, update hostel data, prerequisite, hostel operations, configure settings, permissions, admin privileges, hostel data management

**Synonyms:** hostel settings access, admin rights for hostel management, hostel data permissions

**Related:** hostel-management-settings-super-admin-write-privilege, hostel-management-settings-super-admin-read-privilege

**Tags:** admin, privileges, hostel management, prerequisites, settings

---

## Hostel Building Configuration

<!-- id: hostel-building-configuration | category: Infrastructure Management -->

**What it does**

This feature allows the Admin to add and manage hostel buildings within the platform under Infrastructure Management. The configuration includes specifying building details such as name, location, and available facilities.

**Why it matters**

It is essential for organizing and detailing the physical structure of the hostel, enabling streamlined room allotment based on available buildings and their specific characteristics.

**Questions this answers**

- How do I add a new hostel building?
- What details can I configure for a hostel building?
- Where do I manage hostel buildings in Digii?
- Can I specify facilities for a hostel building?
- What is hostel building configuration?

**Keywords:** hostel building configuration, add building, manage building, infrastructure management, building details, name, location, facilities, hostel structure, organize buildings, room allotment, admin, configure hostel, hostel setup, physical infrastructure

**Synonyms:** manage hostel buildings, hostel building setup, configure hostel structures

**Related:** admin-privileges-infrastructure-management, hostel-room-configuration

**Tags:** hostel management, infrastructure, configuration, administration

---

## Hostel Room Configuration

<!-- id: hostel-room-configuration | category: Infrastructure Management -->

**What it does**

This feature allows Admins to add and manage hostel rooms under a specific building, detailing room numbers, capacities, and available amenities.

**Why it matters**

It helps streamline room allotment by providing detailed information about each room, ensuring assignments are based on student preferences, capacity, and amenities.

**Questions this answers**

- How do I add hostel rooms to a building?
- What details can I configure for a hostel room?
- Can I specify room capacity and amenities?
- Where do I manage hostel rooms in Digii?
- What is hostel room configuration?

**Keywords:** hostel room configuration, add room, manage room, room numbers, capacities, amenities, specific building, infrastructure management, streamline allotment, student preferences, room details, admin, configure room, hostel setup, room management

**Synonyms:** manage hostel rooms, hostel room setup, configure hostel rooms

**Related:** admin-privileges-infrastructure-management, hostel-building-configuration, hostel-bed-configuration

**Tags:** hostel management, infrastructure, configuration, administration

---

## Hostel Bed Configuration

<!-- id: hostel-bed-configuration | category: Infrastructure Management -->

**What it does**

This feature allows Admins to assign and configure individual beds within hostel rooms, ensuring accurate bed assignments for students.

**Why it matters**

It ensures precise tracking and assignment of individual beds, which is crucial for managing room occupancy and student accommodation details accurately.

**Questions this answers**

- How do I assign beds within hostel rooms?
- Can I configure individual beds in Digii?
- What is hostel bed configuration?
- Where do I manage hostel beds?
- How to ensure accurate bed assignments?

**Keywords:** hostel bed configuration, assign bed, configure bed, individual beds, hostel rooms, accurate assignments, student accommodation, infrastructure management, manage beds, admin, configure bed, bed management, occupancy tracking

**Synonyms:** manage hostel beds, hostel bed setup, configure beds in rooms

**Related:** admin-privileges-infrastructure-management, hostel-room-configuration

**Tags:** hostel management, infrastructure, configuration, administration

---
