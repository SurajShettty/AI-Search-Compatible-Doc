# Features And Functionality

**Module:** Hostel Management  
**Tags:** Hostel Management, Configuration, Settings, Payment, Allotment, Student Self-Service, Admin Privileges, Infrastructure


## Overview

This document outlines the features and functionalities of the Digii Hostel Management module, covering configurations for room allotment, fee payment modes, student self-registration, and the definition of hostel policies and infrastructure. It details how institutions can manage hostel accommodations efficiently and transparently.

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

It ensures that designated administrators have the necessary permissions to configure and update critical hostel settings, maintaining operational flexibility and control over hostel operations.

**Questions this answers**

- How do I grant write access for hostel settings?
- What does the Hostel Management Settings Super Admin Write privilege do?
- Can wardens change hostel payment types?
- Who can modify hostel allotment settings?
- What permissions are needed to edit hostel configurations?

**Keywords:** Hostel Management Settings Super Admin Write, admin privilege, warden access, modify settings, payment configuration, allotment type, hostel admin permissions, write access, edit hostel settings, super admin, hostel management, permissions, access control, configure hostel, update hostel

**Synonyms:** Hostel Write Privilege, Admin Write Access for Hostel, Warden Modify Rights

**Related:** hostel-management-settings-super-admin-read-privilege

**Tags:** Admin Privileges, Hostel Management, Configuration, Security

---

## Hostel Management Settings Super Admin Read Privilege

<!-- id: hostel-management-settings-super-admin-read-privilege | category: Admin Privileges -->

**What it does**

This admin privilege allows wardens to only view and access the hostel management configuration settings, primarily payment and allotment types.

**Why it matters**

It provides necessary visibility into hostel configurations without allowing unauthorized modifications, ensuring data integrity and controlled access for monitoring purposes.

**Questions this answers**

- How do I grant read-only access for hostel settings?
- What does the Hostel Management Settings Super Admin Read privilege do?
- Can wardens only view hostel payment types?
- Who can view hostel allotment settings?
- What permissions are needed to see hostel configurations?

**Keywords:** Hostel Management Settings Super Admin Read, admin privilege, warden access, view settings, payment configuration, allotment type, hostel admin permissions, read access, monitor hostel settings, super admin, hostel management, permissions, access control, check hostel settings, view hostel

**Synonyms:** Hostel Read Privilege, Admin Read Access for Hostel, Warden View Rights

**Related:** hostel-management-settings-super-admin-write-privilege

**Tags:** Admin Privileges, Hostel Management, Configuration, Security

---

## Hostel Management Configuration

<!-- id: hostel-management-configuration-overview | category: Hostel Settings -->

**What it does**

This feature allows institutions to configure how hostel rooms are assigned to students and how fee payments are processed. It includes defining payment modes (Dues Management or Offline Payment) and allotment types (Manual or Auto Allotment).

**Why it matters**

It streamlines room allocation and fee payment tracking, ensuring operational efficiency and transparency. By providing flexibility in payment and allotment processes, it accommodates various institutional policies and maintains financial accountability.

**Questions this answers**

- What is Hostel Management Configuration?
- How does Digii manage hostel room assignments?
- What payment options are available for hostel fees?
- Can I automate hostel room allocation?
- How do I set up hostel management in Digii?
- What are the core features of hostel configuration?

**Keywords:** Hostel Management Configuration, room assignment, fee payment processing, hostel settings, payment mode, allotment type, Dues Management, Offline Payment, Manual Allotment, Auto Allotment, operational efficiency, transparency, financial accountability, configure hostel, hostel setup, hostel room allocation, hostel fee management

**Synonyms:** Hostel Setup, Hostel Settings, Hostel Module Configuration

**Related:** hostel-payment-mode, hostel-allotment-type

**Tags:** Hostel Management, Configuration, Payment, Allotment

---

## Hostel Payment Mode

<!-- id: hostel-payment-mode | category: Hostel Settings -->

**What it does**

This feature defines how hostel fee payments are processed, offering two options: Dues Management, where all payment details are tracked within the platform, and Offline Payment, where payments are managed externally and not tracked by the platform.

**Why it matters**

It is critical for smooth financial tracking and room allocation processes. By allowing institutions to choose between Dues Management and Offline Payment, this feature offers flexibility while maintaining transparency in tracking payment status, helping Hostel Administrators efficiently manage and monitor payments.

**How to use**

1. Select 'Dues Management' to track all payment details (amount, due date, status) within the platform, enabling room allocation after dues are cleared.
2. Select 'Offline Payment' for external payments (cash, cheque, or other traditional methods), which are not tracked by the platform, requiring manual room allocation by Hostel Administrators.

