# Features & Functionalities

**Module:** Mess Management  
**Tags:** Mess Management, Dining Services, Meal Planning, Member Management, Admin Privileges, Reporting, Coupon Verification


## Overview

This document outlines the features and functionalities of the Digii campus-management platform's Mess Management module. It details how administrators can configure dining facilities, manage meal schedules, add and control member access, generate consumption reports, and verify meal coupons via web and mobile applications.

## Prerequisites

- **Mess Console** — "Mess Console" admin privilege provides administrators with the access to view the mess console.
- **Mess Management Setting** — "Mess Management Setting" provides the super admin access to the mess management module. Admins with this privilege have access to all features of the mess module which includes mess creation, changing meal timings, adding menus etc.

## Create a New Mess

<!-- id: mess-management-create-mess | category: Mess Configuration -->

**What it does**

This feature allows the mess administrator to create and configure a mess (dining facility) within the platform. The administrator can enter details such as the mess name, location, meal types offered, and meal timings (breakfast, lunch, dinner, snacks). This configuration enables effective management and visibility of dining services across the platform. Key sub-features include defining a unique Mess Name, specifying the Location (optional), enabling 'Multiple Meals Allowed' for flexibility in meal consumption, and setting precise Meal Timings.

**Why it matters**

The Mess Management feature is crucial for maintaining an organized and efficient dining system within the institution. By allowing the mess administrator to create a mess and configure key details like meal types and meal timings, it helps streamline meal distribution and management. The ability to control meal availability with settings like 'Multiple Meals Allowed' and 'Meal Timings' ensures flexibility while maintaining order and reducing food wastage. This feature enables smooth operations, particularly during peak meal times, and ensures that all meal-related activities are aligned with institutional policies. It also helps keep track of member preferences and meal consumption, improving overall resource management.

**How to use**

1. Enter details such as the mess name, location, meal types offered, and meal timings (breakfast, lunch, dinner, snacks).
2. Configure 'Multiple Meals Allowed' if members can have more than one meal during prescribed time slots.

**Examples**

- When a new mess is added, the mess administrator sets breakfast as the meal type, with meal timings configured from 8:00 AM to 9:00 AM. If a student tries to access breakfast after 9:00 AM, the platform will automatically mark the meal coupon as expired, ensuring that meals are consumed within the specified time window. This helps the mess administrator maintain a structured and organized meal schedule.

**Questions this answers**

- How do I set up a new mess?
- Can I define different meal types for my mess?
- How do I configure meal timings?
- What is 'Multiple Meals Allowed'?
- How do I change mess meal timings?
- When do updated meal timings take effect?
- Can I add a mess location?
- What details are needed to create a mess?
- How to manage dining facilities?
- How to add a new dining hall?

**Keywords:** mess management, create mess, configure mess, dining facility, meal types, meal timings, breakfast, lunch, dinner, snacks, mess name, location, multiple meals allowed, mess administrator, dining services, meal distribution, food wastage, meal availability, campus dining, institution mess, add mess, set meal times, update meal timings, mess settings, mess configuration, manage mess, dining hall, cafeteria

**Synonyms:** dining hall setup, cafeteria configuration, meal facility creation

**Tags:** Mess Management, Configuration, Frontend, Meal Timings, Dining Services

---

## Add Menu (Calendar View)

<!-- id: add-menu-calendar-view | category: Meal Planning -->

**What it does**

This option allows the mess administrator to add meals based on meal types (e.g., vegetarian or non-vegetarian) for a specific date on the calendar. Meals are visually marked red for non-vegetarian and green for vegetarian meals, providing an easy and visual way to add meals on a day-by-day basis. Only future meal data can be added, and only meals for the current day are visible to users on their home screen.

**Why it matters**

The Add Menu feature is essential for mess administrators to efficiently manage meal schedules and meal types. Using the Calendar View, it enhances the accuracy and efficiency of the meal planning process by allowing day-by-day meal additions based on vegetarian or non-vegetarian categories. The platform ensures that only future meal data can be added, and meals for the current day are visible to users, improving transparency and communication between the mess and its members.

