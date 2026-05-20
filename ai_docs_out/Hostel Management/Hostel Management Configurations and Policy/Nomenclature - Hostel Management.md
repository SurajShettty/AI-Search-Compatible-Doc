# Hostel Management Nomenclature

**Module:** Hostel Management  
**Tags:** Hostel Management, Terminology, Definitions, Configuration, Payment, Allotment, Policies, Admin Privileges


## Overview

This document defines key terminology and concepts related to Digii's Hostel Management module, covering administrative privileges, configuration settings for payments and room allotments, and detailed hostel policy options.

## Hostel Management Settings Super Admin Write

<!-- id: hostel-management-settings-super-admin-write | category: Privileges -->

**What it does**

This admin privilege allows wardens to access and modify the hostel management configuration settings, which mainly includes payment and allotment type.

**Why it matters**

It grants the necessary permissions for wardens to manage and update critical hostel settings, ensuring operational flexibility and control over payment and allotment processes.

**Questions this answers**

- What is Hostel Management Settings Super Admin Write?
- Who can modify hostel settings?
- How do wardens get permission to change hostel configuration?
- What settings can a Super Admin Write user modify in hostel management?
- Can I edit payment types with this privilege?

**Keywords:** Hostel Management Settings Super Admin Write, admin privilege, warden permissions, modify settings, edit configuration, payment type, allotment type, hostel configuration, access control, write access, super admin, hostel admin, permissions, rights, update hostel settings, change hostel settings

**Synonyms:** Hostel Admin Write Privilege, Warden Edit Rights, Hostel Configuration Modification Access

**Related:** hostel-management-settings-super-admin-read, hostel-management-configuration

**Tags:** Privilege, Hostel Management, Admin, Warden, Settings, Configuration, Permissions

---

## Hostel Management Settings Super Admin Read

<!-- id: hostel-management-settings-super-admin-read | category: Privileges -->

**What it does**

This admin privilege allows wardens to only view and access the hostel management configuration settings, which mainly includes payment and allotment type.

**Why it matters**

It provides transparency and oversight by allowing wardens to monitor hostel settings without making changes, ensuring they can stay informed about payment and allotment configurations.

**Questions this answers**

- What is Hostel Management Settings Super Admin Read?
- Who can view hostel settings?
- How do wardens get permission to view hostel configuration?
- What settings can a Super Admin Read user view in hostel management?
- Can I see payment types with this privilege?

**Keywords:** Hostel Management Settings Super Admin Read, admin privilege, warden permissions, view settings, access configuration, payment type, allotment type, hostel configuration, read access, super admin, hostel admin, permissions, rights, monitor hostel settings, see hostel settings

**Synonyms:** Hostel Admin Read Privilege, Warden View Rights, Hostel Configuration Viewing Access

**Related:** hostel-management-settings-super-admin-write, hostel-management-configuration

**Tags:** Privilege, Hostel Management, Admin, Warden, Settings, Configuration, Permissions

---

## Hostel Management Configuration

<!-- id: hostel-management-configuration | category: Configuration -->

**What it does**

This module enables institutions to configure all essential settings for efficient hostel administration, streamlining payment processes and room allotments, ensuring transparency and accountability.

**Why it matters**

It provides a centralized platform for customizing hostel operations, allowing administrators to align payment modes and allotment methods with institutional policies, which promotes smooth management and optimal resource utilization.

**Examples**

- Customizing payment modes like Dues Management or Offline Payment.
- Defining room allotment methods such as Manual or Auto Allotment.

**Questions this answers**

- What is the Hostel Management Configuration module?
- How do I set up hostel administration?
- What settings can I configure for hostels?
- How does Hostel Management Configuration help with payments?
- Can I customize room allotment methods?

**Keywords:** Hostel Management Configuration, hostel administration, configure settings, payment processes, room allotments, transparency, accountability, customize payment modes, define room allotment methods, institutional policies, resource utilization, hostel module, setup hostel, manage hostel, hostel setup, hostel settings

**Synonyms:** Hostel Setup, Hostel Admin Settings, Hostel Module Configuration

