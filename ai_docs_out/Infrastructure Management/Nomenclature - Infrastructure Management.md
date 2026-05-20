# Nomenclature

**Module:** Infrastructure Management  
**Tags:** infrastructure, nomenclature, definitions, glossary, campus management, facilities, assets


## Overview

This document defines key terms and concepts related to the Infrastructure Management module within the Digii campus-management platform. It covers various aspects from general infrastructure definitions to specific attributes, actions, and booking functionalities.

## Infrastructure management

<!-- id: infrastructure-management | category: Infrastructure Actions -->

**What it does**

Infrastructure management is an admin privilege which allows administrators to access and manage the infrastructure module as a super admin. This includes creating, editing and archiving infrastructures.

**Why it matters**

This privilege allows authorized administrators to control and maintain campus facilities, ensuring efficient operations and data integrity within the Digii platform.

**Questions this answers**

- What is infrastructure management?
- Who can manage infrastructure in Digii?
- What can a super admin do in infrastructure management?
- How do I get infrastructure management access?
- What are the privileges for infrastructure management?

**Keywords:** infrastructure management, admin privilege, administrators, super admin, access infrastructure module, manage infrastructure module, create infrastructure, edit infrastructure, archive infrastructure, infrastructure control, facility management, campus facilities, operations, admin access, infrastructure admin, privileges, module access

**Synonyms:** facility management, campus infrastructure control, infrastructure administration

**Related:** infrastructure, archive

**Tags:** admin, privilege, module, management

---

## Infrastructure

<!-- id: infrastructure | category: Infrastructure Definitions -->

**What it does**

Infrastructure refers to the organized collection of physical facilities and resources administered by an institution to support academic, administrative, and operational functions on campus. It includes buildings, classrooms, laboratories, libraries, hostels, sports complexes, auditoriums, and other essential infrastructure assets. The Infrastructure Management Module allows institutions to platformatically catalog, monitor, and maintain these assets, ensuring optimal utilization, timely maintenance, and effective planning for upgrades or expansion. By offering a centralized repository and real-time visibility of all campus facilities, the module enables streamlined facility allocation, improved space management, and adherence to safety and compliance standards. This centralized repository integrates infrastructure-related data across the Digii campus platform, supporting various modules such as Examination Management System (EMS) (for seating plans), Hostel Management, Mess Management, and Asset Management, thereby enabling seamless data flow and operational efficiency.

**Why it matters**

Provides a centralized system to catalog, monitor, and maintain all campus physical assets, ensuring optimal utilization, timely maintenance, and efficient planning. It integrates data across various Digii modules for seamless operations and compliance.

**How to use**

1. Administrators should add all physical infrastructure details into the module as digital records.

**Examples**

- buildings
- classrooms
- laboratories
- libraries
- hostels
- sports complexes
- auditoriums
- media centers
- IT rooms

**Questions this answers**

- What does infrastructure mean in Digii?
- What types of infrastructure can I manage?
- How do I add campus facilities to the system?
- Which modules use infrastructure data?
- What is the purpose of the Infrastructure Management Module?
- How does Digii help manage campus assets?

**Keywords:** infrastructure, physical facilities, resources, campus assets, buildings, classrooms, laboratories, libraries, hostels, sports complexes, auditoriums, facilities, assets, catalog infrastructure, monitor infrastructure, maintain infrastructure, space management, facility allocation, compliance, digital records, Examination Management System (EMS), Hostel Management, Mess Management, Asset Management, campus infrastructure, physical assets, facility, resource, Digii campus

**Synonyms:** campus facilities, physical assets, institutional resources, campus infrastructure

**Related:** infrastructure-type, belongs-to, capacity, code, floor, opening-time, closing-time, establishment-date, contact-person, number-of-floors, description, disclaimer, can-be-booked, default-infrastructure-type

**Tags:** definition, asset, facility, module, integration

---

## Infrastructure Type

<!-- id: infrastructure-type | category: Infrastructure Definitions -->

**What it does**