**How to use**

1. Use the Calendar View to select a specific date.
2. Add meals based on meal types (e.g., vegetarian or non-vegetarian).

**Examples**

- A mess administrator adds breakfast for the upcoming week using Calendar View. The meals are marked green for vegetarian and red for non-vegetarian on specific days. On Monday, the mess administrator sets vegetarian breakfast and non-vegetarian lunch. Meals for the current day are displayed on the users' home screen, while future meals are available only on the relevant day.

**Questions this answers**

- How do I add meals using the calendar?
- Can I see which meals are vegetarian or non-vegetarian?
- How to schedule meals for a specific day?
- When will future meal menus be visible?
- Can I add past meal menus?
- How to manage daily meal options?

**Keywords:** add menu, calendar view, meal planning, meal types, vegetarian meals, non-vegetarian meals, daily menu, mess administrator, schedule meals, visual menu, day-by-day menu, menu management, food schedule, meal options, current day menu, future menu, add breakfast, add lunch, add dinner, menu calendar, food calendar

**Synonyms:** meal schedule calendar, daily meal planner, visual menu editor

**Related:** add-menu-bulk-upload

**Tags:** Menu Management, Meal Planning, Frontend, Calendar View, Vegetarian, Non-Vegetarian

---

## Add Menu (Bulk Upload via CSV)

<!-- id: add-menu-bulk-upload | category: Meal Planning -->

**What it does**

The mess administrator can download a bulk Comma Separated Values (CSV) template that includes fields like Meal, Date, Item1, Type1, Item2, Type2, and more. After entering the data, the mess administrator can upload the file for efficient bulk meal entry. Only future data can be added; previous meal menus cannot be uploaded. Only meals for the current day will be visible to users on their home screen, with future meal data becoming visible only on the respective day.

**Why it matters**

The Add Menu feature is essential for mess administrators to efficiently manage meal schedules and meal types. The Bulk Upload via CSV option allows for quickly uploading multiple meal entries at once, enhancing the accuracy and efficiency of the meal planning process. This method is particularly useful for managing large institutions with ease, ensuring timely meal information and reducing administrative effort. The platform ensures that only future meal data can be added, and meals for the current day are visible to users, improving transparency and communication.

**How to use**

1. Download a bulk CSV template.
2. Enter meal data including Meal, Date, Item1, Type1, Item2, Type2, etc.
3. Upload the filled CSV file for bulk meal entry.

**Examples**

- A mess administrator uses the bulk upload option to add meals for the entire upcoming week, ensuring all future meals are scheduled efficiently. Meals for the current day are displayed on the users' home screen, while future meals are available only on the relevant day.

**Questions this answers**

- How do I upload multiple meals at once?
- Can I use a CSV file to add menus?
- What fields are in the bulk menu template?
- Can I bulk upload past meal data?
- When will bulk uploaded meals be visible to users?
- How to import meal schedules?

**Keywords:** add menu, bulk upload, CSV template, meal entry, efficient meal entry, mess administrator, upload menu, bulk meal data, future meal data, current day menu, menu management, food schedule, import menu, excel menu, meal items, meal types, bulk add meals, mass menu upload, import menu

**Synonyms:** mass menu upload, import menu, CSV menu upload

**Related:** add-menu-calendar-view

**Tags:** Menu Management, Bulk Upload, CSV, Meal Planning, Frontend

---

## Add Individual Member

<!-- id: add-member-individual | category: Member Management -->

**What it does**

This feature allows the mess administrator to add individual members (students, staff, guests) to the mess management module. Essential details such as Registration ID, Email ID, and phone number can be entered. This ensures an efficient and organized way to manage single member entries.

**Why it matters**

The Add Member feature is crucial for mess administrators to efficiently manage and organize meal access for students and staff. It provides flexibility to add members individually, allowing for precise control over single entries. This simplifies member management, ensures smooth meal distribution, and helps in maintaining an accurate database of individuals with meal access.

**How to use**

