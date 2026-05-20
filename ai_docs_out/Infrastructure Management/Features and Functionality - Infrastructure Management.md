# Features and Functionality

**Module:** Infrastructure Management  
**Tags:** Infrastructure Management, Campus Facilities, Venue Booking, Asset Management, Digii Platform, Admin Privileges, Facility Management, Resource Allocation


## Overview

This document outlines the features and functionalities of the Digii campus-management platform's Infrastructure Management module. It covers the creation, editing, archiving, and booking rules for various infrastructure types and individual infrastructures, along with bulk management and historical tracking capabilities.

## Prerequisites

- **Infrastructure management** — Infrastructure management is an admin privilege which allows administrators to access and manage the infrastructure module as a super admin. This includes creating, editing and archiving infrastructures.

## Add New Infrastructure Type

<!-- id: add-new-infrastructure-type | category: Infrastructure Type -->

**What it does**

The Add New Infrastructure Type feature allows administrators to define and categorize different types of infrastructure available within the institution. This includes facilities such as classrooms, laboratories, hostels, auditoriums, sports complexes, or any other physical or digital infrastructures. By creating a new infrastructure type, the system enables structured data management and helps categorize resources under well-defined heads for easy tracking, reporting, and utilization planning. Additionally, these infrastructure types facilitate easier search and selection of venues within the "Book a Venue" module. Note: While adding a new infrastructure type, if we mark the infrastructure type as "Full Day Usage", it implies the booking is considered overnight. We need to enter the "Check-in Time (Day 1)" and "Check-out Time (Day 2)".

**Why it matters**

Higher education institutions manage a wide variety of infrastructure assets. Without a proper categorization system, it becomes difficult to monitor usage, plan maintenance, and allocate budgets effectively. This feature standardizes the classification of infrastructure resources, ensuring that every facility is organized under a consistent taxonomy. It supports scalability, simplifies infrastructure tracking, improves allocation of maintenance schedules, and enhances data accuracy for infrastructure-related analytics and audits.

**Examples**

- Suppose a university wants to manage different types of research centers. The administrator navigates to the Infrastructure Management Module and selects "Add New Infrastructure Type." They enter the type name as "Research Center". Once saved, this new category appears as an option in the infrastructure management module, allowing the administrators to add and manage multiple research centers under this new classification.
- If a university provides Guest Rooms to faculty or visiting faculty, then we can configure the "Full Day Usage" with check in and check out timings ensuring seamless guest rooms management.

**Questions this answers**

- How do I add a new type of infrastructure?
- Can I categorize different facilities in the system?
- What is 'Full Day Usage' when adding an infrastructure type?
- How do I define a new venue type?
- Where do I set up infrastructure categories?
- What are the steps to create a new facility type?
- How does infrastructure type help with venue booking?
- Can I add a new type for classrooms or laboratories?
- How to manage check-in and check-out times for full-day usage infrastructure?
- What is the purpose of infrastructure types?

**Keywords:** add infrastructure type, create infrastructure type, define infrastructure category, categorize facilities, infrastructure classification, venue types, resource categorization, full day usage, check-in time, check-out time, admin infrastructure, infrastructure management, new facility type, campus infrastructure, Digii infrastructure, add new type, facility categories, resource types, infrastructure setup, manage infrastructure types, infrastructure admin, create facility category, define venue type

**Synonyms:** facility type creation, resource category definition, venue type setup, infrastructure classification, add new category

**Related:** edit-infrastructure-type, delete-infrastructure-type, add-new-attribute-group, booking-rules-infrastructure-type

**Tags:** infrastructure type, creation, categorization, venue booking, full day usage

---

## Edit Infrastructure Type

<!-- id: edit-infrastructure-type | category: Infrastructure Type -->

**What it does**

The "Edit Infrastructure Type" feature allows administrators to modify the details of an existing infrastructure category, specifically by updating its name. However, an infrastructure type can only be edited if no infrastructure items have been mapped to it. Once any infrastructure has been created and linked to a type, the type name becomes locked to preserve system consistency and ensure data integrity.

**Why it matters**

The ability to edit an infrastructure type ensures flexibility and accuracy in maintaining institutional data. Administrators can correct naming errors or update category titles to reflect evolving campus structures or terminology. At the same time, restricting edits once infrastructures are linked prevents accidental inconsistencies, ensuring that all associated records remain reliable and standardized across the system. This balance between flexibility and control helps maintain data integrity and supports efficient infrastructure management.

**Examples**

- Suppose an administrator initially creates an infrastructure type named "Auditorium" but later decides to rename it to "Conference Hall." If no auditoriums have been created under that type, the administrator can edit the name directly. However, if auditoriums are already registered under that category, the system will restrict changes to the name.

**Questions this answers**

- How do I change the name of an infrastructure type?
- Can I edit an existing facility category?
- Why can't I rename an infrastructure type if items are linked?
- What happens if I try to edit a linked infrastructure type?
- How to update an infrastructure category?
- Is it possible to modify an infrastructure type's details?
- What are the restrictions on editing infrastructure types?

**Keywords:** edit infrastructure type, modify infrastructure category, update infrastructure name, rename facility type, change venue type, admin infrastructure edit, infrastructure management, edit existing type, update category title, restrict infrastructure edit, data integrity infrastructure, campus facility update, Digii infrastructure edit, edit type name, modify facility category, update facility name, change facility type

**Synonyms:** modify category, rename type, update facility category

**Related:** add-new-infrastructure-type, delete-infrastructure-type

**Tags:** infrastructure type, editing, modification, data integrity

---

## Delete Infrastructure Type

<!-- id: delete-infrastructure-type | category: Infrastructure Type -->

**What it does**

The Delete Infrastructure Type feature allows administrators to remove an existing infrastructure type from the system. This action is used when a particular type is no longer relevant or was created incorrectly. However, the system enforces a validation check - an infrastructure type can only be deleted if no infrastructure records are currently associated with it. This ensures that data integrity and existing infrastructure mappings are not affected.