Infrastructure Type refers to the classification of various categories of physical facilities and assets within an educational institution's campus that support its academic, administrative, and extracurricular activities. Examples of infrastructure types include classrooms, administrative buildings, laboratories, libraries, hostels, sports complexes, auditoriums, and specialized support facilities such as media centers and IT rooms. Each type serves a distinct functional purpose, enabling institutions to organize, manage, and maintain resources efficiently through the Infrastructure Management Module. This classification supports better space utilization, targeted maintenance, and planning aligned with institutional needs and regulatory standards.

**Why it matters**

Allows for efficient organization, management, and maintenance of campus resources by categorizing facilities, supporting better space utilization, targeted maintenance, and strategic planning.

**Examples**

- classrooms
- administrative buildings
- laboratories
- libraries
- hostels
- sports complexes
- auditoriums
- media centers
- IT rooms

**Questions this answers**

- What are infrastructure types?
- Can I classify my campus facilities?
- What are some examples of infrastructure types?
- How do infrastructure types help manage resources?
- Why categorize infrastructure?

**Keywords:** infrastructure type, classification, categories, physical facilities, assets, campus facilities, classrooms, administrative buildings, laboratories, libraries, hostels, sports complexes, auditoriums, media centers, IT rooms, facility types, asset categories, space utilization, maintenance planning, resource organization, type, category

**Synonyms:** facility category, asset type, campus facility classification

**Related:** infrastructure, default-infrastructure-type

**Tags:** classification, category, facility, asset

---

## Archive

<!-- id: archive | category: Infrastructure Actions -->

**What it does**

Archive refers to the systematic storage and preservation of historical data and records related to an institution's infrastructure and operations. This functionality ensures that outdated, inactive, or unused infrastructure records are securely stored in a centralized repository for future reference, compliance, and audit purposes. Archiving enhances platform efficiency by separating active data from archived information, while still allowing easy retrieval of past records when required. Within the Infrastructure Management Module, archived data includes previous infrastructure information that supports long-term institutional record-keeping and regulatory compliance. Infrastructure can only be archived if it has no current or future bookings. Similarly, any sub-infrastructure associated with it must also have no active or upcoming bookings. Once an infrastructure item is archived, it becomes unavailable for operations in other modules. For example, if a hostel room is archived, it will no longer appear in the Hostel Management module for allotment or related activities.

**Why it matters**

Ensures secure storage of historical infrastructure data for compliance and audit, improves platform efficiency by separating active from inactive records, and prevents items with active bookings from being removed from operational use.

**How to use**

1. Infrastructure can only be archived if it has no current or future bookings.
2. Any sub-infrastructure associated with it must also have no active or upcoming bookings.

**Examples**

- If a hostel room is archived, it will no longer appear in the Hostel Management module for allotment or related activities.

**Questions this answers**

- How do I archive an infrastructure item?
- What happens when I archive an infrastructure?
- Can I archive a room with active bookings?
- Where do archived infrastructure records go?
- Why archive infrastructure?
- Does archiving affect other modules?

**Keywords:** archive, archiving, historical data, records, infrastructure records, store data, preserve data, compliance, audit, platform efficiency, inactive records, unused infrastructure, retrieve records, Infrastructure Management Module, bookings, sub-infrastructure, deactivate, remove, hide, hostel room, Hostel Management, data storage, record keeping

**Synonyms:** deactivate, store, preserve, retire, hide

**Related:** unarchive, infrastructure, can-be-booked

**Tags:** action, data management, historical, compliance, module integration

---

## Unarchive

<!-- id: unarchive | category: Infrastructure Actions -->

**What it does**

Unarchive refers to the process of restoring previously archived infrastructure records back into the active platform. This function enables infrastructure administrators to retrieve and reinstate infrastructure-related information, that was previously moved to the archive for storage. Unarchiving ensures that relevant historical data can be accessed and utilized in current operations or decision-making without requiring data reentry. This capability supports institutional flexibility in managing campus infrastructure, allowing seamless transition between archived and active data states while maintaining data integrity and consistency across modules.

**Why it matters**

Allows administrators to restore inactive infrastructure records for current operations, ensuring data integrity and flexibility in managing campus facilities without re-entering data.

**Questions this answers**

- How do I unarchive an infrastructure item?
- Can I restore an archived room?
- What is the process to unarchive infrastructure?
- Why would I unarchive something?
- Does unarchiving bring back all data?