1. Enter the individual member's Registration ID.
2. Enter the member's Email ID.
3. Enter the member's phone number.

**Examples**

- A new staff member joins the institution. The mess administrator uses the individual member addition feature to add their Registration ID and Email ID to grant them mess access.

**Questions this answers**

- How do I add one student to the mess?
- What details are needed to add an individual member?
- Can I add a staff member to the mess?
- How to manually add a mess member?
- What is the process for adding a single student to the dining hall?

**Keywords:** add member, individual member, mess member, student, staff, guest, registration ID, email ID, phone number, mess administrator, member management, add single member, new member, enroll member, mess access, individual enrollment, single member addition, manual member entry

**Synonyms:** single member addition, manual member entry, add one student

**Related:** add-member-bulk-upload, add-member-group

**Tags:** Member Management, Individual Enrollment, Frontend, Student, Staff

---

## Bulk Member Upload

<!-- id: add-member-bulk-upload | category: Member Management -->

**What it does**

For bulk addition, the mess administrator can download a Comma Separated Values (CSV) template with fields like Registration ID, Email ID, and Coupon Generation Status. After entering the data, the mess administrator can upload the file to add multiple members at once. Coupons are not generated immediately when a member is added; coupon generation will begin from the next day onward.

**Why it matters**

The Add Member feature is crucial for mess administrators to efficiently manage and organize meal access for students and staff. Bulk member uploads using CSV templates allow for easily onboarding multiple members, saving time and reducing manual effort, especially in larger institutions. This feature simplifies member management, ensures smooth meal distribution, and helps in maintaining an accurate database of individuals with meal access.

**How to use**

1. Download a CSV template with fields like Registration ID, Email ID, and Coupon Generation Status.
2. Enter the member data into the template.
3. Upload the filled CSV file to add multiple members.

**Examples**

- During the beginning of a new academic year, the mess administrator uses the bulk upload feature to add 100 students by filling out the CSV template with Registration ID, Email ID, and Coupon Generation Status. This approach ensures that all students have their meal access set up quickly and accurately.

**Questions this answers**

- How do I add many students to the mess at once?
- Can I use a CSV file to add mess members?
- What information is needed for bulk member upload?
- When do coupons generate after bulk upload?
- How to import a list of students for mess access?
- What is the process for bulk adding staff to the dining system?

**Keywords:** bulk member upload, CSV template, add multiple members, mess administrator, registration ID, email ID, coupon generation status, bulk addition, mass enrollment, import members, student enrollment, staff enrollment, mess access, upload members, add many students, bulk add staff, mass member upload, import members

**Synonyms:** mass member upload, import members, CSV member upload

**Related:** add-member-individual, add-member-group

**Tags:** Member Management, Bulk Upload, CSV, Frontend, Student, Staff

---

## Group Addition

<!-- id: add-member-group | category: Member Management -->

**What it does**

The mess administrator can add members in groups by selecting criteria such as a hostel, allotment status (Confirmed/Provisional), and gender (Female/Male/Other). Once the criteria are selected, clicking 'Add' automatically adds the group to the mess. Groups can also be removed if no longer needed, providing flexibility to update or remove groups as necessary.

**Why it matters**

The Add Member feature is crucial for mess administrators to efficiently manage and organize meal access for students and staff. The Group Addition option ensures that members can be added according to specific hostel and allotment status, making it highly adaptable to varying institutional policies. This method allows for scalable management in larger institutions, simplifying member management, ensuring smooth meal distribution, and helping in maintaining an accurate database of individuals with meal access.

**How to use**

1. Select a hostel.
2. Choose the allotment status (Confirmed/Provisional).
3. Select gender (Female/Male/Other).
4. Click 'Add' to automatically add the group to the mess.
5. Optionally, remove the group if no longer needed.

**Examples**

- The mess administrator adds a group of students from a specific hostel and assigns them an allotment status of 'Confirmed'. If there's any change, the group can be removed as needed. This approach ensures that all students have their meal access set up quickly and accurately.

**Questions this answers**

