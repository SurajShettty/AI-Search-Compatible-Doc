# Functionality Not Available

**Module:** Hostel Management  
**Tags:** hostel management, limitations, unavailable features, restrictions, hostel policies, room management


## Overview

This document outlines current features and functionalities that are not available or possible within the Hostel Management Configuration in the Digii campus-management platform.

## Hostel Policy Immutability

<!-- id: editing-archiving-deleting-hostel-policies | category: Hostel Policies -->

**What it does**

Once a hostel policy is created in the Digii campus-management platform, it cannot be edited, archived, or deleted.

**Why it matters**

This limitation reduces flexibility, requiring the creation of an entirely new policy for any necessary adjustments, which can be inefficient and increase administrative overhead.

**How to use**

1. To make changes to an existing hostel policy, create a new policy with the desired adjustments.

**Examples**

- An institution needs to update the terms of a hostel policy. Instead of editing the existing one, they must create a completely new policy.
- A policy is no longer relevant but cannot be archived or deleted, remaining visible in the system.

**Questions this answers**

- Can I edit a hostel policy after it's created?
- How do I delete an old hostel policy?
- Is it possible to archive a hostel policy?
- What if I need to change a hostel policy?
- Why can't I modify hostel policies?
- How to update hostel policy terms?

**Keywords:** hostel policy, edit hostel policy, archive hostel policy, delete hostel policy, modify hostel policy, policy changes, hostel management, policy limitations, policy restrictions, immutability, hostel admin, hostel administrator, policy creation, new policy, update policy, remove policy

**Synonyms:** hostel rule, dorm policy, residence policy, policy modification, policy removal

**Related:** multiple-active-policies, editing-hostel-policy-options

**Tags:** hostel policies, limitations, policy management

---

## Single Active Hostel Policy Restriction

<!-- id: multiple-active-policies | category: Hostel Policies -->

**What it does**

The Digii campus-management platform only allows one hostel policy to be active at any given time.

**Why it matters**

This prevents institutions from simultaneously managing different policies for various departments or student groups, limiting flexibility in complex hostel management scenarios.

**Examples**

- An institution wants to have one policy for undergraduate students and another for postgraduate students, but the system only allows one to be active.
- Different hostel blocks have different rules, but only one set of rules can be enforced at a time.

**Questions this answers**

- Can I have more than one active hostel policy?
- How do I run different hostel policies for different student groups?
- Is it possible to activate multiple hostel policies?
- Why can't I have two active hostel policies?
- What if I need separate policies for different departments?

**Keywords:** multiple policies, active policies, hostel policy, simultaneous policies, different policies, student groups, departments, hostel management, policy limitations, policy restrictions, single policy, active policy, hostel admin, hostel administrator, concurrent policies

**Synonyms:** concurrent policies, multiple rules, simultaneous rules, more than one policy

**Related:** editing-archiving-deleting-hostel-policies, editing-hostel-policy-options

**Tags:** hostel policies, limitations, policy management

---

## Hostel Policy Option Immutability

<!-- id: editing-hostel-policy-options | category: Hostel Policies -->

**What it does**

Once a hostel policy option is created and activated in the Digii campus-management platform, it cannot be modified.

**Why it matters**

Any required changes to fees, dates, or other options necessitate creating an entirely new policy, significantly increasing the administrative workload for Hostel Administrators.

**How to use**

1. To change an activated hostel policy option, a new hostel policy must be created with the updated options.

**Examples**

- A hostel needs to adjust the fee for a specific room type within an active policy option. They cannot edit the existing option and must create a new policy.
- The end date for a policy option needs to be extended, but it cannot be modified directly.

**Questions this answers**

- Can I edit a hostel policy option after it's active?
- How do I change fees in a hostel policy option?
- Is it possible to modify the dates of a policy option?
- What happens if I need to update an activated policy option?
- Why can't I edit hostel policy options?

**Keywords:** hostel policy option, edit policy option, modify policy option, change policy option, policy option fees, policy option dates, policy option changes, hostel management, policy limitations, policy restrictions, immutability, hostel admin, hostel administrator, administrative workload, new policy, update policy option, edit fees, change dates

**Synonyms:** dorm policy option, residence policy option, option modification, option editing

**Related:** editing-archiving-deleting-hostel-policies, multiple-active-policies, automatic-policy-option-end-functionality