**Keywords:** unarchive, unarchiving, restore records, retrieve data, reinstate infrastructure, active platform, historical data, data reentry, institutional flexibility, data integrity, consistency, activate, bring back, reactivate, restore infrastructure

**Synonyms:** restore, reactivate, retrieve, bring back

**Related:** archive

**Tags:** action, data management, restore

---

## Attribute

<!-- id: attribute | category: Infrastructure Definitions -->

**What it does**

An attribute is a distinct characteristic or property used to describe and define specific details of infrastructure. Attributes provide critical information that aids in the categorization, identification, and management of infrastructure resources. For example, attributes of a hostel room may specify whether it is air-conditioned, the presence of an attached or common bathroom, and other relevant features. Within the Infrastructure Management Module, attributes facilitate accurate documentation and enable efficient search, filtering, and reporting functions. These attributes form the essential metadata that enhance data clarity, organization, and operational control across the platform, supporting informed decision-making and resource optimization.

**Why it matters**

Provides detailed characteristics for infrastructure, enabling accurate documentation, efficient search, filtering, and reporting, which supports informed decision-making and resource optimization.

**Examples**

- Attributes of a hostel room may specify whether it is air-conditioned, the presence of an attached or common bathroom, and other relevant features.

**Questions this answers**

- What is an attribute in infrastructure management?
- How do I add attributes to a room?
- What kind of details can I add as attributes?
- How do attributes help manage infrastructure?
- Can I search by attributes?

**Keywords:** attribute, characteristics, property, infrastructure details, categorization, identification, management, hostel room, air-conditioned, bathroom, metadata, search, filtering, reporting, data clarity, organization, operational control, resource optimization, features, properties, detail

**Synonyms:** property, characteristic, feature, detail

**Related:** infrastructure, infrastructure-version

**Tags:** definition, metadata, detail, property

---

## Facility

<!-- id: facility | category: Infrastructure Definitions -->

**What it does**

A facility refers to specific amenities available within infrastructure to support various activities and enhance functionality. For example, a classroom may include a projector, microphone, blackboard, LED display, or instructional resources as facilities.

**Why it matters**

Enhances the functionality and utility of infrastructure by detailing available amenities, supporting better resource planning and user experience.

**Examples**

- A classroom may include a projector, microphone, blackboard, LED display, or instructional resources as facilities.

**Questions this answers**

- What is a facility within infrastructure?
- What are examples of facilities in a classroom?
- How do I list amenities for a room?
- Can I add equipment as a facility?

**Keywords:** facility, amenities, infrastructure amenities, classroom facilities, projector, microphone, blackboard, LED display, instructional resources, features, equipment, resources, support activities, enhance functionality, amenity

**Synonyms:** amenity, equipment, resource, feature

**Related:** infrastructure

**Tags:** definition, amenity, equipment, resource

---

## Infrastructure Version

<!-- id: infrastructure-version | category: Infrastructure Data Management -->

**What it does**

Infrastructure Version refers to the automatic creation of a new iteration of an infrastructure record whenever any detail or attribute of that infrastructure is modified. This new version is linked to all scheduled bookings or plans where the previous version was referenced, ensuring continuity and accuracy in resource allocation. Meanwhile, the prior version is preserved within the infrastructure record for future verification, audit, or historical reference. This versioning mechanism enables seamless tracking of all changes, supporting data integrity and transparency in infrastructure management, while allowing institutions to maintain consistent operations without disruption.

**Why it matters**

Automatically tracks all changes to infrastructure records, ensuring data integrity, transparency, and continuity for bookings and plans, while preserving historical versions for audit and reference.

**How to use**

1. A new iteration of an infrastructure record is automatically created whenever any detail or attribute of that infrastructure is modified.

**Questions this answers**

- What is infrastructure versioning?
- How does infrastructure versioning work?
- When is a new infrastructure version created?
- Does changing an attribute create a new version?
- How does versioning affect bookings?
- Can I see past versions of an infrastructure record?

**Keywords:** infrastructure version, versioning, record iteration, modify infrastructure, update infrastructure, attribute change, detail change, scheduled bookings, resource allocation, data integrity, transparency, audit, historical reference, change tracking, version history, automatic versioning

**Synonyms:** version history, change log, record iteration