- How do I add a group of students to the mess?
- Can I add members based on their hostel?
- What are the options for group addition?
- How to remove a group from the mess?
- Can I add students with 'Provisional' allotment status?
- How to enroll a batch of students for mess services?

**Keywords:** group addition, add members by group, hostel, allotment status, confirmed, provisional, gender, mess administrator, add group, remove group, member management, bulk enrollment, student groups, staff groups, mess access, group enrollment, add students from hostel, batch enrollment, group registration

**Synonyms:** batch enrollment, group registration, hostel-based addition

**Related:** add-member-individual, add-member-bulk-upload

**Tags:** Member Management, Group Enrollment, Frontend, Hostel, Student

---

## Add Member (Action)

<!-- id: actions-add-member | category: Member Actions -->

**What it does**

The 'Add Member' action allows the mess administrator to add individual students or staff to the mess platform by entering essential details like Registration ID and Email ID. For bulk addition, a Comma Separated Values (CSV) template can be downloaded, filled with relevant details, and uploaded. This action ensures members are added efficiently, granting them meal access according to institutional rules and policies, simplifying member management and reducing administrative workload.

**Why it matters**

This action allows the mess administrator to add members based on their eligibility, ensuring that meal access is granted accurately and promptly, in accordance with institutional policies. It simplifies member management, especially during peak periods, reducing administrative workload and maintaining a clean, up-to-date record of active members.

**How to use**

1. For individual members, enter Registration ID and Email ID.
2. For bulk addition, download a CSV template, fill with details, and upload.

**Examples**

- A new student enrolls in the institution. The mess administrator uses the 'Add Member' action to quickly add their Registration ID and Email ID, granting them immediate access to mess services.

**Questions this answers**

- How do I add a new student to the mess?
- Can I add multiple members using a CSV?
- What details are required to add a member?
- How to grant meal access to new students?
- What is the process for adding staff to the mess system?

**Keywords:** add member, mess administrator, individual member, bulk addition, CSV template, registration ID, email ID, meal access, member management, add student, add staff, enroll member, new mess member, member onboarding, register member, create member record

**Synonyms:** register member, create member record, enroll student

**Related:** actions-remove-member, actions-activate-member, actions-deactivate-member, add-member-individual, add-member-bulk-upload

**Tags:** Member Management, Actions, Frontend, Enrollment

---

## Remove Member (Action)

<!-- id: actions-remove-member | category: Member Actions -->

**What it does**

The 'Remove Member' action allows the mess administrator to remove members (students, staff) from the mess when they no longer require meal access. Once removed, the individual will no longer be able to access meal services. This function is useful for cases such as students graduating, leaving the hostel, or changes in meal plan eligibility, helping maintain an accurate and up-to-date database.

**Why it matters**

This action allows the mess administrator to remove members based on their eligibility or status, ensuring that meal access is managed accurately. It helps maintain a clean, up-to-date record of active members, preventing misuse and optimizing meal distribution by removing individuals who no longer need meal services.

**How to use**

1. Select a member from the platform.
2. Initiate the 'Remove Member' action.

**Examples**

- A student graduates and no longer requires mess services. The mess administrator uses the 'Remove Member' action to take them off the meal allocation list, ensuring the database is accurate.

**Questions this answers**

- How do I remove a student from the mess?
- Can I remove a staff member's meal access?
- What happens when a member is removed?
- When should I remove a mess member?
- How to update member eligibility for meals?

**Keywords:** remove member, delete member, mess administrator, student, staff, meal access, deactivate member, member management, remove student, remove staff, discontinue meal service, member exit, update member status, clean database, delete mess member, unenroll member, revoke meal access

**Synonyms:** delete mess member, unenroll member, revoke meal access

**Related:** actions-add-member, actions-activate-member, actions-deactivate-member

**Tags:** Member Management, Actions, Frontend, De-enrollment

---

## Activate Member (Action)

<!-- id: actions-activate-member | category: Member Actions -->

**What it does**