**Why it matters**

Maintaining a clean and accurate list of infrastructure types is essential for streamlined asset management. Over time, administrators may need to remove obsolete or duplicate types to keep the categorization meaningful and easy to navigate. The built-in restriction prevents accidental deletion of active or linked data, safeguarding institutional records and preventing operational inconsistencies in infrastructure reports and usage analytics.

**Examples**

- An administrator notices that a duplicate entry named "Lecture Hall" was mistakenly created in addition to an existing type "Classroom". Before deleting "Lecture Hall," the system checks whether any infrastructure (like individual rooms) is linked to it. If no records are associated, the administrator can proceed with deletion. However, if any are linked, the system will display a validation message such as " Academic Building is mapped to a infrastructure, it cannot be deleted." This ensures that no data loss or structural inconsistency occurs within the Infrastructure Management Module.

**Questions this answers**

- How do I delete an infrastructure type?
- Can I remove a facility category from the system?
- What are the conditions for deleting an infrastructure type?
- Why can't I delete an infrastructure type if it has linked records?
- How to remove an obsolete infrastructure category?
- What message appears if I try to delete a linked infrastructure type?
- Is it possible to delete a duplicate infrastructure type?

**Keywords:** delete infrastructure type, remove infrastructure category, erase facility type, delete venue type, admin infrastructure delete, infrastructure management, delete obsolete type, remove duplicate type, data integrity infrastructure delete, campus facility delete, Digii infrastructure delete, delete type restriction, unmap infrastructure type, remove category, delete facility category

**Synonyms:** remove category, erase type, discard facility type

**Related:** add-new-infrastructure-type, edit-infrastructure-type

**Tags:** infrastructure type, deletion, removal, data integrity

---

## Add New Attribute Group

<!-- id: add-new-attribute-group | category: Infrastructure Type -->

**What it does**

The Add New Group feature allows administrators to map an existing Attribute Group to any Infrastructure Type. This mapping determines which attributes will be available for selection when an infrastructure record of that type is created or updated. Once an attribute group is added to an infrastructure type, administrators can choose relevant attributes while adding or editing infrastructure details. The feature also supports two selection modes: Single Select: Only one attribute can be chosen from the group (e.g., selecting Air-Conditioned or Non-Air-Conditioned). Multi Select: Multiple attributes can be selected simultaneously (e.g., Wi-Fi Enabled, Projector Available, and Smart Board Equipped). This flexibility ensures that each infrastructure record is described accurately and consistently according to its real-world characteristics. NOTE : Attribute group can not be removed or deleted from an infrastructure type once it is added.

**Why it matters**

Every institution manages a diverse range of infrastructures, each requiring detailed metadata for tracking, maintenance, and reporting. The Add New Attribute Group feature standardizes how these details are captured by linking relevant attributes directly to specific infrastructure types. This eliminates redundancy, improves data consistency, and allows for deeper insights during analysis and planning. By structuring data at the attribute level, the system enhances the institution's ability to search, filter, and generate meaningful reports, ultimately improving operational efficiency and decision-making.

**Examples**

- An administrator is defining infrastructure details for the "Hostel Room" type. To ensure accurate data capture, multiple Attribute Groups are added to this infrastructure type, each serving a distinct purpose: Room Cooling Type (Single Select) Attributes: Air Conditioned, Air Cooled, Non Air Conditioned This group is configured as Single Select, so the administrator can choose only one option while creating or editing a room record. Example: For Room No. H-201, the administrator selects Air Conditioned. Room Facilities (Multi Select) Attributes: Attached Bathroom, Wi-Fi Enabled, Balcony Present, Laundry Access The group allows multiple selections, so the administrator can choose several applicable facilities for each room. Example: The same Room No. H-201 is marked with Attached Bathroom and Wi-Fi Enabled. After these configurations, when the admin or staff view the hostel inventory, each room displays standardized, structured information such as: Room No. H-201 — Air Conditioned, Attached Bathroom, Wi-Fi Enabled This structured use of single or multiple attribute groups ensures consistent data entry, enhances clarity in infrastructure details, and simplifies searches and reporting — for example, quickly identifying all Air Cooled Double Sharing Rooms with Wi-Fi.

**Questions this answers**

- How do I add an attribute group to an infrastructure type?
- What are attribute groups and how do they work?
- Can I define custom characteristics for infrastructure types?
- What is the difference between Single Select and Multi Select attributes?
- How do I map attributes to a facility type?
- Can attribute groups be removed once added to an infrastructure type?
- How do I ensure consistent data entry for infrastructure details?
- How to configure room facilities for a hostel type?
- What kind of attributes can I add to an infrastructure?

**Keywords:** add attribute group, map attribute group, infrastructure type attributes, single select attributes, multi select attributes, define infrastructure characteristics, facility metadata, standardize infrastructure details, attribute mapping, infrastructure configuration, admin attribute group, Digii infrastructure attributes, add group to type, attribute selection modes, room cooling type, room facilities, hostel room attributes, attribute group management, infrastructure data consistency, search attributes, filter attributes

**Synonyms:** link attribute group, assign attributes, configure facility details, attribute mapping

**Related:** add-new-infrastructure-type, add-new-infrastructure

**Tags:** infrastructure type, attributes, configuration, data consistency, single select, multi select

---

## Booking Rules

<!-- id: booking-rules-infrastructure-type | category: Infrastructure Type -->

**What it does**