**Related:** attribute, can-be-booked

**Tags:** versioning, data management, audit, history

---

## Belongs To

<!-- id: belongs-to | category: Infrastructure Definitions -->

**What it does**

"Belongs To" defines the hierarchical relationship where one infrastructure component is associated as a part of a parent infrastructure. For example, a hostel room belongs to a hostel building, indicating it is a subdivision or constituent of the larger structure. Conversely, a hostel building is considered an independent infrastructure element and does not belong to any other infrastructure. This relationship clarifies the structural organization of campus assets, facilitating accurate management, reporting, and resource allocation by establishing clear parent-child associations between infrastructure components.

**Why it matters**

Establishes clear hierarchical relationships between infrastructure components, facilitating accurate management, reporting, and resource allocation by defining parent-child associations.

**Examples**

- A hostel room belongs to a hostel building, indicating it is a subdivision or constituent of the larger structure.
- A hostel building is considered an independent infrastructure element and does not belong to any other infrastructure.

**Questions this answers**

- What does 'Belongs To' mean for infrastructure?
- How do I define a parent-child relationship for infrastructure?
- Can a hostel room belong to a building?
- What is the hierarchy of infrastructure?
- How does 'Belongs To' help with reporting?

**Keywords:** belongs to, hierarchical relationship, parent infrastructure, child infrastructure, infrastructure component, hostel room, hostel building, subdivision, structural organization, campus assets, management, reporting, resource allocation, parent-child association, hierarchy, relationship

**Synonyms:** parent-child relationship, hierarchical structure, part of

**Related:** infrastructure

**Tags:** hierarchy, relationship, structure, asset management

---

## Capacity

<!-- id: capacity | category: Infrastructure Attributes -->

**What it does**

Capacity refers to the maximum number of individuals, objects, or units that a specific infrastructure element can accommodate or support effectively. For instance, a classroom's capacity indicates the total number of students it can seat comfortably, while a hostel room's capacity defines the number of occupants it can house. In Infrastructure Management Module, capacity is a key attribute used to optimize space utilization, plan resource allocation, and ensure compliance with safety and operational standards. Clear documentation of capacity helps institutions manage their infrastructure efficiently and make informed decisions related to scheduling, occupancy, and facility upgrades.

**Why it matters**

Optimizes space utilization, aids in resource allocation planning, and ensures compliance with safety standards by defining the maximum occupancy for each infrastructure element.

**Examples**

- A classroom's capacity indicates the total number of students it can seat comfortably.
- A hostel room's capacity defines the number of occupants it can house.

**Questions this answers**

- What is infrastructure capacity?
- How do I set the capacity for a classroom?
- What does capacity mean for a hostel room?
- Why is capacity important for infrastructure?
- How does capacity affect scheduling?

**Keywords:** capacity, maximum number, individuals, objects, units, accommodate, support, classroom capacity, hostel room capacity, students, occupants, space utilization, resource allocation, safety standards, operational standards, scheduling, occupancy, facility upgrades, attribute, limit, size

**Synonyms:** occupancy limit, maximum occupancy, size limit

**Related:** infrastructure, attribute

**Tags:** attribute, limit, occupancy, planning

---

## Code

<!-- id: code | category: Infrastructure Attributes -->

**What it does**

Code refers to a unique identifier or alphanumeric tag assigned to an infrastructure within the platform. This code enables precise identification, categorization, and tracking of individual infrastructures. Codes are essential for efficient database management, facilitating quick search, referencing, and integration across various modules of the platform. They help avoid duplication, simplify reporting, and support automated processes. Either the codes can be entered by infrastructure admin manually while creating the infrastructure or codes can be generated by platform automatically while creation of infrastructure. The code should be a 6 character alphanumeric code. The infrastructure can be searched through name only and currently the infrastructure can not be searched using code.

**Why it matters**

Provides a unique alphanumeric identifier for each infrastructure, enabling precise identification, categorization, and tracking, which is crucial for efficient database management, preventing duplication, and simplifying reporting.

**How to use**

1. Codes can be entered by infrastructure admin manually while creating the infrastructure.
2. Codes can be generated by platform automatically while creation of infrastructure.
3. The code should be a 6 character alphanumeric code.

**Questions this answers**