The 'Activate' action allows the mess administrator to enable meal access for a member whose coupon status was previously inactive. Once activated, the member can avail themselves of meals as per the schedule and mess rules. This feature is useful for members who were temporarily inactive (e.g., due to vacation, late admission, or pending approvals) and need their access restored quickly without being added again.

**Why it matters**

This action allows the mess administrator to activate members based on their eligibility, ensuring that meal access is granted accurately and promptly. It ensures smooth operations within the mess by restoring access for those temporarily suspended, improving flexibility and ensuring uninterrupted meal services for eligible members.

**How to use**

1. Select an inactive member.
2. Initiate the 'Activate Member' action.

**Examples**

- If a student has cleared their dues after a temporary suspension, the mess administrator can use the 'Activate' action to restore the student's meal access. This ensures the student can immediately avail of meals once eligibility is restored, without the need for re-entry into the platform.

**Questions this answers**

- How do I activate a suspended student's meal access?
- Can I reactivate a member's mess coupon?
- What happens when a member is activated?
- When should I activate a member?
- How to restore meal services for a student on leave?

**Keywords:** activate member, enable meal access, inactive coupon, restore access, mess administrator, reactivate member, temporary suspension, meal eligibility, student, staff, pending approvals, resume meal service, member status, activate student, activate staff, re-enable meal access, un-suspend member

**Synonyms:** re-enable meal access, un-suspend member, restore meal service

**Related:** actions-add-member, actions-remove-member, actions-deactivate-member

**Tags:** Member Management, Actions, Frontend, Activation

---

## Deactivate Member (Action)

<!-- id: actions-deactivate-member | category: Member Actions -->

**What it does**

The 'Deactivate' action allows the mess administrator to temporarily suspend a member's access to meals without removing them from the system. Once deactivated, the member's meal coupon becomes inactive, preventing them from availing any meals until reactivated. This action is often used for students on leave or with unpaid dues, helping control meal distribution and maintain financial accountability. Since deactivation does not delete the member's record, the mess administrator can easily reactivate the member later.

**Why it matters**

This action allows the mess administrator to deactivate members based on their eligibility or status, ensuring that meal access is managed accurately. It helps the institution control meal distribution, avoid misuse, and maintain financial accountability. Since deactivation does not delete the member's record, it provides flexibility for future reactivation, ensuring smooth operations within the mess.

**How to use**

1. Select an active member.
2. Initiate the 'Deactivate Member' action.

**Examples**

- A student goes on a month-long leave. The mess administrator uses the 'Deactivate Member' action to temporarily suspend their meal access, preventing coupon generation and misuse during their absence.

**Questions this answers**

- How do I temporarily stop a student's meal access?
- Can I deactivate a member without deleting them?
- What happens when a member is deactivated?
- When should I deactivate a mess member?
- How to suspend meal services for a student with unpaid dues?

**Keywords:** deactivate member, suspend meal access, inactive coupon, mess administrator, temporary suspension, student on leave, unpaid dues, financial accountability, meal distribution control, reactivate later, member status, deactivate student, deactivate staff, suspend mess member, temporarily disable meal access

**Synonyms:** suspend mess member, temporarily disable meal access, pause meal service

**Related:** actions-add-member, actions-remove-member, actions-activate-member

**Tags:** Member Management, Actions, Frontend, Deactivation

---

## Download Report (Vision Tab)

<!-- id: download-report-vision-tab | category: Reporting & Analytics -->

**What it does**

The 'Vision' tab in the Mess Management module allows the mess administrator to download detailed reports related to meal consumption. Reports can be filtered by month and year, and by selecting either all messes or specific meal types (e.g., breakfast, lunch, or dinner). Once filters are applied, a consolidated report with all relevant data can be easily downloaded, simplifying report generation and providing valuable insights for decision-making.

**Why it matters**

The Vision feature is crucial for mess administrators to track meal consumption efficiently. By allowing the generation of detailed reports based on filters like month, year, and meal types, it provides flexibility in analyzing meal data over specific periods. The ability to download consolidated reports helps mess administrators make informed decisions about meal planning and resource allocation, ensuring that meal distribution is efficient, transparent, and aligned with institutional needs, and aiding in food supply and waste management.