**Related:** hostel-payment-mode, hostel-allotment-type, consolidated-settings, core-data-management-consolidated-settings-module

**Tags:** Hostel Management, Configuration, Settings, Module, Administration, Payment, Allotment

---

## Hostel Payment Mode

<!-- id: hostel-payment-mode | category: Payment Configuration -->

**What it does**

This setting allows institutions to define how hostel fee payments are processed and recorded, offering options like Dues Management (tracked within the platform) or Offline Payment (handled externally).

**Why it matters**

It provides flexibility in managing hostel fees, allowing institutions to choose between integrated tracking for full visibility or external handling for traditional methods, ensuring operational control and alignment with financial processes.

**Examples**

- Selecting 'Dues Management' to track all payments, due dates, and statuses within the platform.
- Choosing 'Offline Payment' for cash or cheque transactions managed manually.

**Questions this answers**

- What is Hostel Payment Mode?
- How do I set up hostel fee payments?
- What are the options for hostel payment modes?
- Can I track hostel payments within the platform?
- What is the difference between Dues Management and Offline Payment?

**Keywords:** Hostel Payment Mode, hostel fee payments, payment processing, payment recording, Dues Management, Offline Payment, fee amount, due date, payment status, Hostel Administrators, cash transactions, cheque transactions, manual record-keeping, payment settings, configure payments, hostel billing

**Synonyms:** Hostel Fee Payment Method, Hostel Payment Option, Hostel Billing Mode

**Related:** dues-management, offline-payment, hostel-management-configuration

**Tags:** Hostel Management, Payment, Configuration, Fees, Dues, Offline

---

## Dues Management

<!-- id: dues-management | category: Payment Tracking -->

**What it does**

The platform records hostel payment details, including amounts, due dates, and payment status, enabling both Hostel Administrators and students to track outstanding fees easily. Room allocation is carried out based on the configured Hostel Payment Mode and Hostel Allotment Type.

**Why it matters**

It ensures transparency and ease of tracking for hostel fees, providing complete visibility to both administrators and students, and integrates seamlessly with room allocation processes for a smooth and transparent allotment.

**Examples**

- Students checking their outstanding hostel fees and due dates on the platform.
- Hostel Administrators viewing payment statuses and allocating rooms after dues are cleared.

**Questions this answers**

- What is Dues Management in Digii?
- How can students track their hostel fees?
- Where are hostel payment details recorded?
- How does Dues Management affect room allocation?
- Can I see outstanding hostel fees?

**Keywords:** Dues Management, hostel payment details, fee amounts, due dates, payment status, track outstanding fees, Hostel Administrator, students, room allocation, Hostel Payment Mode, Hostel Allotment Type, payment records, platform tracking, online payments, fee tracking, outstanding fees, manage dues

**Synonyms:** Online Fee Tracking, Hostel Fee Dues, Payment Tracking System

**Related:** hostel-payment-mode, offline-payment, hostel-allotment-type, hostel-management-configuration

**Tags:** Hostel Management, Payment, Dues, Tracking, Students, Admin, Allotment

---

## Offline Payment

<!-- id: offline-payment | category: Payment Configuration -->

**What it does**

This is an alternative payment option where transactions occur outside the platform (e.g., cash, cheque). These payments are not tracked within the platform and require manual updates by Hostel Administrators.

**Why it matters**

It offers flexibility for institutions preferring traditional payment handling methods, allowing them to accept payments externally while maintaining organizational control through manual record-keeping.

**Examples**

- A student paying hostel fees by cash at the administrative office.
- An institution accepting a cheque for hostel fees and manually updating the student's record.

**Questions this answers**

- What is Offline Payment for hostel fees?
- How do I record offline hostel payments?
- Are offline payments tracked in Digii?
- Can students pay hostel fees by cash or cheque?
- Who manages offline payment records?

**Keywords:** Offline Payment, alternative payment option, transactions outside platform, cash payment, cheque payment, manual record-keeping, Hostel Administrators, external payments, traditional payment methods, payment flexibility, not tracked in platform, manual payment, hostel fee cash, hostel fee cheque