- What is an infrastructure code?
- How do I assign a code to an infrastructure?
- Can the system generate codes automatically?
- What are the rules for infrastructure codes?
- Can I search for infrastructure using its code?
- What is the purpose of an infrastructure code?

**Keywords:** code, unique identifier, alphanumeric tag, infrastructure code, identification, categorization, tracking, database management, search, referencing, integration, modules, duplication, reporting, automated processes, infrastructure admin, manual code, auto-generated code, 6 character code, ID, tag

**Synonyms:** ID, identifier, tag, reference number

**Related:** infrastructure, attribute

**Tags:** attribute, identifier, unique, data management

---

## Floor

<!-- id: floor | category: Infrastructure Attributes -->

**What it does**

Floor refers to the specific storey of a building where a room or infrastructure element is located. This attribute helps in precisely identifying the location of rooms within multi-level buildings for ease of navigation, management, and booking. When creating a building, the floor field is not required, as this applies only to sub-units or rooms within the building structure. Clear floor documentation supports efficient space management and allocation within the institution's infrastructure.

**Why it matters**

Precisely identifies the location of rooms within multi-level buildings, aiding navigation, management, and booking, and supporting efficient space management and allocation.

**How to use**

1. When creating a building, the floor field is not required, as this applies only to sub-units or rooms within the building structure.

**Questions this answers**

- What is the 'Floor' attribute for infrastructure?
- How do I specify the floor for a room?
- Is the floor field required for buildings?
- How does floor information help with room management?

**Keywords:** floor, storey, building level, room location, infrastructure element, multi-level buildings, navigation, management, booking, sub-units, rooms, space management, allocation, ground floor, underground, levels, attribute

**Synonyms:** storey, level, building level

**Related:** infrastructure, attribute, number-of-floors

**Tags:** attribute, location, building, structure

---

## Opening Time

<!-- id: opening-time | category: Infrastructure Attributes -->

**What it does**

Opening Time refers to the scheduled time at which a specific infrastructure facility or resource becomes available for use on everyday. This attribute helps in defining operational hours for buildings, rooms, or other campus facilities. The opening time will be recorded in the platform for reference only and it does not define the timings for booking of the infrastructure.

**Why it matters**

Defines the daily operational hours for infrastructure facilities, providing a reference for availability and supporting general campus management.

**How to use**

1. The opening time will be recorded in the platform for reference only and it does not define the timings for booking of the infrastructure.

**Questions this answers**

- What is 'Opening Time' for infrastructure?
- How do I set the opening time for a facility?
- Does opening time affect bookings?
- Is opening time just for reference?

**Keywords:** opening time, scheduled time, available for use, operational hours, buildings, rooms, campus facilities, reference, availability, facility timing, resource timing, start time, attribute

**Synonyms:** start time, availability time, operational start

**Related:** infrastructure, attribute, closing-time, can-be-booked

**Tags:** attribute, time, schedule, operational

---

## Closing Time

<!-- id: closing-time | category: Infrastructure Attributes -->

**What it does**

Closing Time refers to the scheduled time at which a particular infrastructure facility or resource ceases to be available for use everyday. This attribute helps in defining the end of operational hours for buildings, rooms, or other campus facilities. The closing time will be recorded in the platform for reference only and it does not define the timings for booking of the infrastructure.

**Why it matters**

Defines the daily end of operational hours for infrastructure facilities, providing a reference for availability and supporting general campus management.

**How to use**

1. The closing time will be recorded in the platform for reference only and it does not define the timings for booking of the infrastructure.

**Questions this answers**

- What is 'Closing Time' for infrastructure?
- How do I set the closing time for a facility?
- Does closing time affect bookings?
- Is closing time just for reference?

**Keywords:** closing time, scheduled time, ceases to be available, end of operational hours, buildings, rooms, campus facilities, reference, unavailability, facility timing, resource timing, end time, attribute

**Synonyms:** end time, availability end, operational end

**Related:** infrastructure, attribute, opening-time, can-be-booked

**Tags:** attribute, time, schedule, operational

---

## Establishment Date

<!-- id: establishment-date | category: Infrastructure Attributes -->

**What it does**