**How to use**

1. Navigate to the Vision tab in the Mess Management module.
2. Filter the report by month and year.
3. Select 'all messes' or specific meal types (breakfast, lunch, dinner).
4. Apply filters and download the consolidated report.

**Examples**

- At the end of the month, a mess administrator uses the Vision tab to filter the report for April and focuses on lunch meals across all messes. The mess administrator can then download a consolidated report showing meal consumption, which helps in analyzing trends and adjusting future meal planning to optimize resources and reduce waste.

**Questions this answers**

- How do I download a report on meal consumption?
- Can I filter reports by month and year?
- How to get a report for specific meal types?
- What kind of data is in the Vision tab report?
- How to track meal consumption trends?
- Can I export mess reports?

**Keywords:** download report, vision tab, meal consumption report, mess administrator, filter report, month, year, meal types, breakfast, lunch, dinner, consolidated report, meal data, analytics, reporting, insights, decision-making, meal tracking, food supply, waste management, export report, mess reports, mess analytics, consumption data, meal statistics

**Synonyms:** mess analytics, consumption data, meal statistics, report generation

**Tags:** Reporting, Analytics, Frontend, Data Export, Meal Consumption

---

## Avail Coupon (Web Interface)

<!-- id: avail-coupon-web | category: Meal Access & Verification -->

**What it does**

On the Web interface, a Mess Console Member or mess administrator can manually enter the meal code provided by a student or staff member. The platform then checks if the code is valid for the selected meal session. If valid, access is granted; if invalid, access is denied. This feature ensures that only valid members can access meals, preventing misuse and ensuring smooth and accurate meal distribution.

**Why it matters**

This feature helps prevent misuse of meal services, such as unauthorized access by students or staff who are not eligible. It also ensures efficient tracking of meal consumption, making it easier for mess administrators to monitor and manage meal allocations. Manual entry via the web interface promotes a streamlined, secure, and organized process for managing meals.

**How to use**

1. On the Web interface, manually enter the meal code provided by the member.
2. The platform verifies the code for the selected meal session.

**Examples**

- At the mess counter, a Mess Console Member on the Web interface manually enters a student's meal code. The system instantly verifies the code, granting the student access to their meal.

**Questions this answers**

- How do I verify a meal code on the web?
- Can I manually enter a meal code?
- What happens if a meal code is invalid?
- How to grant meal access using the web interface?
- How does coupon verification work on the web?

**Keywords:** avail coupon, web interface, meal code, verify meal access, mess console member, mess administrator, meal session, valid code, invalid code, meal distribution, prevent misuse, meal tracking, manual entry, web access, coupon verification, redeem coupon, check meal code, validate meal access

**Synonyms:** redeem coupon, check meal code, validate meal access

**Related:** avail-coupon-mobile-app

**Tags:** Meal Access, Verification, Frontend, Web, Coupon

---

## Avail Coupon (Digiicampus Mobile Application)

<!-- id: avail-coupon-mobile-app | category: Meal Access & Verification -->

**What it does**

In the Digiicampus Mobile Application, a Mess Console Member or mess administrator can scan the Quick Response (QR) code or manually enter the meal code. The platform automatically verifies the code's validity before granting meal access. This feature ensures that only valid members can access meals, preventing misuse and ensuring smooth and accurate meal distribution. Note: QR code scanning is available on the Android version of the Digiicampus Mobile Application only.

**Why it matters**

This feature helps prevent misuse of meal services, such as unauthorized access by students or staff who are not eligible. It also ensures efficient tracking of meal consumption, making it easier for mess administrators to monitor and manage meal allocations. Whether through manual entry or QR code scanning on the mobile app, this feature promotes a streamlined, secure, and organized process for managing meals.

**How to use**

1. Open the Digiicampus Mobile Application.
2. Scan the QR code or manually enter the meal code.
3. The platform automatically verifies the code's validity.

**Examples**