**Synonyms:** Manual Hostel Payment, External Fee Payment, Cash/Cheque Hostel Payment

**Related:** hostel-payment-mode, dues-management

**Tags:** Hostel Management, Payment, Offline, Manual, Fees

---

## Consolidated Settings

<!-- id: consolidated-settings | category: Payment Configuration -->

**What it does**

This section enables Hostel Administrators to configure a single, common payment page where students can make multiple payments (e.g., Academic, Transport, and Hostel fees) simultaneously. Administrators can define which fee categories appear and allowed combinations.

**Why it matters**

It simplifies and speeds up the payment process for both students and administrators by offering a convenient single point of payment for various fees, improving user experience and administrative efficiency.

**Examples**

- Allowing students to pay Academic and Transport fees together on one page.
- Configuring the system so Hostel fees can only be paid through the consolidated page.

**Questions this answers**

- What are Consolidated Settings for payments?
- How can students pay multiple fees at once?
- Can I combine Academic and Hostel fees for payment?
- How do I configure the consolidated payment page?
- What is the benefit of consolidated payments?

**Keywords:** Consolidated Settings, common payment page, multiple payments, Academic Fee, Transport Fee, Hostel fees, fee categories, payment combinations, simplify payment process, faster payments, convenient payments, Hostel administrators, payment configuration, single payment gateway, unified payment

**Synonyms:** Unified Payment Page, Combined Fee Payment, Integrated Payment Settings

**Related:** core-data-management-consolidated-settings-module

**Tags:** Hostel Management, Payment, Configuration, Fees, Consolidated, Student Self-Service

---

## Hostel Allotment Type

<!-- id: hostel-allotment-type | category: Allotment Configuration -->

**What it does**

This configuration determines how hostel rooms are assigned to students, offering choices between Manual or Auto Allotment methods based on operational preferences.

**Why it matters**

It provides institutions with flexibility to manage room assignments, allowing them to choose between personalized manual allocation or efficient, criteria-based automatic allocation, ensuring fairness and optimal resource use.

**Examples**

- Choosing 'Manual Allotment' to personally assign rooms based on student preferences.
- Selecting 'Auto Allotment' for systematic, criteria-based room assignments.

**Questions this answers**

- What is Hostel Allotment Type?
- How are hostel rooms assigned?
- What are the options for hostel room allotment?
- Can I manually assign hostel rooms?
- What is auto allotment?

**Keywords:** Hostel Allotment Type, hostel rooms assigned, Manual Allotment, Auto Allotment, operational preferences, room assignment methods, student preference, gender, availability, systematic allotment, criteria-based allotment, efficiency, fairness, allotment configuration, room allocation

**Synonyms:** Hostel Room Assignment Method, Room Allocation Type, Hostel Allotment Setting

**Related:** manual-allotment, auto-allotment, hostel-management-configuration

**Tags:** Hostel Management, Allotment, Configuration, Rooms, Students

---

## Manual Allotment

<!-- id: manual-allotment | category: Allotment Method -->

**What it does**

Under this allotment type, Hostel Administrators personally assign rooms to students based on the Hostel Payment Mode configuration. If Dues Management is used, allotment occurs after dues are cleared; if Offline Payment is used, allotment follows external payment confirmation.

**Why it matters**

It allows for personalized room assignments, accommodating individual student preferences or specific institutional guidelines, while ensuring that payment status is considered before final allocation.

**Examples**

- An administrator assigning a specific room to a student after verifying their Dues Management payment.
- An administrator assigning a room after receiving an offline payment confirmation.

**Questions this answers**

- How does Manual Allotment work?
- Who assigns rooms in Manual Allotment?
- When does room allotment happen with Dues Management in Manual Allotment?
- What if a student pays offline for Manual Allotment?
- Can I assign specific rooms to students?

**Keywords:** Manual Allotment, Hostel administrators, personally assign rooms, Hostel Payment Mode, Dues Management, dues cleared, Offline Payment, external payment, room allocation, student preferences, institutional guidelines, manual room assignment, assign rooms manually, hostel admin allotment

