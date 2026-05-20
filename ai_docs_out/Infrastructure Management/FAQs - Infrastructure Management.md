# FAQs

**Module:** Infrastructure Management  
**Tags:** FAQ, Infrastructure Management, Facilities Management, Campus Management, Digii Platform


## Overview

This document addresses frequently asked questions about the Digii Infrastructure Management Module, covering topics such as its purpose, restrictions on deleting or editing records, the process for archiving and reactivating facilities, bulk update capabilities, and how listing filters work.

## Infrastructure Management Module Purpose

<!-- id: infrastructure-management-module-purpose | category: Module Overview -->

**What it does**

The Infrastructure Management Module allows institutions to create, manage, and categorize all physical infrastructures such as classrooms, labs, auditoriums, hostels, and other facilities.

**Why it matters**

It helps maintain centralized data for capacity planning, bookings, and utilization tracking across various modules like Timetable, Venue Booking, Examination Management System (EMS) for seating plan and Asset Management.

**Examples**

- Managing classrooms for timetable scheduling.
- Tracking lab utilization for resource allocation.
- Planning auditorium bookings for events.

**Questions this answers**

- What is the Infrastructure Management Module for?
- What can I do with the Infrastructure Management Module?
- How does Digii help manage campus facilities?
- What modules integrate with Infrastructure Management?
- What kind of infrastructure can I manage?
- Why use the Infrastructure Management Module?

**Keywords:** Infrastructure Management Module, purpose, functionality, overview, facilities management, campus infrastructure, physical infrastructure, classrooms, labs, auditoriums, hostels, capacity planning, bookings, utilization tracking, Timetable module, Venue Booking module, Examination Management System (EMS), Asset Management, Digii platform, institution facilities, manage infrastructure, create infrastructure, categorize infrastructure, what is infrastructure module

**Synonyms:** facilities module, campus infrastructure tool, building management, infrastructure system

**Tags:** Module Overview, Infrastructure Management, Facilities

---

## Infrastructure Record Deletion Restriction

<!-- id: infrastructure-record-deletion-restriction | category: Data Management -->

**What it does**

The system does not allow deletion of infrastructure records once created, instead providing an 'Archive' feature to hide them from active lists.

**Why it matters**

This restriction maintains data integrity and audit history, preventing broken references in related modules like venue bookings, assets, or timetable scheduling. Archiving ensures historical data remains accessible for reporting and compliance.

**Examples**

- An old classroom linked to past timetables cannot be deleted.
- A lab that is no longer in use can be archived instead of deleted.

**Questions this answers**

- Can I delete an infrastructure record?
- Why can't I delete old classrooms?
- What happens if I try to delete an infrastructure?
- How do I remove an infrastructure that's no longer used?
- Is there an alternative to deleting infrastructure?
- Why is infrastructure deletion restricted?
- Can I permanently delete a facility?

**Keywords:** delete infrastructure, remove infrastructure, data deletion, infrastructure records, deletion restriction, archive infrastructure, data integrity, audit history, broken records, missing references, venue bookings, assets, timetable scheduling, reporting, compliance, hide infrastructure, deactivate infrastructure, remove facility, Digii infrastructure, cannot delete, why can't I delete, delete facility, delete classroom, delete lab

**Synonyms:** remove facility, erase infrastructure, data removal policy, permanent deletion

**Related:** archive-infrastructure-how-to, infrastructure-reactivation

**Tags:** Data Management, Infrastructure Management, Archiving, Restrictions

---

## Editing Infrastructure Structural Details Restriction

<!-- id: infrastructure-structural-details-editing-restriction | category: Data Management -->

**What it does**

The system locks editing for 'Infrastructure Type', 'Belongs To', and 'Floor' details once an infrastructure is in use (linked to modules, bookings, or assets).

**Why it matters**

This restriction prevents data inconsistency, ensuring that changes to structural attributes do not result in mismatched records across modules like active timetables or event bookings.

**How to use**

1. To update these details, ensure that the infrastructure has no active or upcoming bookings.
2. Also, ensure that no assets are currently assigned to it.
3. After clearing these dependencies, the fields will become editable again.

**Examples**

- Changing a classroom's building while it's part of an active timetable is prevented.
- You cannot change a lab's floor if equipment is still assigned to it.

**Questions this answers**