**Examples**

- An institution chooses 'Dues Management' so students can see their hostel fees and pay online, and rooms are automatically allotted once payment is confirmed.
- An institution selects 'Offline Payment' because they prefer students to pay via bank transfer, and the hostel administrator manually updates the payment status and assigns rooms.

**Questions this answers**

- How do I set up hostel fee payment methods?
- What is Dues Management for hostel fees?
- Can I track offline hostel payments in Digii?
- How does the Hostel Payment Mode affect room allocation?
- What are the options for hostel fee collection?
- How to configure hostel payment?

**Keywords:** Hostel Payment Mode, Dues Management, Offline Payment, hostel fees, payment processing, financial tracking, payment status, fee amount, due date, external payments, cash payment, cheque payment, online payment, hostel administrator, manage payments, payment options, configure payment, hostel fee collection

**Synonyms:** Hostel Fee Payment Options, Hostel Payment Method, Hostel Dues Management

**Related:** hostel-management-configuration-overview, hostel-allotment-type, enable-hostel-fee, hostel-policy-option

**Tags:** Hostel Management, Payment, Configuration, Finance

---

## Hostel Allotment Type

<!-- id: hostel-allotment-type | category: Hostel Settings -->

**What it does**

This configuration determines how hostel rooms are assigned to students, offering 'Manual Allotment' (Hostel Administrators personally assign rooms) and 'Auto Allotment' (rooms are allocated based on payment status, applicable only with Dues Management).

**Why it matters**

It is crucial for ensuring a smooth and efficient room allocation process. It allows Hostel Administrators to manage room assignments based on payment methods and student preferences, ensuring fairness and transparency, and providing flexibility to align with operational needs.

**How to use**

1. Select 'Manual Allotment' to personally assign rooms to students, considering factors like preferences or availability. If the hostel payment method is Dues Management, allocation occurs after dues are cleared; if Offline Payment, administrators assign rooms after external payment confirmation.
2. Select 'Auto Allotment' for systematic, criteria-based allocation (only available when the payment method is Dues Management). Students can select preferred rooms, and allocation happens automatically once payment is cleared through the Dues Management module.

**Examples**

- An institution uses 'Manual Allotment' for specific student groups, allowing the warden to personally place students based on special requests.
- An institution uses 'Auto Allotment' for general admissions, where students choose their room online and get it confirmed automatically upon paying their dues through the platform.

**Questions this answers**

- How do I configure hostel room assignments?
- What is Manual Allotment for hostels?
- When can I use Auto Allotment for hostel rooms?
- Does Auto Allotment work with offline payments?
- How do students get assigned hostel rooms?
- Can I manually assign hostel rooms?

**Keywords:** Hostel Allotment Type, Manual Allotment, Auto Allotment, room assignment, room allocation, student preferences, payment status, Dues Management, Offline Payment, Hostel Administrators, automated allocation, manual allocation, configure allotment, hostel rooms, assign rooms, hostel room assignment

**Synonyms:** Hostel Room Assignment Method, Hostel Allocation Type, Room Allotment Settings

**Related:** hostel-management-configuration-overview, hostel-payment-mode, allow-student-self-registration-for-hostel-allotments

**Tags:** Hostel Management, Allotment, Configuration, Automation

---

## Enable Hostel Fee

<!-- id: enable-hostel-fee | category: Consolidated Settings - Hostel Management -->

**What it does**

This feature allows institutions to collect hostel fees efficiently through an integrated system. When enabled under consolidated settings, students can view and pay hostel fees seamlessly alongside other dues via a unified 'Payments' interface in their student account.

**Why it matters**

It simplifies fee collection, enhances transparency through consolidated payment records, reduces administrative workload, and offers students a convenient, single-point platform for managing all their payments. It also supports timely reminders and penalty enforcement where applicable.

**How to use**

1. Navigate to 'Consolidated Settings'.
2. Enable the 'Hostel Fee' feature.
3. Students can then access the 'Payments' option in their account to view and pay hostel fees along with other dues.

**Examples**

- A student logs into their Digii account, goes to the 'Payments' section, and sees their tuition fees, library fines, and hostel fees all listed together, which they can pay in one go.

**Questions this answers**

- How do I enable hostel fee collection?
- Where can students pay hostel fees?
- Does Digii integrate hostel fees with other payments?
- What are the benefits of enabling hostel fees in consolidated settings?
- Can students see all their dues in one place?