**Tags:** hostel policies, limitations, policy management

---

## Manual Room Allotment Cancellation

<!-- id: automatic-policy-option-end-functionality | category: Room Allotment -->

**What it does**

Even when a Policy Option End Date is set, the Digii campus-management platform does not automatically cancel room allotments after the policy concludes.

**Why it matters**

Hostel Administrators must manually cancel room allocations, leading to increased administrative effort and potential oversight if not managed diligently.

**How to use**

1. Hostel Administrators must manually cancel room allotments after a policy option's end date has passed.

**Examples**

- A policy option for a summer semester ends on August 31st. On September 1st, the system does not automatically free up the rooms; a Hostel Administrator must manually cancel each allotment.
- Students remain allotted to rooms past their policy end date until a Hostel Administrator intervenes.

**Questions this answers**

- Does the system automatically cancel room allotments when a policy ends?
- How do I cancel room allotments after a policy option end date?
- What happens when a policy option end date is reached?
- Why aren't room allotments automatically cancelled?
- Do I need to manually cancel room allocations?

**Keywords:** automatic cancellation, policy option end date, room allotment, cancel room allotment, manual cancellation, hostel admin, hostel administrator, administrative effort, room allocation, hostel management, policy end, end date, room release, auto cancel, room deallocation, room de-allotment

**Synonyms:** auto-cancel rooms, room de-allotment, policy expiry, automatic room release, manual room release

**Related:** editing-hostel-policy-options

**Tags:** room allotment, automation, limitations, hostel management

---

## Room Capacity Immutability After Allotment

<!-- id: modifying-room-capacity-after-allocation | category: Infrastructure Management -->

**What it does**

Once rooms are allotted, their capacity cannot be changed in the Infrastructure Module of the Digii campus-management platform.

**Why it matters**

This restricts flexibility in managing room allocation adjustments, even if there's a legitimate need to change capacity after initial assignments, potentially leading to inefficient space utilization.

**Examples**

- A room initially allotted as a double needs to be converted to a single after students have moved in. The capacity cannot be updated in the system.
- Due to unforeseen circumstances, a room's capacity needs to be reduced, but the system prevents this change once it's allotted.

**Questions this answers**

- Can I change room capacity after rooms are allotted?
- How do I modify room capacity in the Infrastructure Module once rooms are assigned?
- What if I need to adjust room capacity after allocation?
- Why can't I change room capacity after students are allotted?
- Is it possible to edit room capacity post-allotment?

**Keywords:** room capacity, modify room capacity, change room capacity, room allotment, infrastructure module, hostel management, room allocation, capacity adjustment, flexibility, limitations, hostel admin, hostel administrator, room size, room type, edit room capacity, post-allotment capacity

**Synonyms:** dorm capacity, residence capacity, room size modification, post-allotment capacity, change room size

**Tags:** infrastructure, room management, limitations, hostel management

---

## Individual Hostel Policy Option Entry

<!-- id: bulk-upload-hostel-policy-option-entries | category: Hostel Policies -->

**What it does**

The Digii campus-management platform requires Hostel Policy Options to be added individually, without a bulk upload functionality.

**Why it matters**

This significantly increases the workload for the Hostel Administrator when a large number of policy options need to be configured, making the process time-consuming and prone to manual errors.

**How to use**

1. Add each Hostel Policy Option individually through the user interface.

**Examples**

- An institution has 100 different room types and fee structures, each requiring a separate policy option. The Hostel Administrator must enter each one manually.
- During a new academic year setup, many policy options need to be created, but there's no option to upload them via a spreadsheet.

**Questions this answers**

- Can I bulk upload hostel policy options?
- How do I add many hostel policy options at once?
- Is there a way to import hostel policy options?
- Why can't I use bulk upload for hostel policy options?
- What is the process for adding multiple hostel policy options?

**Keywords:** bulk upload, hostel policy option, individual entry, manual entry, hostel administrator, workload, policy configuration, hostel management, data entry, upload options, mass upload, import policy options, policy option entries, add policy options, batch entry

**Synonyms:** mass entry, batch upload, import options, bulk add policy options, upload policy options

**Related:** editing-hostel-policy-options

**Tags:** hostel policies, bulk operations, limitations, hostel management

---
