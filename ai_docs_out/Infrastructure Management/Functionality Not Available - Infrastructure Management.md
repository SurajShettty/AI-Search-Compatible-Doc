# Functionality Not Available

**Module:** Infrastructure Management  
**Tags:** infrastructure, restrictions, data integrity, campus management, feature limitations


## Overview

This document outlines specific functionalities related to infrastructure management that are currently not supported in the Digii platform. It details restrictions on deleting infrastructure records and editing key infrastructure attributes once they are linked or booked, emphasizing data integrity and consistency.

## Deletion of Infrastructure

<!-- id: deletion-of-infrastructure | category: Infrastructure Management Restrictions -->

**What it does**

The Digii platform currently does not support the direct deletion of infrastructure records once they have been created. This restriction is in place to maintain data integrity and ensure historical records, associations, and usage data remain intact. Users can, however, mark infrastructures as 'Archived' to hide them from active listings.

**Why it matters**

This restriction ensures data integrity by preserving historical records, associations, and usage data for reporting and audit purposes. Archiving provides a way to manage inactive infrastructure without losing critical historical context, preventing potential data inconsistencies across modules.

**How to use**

1. Mark infrastructures as 'Archived' to hide them from active listings while preserving all related data for reporting and audit purposes.

**Examples**

- If a college administrator mistakenly adds a laboratory named "Physics Lab 2" and later realizes it's a duplicate of "Physics Lab II", the system does not allow direct deletion. Instead, the user can archive the duplicate infrastructure. This ensures that any workflows, tickets, or capacity utilization linked to that lab remain traceable, preventing potential data inconsistencies across modules.

**Questions this answers**

- Can I delete an infrastructure record?
- How do I remove an old lab from the system?
- What happens if I create a duplicate infrastructure?
- How do I hide an infrastructure without deleting its data?
- Why can't I delete an infrastructure?
- What is the process for archiving an infrastructure?
- Does deleting infrastructure affect historical data?
- How to manage unused infrastructure records?
- Can I permanently remove an infrastructure?
- What are the options for an incorrect infrastructure entry?

**Keywords:** delete infrastructure, remove infrastructure, archive infrastructure, deactivate infrastructure, hide infrastructure, infrastructure record deletion, data integrity, historical data, audit trail, campus infrastructure, facility management, asset management, space management, room deletion, lab deletion, building deletion, block deletion, infrastructure management, admin, super admin, campus admin, facility admin, delete facility, remove facility, archive facility, facility record deletion, unsupported deletion

**Synonyms:** remove infrastructure, get rid of infrastructure, deactivate infrastructure, hide infrastructure, archive facility, delete facility record, cannot delete infrastructure

**Tags:** infrastructure, deletion, archiving, data integrity, restrictions, campus management

---

## Editing of Infrastructure Type, Belongs To, and Floor

<!-- id: editing-infrastructure-attributes | category: Infrastructure Management Restrictions -->

**What it does**

Once an infrastructure is linked to any module or has a current or future booking associated with it, the fields Infrastructure Type, Belongs To, and Floor become non-editable. This restriction ensures data consistency across dependent modules.

**Why it matters**

This restriction ensures data consistency across dependent modules such as Asset Management, Timetable, and Venue Booking. Modifying these key attributes while active associations exist could lead to discrepancies in linked data, reports, and scheduled activities, causing operational issues.

**How to use**

1. To make changes to Infrastructure Type, Belongs To, or Floor, first ensure that there are no active or future bookings associated with the infrastructure.
2. Also, confirm that no assets or workflows are currently tagged to that infrastructure.
3. Only after clearing all such associations can the attributes be updated.

**Examples**

- Suppose a classroom named "Seminar Hall - 1" has been booked for an upcoming event or an asset (like a projector) has been allocated to it. In such cases, users cannot change the infrastructure's Type (e.g., from Classroom to Lab), Belongs To (e.g., from Engineering Block to Science Block), or Floor details. To make such changes, the user must first ensure that there are no active or future bookings, and that no assets or workflows are currently tagged to that infrastructure.

**Questions this answers**

- Why can't I change the type of a classroom?
- How do I update the floor number for a lab?
- Can I change which block an infrastructure belongs to?
- What makes infrastructure fields non-editable?
- How to edit infrastructure type if it's booked?
- What are the conditions for editing infrastructure attributes?
- Can I change the 'Belongs To' field for an active infrastructure?
- What modules are affected by infrastructure attribute changes?
- How to unlock infrastructure details for editing?
- What to do before changing an infrastructure's location?

**Keywords:** edit infrastructure type, change infrastructure type, modify infrastructure type, update infrastructure type, edit belongs to, change belongs to, modify belongs to, update belongs to, edit floor, change floor, modify floor, update floor, infrastructure attributes, non-editable fields, locked fields, data consistency, asset management, timetable, venue booking, linked modules, active bookings, future bookings, tagged assets, workflows, campus infrastructure, facility management, room type, building block, floor number, infrastructure management, admin, super admin, campus admin, facility admin, edit facility type, change facility location, update facility floor, unsupported editing

**Synonyms:** modify infrastructure details, update infrastructure properties, change facility attributes, alter room type, relocate infrastructure, change building assignment, cannot edit infrastructure details

**Tags:** infrastructure, editing, restrictions, data consistency, attributes, bookings, asset management, campus management

---