- Why can't I edit the infrastructure type?
- How do I change the 'Belongs To' field for an infrastructure?
- What prevents me from editing an infrastructure's floor?
- When can I edit structural infrastructure details?
- What are the conditions for editing infrastructure type?
- How to update a classroom's building?
- Why are some infrastructure fields locked?

**Keywords:** edit infrastructure type, change infrastructure type, edit belongs to, change belongs to, edit floor, change floor, infrastructure details, editing restriction, data inconsistency, active bookings, upcoming bookings, assets allocated, linked modules, timetable, event booking, structural attributes, locked fields, update infrastructure details, dependencies, Digii infrastructure editing, why can't I edit, cannot edit infrastructure, locked fields, edit facility type, change building, change level

**Synonyms:** modify infrastructure type, update building, change location details, edit facility attributes

**Tags:** Data Management, Infrastructure Management, Restrictions, Editing

---

## Archiving an Infrastructure

<!-- id: archive-infrastructure-how-to | category: Data Management -->

**What it does**

Archiving allows users to hide infrastructures that are no longer in active use from active lists, while retaining their historical data for reference.

**Why it matters**

This is the recommended method for managing inactive facilities, ensuring data transparency and traceability without permanently deleting records or causing data inconsistencies.

**How to use**

1. 1. Navigate to the Infrastructure Management Module.
2. 2. Search the specific infrastructure record you wish to archive.
3. 3. Click on the ellipsis (three horizontal dots to open the action menu) of desired infrastructure.
4. 4. Select "Archive" and confirm the action when prompted.

**Examples**

- Archiving a lab that is temporarily closed for renovation.
- Archiving an old hostel block that is no longer used for student accommodation.

**Questions this answers**

- How do I archive an infrastructure?
- What are the steps to archive a classroom?
- Where is the archive option for infrastructure?
- Can I hide an infrastructure from active lists?
- How to mark an infrastructure as inactive?
- What happens after I archive an infrastructure?

**Keywords:** archive infrastructure, how to archive, hide infrastructure, deactivate infrastructure, remove from active list, historical data, reference data, Infrastructure Management Module, action menu, ellipsis, confirm archive, Digii archive, inactive infrastructure, facility archiving, archive process, archive steps, archive facility, archive classroom, archive lab

**Synonyms:** deactivate facility, put infrastructure offline, hide record, mark as inactive

**Related:** infrastructure-record-deletion-restriction, infrastructure-reactivation, infrastructure-listing-filters

**Tags:** Data Management, Infrastructure Management, Archiving, How-to

---

## Infrastructure Listing Filters

<!-- id: infrastructure-listing-filters | category: User Interface -->

**What it does**

These filters control the display of infrastructures on the listing screen, allowing users to view either all infrastructures (active and archived) or only active ones.

**Why it matters**

Effective use of these filters helps administrators maintain better control over infrastructure visibility, preventing confusion during operational tasks and enabling comprehensive review of all created facilities.

**How to use**

1. Use 'Show All Infrastructures' to display both active and archived infrastructures together for a complete list.
2. Use 'Hide Archived Infrastructures' to display only active infrastructures available for operational use (bookings, asset allocations, scheduling).

**Examples**

- An administrator uses 'Show All Infrastructures' to review all facilities ever created.
- A booking manager uses 'Hide Archived Infrastructures' to see only available venues for new bookings.

**Questions this answers**

- What is the difference between 'Show All Infrastructures' and 'Hide Archived Infrastructures'?
- How do I see archived infrastructures?
- How can I view only active facilities?
- What do the infrastructure filters do?
- How to control infrastructure visibility?
- Which filter shows all facilities, including inactive ones?

**Keywords:** show all infrastructures, hide archived infrastructures, filters, listing screen, display options, active infrastructures, archived infrastructures, operational use, bookings, asset allocations, scheduling, visibility control, Digii filters, infrastructure list, view options, filter infrastructure, show inactive, hide inactive, filter facilities

**Synonyms:** infrastructure display modes, view archived, filter active facilities, listing view options

**Related:** archive-infrastructure-how-to, infrastructure-reactivation

**Tags:** User Interface, Infrastructure Management, Filtering

---

## Bulk Update Infrastructure Details

<!-- id: infrastructure-bulk-update | category: Data Management -->