The Booking Rules feature in Infrastructure Management allows administrators to define and manage booking permissions and configurations for each Infrastructure Type. These rules are applied at the infrastructure type level and are automatically inherited by all bookable venues under that type, though they can also be overridden at the individual venue level. Administrators can configure rules for three default user groups which are Administrator, Faculty, and Student. There are two booking modes which can be defined for an Infrastructure Type: 1. Single Booking: Only one venue within an infrastructure type can be booked under a single request. 2. Multi Booking: Multiple venues within the same infrastructure type can be booked under a single request. For each user group under both booking modes, the following settings can be configured: * Booking Allowed: A toggle to enable or disable booking permission for that user group. * Booking Type: A dropdown to define the type of booking (Direct Booking and Request Based Booking). In Direct Booking, the requester can select a preferred venue, subject to admin approval. In Request-Based Booking, the requester specifies the number of venues required under a particular infrastructure type, and the admin allocates the venues based on availability. * Admin Action Required: A checkbox to indicate whether admin approval is mandatory before the booking is confirmed. Administrators can also Add User Groups using the "+ Add User Group" button to extend booking permissions to additional user categories beyond the defaults. The Edit button allows modification of existing rule configurations. NOTE: These rules will be applied to all bookable venues of a given infrastructure type. They can be edited here or overridden at the individual venue level.

**Why it matters**

Booking Rules are foundational to managing equitable and controlled access to institutional venues. Without clearly defined rules, venues may be over-booked, misused, or accessed by unauthorized user groups. Setting rules at the infrastructure type level ensures consistency across all venues of that type, while still allowing venue-level customization where needed. This feature supports: * Access control by defining which user groups can book a venue. * Workflow governance by requiring admin approval for specific user groups or booking types. * Operational clarity by distinguishing between single and multi bookings with separate permission sets. * Scalability by applying one rule set across all venues of an infrastructure type, reducing administrative effort. * Transparency by making booking permissions explicit and auditable for all user groups.

**Examples**

- For example, if a university has 2 seminar halls and 10 classrooms, the administrator may choose to allow faculty to book only one seminar hall per request (with admin approval), while permitting multiple classrooms to be booked in a single request (also with admin approval). In this case, Single Booking will be enabled for the infrastructure type Seminar Hall, and Multi Booking will be enabled for the infrastructure type Classrooms. These configurations are then uniformly applied to all bookable seminar halls and classrooms across the campus, ensuring consistent and well-governed venue access.

**Questions this answers**

- How do I set booking rules for an infrastructure type?
- What are the different booking modes available?
- Can I allow faculty to book multiple venues at once?
- How do I require admin approval for venue bookings?
- What is the difference between Direct Booking and Request-Based Booking?
- Can I add custom user groups for booking permissions?
- How do booking rules apply to all venues of a type?
- Where can I configure booking permissions for students?
- How to manage venue access control?

**Keywords:** booking rules, infrastructure type booking, venue booking permissions, single booking, multi booking, direct booking, request based booking, admin approval booking, user group booking, facility booking rules, access control venues, manage venue bookings, infrastructure management booking, Digii booking rules, configure booking, booking allowed, booking type, admin action required, override booking rules, campus venue booking, seminar hall booking, classroom booking

**Synonyms:** venue reservation rules, facility access rules, booking configuration, reservation permissions

**Related:** add-new-infrastructure-type, add-new-infrastructure, booking-rules-infrastructure

**Tags:** infrastructure type, booking, rules, permissions, access control, single booking, multi booking, admin approval

---

## Add New Infrastructure

<!-- id: add-new-infrastructure | category: Add New Infrastructure -->

**What it does**

The Add New Infrastructure feature allows administrators to create a new infrastructure record under a specific Infrastructure Type. It helps institutions maintain a detailed digital record of all physical infrastructures such as classrooms, laboratories, hostels, offices, sports facilities, and buildings. While creating a new infrastructure, administrators can enter essential and optional details, including: - Infrastructure Type (mandatory) - Name (mandatory) - Code (mandatory) - Belongs To - Floor - Capacity - Opening Time / Closing Time - Number of Rooms - Number of Floors (Underground and Ground & Above) - Establishment Date - Contact Person - Description / Disclaimer - Attributes Among these, only Infrastructure Type, Name, and Code are mandatory fields. The remaining fields are optional and can be used based on the nature and use case of the infrastructure being created. For instance: When creating a Building, the administrator should enter the number of floors and rooms, but can leave the Belongs To and Floor fields blank, since a building is an independent unit and not located within another infrastructure. When creating a Classroom, the Capacity, Belongs To (building association), and Floor details become relevant, while Number of Floors and Number of Rooms are not required, as a classroom is a single-space unit. This flexible structure ensures that administrators can maintain accurate and relevant information for each type of infrastructure without unnecessary data entry. Additionally, any Attribute Groups mapped to the selected Infrastructure Type automatically appear, allowing administrators to select appropriate Attributes such as Air Conditioned, Wi-Fi Enabled, Seating Capacity, etc. This ensures standardized and detailed documentation for every infrastructure, supporting efficient tracking, allocation, and reporting. The feature also includes a "Can Be Booked" option, which integrates with the Venue Booking Module. When enabled, the selected infrastructure can be used for booking purposes (e.g., events, classes, or seminars). Administrators can configure: * Pricing type — per day or fixed fee. * Payment mode — currently offline (online payment integration not available). * Associated services from other departments (e.g., housekeeping, Information Technology (IT) support, transport) that can be availed during the booking. This configuration ensures a controlled, transparent, and efficient system for managing campus resource reservations.

**Why it matters**

The Add New Infrastructure feature is fundamental to building a structured digital ecosystem for managing institutional facilities. It allows accurate tracking and categorization of physical assets, ensures standardized data entry, and supports seamless integration with other operational modules like Hostel Management, Examination Management System (EMS) and Venue Booking. By enabling flexible field usage, the system adapts to diverse infrastructure types — from a single classroom to a multi-storey hostel building — ensuring data relevance and clarity. The integration with booking mechanism enhances utilization efficiency by allowing institutions to manage space availability, permissions dependencies in one place. Overall, this feature supports better planning, transparent allocation, and optimal utilization of institutional infrastructure resources.