**Synonyms:** Personal Room Assignment, Admin Allotment, Handled Allotment

**Related:** hostel-allotment-type, dues-management, offline-payment

**Tags:** Hostel Management, Allotment, Manual, Admin, Rooms, Payment

---

## Auto Allotment

<!-- id: auto-allotment | category: Allotment Method -->

**What it does**

Under the Auto Allotment type, rooms are allocated to students based on the Hostel Payment Mode configuration. If Dues Management is selected, students can choose their preferred room, and dues are generated for payment. This type does not apply when the hostel payment method is set to Offline Payment.

**Why it matters**

It streamlines the room allocation process by allowing students to self-select rooms and automatically generating dues, enhancing efficiency and student convenience, especially when integrated with online payment tracking.

**Examples**

- A student selecting an available room through the portal, which then generates a payment due for that room.
- The system automatically assigning rooms based on predefined criteria after payment.

**Questions this answers**

- How does Auto Allotment work for hostels?
- Can students choose their own rooms with Auto Allotment?
- What happens after a student selects a room in Auto Allotment?
- Does Auto Allotment work with Offline Payment?
- How are dues generated for Auto Allotment?

**Keywords:** Auto Allotment, rooms allocated, Hostel Payment Mode, Dues Management, students select room, preferred room, dues generated, Payments tab, Offline Payment not applicable, automatic room assignment, systematic allocation, student self-service, efficient allotment, automated room allocation

**Synonyms:** Automatic Room Assignment, System Allotment, Self-Service Allotment

**Related:** hostel-allotment-type, dues-management

**Tags:** Hostel Management, Allotment, Auto, Students, Rooms, Payment

---

## Hostel Policy

<!-- id: hostel-policy | category: Policy Management -->

**What it does**

The Hostel Policy allows institutions to define specific policies by name and code for hostel management. Only one active policy is allowed at a time, which can be defined on an institution basis or for specific academic years or semesters. Once created, a policy cannot be edited, archived, or deleted.

**Why it matters**

It ensures consistent and clear guidelines for hostel management, aligning operations with institutional policies and streamlining allocation, while preventing unauthorized changes to established rules.

**Examples**

- Creating a policy named "UG Hostel Policy 2024" for undergraduate (UG) students in the 2024 academic year.
- Defining a policy with a unique code for easy reference.

**Questions this answers**

- What is a Hostel Policy?
- How do I create a hostel policy?
- Can I edit an existing hostel policy?
- How many active hostel policies can I have?
- Can a hostel policy apply to specific academic years?

**Keywords:** Hostel Policy, define policies, policy name, policy code, hostel management, active policy, institution basis, academic years, semesters, cannot be edited, cannot be archived, cannot be deleted, policy guidelines, hostel rules, accommodation policy, create policy

**Synonyms:** Hostel Rules, Accommodation Policy, Hostel Guidelines

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Rules, Admin

---

## Hostel Policy Option

<!-- id: hostel-policy-option | category: Policy Management -->

**What it does**

Hostel Policy Options are defined based on specific criteria like room sharing preferences, gender, department, program, batch year, and quota. Institutions can create multiple options, but once created, these options cannot be edited, archived, or deleted. These predefined options allow for a customized allocation of rooms, ensuring that students are assigned hostel accommodations in line with institutional policies.

**Why it matters**

It provides flexibility to tailor room allocations to diverse student needs while ensuring adherence to standardized criteria, making the process efficient, fair, and aligned with institutional rules.

**Examples**

- Creating an option for "Double Sharing - Female - Engineering Dept - 2025 Batch".
- Defining an option for "Single Room - Non-Resident Indian (NRI) Quota".

**Questions this answers**

- What are Hostel Policy Options?
- How do I define criteria for hostel room allocation?
- Can I edit a hostel policy option after creating it?
- What factors can be used to define policy options?
- How do policy options ensure fair room assignments?

**Keywords:** Hostel Policy Option, room sharing preferences, gender, department, program, batch year, quota, create policy options, cannot be edited, cannot be archived, cannot be deleted, customized allocation, institutional policies, standardized criteria, room assignment, multiple policy options, define policy options