**Keywords:** Enable Hostel Fee, consolidated settings, fee collection, integrated system, student payments, unified interface, Payments option, hostel dues, administrative workload, financial operations, timely reminders, penalty enforcement, collect hostel fees, student account, payment portal, hostel fee payment

**Synonyms:** Activate Hostel Fee Collection, Hostel Fee Integration, Consolidated Hostel Payments

**Related:** hostel-payment-mode

**Tags:** Hostel Management, Payment, Consolidated Settings, Student Experience

---

## Allow Student Self Registration for Hostel Allotments

<!-- id: allow-student-self-registration-for-hostel-allotments | category: Consolidated Settings - Hostel Management -->

**What it does**

This feature enables students to independently choose their hostel policy, building, and room using the 'Payments' option. Once activated, students can view available options, select their preferences, and pay the associated hostel allotment fee to secure their allotment without administrative intervention.

**Why it matters**

It streamlines the registration process, reduces administrative burden, and provides students with greater flexibility. It ensures payment compliance by linking hostel allotments with the Dues Management module, automating workflows, capturing accurate data, and expediting allotments, particularly valuable for large institutions.

**How to use**

1. Activate the "Allow Student Self Registration for Hostel" feature in Consolidated Settings.
2. Students access the 'Payments' section in their account.
3. They view available hostel policies, buildings, and rooms under the 'Hostel' option.
4. Students select their preferred options and proceed to pay the hostel allotment fee.
5. Once payment is complete and verified by the system, the student's allotment is automatically confirmed.

**Examples**

- At an institute, the Hostel department activates the "Allow Student Self Registration for Hostel" feature. Students can now access the 'Payments' section, where they see a list of available hostel policies, building and rooms under the Hostel option. Each student can select a convenient hostel policy, building and room based on their residence. After selecting, they proceed to pay the hostel allotment fee through various options available. Once payment is complete and verified by the system, the student's allotment to the selected hostel policy, building and room is confirmed automatically, without manual intervention by hostel warden. This streamlined system reduces delays and administrative load, allowing hostel wardens and administrators to focus on monitoring and support rather than processing registrations manually. It also empowers students with autonomy and clarity in managing their hostel needs, linked with hostel fee payment tracking.

**Questions this answers**

- Can students register for hostels themselves?
- How do students choose their hostel rooms?
- What is student self-registration for hostels?
- Does self-registration require admin approval?
- How does payment work with student self-registration for hostels?
- How to enable student self-allotment for hostels?

**Keywords:** Allow Student Self Registration, Hostel Allotments, student self-service, choose hostel, hostel policy, hostel building, hostel room, Payments option, administrative intervention, streamline registration, reduce administrative burden, payment compliance, Dues Management module, automate workflow, expedite allotments, student satisfaction, self-register hostel, hostel booking, online hostel registration, student hostel enrollment

**Synonyms:** Student Hostel Self-Service, Hostel Self-Enrollment, Automated Hostel Allotment for Students

**Related:** hostel-allotment-type, enable-hostel-fee, hostel-policy, hostel-policy-option

**Tags:** Hostel Management, Student Self-Service, Allotment, Payment, Automation, Consolidated Settings

---

## Hostel Policy

<!-- id: hostel-policy | category: Hostel Fee Configuration -->

**What it does**

This feature allows institutions to define specific, uneditable policies by name and code for hostel management. Only one active policy is permitted at a time, which can be set institution-wide or for specific academic years/semesters, and includes options based on criteria like room sharing, gender, department, program, batch year, and quota.

**Why it matters**

It is essential for ensuring consistency in hostel room allocation by aligning the process with academic schedules and institutional guidelines. This feature prevents accidental modifications and maintains a streamlined, standardized approach for managing student allocations, ensuring clarity and efficient management.

**How to use**

1. Define a unique name and code for the hostel policy.
2. Set the policy to be active for the entire institution or specific academic years/semesters.
3. Create one or more policy options based on criteria such as room sharing preferences, gender, department, program, batch year, and quota.

**Examples**

- An institution creates a 'UG Boys Hostel Policy 2024-25' for undergraduate male students, defining specific room types and allocation rules for that academic year.
- A policy is set for 'PG Girls Hostel' that applies to all postgraduate female students, regardless of their department.

**Questions this answers**

- How do I create a hostel policy?
- Can I edit an active hostel policy?
- How many hostel policies can be active at once?
- Can hostel policies be specific to academic years?
- What criteria can be used for hostel policy options?
- How to define hostel rules?

**Keywords:** Hostel Policy, define policy, policy name, policy code, active policy, academic year, semester, room sharing, gender, department, program, batch year, quota, policy options, room allocation rules, hostel management rules, configure policy, institutional guidelines, consistency, hostel rules