**How to use**

1. Navigate to Infrastructure Management → Add New Infrastructure.

**Examples**

- An administrator wants to create a new Auditorium that can be booked for academic and cultural events. Select Infrastructure Type: Auditorium. Enter Name: Main Auditorium, and Code: AUD-01 (mandatory fields). Provide optional details such as: Belongs To: Academic Block – B, Floor: Ground Floor, Capacity: 500, Opening & Closing Time: 8:00 AM – 9:00 PM, Contact Person: -, Description: Auditorium equipped with sound and lighting systems. The mapped Attribute Groups (e.g., Facilities, Technical Equipment, Seating Type) appear automatically. Under Facilities (Multi Select), the admin selects Air Conditioned, Wi-Fi Enabled, and Projector Available. Under Seating Type (Single Select), the admin selects Theatre Style. Enables the Can Be Booked option to make it available in the Venue Booking Module. Defines: Booking allowed for Faculty and Admins. Approval required before booking confirmation. Pricing Type: Per Day (₹5,000/day, payment offline). Linked services: Housekeeping and Technical Support. After saving, Main Auditorium (AUD-01) is successfully created and appears in the infrastructure list. It can now be booked through the Venue Booking Module and managed for events and institutional activities.

**Questions this answers**

- How do I add a new classroom to the system?
- What are the mandatory fields when creating new infrastructure?
- Can I add details like capacity and floor for a new building?
- How do I make an infrastructure bookable?
- What pricing options are available for booking an infrastructure?
- Can I link services like IT support to a bookable venue?
- How to create a new hostel record?
- Where do I enter attributes for a new infrastructure?
- What is the process to add a new sports facility?
- How to configure booking for a new auditorium?

**Keywords:** add new infrastructure, create infrastructure record, physical assets management, digital record facilities, classroom creation, laboratory creation, hostel creation, office creation, sports facility creation, building creation, infrastructure type mandatory, infrastructure name mandatory, infrastructure code mandatory, capacity infrastructure, opening time, closing time, number of rooms, number of floors, establishment date, contact person, description infrastructure, disclaimer infrastructure, attributes infrastructure, can be booked option, venue booking module, pricing type, payment mode offline, associated services, housekeeping, IT support, transport services, admin infrastructure creation, Digii infrastructure creation, create facility, add venue, campus resource reservation, facility details, asset tracking

**Synonyms:** create facility, register infrastructure, add campus asset, new venue setup

**Related:** add-new-infrastructure-type, add-new-attribute-group, booking-rules-infrastructure, show-all-infrastructures

**Tags:** infrastructure, creation, asset management, venue booking, configuration, mandatory fields, optional fields, attributes

---

## Booking Rules

<!-- id: booking-rules-infrastructure | category: Infrastructure -->

**What it does**

Once an infrastructure record has been created and if the "Can Be Booked" toggle is enabled while creating the infrastructure, administrators can define or modify the booking rules specifically for that infrastructure. By default, the booking rules configured at the Infrastructure Type level are automatically inherited by all infrastructures of that type. However, these rules can be customized at the individual infrastructure level to accommodate specific requirements — without affecting the rules set for the infrastructure type or other infrastructures under the same type. For each infrastructure, administrators can configure the following under both Single Booking and Multi Booking modes, for each user group: - Booking Allowed: Enable or disable booking permission for that user group. - Booking Type: Define the type of booking applicable. - Admin Action Required: Set whether admin approval is needed before the booking is confirmed. Additionally, new user groups can be added at the infrastructure level to extend or restrict access beyond what is defined at the type level.

**Why it matters**

Different infrastructures of the same type may have unique operational requirements. For example, two auditoriums under the same infrastructure type may have different capacities, purposes, or management preferences — requiring distinct booking rules for each. Allowing rule customization at the infrastructure level ensures: - Flexibility to handle exceptions without altering the overarching type-level rules. - Precision in access control, tailored to the specific use case of each venue. - Consistency as a baseline through inherited rules, reducing the need for manual configuration unless customization is needed. - Operational efficiency by allowing bulk rule management at the type level while still supporting individual overrides where necessary.

**Examples**

- A university has two auditoriums - Main Auditorium (AUD-01) and Mini Auditorium (AUD-02) both under the "Auditorium" infrastructure type. The type-level booking rules allow Faculty and Administrators to book without approval. However, AUD-01 is a premium venue used for large events and requires additional oversight. The infrastructure administrator navigates to AUD-01's infrastructure details and overrides the inherited rules. The administrator adds a user group Admin Office and provides the right to request for AUD-01 only for one administrative officer. AUD-02 retains the default inherited rules without any changes. This ensures AUD-01 has venue booking access to a specific user only while AUD-02 continues to follow the booking rules defined for the infrastructure type Auditorium.

**Questions this answers**

- How do I set booking rules for a specific infrastructure?
- Can I override the booking rules from the infrastructure type?
- How to customize booking permissions for an individual venue?
- What settings can I configure for infrastructure-level booking?
- Can I add a new user group for a single infrastructure's booking?
- What happens if I don't customize booking rules for an infrastructure?
- How to manage booking access for a premium venue like Main Auditorium?
- Can I disable booking for a specific classroom?

**Keywords:** booking rules infrastructure, modify infrastructure booking, override type rules, individual venue booking, custom booking rules, single booking infrastructure, multi booking infrastructure, booking allowed infrastructure, booking type infrastructure, admin action required infrastructure, add user groups infrastructure, venue specific rules, facility booking customization, admin infrastructure booking, Digii booking rules, auditorium booking rules, classroom booking rules, manage venue access, override inherited rules

**Synonyms:** venue specific booking, customize booking rules, override facility rules, individual booking settings

**Related:** add-new-infrastructure, booking-rules-infrastructure-type

**Tags:** infrastructure, booking, rules, customization, override, permissions, access control

---

## Archive Infrastructure