**Synonyms:** Policy Criteria, Allocation Options, Hostel Rule Options

**Related:** hostel-policy, option-name, option-code, option-fee-amount, option-department, programme, batch-year, quota, gender, capacity-of-the-room, allotment-start-date, allotment-end-date

**Tags:** Hostel Management, Policy, Configuration, Criteria, Rooms, Students

---

## Option Name

<!-- id: option-name | category: Policy Option Details -->

**What it does**

This is a unique identifier for a hostel policy option, reflecting its allocation criteria or focus.

**Why it matters**

It provides a clear and descriptive label for each policy option, making it easy to identify and manage specific room allocation rules.

**Examples**

- Naming an option "Girls Hostel - Single Room - Undergraduate (UG)".
- Using "Boys Hostel - Double Sharing - Postgraduate (PG) - Non-Resident Indian (NRI)".

**Questions this answers**

- What is the Option Name for a hostel policy?
- How do I name a hostel policy option?
- What should an Option Name reflect?

**Keywords:** Option Name, unique identifier, hostel policy option, allocation criteria, policy focus, policy option name, label, identification, name policy option

**Synonyms:** Policy Option Title, Option Label

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Naming

---

## Option Code

<!-- id: option-code | category: Policy Option Details -->

**What it does**

This is a platform-generated or manually created code representing a specific hostel policy for easy reference and identification. A toggle allows for auto-generation or manual entry.

**Why it matters**

It provides a concise and unique reference for each policy option, simplifying identification and management, especially in systems where codes are used for internal processes.

**How to use**

1. 1. Navigate to Hostel Policy Options.
2. 2. When creating a new option, locate the 'Option Code' field.
3. 3. Toggle the auto-generate switch ON for platform-generated code, or OFF to manually enter a custom code.

**Examples**

- A platform-generated code like "HPLCY001".
- A manually entered code such as "BH-DS-PG-NRI".

**Questions this answers**

- What is the Option Code for a hostel policy?
- Can I manually enter the Option Code?
- How is the Option Code generated?
- What is the purpose of an Option Code?

**Keywords:** Option Code, platform-generated code, manually created code, hostel policy, easy reference, identification, toggle, auto-generate code, manual entry, policy option code, create code, generate code

**Synonyms:** Policy Option ID, Hostel Policy Identifier

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Code, Admin

---

## Option Fee Amount

<!-- id: option-fee-amount | category: Policy Option Details -->

**What it does**

This is the fee associated with the policy option, including hostel fees based on room type, sharing, and other factors. If Dues Management is selected, the amount is paid through the platform; if Offline Payment is selected, it's paid offline, and the Hostel Administrator allots the room upon payment confirmation.

**Why it matters**

It clearly defines the financial cost for each specific hostel policy option, ensuring transparency for students and guiding administrators in room allotment based on payment status, whether online or offline.

**Examples**

- Setting an Option Fee Amount of $1500 for a single room.
- Defining a fee of $1000 for a double-sharing room with Dues Management.

**Questions this answers**

- What is the Option Fee Amount?
- How is the Option Fee Amount determined?
- Does the Option Fee Amount vary by room type?
- How is the Option Fee Amount paid with Dues Management?
- What happens if the Option Fee Amount is paid offline?

**Keywords:** Option Fee Amount, fee associated, policy option, hostel fees, room type, sharing, Dues Management, paid through platform, Offline Payment, paid offline, Hostel Administrator, allot room, payment confirmation, fee calculation, hostel charges, cost of hostel

**Synonyms:** Policy Option Fee, Hostel Option Cost, Room Fee

**Related:** hostel-policy-option, dues-management, offline-payment

**Tags:** Hostel Management, Policy, Fees, Payment, Configuration

---

## Option Department

<!-- id: option-department | category: Policy Option Criteria -->

**What it does**

This specifies the academic department under which the hostel policy option applies, managing room allocations based on departmental requirements. The platform allows selection of either all departments or specific selected departments.

**Why it matters**