**Synonyms:** Hostel Rules, Hostel Guidelines, Hostel Allocation Policy

**Related:** hostel-policy-option, allow-student-self-registration-for-hostel-allotments

**Tags:** Hostel Management, Configuration, Policy, Rules

---

## Hostel Policy Option

<!-- id: hostel-policy-option | category: Hostel Fee Configuration -->

**What it does**

This feature allows defining specific criteria within a Hostel Policy, including Option Name, Code (auto-generated or manual), Fee Amount, and criteria like Department, Programme, Batch Year, Quota, Gender, and Room Type, along with Allotment Start and End Dates.

**Why it matters**

It is critical for tailoring room allocations to institutional rules and student preferences. It provides flexibility in selecting criteria, ensuring assignments meet administrative requirements and student needs, and helps maintain organized, transparent, and efficient room allocation systems.

**How to use**

1. Provide a unique 'Option Name' and 'Option Code' (can be auto-generated or manually entered).
2. Specify the 'Option Fee Amount', noting if it's for Dues Management (platform-tracked) or Offline Payment (externally managed).
3. Select applicable 'Option Department', 'Programme', 'Batch Year', 'Quota', and 'Gender' (can select all or specific options).
4. Define the 'Room Type' (e.g., single, double, triple).
5. Set the 'Allotment Start Date' and 'Allotment End Date' for the policy option period.

**Examples**

- An institution creates a 'Double Room - SC/ST Quota' policy option for the 'UG Boys Hostel Policy', specifying a fee amount, applicable only to the Computer Science department, and available for the 2024 batch.
- A 'Single Room - Female - General Quota' option is defined with a specific fee, open to all departments and programs for a particular academic year.

**Questions this answers**

- How do I define specific criteria for hostel room allocation?
- What details can I set for a hostel policy option?
- Can I specify different fees for different room types?
- How do I set gender-specific hostel rooms?
- What is an allotment start and end date for a policy option?
- Can I create policy options for specific departments or programs?

**Keywords:** Hostel Policy Option, Option Name, Option Code, Option Fee Amount, Option Department, Programme, Batch Year, Quota, Gender, Room Type, Allotment Start Date, Allotment End Date, allocation criteria, customized allocation, room assignment rules, Dues Management, Offline Payment, configure policy option, hostel fees, room types, gender-based accommodation, hostel policy criteria

**Synonyms:** Hostel Policy Criteria, Hostel Allocation Options, Specific Hostel Rules

**Related:** hostel-policy, hostel-payment-mode, hostel-allotment-type

**Tags:** Hostel Management, Configuration, Policy, Rules, Fees

---

## Admin Privileges (Infrastructure Management)

<!-- id: admin-privileges-infrastructure-management | category: Admin Privileges -->

**What it does**

This prerequisite requires the administrator to first add hostel buildings, rooms, and beds within the Infrastructure Management section to ensure the necessary physical infrastructure is available for room allocation.

**Why it matters**

It ensures that the foundational physical infrastructure (hostel buildings, rooms, beds) is properly defined and available in the system before any room allocation or management can occur, preventing errors and ensuring accurate data.

**How to use**

1. Access the 'Infrastructure Management' section.
2. Add details for hostel buildings.
3. Add details for hostel rooms within those buildings.
4. Configure individual beds within the rooms.

**Questions this answers**

- What are the prerequisites for setting up hostels?
- How do I add hostel buildings in Digii?
- Where do I configure hostel rooms and beds?
- What permissions are needed for infrastructure management?
- Can I allocate rooms without defining buildings first?

**Keywords:** Admin Privileges, Infrastructure Management, hostel buildings, hostel rooms, hostel beds, room allocation, physical infrastructure, add buildings, add rooms, add beds, prerequisite, admin access, hostel setup, infrastructure setup

**Synonyms:** Infrastructure Management Permissions, Hostel Infrastructure Setup Rights

**Related:** hostel-building-configuration, hostel-room-configuration, hostel-bed-configuration

**Tags:** Admin Privileges, Infrastructure Management, Hostel Management, Configuration

---

## Hostel Management Settings (General Prerequisite)

<!-- id: hostel-management-settings-general-prerequisite | category: Admin Privileges -->

**What it does**

This prerequisite requires administrators to have appropriate read and write permissions for Hostel Management settings to effectively manage and update all hostel-related data within the platform.

**Why it matters**

It ensures that administrators have the necessary access rights to perform all functions related to hostel management, from viewing configurations to making updates, which is crucial for maintaining accurate records and smooth operations.