<!-- id: archive-infrastructure | category: Archive -->

**What it does**

The Archive Infrastructure feature allows administrators to deactivate or temporarily remove an existing infrastructure record from active use without permanently deleting it. This feature is typically used when an infrastructure (such as a classroom, hostel, lab, or office space) is under renovation, repurposed, or no longer in use but its data needs to be retained for reference, audit, or historical reporting. When an infrastructure is archived: It is excluded from active listings, allocation, and booking operations. All historical records, usage logs, and references remain preserved in the system. The archived item can be unarchived later if it becomes operational again. This ensures that inactive or obsolete infrastructures do not clutter operational workflows, while still maintaining full data integrity and historical traceability. An infrastructure can be archived only if there is no future or present booking in it or its sub-infrastructure.

**Why it matters**

Institutions frequently undergo infrastructure changes — such as building renovations, space reassignments, or temporary closures. Permanently deleting such records can result in data loss, affect historical reports, and disrupt dependent modules such as maintenance or venue booking. The Archive Infrastructure feature helps maintain a clean, accurate, and up-to-date infrastructure list by separating inactive assets from active ones. At the same time, it ensures that administrators retain access to all historical data for compliance, audit, and planning purposes.

**How to use**

1. Navigate to Infrastructure Management → Infrastructure List.
2. Locate the record Mechanical Engineering Classroom (MEW-01).
3. Click Archive from the available actions.
4. Confirm the archival action.

**Examples**

- An institution is renovating the Mechanical Engineering Classroom (MEW-01) for modernization. Since it will remain closed for six months, the administrator decides to archive it to prevent accidental bookings or maintenance scheduling. Once archived: The MEW-01 record is no longer displayed in the active infrastructure list. It cannot be booked or assigned for any academic activity. The record remains accessible under Archived Infrastructures, where administrators can view details or choose to Restore it once the renovation is complete. When the renovation is finished, the admin can restore MEW-01 by selecting Unarchive action, instantly making it available again for operational use.

**Questions this answers**

- How do I archive an infrastructure?
- When should I archive a classroom?
- What happens when an infrastructure is archived?
- Can I still access archived infrastructure data?
- How to temporarily remove a facility from active use?
- What are the conditions for archiving an infrastructure?
- Can an archived infrastructure be restored?
- How does archiving affect bookings?
- Why would I archive an infrastructure instead of deleting it?

**Keywords:** archive infrastructure, deactivate infrastructure, temporarily remove infrastructure, hide infrastructure, infrastructure renovation, repurpose infrastructure, retain infrastructure data, historical reporting infrastructure, audit infrastructure, exclude from booking, preserve historical records, unarchive infrastructure, data integrity infrastructure, admin archive, Digii archive, facility archive, asset archive, classroom archive, hostel archive, lab archive, office archive, decommission infrastructure, inactive infrastructure, archive restrictions, no future booking archive

**Synonyms:** deactivate facility, hide asset, soft delete infrastructure, put infrastructure offline

**Related:** unarchive-infrastructure, bulk-archive-unarchive, hide-archived-infrastructures, show-only-archived-infrastructures

**Tags:** archive, deactivation, data retention, historical data, renovation, infrastructure management

---

## Unarchive Infrastructure

<!-- id: unarchive-infrastructure | category: Archive -->

**What it does**

The Unarchive Infrastructure feature allows administrators to restore previously archived infrastructure records back to active status. This action is used when an infrastructure, such as a classroom, laboratory, hostel, or any other facility, becomes operational again after being temporarily closed, renovated, or repurposed. When an infrastructure is unarchived, it is reactivated and becomes visible in all relevant system modules, including allocation, venue booking, and examination seating plan. The record retains all its previously stored information — such as infrastructure details, attributes, and linked data — ensuring continuity without requiring re-entry of information.

**Why it matters**

Institutions often archive infrastructure that is temporarily unavailable to keep the system organized and prevent accidental use. Once the facility becomes functional again, manually re-creating its record would be time-consuming and prone to inconsistencies. The Unarchive Infrastructure feature solves this by enabling quick reactivation of archived records while preserving their historical data and configurations. This feature supports: Operational efficiency: Reactivating existing data without duplication. Data continuity: Retaining all past usage and maintenance records. Flexibility: Quickly making infrastructure available for allocation, booking, or reporting once it's ready for use. Accuracy: Ensuring the system reflects the current operational status of all institutional facilities.

**How to use**

1. Navigate to Infrastructure Management → Show all infrastructures.
2. Locate the record Mechanical Engineering Workshop (MEW-01).
3. Click Unarchive from the available actions.
4. Confirm the action.

**Examples**

- The Mechanical Engineering Workshop (MEW-01) was archived six months ago for renovation. After the upgrade is completed, the administrator needs to make it available again for academic and practical sessions. Once unarchived: MEW-01 reappears in the Active Infrastructure List. It becomes eligible for allocation or bookings (if applicable). All previous attributes, facility information, and linked data are retained exactly as before. For example, if the workshop was earlier linked to the Engineering Block and had attributes such as Air Conditioned and Wi-Fi Enabled, those settings are automatically restored — allowing smooth resumption of operations without additional configuration.

**Questions this answers**

- How do I unarchive an infrastructure?
- What happens when I unarchive a facility?
- Can I restore an archived classroom?
- How to make a renovated infrastructure available again?
- Does unarchiving restore all previous settings?
- What are the steps to reactivate an archived workshop?
- How to view unarchived infrastructures?

**Keywords:** unarchive infrastructure, restore infrastructure, reactivate infrastructure, make infrastructure active, bring infrastructure online, infrastructure operational again, restore archived facility, unarchive classroom, unarchive laboratory, unarchive hostel, unarchive venue, admin unarchive, Digii unarchive, facility reactivation, asset reactivation, restore historical data, data continuity infrastructure, operational efficiency infrastructure, unarchive process