It enables institutions to tailor hostel allocations to specific departmental needs or quotas, ensuring that accommodation policies align with academic structures and student demographics.

**How to use**

1. 1. When configuring a Hostel Policy Option, locate the 'Option Department' setting.
2. 2. Select the 'All Departments' checkbox to apply the policy to all academic departments.
3. 3. Alternatively, uncheck 'All Departments' and use the checkboxes to select specific departments for which the policy option is applicable.

**Examples**

- Applying a policy option only to the "Engineering Department".
- Making a policy option available to "All Departments".

**Questions this answers**

- How do I apply a hostel policy option to a specific department?
- Can a hostel policy option apply to all departments?
- What is Option Department?
- How does department selection affect room allocation?

**Keywords:** Option Department, academic department, hostel policy option, room allocations, departmental requirements, all departments, selected department, checkbox, department-specific policy, assign by department

**Synonyms:** Policy Department, Departmental Allocation

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Department, Criteria

---

## Programme

<!-- id: programme | category: Policy Option Criteria -->

**What it does**

This specifies the academic program (e.g., undergraduate (UG), postgraduate (PG), or diploma programs) to which the hostel policy option applies. The platform allows selection of all programs or multiple specific programs.

**Why it matters**

It ensures that hostel accommodation policies are aligned with the specific needs and structures of different academic programs, allowing for targeted and relevant room allocations.

**How to use**

1. 1. When configuring a Hostel Policy Option, locate the 'Programme' setting.
2. 2. Select the 'All Programs' checkbox to apply the policy to all academic programs.
3. 3. Alternatively, uncheck 'All Programs' and use the checkboxes to select multiple specific programs for which the policy option is applicable.

**Examples**

- Applying a policy option only to "Undergraduate Programs".
- Making a policy option available to "Postgraduate" and "Diploma" programs.

**Questions this answers**

- How do I apply a hostel policy option to a specific academic program?
- Can a hostel policy option apply to all programs?
- What is the 'Programme' setting for hostel policies?
- How does program selection affect room allocation?

**Keywords:** Programme, academic program, hostel policy option, undergraduate, postgraduate, diploma, all programs, multiple programs, checkbox, program-specific policy, UG, PG, assign by program

**Synonyms:** Academic Program, Course of Study, Study Programme

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Program, Criteria

---

## Batch Year

<!-- id: batch-year | category: Policy Option Criteria -->

**What it does**

This specifies the specific academic year or batch of students to which the policy option applies, ensuring room allocation aligns with the academic cycle. The platform allows selection of all batch years or multiple specific batch years.

**Why it matters**

It enables institutions to manage hostel allocations precisely for different student cohorts, ensuring that policies are relevant to the academic cycle and student intake.

**How to use**

1. 1. When configuring a Hostel Policy Option, locate the 'Batch Year' setting.
2. 2. Select the 'All Batch Years' checkbox to apply the policy to all academic batches.
3. 3. Alternatively, uncheck 'All Batch Years' and use the checkboxes to select multiple specific batch years for which the policy option is applicable.

**Examples**

- Applying a policy option only to the "2023 Batch".
- Making a policy option available to "2022" and "2023" batch years.

**Questions this answers**

- How do I apply a hostel policy option to a specific batch year?
- Can a hostel policy option apply to all batch years?
- What is the 'Batch Year' setting for hostel policies?
- How does batch year selection affect room allocation?

**Keywords:** Batch Year, academic year, batch of students, policy option, room allocation, academic cycle, all batch years, multiple batch years, checkbox, batch-specific policy, student cohort, assign by batch

**Synonyms:** Academic Batch, Student Intake Year, Admission Year

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Batch, Criteria

---

## Quota

<!-- id: quota | category: Policy Option Criteria -->

**What it does**

This specifies a particular category under which students are assigned to the hostel, such as general, Non-Resident Indian (NRI), Scheduled Caste/Scheduled Tribe (SC/ST), or others. The platform allows selection of all quotas or multiple specific quotas.

**Why it matters**

It allows institutions to implement reservation policies or specific allocation rules based on student categories, ensuring compliance and equitable distribution of hostel accommodations.