Establishment Date refers to the specific date on which an infrastructure, such as a building, was officially constructed, commissioned, or became operational within the institution. This attribute provides historical context for the asset, supporting lifecycle management, maintenance scheduling, and compliance tracking. In the Infrastructure Management Module, recording the establishment date enables institutions to monitor the age of their assets, plan renovations or replacements, and maintain accurate institutional records. This information contributes to strategic infrastructure planning and ensures transparency in asset management.

**Why it matters**

Provides historical context for assets, supporting lifecycle management, maintenance scheduling, and compliance tracking, which aids in strategic planning, monitoring asset age, and maintaining accurate institutional records.

**Examples**

- The date on which an infrastructure, such as a building, was officially constructed, commissioned, or became operational.

**Questions this answers**

- What is the 'Establishment Date' for infrastructure?
- How do I record the establishment date of a building?
- Why is the establishment date important?
- Does the establishment date help with maintenance planning?

**Keywords:** establishment date, construction date, commissioned date, operational date, infrastructure date, building date, historical context, asset lifecycle, maintenance scheduling, compliance tracking, asset age, renovations, replacements, institutional records, strategic planning, asset management, date, attribute

**Synonyms:** construction date, commissioning date, operational date

**Related:** infrastructure, attribute

**Tags:** attribute, date, history, asset management

---

## Contact Person

<!-- id: contact-person | category: Infrastructure Attributes -->

**What it does**

Contact Person refers to the designated individual responsible for managing or overseeing a specific infrastructure asset.

**Why it matters**

Identifies the responsible individual for an infrastructure asset, facilitating clear communication and accountability for management and oversight.

**Questions this answers**

- Who is the 'Contact Person' for an infrastructure?
- How do I assign a contact person to a facility?
- What is the role of the contact person?
- Can I find out who manages a specific asset?

**Keywords:** contact person, designated individual, responsible person, managing infrastructure, overseeing infrastructure, infrastructure asset, accountability, communication, point of contact, attribute, manager

**Synonyms:** responsible person, asset manager, point of contact

**Related:** infrastructure, attribute

**Tags:** attribute, contact, responsibility, person

---

## Number of Floors

<!-- id: number-of-floors | category: Infrastructure Attributes -->

**What it does**

Number of Floors refers to the total count of levels or storeys in a building, which serves as the basis for creating and organizing rooms. Floors can be categorized as 'Ground and Above' levels, as well as 'Underground' levels. This attribute helps define the vertical structure of the building, ensuring accurate mapping and management of infrastructure. It is essential for room creation, space allocation, and navigation within the institution's facilities.

**Why it matters**

Defines the vertical structure of a building, which is essential for accurate mapping, room creation, space allocation, and navigation within multi-level facilities.

**Examples**

- Floors can be categorized as 'Ground and Above' levels, as well as 'Underground' levels.

**Questions this answers**

- What is 'Number of Floors' for a building?
- How do I specify the number of floors?
- Can I include underground levels?
- Why is the number of floors important for room creation?

**Keywords:** number of floors, total count, levels, storeys, building structure, organizing rooms, ground levels, underground levels, vertical structure, accurate mapping, room creation, space allocation, navigation, building attribute, floor count, attribute

**Synonyms:** total floors, building levels, storey count

**Related:** infrastructure, attribute, floor

**Tags:** attribute, building, structure, count

---

## Description

<!-- id: description | category: Infrastructure Attributes -->

**What it does**

Description refers to a detailed textual explanation or summary provided for an infrastructure. This field captures essential information that defines the purpose, features, or distinguishing characteristics of the infrastructure. A clear and comprehensive description facilitates better understanding, identification, and communication about the infrastructure among infrastructure administrators.

**Why it matters**

Provides a detailed textual explanation of an infrastructure's purpose, features, and characteristics, facilitating better understanding, identification, and communication among administrators.

**Questions this answers**

- What should I include in the infrastructure description?
- Why is a detailed description important?
- Where can I add notes about an infrastructure item?

**Keywords:** description, textual explanation, summary, infrastructure purpose, features, distinguishing characteristics, essential information, understanding, identification, communication, infrastructure administrators, details, notes, attribute

**Synonyms:** details, notes, summary, explanation

**Related:** infrastructure, attribute

**Tags:** attribute, text, detail, information