**Synonyms:** restore facility, reactivate asset, make active again, bring back online

**Related:** archive-infrastructure, bulk-archive-unarchive, hide-archived-infrastructures, show-only-archived-infrastructures

**Tags:** unarchive, reactivation, restoration, data continuity, operational status, infrastructure management

---

## Bulk Archive/Unarchive

<!-- id: bulk-archive-unarchive | category: Archive -->

**What it does**

The Bulk Archive / Unarchive feature allows administrators to manage the status of multiple infrastructure records simultaneously. Instead of archiving or restoring infrastructures one by one, this feature enables bulk actions to save time and maintain consistency across large datasets. Administrators can archive/unarchive multiple infrastructures using the predefined Excel format: Bulk Archive: Temporarily deactivate several infrastructures at once, removing them from active operations such as allocation, booking, and maintenance. Bulk Unarchive: Restore multiple previously archived infrastructures back to active status in a single action. This feature ensures efficient management of infrastructure data, particularly useful during institution-wide changes such as building renovations, semester transitions, or space reassignments.

**Why it matters**

Institutions often need to update the operational status of multiple infrastructures at the same time. For example, entire floors of a block may be closed for maintenance or reopened after renovation. Performing these actions individually for each record is time-consuming and prone to oversight. The Bulk Archive / Unarchive feature simplifies this process by enabling multi-selection and single-click actions, ensuring: Time efficiency in administrative operations. Consistency in data handling across similar infrastructures. Reduced manual errors during large-scale updates. Improved accuracy in reporting and system visibility. Additionally, the feature preserves all historical and associated data for each infrastructure record, ensuring that no information is lost during bulk operations.

**How to use**

1. Navigate to Infrastructure Management → Actions → Bulk Archive/ Unarchive.
2. Download sample excel template.
3. Enter Name, code and status (archive/unarchive) for multiple infrastructures such as Physics Lab (PHY-01), Chemistry Lab (CHEM-02), and Classroom S-101.
4. Upload excel file and complete the action.

**Examples**

- The institution plans to renovate the Science Block, which includes several laboratories and classrooms. The administrator decides to archive all related infrastructures to prevent usage during the renovation period. Result: All selected infrastructures are archived/unarchived at once. They are no longer available for bookings, allocations, or active reporting. Historical data remains preserved. NOTE : All child infrastructures will also be archived on archiving parent infrastructures example, On archiving science block mapped classrooms, laboratories etc will also be archived.

**Questions this answers**

- How do I archive multiple infrastructures at once?
- Can I unarchive several facilities using an Excel file?
- What is the process for bulk archiving infrastructures?
- How to use the bulk archive/unarchive template?
- What happens to child infrastructures during bulk archiving?
- Can I update the status of many classrooms simultaneously?
- How to manage infrastructure status during a building renovation?

**Keywords:** bulk archive infrastructure, bulk unarchive infrastructure, multiple infrastructure status, simultaneous archive, simultaneous unarchive, excel template archive, deactivate multiple facilities, restore multiple assets, mass archive, mass unarchive, admin bulk actions, Digii bulk archive, efficient infrastructure management, building renovation archive, semester transition archive, space reassignment archive, upload excel for archive, child infrastructure archive

**Synonyms:** mass facility deactivation, batch asset restoration, bulk status update, excel archive/unarchive

**Related:** archive-infrastructure, unarchive-infrastructure

**Tags:** bulk action, archive, unarchive, excel upload, efficiency, data consistency, infrastructure management

---

## Bulk Update

<!-- id: bulk-update-infrastructure | category: Update -->

**What it does**

The Bulk Update feature allows administrators to update multiple infrastructure records at once by uploading an Excel file in a predefined format. This functionality ensures quick and consistent updates across the Infrastructure database without the need to manually edit each record individually. Administrators can download the predefined Excel template, fill in the updated details for existing infrastructures, and re-upload the file to apply the changes in bulk. The system automatically validates the entries based on existing Infrastructure Codes and updates only the relevant records. The following fields can be updated through the Bulk Update feature: Infrastructure Name*, Infrastructure Type*, Capacity, Belongs To Infrastructure Name, Belongs To Infrastructure Code, Floor, Opening Time, Closing Time, Number Of Floors (Ground and Above), Number Of Floors (Under Ground), Number Of Rooms, Establishment Date, Description, Contact Person (Email/Registration ID), Disclaimer (Mandatory fields are required to identify and update the correct record.) NOTE: All correct details must be added in the file for all infrastructures, if fields are kept blank the system will update value for such field as null.

**Why it matters**

The Bulk Update feature is essential for maintaining up-to-date and accurate infrastructure data at scale. Institutions often need to modify or enrich existing infrastructure details — for instance, updating capacities, changing assigned contacts, or adding new descriptions — across multiple records. Doing this manually for each entry can be tedious and prone to human error. With Bulk Update, administrators can: Save time by applying multiple changes simultaneously. Ensure data accuracy with validation checks and consistent formats. Maintain data integrity by updating only recognized and authorized records. Simplify large-scale corrections after audits, departmental changes, or infrastructure reassignments.

**How to use**

1. Download the predefined Excel template.
2. Fill in the updated details for existing infrastructures.
3. Re-upload the file to apply the changes in bulk.

**Examples**

- Suppose the institution upgrades several computer labs across different buildings, increasing their capacity and changing contact persons. Instead of editing each lab record individually, the administrator can simply download the Bulk Update template, update the Capacity and Contact Person fields in Excel, and upload the file to apply all changes in one go — ensuring faster, standardized, and error-free updates.

**Questions this answers**

- How do I update multiple infrastructure records at once?
- Can I change the capacity of several labs using an Excel file?
- What fields can be updated using the bulk update feature?
- How to use the bulk update Excel template?
- What happens if I leave fields blank in the bulk update file?
- How to ensure data accuracy during bulk infrastructure updates?
- Can I update the contact person for many facilities simultaneously?