**How to use**

1. 1. When configuring a Hostel Policy Option, locate the 'Quota' setting.
2. 2. Select the 'All Quotas' checkbox to apply the policy to all student categories.
3. 3. Alternatively, uncheck 'All Quotas' and use the checkboxes to select multiple specific quotas (e.g., General, NRI, SC/ST) for which the policy option is applicable.

**Examples**

- Applying a policy option only to the "Non-Resident Indian (NRI) Quota".
- Making a policy option available to "General" and "Scheduled Caste/Scheduled Tribe (SC/ST)" quotas.

**Questions this answers**

- How do I apply a hostel policy option to a specific quota?
- Can a hostel policy option apply to all quotas?
- What is the 'Quota' setting for hostel policies?
- How does quota selection affect room allocation?
- Can I set policies for NRI students?

**Keywords:** Quota, student category, hostel assignment, general quota, NRI, SC/ST, all quotas, multiple quotas, checkbox, reservation policy, allocation rules, student demographics, assign by quota

**Synonyms:** Reservation Category, Student Category, Admission Quota

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Quota, Criteria

---

## Gender

<!-- id: gender | category: Policy Option Criteria -->

**What it does**

This specifies the gender-based accommodation policy, ensuring male and female students are assigned to gender-appropriate rooms. The platform allows selection of male, female, other, or all genders, with the option to select multiple.

**Why it matters**

It ensures adherence to gender-specific accommodation rules, promoting safety, privacy, and appropriate living environments for all students within the hostel.

**How to use**

1. 1. When configuring a Hostel Policy Option, locate the 'Gender' setting.
2. 2. Select 'All Genders' to apply the policy to all genders.
3. 3. Alternatively, select specific options like 'Male', 'Female', or 'Other' to define gender-appropriate room assignments.

**Examples**

- Applying a policy option only to "Female" students for a specific hostel block.
- Making a policy option available to "Male" and "Other" genders.

**Questions this answers**

- How do I set gender-specific hostel policies?
- Can a hostel policy option apply to all genders?
- What are the gender options for hostel policies?
- How does gender selection affect room allocation?

**Keywords:** Gender, gender-based accommodation, male students, female students, gender-appropriate rooms, all genders, select multiple genders, gender policy, room assignment, safety, privacy, assign by gender

**Synonyms:** Gender Policy, Gender-Specific Accommodation

**Related:** hostel-policy-option

**Tags:** Hostel Management, Policy, Configuration, Gender, Criteria

---

## Capacity of the Room

<!-- id: capacity-of-the-room | category: Policy Option Criteria -->

**What it does**

This defines the capacity of the hostel accommodation, such as single, double, or triple occupancy. It helps institutions categorize rooms based on the number of students sharing a space.

**Why it matters**

It ensures transparent allocation, accurate fee calculation, and efficient utilization of available hostel infrastructure by clearly defining room types based on occupancy.

**Examples**

- Setting a policy option for "Single Occupancy" rooms.
- Defining a policy option for "Double Occupancy" rooms with a specific fee.

**Questions this answers**

- How do I define room capacity for hostel policies?
- What are the room capacity options?
- How does room capacity affect fees?
- Can I set policies for single occupancy rooms?

**Keywords:** Capacity of the Room, hostel accommodation capacity, single occupancy, double occupancy, triple occupancy, categorize rooms, number of students sharing, transparent allocation, accurate fee calculation, efficient utilization, hostel infrastructure, room type, occupancy, room capacity

**Synonyms:** Room Occupancy, Room Type Capacity, Sharing Capacity

**Related:** hostel-policy-option, option-fee-amount

**Tags:** Hostel Management, Policy, Configuration, Rooms, Capacity, Fees

---

## Allotment Start Date

<!-- id: allotment-start-date | category: Policy Option Timing -->

**What it does**

This is the date when the hostel allotment starts for a particular policy option.

**Why it matters**

It ensures that room allocations begin at the designated time, aligning with the academic calendar and providing a structured timeline for students to secure accommodation.

**Examples**