**Questions this answers**

- What permissions do I need for hostel management?
- How do I get access to hostel settings?
- Can I manage hostel data without specific permissions?
- What are the general prerequisites for hostel management?
- Who can update hostel information?

**Keywords:** Hostel Management Settings, admin permissions, read permissions, write permissions, manage hostel data, update hostel data, hostel-related data, access rights, prerequisite, hostel administration, hostel admin access

**Synonyms:** Hostel Management Access Rights, Hostel Admin Permissions, Hostel Settings Privileges

**Related:** hostel-management-settings-super-admin-write-privilege, hostel-management-settings-super-admin-read-privilege

**Tags:** Admin Privileges, Hostel Management, Security, Configuration

---

## Hostel Building Configuration

<!-- id: hostel-building-configuration | category: Infrastructure Management -->

**What it does**

This feature allows administrators to add and manage hostel buildings within the platform under Infrastructure Management, including specifying building details such as name, location, and available facilities.

**Why it matters**

It is essential for establishing the foundational structure of hostel accommodations, enabling systematic organization and management of physical spaces. It ensures that all buildings are properly cataloged with their specific attributes.

**How to use**

1. Navigate to 'Infrastructure Management'.
2. Select the option to add or manage hostel buildings.
3. Enter building details such as name, location, and available facilities.

**Questions this answers**

- How do I add a new hostel building?
- Where can I manage hostel building details?
- What information can I configure for a hostel building?
- Can I specify facilities for a hostel building?
- How to set up hostel buildings in Digii?

**Keywords:** Hostel Building Configuration, add hostel buildings, manage hostel buildings, Infrastructure Management, building details, name, location, facilities, hostel infrastructure, physical spaces, building setup, configure buildings, hostel structure

**Synonyms:** Hostel Building Setup, Manage Hostel Buildings, Hostel Infrastructure Building

**Related:** admin-privileges-infrastructure-management, hostel-room-configuration

**Tags:** Hostel Management, Infrastructure Management, Configuration

---

## Hostel Room Configuration

<!-- id: hostel-room-configuration | category: Infrastructure Management -->

**What it does**

This feature enables administrators to add and manage hostel rooms under a specific building, detailing room numbers, capacities, and available amenities, which helps streamline room allotment based on student preferences and availability.

**Why it matters**

It is crucial for organizing and detailing the individual living spaces within hostels. It allows for precise management of room attributes, facilitating efficient room allocation and ensuring students are assigned appropriate accommodations.

**How to use**

1. Navigate to 'Infrastructure Management'.
2. Select a specific hostel building.
3. Add or manage hostel rooms, specifying room numbers, capacities, and amenities.

**Questions this answers**

- How do I add rooms to a hostel building?
- What details can I configure for a hostel room?
- Can I set room capacity?
- Where do I manage hostel room amenities?
- How to streamline room allotment based on room details?

**Keywords:** Hostel Room Configuration, add hostel rooms, manage hostel rooms, room numbers, capacities, amenities, room allotment, student preferences, availability, hostel infrastructure, configure rooms, room setup, hostel room details

**Synonyms:** Hostel Room Setup, Manage Hostel Rooms, Room Details Configuration

**Related:** admin-privileges-infrastructure-management, hostel-building-configuration, hostel-bed-configuration

**Tags:** Hostel Management, Infrastructure Management, Configuration

---

## Hostel Bed Configuration

<!-- id: hostel-bed-configuration | category: Infrastructure Management -->

**What it does**

This feature allows administrators to assign and configure individual beds within hostel rooms, ensuring accurate bed assignments for students.

**Why it matters**

It ensures granular control over bed allocation, preventing double bookings and facilitating precise management of student placements within rooms. This is vital for accurate record-keeping and efficient space utilization.

**How to use**

1. Navigate to 'Infrastructure Management'.
2. Select a specific hostel room.
3. Assign and configure individual beds within that room.

**Questions this answers**

- How do I assign beds in a hostel room?
- Can I configure individual beds?
- Where do I manage hostel bed assignments?
- How to ensure accurate bed allocation for students?
- What is hostel bed configuration?

**Keywords:** Hostel Bed Configuration, assign beds, configure beds, individual beds, hostel rooms, accurate bed assignments, bed management, hostel infrastructure, bed setup, hostel bed details

**Synonyms:** Hostel Bed Setup, Manage Hostel Beds, Bed Assignment

**Related:** admin-privileges-infrastructure-management, hostel-room-configuration

**Tags:** Hostel Management, Infrastructure Management, Configuration

---