**Keywords:** bulk update infrastructure, update multiple infrastructures, excel file update, mass infrastructure update, edit infrastructure in bulk, update infrastructure name, update infrastructure type, update capacity, update belongs to, update floor, update opening time, update closing time, update number of floors, update number of rooms, update establishment date, update description, update contact person, update disclaimer, admin bulk update, Digii bulk update, data accuracy infrastructure, data integrity infrastructure, large-scale corrections, excel template update

**Synonyms:** mass update facilities, batch edit infrastructure, excel infrastructure modification, bulk data change

**Related:** add-new-infrastructure, view-old-versions

**Tags:** bulk action, update, excel upload, efficiency, data accuracy, infrastructure management

---

## View Old Versions

<!-- id: view-old-versions | category: Update -->

**What it does**

The View Old Versions feature allows administrators to access and review the previous versions of any infrastructure record. Each time an infrastructure record is updated — whether manually or through bulk upload — the system maintains a version history that captures the earlier state of the data. This includes details such as infrastructure name, code, type, capacity, location (belongs to, floor), facilities, attributes, and other configuration details that were previously associated with the record. By viewing old versions, administrators can track changes made over time and ensure complete traceability of infrastructure information. Each version entry typically includes: - Version number - Details of that version - User who performed the update - Date and time of modification All the versions of an infrastructure can be accessed from the infrastructure details page by clicking on 'View Older Versions'.

**Why it matters**

Maintaining historical versions of infrastructure data is critical for auditability, accountability, and operational transparency. Institutions frequently modify infrastructure details due to renovations, reassignments, or administrative corrections. Without version tracking, it becomes difficult to identify what changed, when it changed, and who made the change. The View Old Versions feature helps institutions to: - Track historical data for compliance and audit purposes. - Verify accuracy of recent updates against older records. - Restore context in case incorrect or accidental changes are made. Support decision-making by understanding how infrastructure configurations evolved over time.

**How to use**

1. Access from the infrastructure details page by clicking on 'View Older Versions'.

**Examples**

- Suppose an administrator notices a discrepancy in the capacity listed for a specific seminar hall. By using the View Old Versions feature, they can review previous records to check when the capacity value was last updated and by whom. If the hall's capacity was reduced due to renovation, the old record will confirm the original capacity and related details — helping the admin validate or correct the current entry based on accurate historical data.

**Questions this answers**

- How can I see previous versions of an infrastructure record?
- Where is the version history for infrastructure details?
- Who made changes to an infrastructure and when?
- Can I track changes made to a classroom's capacity?
- Why is version tracking important for infrastructure data?
- How to audit infrastructure modifications?
- What information is included in an old version record?

**Keywords:** view old versions, infrastructure version history, track infrastructure changes, historical infrastructure data, audit infrastructure records, previous infrastructure state, version number, user who updated, date of modification, admin view versions, Digii version history, data traceability infrastructure, infrastructure audit, restore context infrastructure, infrastructure configuration evolution, seminar hall capacity history, facility change log

**Synonyms:** version history, change log, previous states, historical records

**Related:** bulk-update-infrastructure

**Tags:** version history, audit, data traceability, updates, infrastructure management

---

## Show All Infrastructures

<!-- id: show-all-infrastructures | category: Infrastructure Filter -->

**What it does**

The Show All Infrastructures feature allows administrators to view a complete list of all infrastructures created within the system, including both active and archived records. The purpose of this view is to offer a quick reference to all infrastructures available in the database without any additional filters. It serves as a straightforward, read-only summary for validation.

**Why it matters**

Institutions often need a quick overview of all existing infrastructures — irrespective of their current status — for verification or reporting. The Show All Infrastructures feature provides a clean, minimal view that helps administrators quickly confirm the presence and basic details of all infrastructures without navigating through detailed lists or performing complex searches.

**Examples**

- Suppose an institution's admin team wants to verify whether all departmental laboratories have been correctly added to the system. By accessing the Show All Infrastructures view, they can instantly see a list of all infrastructures — active and archived — along with their names, codes, and capacities. This allows them to quickly identify missing entries or inconsistencies without opening each record individually.

**Questions this answers**

- How do I see a list of all infrastructures?
- Can I view both active and archived facilities?
- Where can I get a complete list of all campus infrastructures?
- How to quickly verify all labs are in the system?
- What is the purpose of 'Show All Infrastructures'?
- Does 'Show All Infrastructures' include deactivated items?

**Keywords:** show all infrastructures, view all facilities, complete infrastructure list, active and archived infrastructures, infrastructure database view, quick reference infrastructure, read-only infrastructure list, admin infrastructure view, Digii all infrastructures, verify infrastructure entries, check all facilities, infrastructure summary, unfiltered infrastructure list

**Synonyms:** all facilities list, complete asset view, total infrastructure records

**Related:** hide-archived-infrastructures, show-only-archived-infrastructures

**Tags:** infrastructure filter, view, all records, active, archived, summary

---

## Hide Archived Infrastructures

<!-- id: hide-archived-infrastructures | category: Infrastructure Filter -->

**What it does**

The Hide Archived Infrastructures feature allows administrators to view only the active infrastructures within the system by hiding all archived entries from the list. When this option is selected, the system filters out infrastructures that have been archived, ensuring that only currently active and usable infrastructures are displayed. This view typically shows essential information such as Infrastructure Name, Infrastructure Code, and Capacity, providing a concise and focused overview of infrastructures currently in use.

**Why it matters**

As institutions manage hundreds of infrastructures over time, archived records can clutter the main list and make it difficult to focus on active resources. The Hide Archived Infrastructures feature helps streamline visibility and simplifies daily management by displaying only relevant, active infrastructures. This is particularly beneficial for: Operational efficiency, ensuring users interact only with active infrastructure data. Avoiding confusion between usable and retired infrastructures. Improving accuracy during resource planning, scheduling, or updates. By temporarily hiding archived items, administrators can work on live data without permanently removing or modifying historical records.