- A Mess Console Member uses the Mobile App to scan the QR code provided by a student at the mess entrance. The platform automatically verifies if the student's meal coupon is valid. If the code is valid, the member is granted meal access; if the code is invalid, the member is denied access. This ensures that only eligible members are allowed to access meals.

**Questions this answers**

- How do I scan a QR code for meal access?
- Can I enter a meal code on the mobile app?
- Which mobile app is used for coupon verification?
- Is QR code scanning available on iOS?
- How to grant meal access using the mobile app?
- What happens if a mobile meal code is invalid?

**Keywords:** avail coupon, mobile application, Digiicampus, QR code, scan QR code, meal code, verify meal access, mess console member, mess administrator, meal session, valid code, invalid code, meal distribution, prevent misuse, meal tracking, mobile app, Android, coupon verification, redeem coupon mobile, check meal code app, validate meal access mobile

**Synonyms:** redeem coupon mobile, check meal code app, validate meal access mobile

**Related:** avail-coupon-web

**Tags:** Meal Access, Verification, Frontend, Mobile App, QR Code, Coupon

---

## Mess Management Admin Privilege

<!-- id: prerequisite-mess-management-privilege | category: Admin Privileges -->

**What it does**

This privilege grants the Mess Administrator access to the Mess Management module, enabling them to perform essential functions such as adding, modifying, and managing mess details. The Mess Administrator can configure mess names, meal types, meal timings, and manage member access, ensuring smooth and efficient meal distribution across the platform. The privilege allows full control over the mess setup and meal scheduling, making it a critical function for managing mess operations.

**Why it matters**

This privilege is critical for managing all aspects of mess operations, from initial setup to daily meal scheduling and member management. It ensures that only authorized personnel can configure and control dining services, maintaining order, efficiency, and compliance with institutional policies.

**Questions this answers**

- What does the Mess Management Admin Privilege allow?
- Who can configure mess details?
- What functions can a Mess Administrator perform?
- How to get access to the Mess Management module?
- What are the responsibilities of a Mess Administrator?

**Keywords:** mess management admin privilege, mess administrator, access control, module access, add mess, modify mess, manage mess details, configure mess names, meal types, meal timings, manage member access, meal distribution, mess setup, meal scheduling, admin role, permissions, privilege, mess admin role, mess module access, dining management privilege

**Synonyms:** mess admin role, mess module access, dining management privilege

**Related:** prerequisite-mess-console-privilege

**Tags:** Admin Privilege, Access Control, Configuration, Mess Management

---

## Mess Console Admin Privilege

<!-- id: prerequisite-mess-console-privilege | category: Admin Privileges -->

**What it does**

Mess Console is a privilege granted exclusively to the Mess Administrator. It provides access through two platforms: the Web and the Digiicampus Mobile Application. On the Web, the Mess Administrator can manually enter the meal code for students or staff to avail of meals. On the Digiicampus Mobile Application, the Mess Administrator has two options: they can either scan the Quick Response (QR) code of the meal to verify meal access or manually enter the meal code. This flexibility ensures that meal access can be granted in real time, whether the Mess Administrator is using a mobile device or working on the Web platform.

**Why it matters**

This privilege is essential for real-time meal access verification, ensuring that only eligible members receive meals. It provides flexibility for Mess Administrators to use both web and mobile platforms, streamlining the process of coupon validation and preventing unauthorized meal consumption.

**Questions this answers**

- What does the Mess Console Admin Privilege do?
- Can Mess Administrators verify meals on mobile?
- How to grant meal access using the Mess Console?
- What are the options for meal verification with this privilege?
- Who can use the Mess Console?

**Keywords:** mess console admin privilege, mess administrator, web access, mobile application, Digiicampus, scan QR code, enter meal code, verify meal access, real-time access, meal validation, coupon verification, admin role, permissions, privilege, mess verification privilege, meal access control privilege

**Synonyms:** mess verification privilege, meal access control privilege

**Related:** prerequisite-mess-management-privilege

**Tags:** Admin Privilege, Access Control, Meal Verification, Mobile App, Web

---