**What it does**

The system provides a Bulk Update feature allowing administrators to update multiple infrastructure records simultaneously using a predefined Excel template.

**Why it matters**

This feature simplifies large-scale data management, enabling efficient updates of information like names, capacities, descriptions, and disclaimers across numerous facilities.

**How to use**

1. 1. Download the predefined Excel template.
2. 2. Fill in updated information (such as names, capacities, description, disclaimer etc.) in the template.
3. 3. Upload the filled Excel file back into the system.
4. The platform will automatically process the file and update matching infrastructure records accordingly.

**Examples**

- Updating the capacity for 50 classrooms at once.
- Adding a new disclaimer to all lab facilities.

**Questions this answers**

- Can I update infrastructure details in bulk?
- How do I perform a bulk update for infrastructures?
- What is the process for updating multiple facilities at once?
- Can I use an Excel file to update infrastructure information?
- What fields can be updated using the bulk update feature?
- Are there any restrictions for bulk updates?

**Keywords:** bulk update infrastructure, update multiple infrastructures, mass update, Excel template, download template, upload file, update names, update capacities, update description, update disclaimer, large-scale data management, Digii bulk update, infrastructure records, batch update, edit multiple facilities, bulk edit, import updates, update facilities

**Synonyms:** mass edit infrastructure, import updates, batch modification, bulk data entry

**Related:** infrastructure-structural-details-editing-restriction

**Tags:** Data Management, Infrastructure Management, Bulk Operations

---

## Reactivating Archived Infrastructures

<!-- id: infrastructure-reactivation | category: Data Management -->

**What it does**

The system allows administrators to unarchive (reactivate) infrastructures, making them available for reuse in operations like bookings, asset assignments, or timetables.

**Why it matters**

This feature is useful for bringing previously inactive facilities back into academic use, ensuring flexibility in campus management and efficient resource allocation.

**How to use**

1. 1. Apply the "Show Archived Infrastructures" filter on the listing page.
2. 2. Click on the ellipsis (three horizontal dots to open the action menu) of desired infrastructure.
3. 3. Select "Unarchive" from the action menu.

**Examples**

- Reactivating a lab that was previously closed for maintenance.
- Bringing an old building back into use for new academic programs.

**Questions this answers**

- Can archived infrastructures be reactivated?
- How do I unarchive an infrastructure?
- What are the steps to reactivate a facility?
- How can I make an inactive classroom available again?
- Where is the unarchive option?
- What happens when I unarchive an infrastructure?

**Keywords:** reactivate infrastructure, unarchive infrastructure, reuse infrastructure, bring back online, active list, bookings, asset assignments, timetables, Show Archived Infrastructures filter, action menu, ellipsis, Digii unarchive, reopen facility, activate inactive infrastructure, restore archived, make infrastructure active

**Synonyms:** restore infrastructure, make active again, enable facility, unarchive facility

**Related:** archive-infrastructure-how-to, infrastructure-listing-filters

**Tags:** Data Management, Infrastructure Management, Archiving, Reactivation, How-to

---

## Modifying Venue Check-in/Check-out Timings

<!-- id: venue-check-in-out-timing-modification | category: Venue Booking -->

**What it does**

Check-in/check-out timings defined for a particular venue can be modified, but these changes will only apply to future bookings.

**Why it matters**

This ensures that existing bookings are not disrupted by changes to venue timings, maintaining consistency for already scheduled events while allowing flexibility for future planning.

**Examples**

- If a venue's check-out time is changed from 5 PM to 6 PM, all bookings made after this change will reflect the new 6 PM check-out.
- Existing bookings for the same venue will retain their original check-out times.

**Questions this answers**

- Can I change check-in/check-out timings for a venue?
- What happens if I modify venue timings with existing bookings?
- Do venue timing changes affect past bookings?
- How do I update venue check-in/check-out times?
- Will new bookings use the updated venue timings?

**Keywords:** check-in timings, check-out timings, venue timings, modify timings, change timings, future bookings, existing bookings, venue booking, Digii venue management, booking rules, timing changes, update venue schedule, modify venue hours, check-in time, check-out time, venue availability

**Synonyms:** adjust venue hours, alter booking times, change facility access times, update venue schedule

**Tags:** Venue Booking, Infrastructure Management, Timings

---