**Examples**

- Suppose the facilities management team wants to review all currently available classrooms for the upcoming semester. By enabling the Hide Archived Infrastructures feature, the team can instantly filter out all old or decommissioned infrastructures under Classroom infrastructure type, ensuring their list only displays active facilities ready for use or booking.

**Questions this answers**

- How do I view only active infrastructures?
- Can I hide archived facilities from my list?
- What is the purpose of hiding archived infrastructures?
- How to get a clean list of currently usable facilities?
- Does this feature remove archived data permanently?
- How to filter for available classrooms for the next semester?

**Keywords:** hide archived infrastructures, view active infrastructures only, filter archived facilities, show only active facilities, streamline infrastructure visibility, operational efficiency infrastructure, resource planning infrastructure, scheduling infrastructure, admin filter, Digii active infrastructures, hide inactive facilities, current infrastructure list, usable infrastructure view, classroom availability

**Synonyms:** filter active facilities, show live assets, exclude archived records

**Related:** show-all-infrastructures, show-only-archived-infrastructures, archive-infrastructure

**Tags:** infrastructure filter, view, active records, hide archived, efficiency

---

## Show Only Archived Infrastructures

<!-- id: show-only-archived-infrastructures | category: Infrastructure Filter -->

**What it does**

The Show Only Archived Infrastructures feature allows administrators to filter and view only those infrastructures that have been archived within the system. When this option is selected, the list displays all infrastructures that are no longer active or have been intentionally archived for record-keeping purposes. This view presents limited but essential details such as Infrastructure Name, Infrastructure Code, and Capacity, helping administrators quickly identify archived records without displaying active ones.

**Why it matters**

Over time, institutions may archive infrastructures that are decommissioned, under renovation, or no longer in use. However, these records often need to be referenced for auditing, reporting, or reinstatement purposes. The Show Only Archived Infrastructures feature provides a simple, dedicated view to access and review all such records efficiently. Key benefits include: Easy access to historical data without mixing it with active infrastructures. Improved management of archived assets that might need reactivation or verification. Better reporting accuracy by isolating archived data during audits or compliance checks. This feature ensures that administrators maintain full visibility and control over the institution's complete infrastructure lifecycle.

**Examples**

- Suppose an institution has recently completed renovation work for several hostels that were archived during the maintenance period. Before reactivating them, the administrator wants to review all archived hostel infrastructures to verify which ones are ready to be restored. By using the Show Only Archived Infrastructures feature, they can quickly view the list of archived hostels, confirm their details, and proceed with the unarchive process for the relevant entries.

**Questions this answers**

- How do I see only archived infrastructures?
- Can I filter to view only inactive facilities?
- Where can I find a list of all decommissioned infrastructures?
- How to review archived hostels before unarchiving?
- What details are shown for archived infrastructures?
- Is it possible to view only historical infrastructure records?
- How to check which facilities are under renovation?

**Keywords:** show only archived infrastructures, view archived facilities, filter inactive infrastructures, access historical infrastructure data, archived records list, admin archived view, Digii archived infrastructures, decommissioned facilities, under renovation facilities, record-keeping infrastructure, audit archived data, compliance checks infrastructure, infrastructure lifecycle, hostel renovation archived, reactivate archived facilities

**Synonyms:** archived assets list, inactive facilities view, historical infrastructure view, deactivated records

**Related:** show-all-infrastructures, hide-archived-infrastructures, unarchive-infrastructure

**Tags:** infrastructure filter, view, archived records, historical data, auditing

---

## Search Infrastructure

<!-- id: search-infrastructure | category: Search Infrastructure -->

**What it does**

The Search Infrastructure feature allows users to quickly locate a specific infrastructure record under any selected Infrastructure Type by searching through its Name. This feature enables efficient navigation within large datasets by filtering visible infrastructures to match the entered search term. Once the user selects an Infrastructure Type (e.g., Building, Classroom, Laboratory, Hostel), they can type the name — or part of the name — of the desired infrastructure. The system dynamically displays matching results, showing essential details such as Infrastructure Name, Code, and Capacity for quick identification.

**Why it matters**

As institutions manage numerous infrastructures across different categories, manually browsing through extensive lists can be time-consuming and error-prone. The Search Infrastructure feature improves usability and data accessibility by allowing users to pinpoint specific infrastructures with minimal effort. By enabling focused, type-wise search, the feature ensures faster data retrieval and a smoother administrative workflow.

**How to use**

1. Select an Infrastructure Type (e.g., Building, Classroom, Laboratory, Hostel).
2. Type the name — or part of the name — of the desired infrastructure in the search bar.

**Examples**

- Suppose an administrator wants to update the capacity of a classroom named "CSE Lab 101". Instead of scrolling through a long list of classroom infrastructures, the admin selects Infrastructure Type – Classroom, enters "CSE Lab" in the search bar, and instantly sees the matching record "CSE Lab 101". This allows them to quickly access and edit the desired infrastructure without navigating through unrelated entries.

**Questions this answers**

- How do I search for a specific infrastructure?
- Can I find a classroom by its name?
- How to quickly locate a lab record?
- What details are shown in search results for infrastructure?
- Can I search for infrastructure by type?
- How to find 'CSE Lab 101'?
- What is the fastest way to find a specific venue?

**Keywords:** search infrastructure, locate infrastructure record, find facility by name, filter infrastructure by type, search classroom, search laboratory, search hostel, search building, infrastructure name search, infrastructure code search, capacity search, admin search, Digii search infrastructure, efficient navigation, data retrieval infrastructure, search bar infrastructure, find venue, search asset

**Synonyms:** find facility, locate asset, infrastructure lookup, search venue

**Related:** show-all-infrastructures

**Tags:** search, filter, navigation, efficiency, infrastructure management

---