---

## Disclaimer

<!-- id: disclaimer | category: Infrastructure Attributes -->

**What it does**

The Disclaimer field in the infrastructure module provides a brief statement that limits the liability of the institution regarding the accuracy, completeness, and usage of the infrastructure.

**Why it matters**

Limits the institution's liability regarding the accuracy, completeness, and usage of infrastructure information, providing legal protection and clarity.

**Questions this answers**

- What is the 'Disclaimer' field for?
- How do I add a disclaimer to infrastructure?
- What kind of information goes in the disclaimer?
- Does the disclaimer protect the institution?

**Keywords:** disclaimer, disclaimer field, infrastructure module, brief statement, limits liability, institution liability, accuracy, completeness, usage, legal statement, legal protection, attribute

**Synonyms:** legal notice, liability statement

**Related:** infrastructure, attribute

**Tags:** attribute, legal, liability, statement

---

## Can be booked

<!-- id: can-be-booked | category: Infrastructure Booking -->

**What it does**

This feature enables an infrastructure to be reserved through the Venue Booking module. When activated, infrastructure administrators can specify which user types—such as students, faculty, or admins—are permitted to book the resource. Additionally, they can determine which bookings require approval for confirmation, set allowable booking timeframes, and define any fees associated with the booking (currently, payments are handled offline as online payment integration is not available for this feature). The module also allows linking required services from various departments to support the booking. This functionality ensures controlled, transparent, and efficient management of campus resource reservations.

**Why it matters**

Enables controlled and efficient reservation of infrastructure through the Venue Booking module, allowing administrators to define user permissions, approval workflows, booking timeframes, and associated fees, ensuring transparent resource management.

**How to use**

1. When activated, infrastructure administrators can specify which user types—such as students, faculty, or admins—are permitted to book the resource.
2. Determine which bookings require approval for confirmation.
3. Set allowable booking timeframes.
4. Define any fees associated with the booking (payments are handled offline as online payment integration is not available).
5. Link required services from various departments to support the booking.

**Examples**

- User types—such as students, faculty, or admins—are permitted to book the resource.

**Questions this answers**

- How do I make an infrastructure item bookable?
- Who can book a facility?
- Can I set booking approval for a venue?
- How do I define booking timeframes?
- Are there fees for booking infrastructure?
- Can I link services to a booking?
- Is online payment available for venue booking?

**Keywords:** can be booked, bookable, venue booking, Venue Booking module, reserve infrastructure, infrastructure reservation, user types, students, faculty, admins, booking approval, booking confirmation, booking timeframes, booking fees, offline payments, online payment integration, required services, campus resource reservations, controlled booking, transparent booking, efficient booking, reservation

**Synonyms:** bookable, reservable, available for booking

**Related:** infrastructure, opening-time, closing-time, archive

**Tags:** booking, venue, reservation, module, access control, fees

---

## Default Infrastructure Type

<!-- id: default-infrastructure-type | category: Infrastructure Definitions -->

**What it does**

The Infrastructure Management module has a pre defined set of default infrastructure types such as Classroom, Academic Building, Auditorium, Mess, Hostel, Hostel Bed, Hostel Building, Guest Room, Building. These act as platform-recognised base infrastructure types and drive venue booking and operational behaviour.

**Why it matters**

Provides a set of pre-defined, platform-recognized base infrastructure types that streamline setup and drive consistent venue booking and operational behavior across the system.

**Examples**

- Classroom
- Academic Building
- Auditorium
- Mess
- Hostel
- Hostel Bed
- Hostel Building
- Guest Room
- Building

**Questions this answers**

- What are the default infrastructure types?
- Can I use pre-defined infrastructure types?
- How do default types affect venue booking?
- What are some examples of default infrastructure types?

**Keywords:** default infrastructure type, pre-defined types, base infrastructure types, Classroom, Academic Building, Auditorium, Mess, Hostel, Hostel Bed, Hostel Building, Guest Room, Building, platform-recognized, venue booking, operational behaviour, standard types, infrastructure categories, default types

**Synonyms:** standard infrastructure types, pre-set types, built-in types

**Related:** infrastructure, infrastructure-type, can-be-booked

**Tags:** default, type, category, module, booking

---