- Setting the Allotment Start Date to "August 1st, 2024".

**Questions this answers**

- When does hostel allotment begin for a policy option?
- How do I set the allotment start date?
- What is the Allotment Start Date?

**Keywords:** Allotment Start Date, hostel allotment starts, policy option, designated time, academic calendar, structured timeline, room allocation start, start date for allotment

**Synonyms:** Allocation Start Date, Room Assignment Start Date

**Related:** hostel-policy-option, allotment-end-date

**Tags:** Hostel Management, Policy, Configuration, Dates, Allotment

---

## Allotment End Date

<!-- id: allotment-end-date | category: Policy Option Timing -->

**What it does**

This is the date when the hostel allotment ends for a particular policy option.

**Why it matters**

It ensures that room allocations conclude by a specific deadline, providing clarity for students and administrators and facilitating timely finalization of accommodation arrangements.

**Examples**

- Setting the Allotment End Date to "August 31st, 2024".

**Questions this answers**

- When does hostel allotment end for a policy option?
- How do I set the allotment end date?
- What is the Allotment End Date?

**Keywords:** Allotment End Date, hostel allotment ends, policy option, specific deadline, clarity, timely finalization, room allocation end, end date for allotment

**Synonyms:** Allocation End Date, Room Assignment End Date

**Related:** hostel-policy-option, allotment-start-date

**Tags:** Hostel Management, Policy, Configuration, Dates, Allotment

---

## Core Data Management - Consolidated Settings Module

<!-- id: core-data-management-consolidated-settings-module | category: Payment Configuration -->

**What it does**

This module within Core Data Management allows hostel administrators to configure important dues and manage fee-related settings for students. It includes options for 'Select Fee to be Displayed in Consolidated Payments' (Academic Fee, Hostel Fee, and Transport Fee) and enables 'Student Self-Registration for Hostel' based on policy options (Hostel Building, Hostel Room, Hostel Bed).

**Why it matters**

It provides a central hub for comprehensive fee and hostel self-service management, offering clear visibility of all applicable fees in a single view and empowering students with self-registration options, which enhances efficiency and user experience.

**How to use**

1. 1. Navigate to the Core Data Management module.
2. 2. Access the 'Consolidated Settings' section.
3. 3. Configure 'Select Fee to be Displayed in Consolidated Payments' by choosing Academic Fee, Hostel Fee, and/or Transport Fee.
4. 4. Enable 'Student Self-Registration for Hostel' and select policy options like Hostel Building, Hostel Room, or Hostel Bed to determine student visibility under the Important Dues section of the Payments tab.
5. 5. Use the edit button to add groups and customize fee optionality, such as combining Academic Fee and Hostel Fee or Transport Fee.

**Examples**

- Configuring the consolidated payment page to show Academic, Hostel, and Transport fees.
- Enabling students to self-register for a specific hostel room based on a policy option.
- Defining a fee group that allows payment for Academic and Hostel fees together.

**Questions this answers**

- What is the Core Data Management - Consolidated Settings Module?
- How do I configure consolidated payments for hostel fees?
- Can students self-register for hostels?
- How do I enable student self-registration for hostel rooms?
- What fee categories can be displayed in consolidated payments?
- How can I customize fee optionality in consolidated settings?

**Keywords:** Core Data Management, Consolidated Settings Module, hostel administrators, configure dues, manage fee-related settings, Select Fee to be Displayed in Consolidated Payments, Academic Fee, Hostel Fee, Transport Fee, clear visibility, student self-service, Student Self-Registration for Hostel, policy option, Hostel Building, Hostel Room, Hostel Bed, Important Dues section, Payments tab, fee optionality, edit button, add groups, customize optionality, fee management, user-friendly experience, centralized fee management, student hostel registration

**Synonyms:** Core Data Consolidated Settings, Hostel Fee Management Module, Student Self-Service Hostel Configuration

**Related:** consolidated-settings, hostel-policy-option, hostel-payment-mode, dues-management

**Tags:** Hostel Management, Core Data Management, Consolidated Payments, Self-Registration, Fees, Configuration, Students, Admin

---
