# Asset Management Features

**Module:** Asset Management  
**Tags:** Asset Management, Vendors, Privileges, Asset Categories, Sub-Categories, Consumable Assets, Products, Purchase Orders, Allotment, Returns, Bulk Upload, CSV, Excel, Templates, Inventory Management


## Overview

This document outlines various features within the Digii Asset Management module, covering vendor creation, administrative privilege assignment, defining asset categories and sub-categories, managing consumable products, recording purchase details, and handling asset allotments and returns.

## Prerequisites

- **Admin Console Access** — Users must have appropriate administrative access to the Digii Admin Console to access the Asset Management module and its features.

## Add Vendor in Asset Management

<!-- id: add-vendor-asset-management | category: Vendor Management -->

**What it does**

Allows users to add new vendor details within the Asset Management module, including their contact and other relevant information.

**Why it matters**

Essential for tracking suppliers of assets and consumables, streamlining procurement processes, and maintaining a comprehensive vendor database.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Go to the Vendor Details tab.
3. Click on the "Add Vendor" button.
4. Enter the required vendor details.
5. Click on "Save".

**Examples**

- An administrator needs to add 'Office Supplies Inc.' as a new vendor after signing a new procurement contract.

**Questions this answers**

- How do I add a new vendor?
- Where can I find vendor details?
- What information is needed to add a vendor?
- Can I manage suppliers in Asset Management?
- How to register a new supplier?

**Keywords:** add vendor, create vendor, new vendor, vendor details, vendor management, asset management, supplier, procurement, vendor record, add supplier, vendor information, asset admin, admin console, save vendor, vendors

**Synonyms:** supplier, provider, seller

**Tags:** vendor, supplier, asset management, create

---

## Assign Admin Privileges in Asset Management

<!-- id: assign-admin-privileges-asset-management | category: Privilege Management -->

**What it does**

Enables administrators to assign specific privileges to members for managing categories, sub-categories, products, or individual assets within the Asset Management module.

**Why it matters**

Ensures proper access control and delegation of responsibilities, allowing different users to manage specific aspects of assets without granting full administrative access.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Click on the "Admin Privileges" tab.
3. Click on the "Add Member" button to assign privileges to a member.
4. To view assigned privileges, click on the "View" hyperlink.
5. To modify privileges, click on the "Edit" button, make changes, and save.

**Examples**

- An administrator assigns a specific staff member the privilege to manage only 'IT Equipment' categories.

**Questions this answers**

- How do I give someone access to manage assets?
- Can I restrict a user to only certain asset categories?
- Where can I see who has asset management privileges?
- How do I change a user's asset permissions?
- What are admin privileges in Asset Management?
- How to add a member to asset privileges?

**Keywords:** assign privileges, admin privileges, manage access, user roles, asset management access, category privileges, sub-category privileges, product privileges, asset privileges, delegate access, edit privileges, view privileges, add member, access control, permissions, asset admin, security, privilege management

**Synonyms:** permissions, access rights, user roles, delegation

**Tags:** privileges, access control, security, roles, admin

---

## Asset Schema Configuration

<!-- id: asset-schema-configuration | category: Asset Configuration -->

**What it does**

Allows administrators to define and manage the structure of assets by adding categories and sub-categories within the Asset Management module.

**Why it matters**

Provides a structured framework for organizing and classifying all assets, which is crucial for efficient inventory management, reporting, and tracking.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Click on the "Asset Schema" tab.
3. From here, you can add categories and sub-categories.
4. NOTE: Fields are not applicable for Sub-category created for Consumable Assets.

**Examples**

- Setting up 'IT Equipment' as a category and 'Laptops' or 'Printers' as sub-categories.

**Questions this answers**

- How do I set up asset categories?
- What is an asset schema?
- Can I create sub-categories for assets?
- Where do I define asset types?
- How to organize my assets?

**Keywords:** asset schema, asset categories, asset sub-categories, define schema, configure assets, asset structure, inventory classification, asset organization, manage categories, manage sub-categories, asset management, asset admin, schema configuration

**Synonyms:** asset structure, classification, taxonomy

**Related:** add-asset-category-individually, bulk-upload-asset-category, add-asset-sub-category-individually, bulk-upload-asset-sub-category

**Tags:** asset schema, categories, sub-categories, configuration, asset management

---

## Add Asset Category Individually

<!-- id: add-asset-category-individually | category: Asset Configuration -->

**What it does**

Enables administrators to add new asset categories one by one within the Asset Schema section of the Asset Management module.

**Why it matters**

Provides flexibility for creating specific asset classifications as needed, ensuring that all types of assets can be properly categorized and tracked.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Click on the "Asset Schema" tab.
3. In the Category section, click on the "+Add" button.
4. Select "Add Single" to add a category individually.

**Examples**

- Adding 'Furniture' or 'Lab Equipment' as a new asset category.

**Questions this answers**

- How do I add one asset category?
- Can I create a new asset category manually?
- What are the steps to add a single asset category?
- Where do I define a new asset type?

**Keywords:** add category, create category, single category, asset category, new asset type, individual category, asset schema, asset management, asset admin, add single category, categories

**Synonyms:** create asset type, new classification

**Related:** asset-schema-configuration, bulk-upload-asset-category

**Tags:** asset category, add, individual, asset management

---

## Bulk Upload Asset Category

<!-- id: bulk-upload-asset-category | category: Asset Configuration -->

**What it does**

Allows Asset Administrators to efficiently add multiple asset categories simultaneously by uploading a Comma Separated Values (CSV) file.

**Why it matters**

Significantly speeds up the process of populating the asset management system with a large number of categories, reducing manual entry and potential errors.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Click on the "Asset Schema" tab.
3. In the Category section, click on the "+Add" button.
4. Select "Add Bulk" to upload multiple categories.
5. Prepare a CSV file with mandatory fields: Name, Auto Generate ID, Category ID (if Auto Generate Id is false), and Type.
6. Upload the CSV file.

**Examples**

- An administrator uploads a CSV file containing 50 new categories for different types of office supplies and equipment.

**Questions this answers**

- How can I add many asset categories at once?
- What is the process for bulk uploading asset categories?
- Which fields are required for the asset category CSV template?
- Can I import asset categories from a file?
- How to add multiple categories using a CSV?

**Keywords:** bulk upload, asset category, multiple categories, CSV upload, import categories, add many categories, asset schema, asset management, asset admin, mandatory fields, category name, auto generate ID, category ID, type, add bulk, categories, template

**Synonyms:** import categories, mass upload, batch add

**Related:** asset-schema-configuration, add-asset-category-individually

**Tags:** asset category, bulk upload, CSV, import, asset management, template

---

## Add Asset Sub-Category Individually

<!-- id: add-asset-sub-category-individually | category: Asset Configuration -->

**What it does**

Enables administrators to add new asset sub-categories one by one within the Asset Schema section of the Asset Management module.

**Why it matters**

Provides granular classification for assets, allowing for more detailed organization and tracking within broader categories.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Click on the "Asset Schema" tab.
3. In the Sub-Category section, click on the "+Add" button.
4. Select "Add Single" to add a sub-category individually.
5. Note: Consumable category does not support custom fields.

**Examples**

- Adding 'Laser Printers' as a sub-category under the 'IT Equipment' category.

**Questions this answers**

- How do I add one asset sub-category?
- Can I create a new asset sub-category manually?
- What are the steps to add a single asset sub-category?
- Do consumable sub-categories have custom fields?

**Keywords:** add sub-category, create sub-category, single sub-category, asset sub-category, new sub-type, individual sub-category, asset schema, asset management, asset admin, add single sub-category, consumable category, sub-categories

**Synonyms:** create sub-type, new sub-classification

**Related:** asset-schema-configuration, bulk-upload-asset-sub-category

**Tags:** asset sub-category, add, individual, asset management

---

## Bulk Upload Asset Sub-Category

<!-- id: bulk-upload-asset-sub-category | category: Asset Configuration -->

**What it does**

Allows Asset Administrators to efficiently add multiple asset sub-categories simultaneously by uploading a Comma Separated Values (CSV) file.

**Why it matters**

Streamlines the process of populating the asset management system with detailed sub-classifications, improving data entry efficiency and accuracy for large inventories.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Click on the "Asset Schema" tab.
3. In the Sub-Category section, click on the "+Add" button.
4. Select "Add Bulk" to upload multiple sub-categories.
5. Prepare a CSV file with mandatory fields: Category Name, Category ID, Sub-Category Name, Auto Generate ID, and Sub-Category ID (if Auto Generate Id is false).
6. Upload the CSV file.

**Examples**

- An administrator imports a CSV file to add all sub-categories for 'Office Furniture' like 'Chairs', 'Desks', and 'Cabinets'.

**Questions this answers**

- How can I add many asset sub-categories at once?
- What is the process for bulk uploading asset sub-categories?
- Which fields are required for the asset sub-category CSV template?
- Can I import asset sub-categories from a file?
- How to add multiple sub-categories using a CSV?

**Keywords:** bulk upload, asset sub-category, multiple sub-categories, CSV upload, import sub-categories, add many sub-categories, asset schema, asset management, asset admin, mandatory fields, category name, category ID, sub-category name, auto generate ID, sub-category ID, add bulk, sub-categories, template

**Synonyms:** import sub-types, mass upload sub-categories, batch add sub-categories

**Related:** asset-schema-configuration, add-asset-sub-category-individually

**Tags:** asset sub-category, bulk upload, CSV, import, asset management, template

---

## Add Products for Consumable Assets Individually

<!-- id: add-consumable-product-individually | category: Consumable Asset Management -->

**What it does**

Allows administrators to create and add individual product entries specifically for consumable assets within the Asset Management module.

**Why it matters**

Enables precise tracking and management of individual consumable items, facilitating inventory control and ensuring availability of necessary supplies.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Go to the "Consumable Asset" tab.
3. In the "Manage Products" tab, click on the "Create Product" button to add individual product.

**Examples**

- Adding 'Printer Ink Cartridge Model XYZ' as a new consumable product.

**Questions this answers**

- How do I add a single consumable product?
- Where can I create new consumable items?
- What is the process to add a product for consumable assets?
- Can I add one consumable product at a time?

**Keywords:** add product, create product, consumable asset, manage products, individual product, new consumable, asset management, asset admin, create product button, consumable asset tab, products

**Synonyms:** create consumable item, add stock item

**Related:** bulk-upload-consumable-products

**Tags:** consumable assets, products, add, individual, asset management

---

## Bulk Upload Products for Consumable Assets

<!-- id: bulk-upload-consumable-products | category: Consumable Asset Management -->

**What it does**

Enables Asset Administrators to efficiently upload a large number of consumable products using an Excel sheet (or CSV file), streamlining inventory setup.

**Why it matters**

Significantly reduces the time and effort required to onboard new consumable product lines or update existing ones in bulk, improving data accuracy and operational efficiency.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Go to the "Consumable Asset" tab.
3. In the "Manage Products" tab, click on the "Bulk Upload" button to add products in bulk.
4. Prepare an Excel sheet (or CSV) with mandatory fields: Product Name, Product Code, Company Name, Sub-Category Name, Sub-Category Code, and Unit Name.
5. Upload the file.

**Examples**

- An administrator uploads an Excel sheet containing 200 new stationery items to be tracked as consumable assets.

**Questions this answers**

- How can I add many consumable products at once?
- What is the process for bulk uploading consumable products?
- Which fields are required for the consumable product bulk upload template?
- Can I import consumable products from an an Excel file?
- How to add multiple products using a spreadsheet?

**Keywords:** bulk upload, consumable products, multiple products, Excel upload, CSV upload, import products, add many products, manage products, consumable asset, asset management, asset admin, mandatory fields, product name, product code, company name, sub-category name, sub-category code, unit name, products, template

**Synonyms:** import consumable items, mass upload products, batch add products

**Related:** add-consumable-product-individually

**Tags:** consumable assets, products, bulk upload, Excel, CSV, import, asset management, template

---

## Add New Purchase Details for Consumable Assets

<!-- id: add-new-purchase-details | category: Consumable Asset Management -->

**What it does**

Allows Asset Administrators to record new purchase orders and their details for consumable assets within the Asset Management module.

**Why it matters**

Essential for maintaining accurate records of inventory acquisition, managing budgets, and tracking the cost and source of consumable supplies.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Go to the "Consumable Asset" tab.
3. In the "Purchase Details" tab, click on the "New Purchase" button to add new purchase details.
4. Enter the purchase order details.
5. Save the purchase details.

**Examples**

- Recording a new purchase order for 100 reams of paper from 'Office Supplies Inc.'.

**Questions this answers**

- How do I record a new purchase for consumable assets?
- Where can I add purchase order details?
- What information is needed for a new consumable purchase?
- How to log a new inventory acquisition?

**Keywords:** add purchase, new purchase, purchase details, purchase order, consumable asset, record purchase, inventory acquisition, manage purchases, asset management, asset admin, new purchase button, purchase details tab, purchases

**Synonyms:** create purchase order, log acquisition

**Related:** view-existing-purchase-details

**Tags:** consumable assets, purchase, purchase order, inventory, asset management

---

## View Existing Purchase Details for Consumable Assets

<!-- id: view-existing-purchase-details | category: Consumable Asset Management -->

**What it does**

Enables Asset Administrators to review the details of previously recorded purchase orders for consumable assets.

**Why it matters**

Provides transparency and historical data for auditing, budget reconciliation, and understanding past procurement activities for consumable supplies.

**How to use**

1. Navigate to the Asset Management module from the Admin Console.
2. Go to the "Consumable Asset" tab.
3. In the "Purchase Details" tab, click on the "View" hyperlink next to each purchase order.

**Examples**

- Reviewing the details of a purchase order from six months ago to check the quantity and cost of a specific consumable.

**Questions this answers**

- How do I view past purchase orders for consumables?
- Where can I find existing purchase details?
- Can I see the history of consumable asset purchases?
- How to check a specific purchase order?

**Keywords:** view purchase, existing purchase, purchase details, purchase order, consumable asset, review purchase, historical purchases, asset management, asset admin, view hyperlink, purchase details tab, purchases

**Synonyms:** check purchase history, review acquisition records

**Related:** add-new-purchase-details

**Tags:** consumable assets, purchase, view, history, asset management

---

## Allot Consumable Assets

<!-- id: allot-consumable-assets | category: Consumable Asset Management -->

**What it does**

Allows Asset Administrators to allocate consumable assets to specific members or departments within the organization.

**Why it matters**

Facilitates the distribution of supplies, ensures accountability for allocated items, and helps track inventory movement within the campus.

**How to use**

1. Go to the "Consumable Asset" tab.
2. Click the "Allotment" section.
3. Click "Create New Allotment" to allocate consumable assets to members or departments.

**Examples**

- Allocating 50 pens and 20 notebooks to the 'Marketing Department'.

**Questions this answers**

- How do I allocate consumable assets?
- Can I assign consumables to a department?
- Where do I create a new allotment?
- How to distribute office supplies?
- What is the process for allotting assets?

**Keywords:** allot assets, allocate consumables, assign assets, distribute supplies, create allotment, new allotment, consumable asset, allotment section, asset management, asset admin, assign to member, assign to department, allotments

**Synonyms:** issue consumables, distribute assets, assign supplies

**Related:** return-consumable-assets, view-consumable-allotments

**Tags:** consumable assets, allotment, allocation, distribution, asset management

---

## Return Consumable Assets

<!-- id: return-consumable-assets | category: Consumable Asset Management -->

**What it does**

Enables Asset Administrators to log the return of unused consumable assets from assigned members or departments back into inventory.

**Why it matters**

Ensures accurate inventory counts, prevents waste, and allows for reallocation of returned items, optimizing resource utilization.

**How to use**

1. Go to the "Consumable Asset" tab.
2. Click the "Allotment" section.
3. Click the "View or Return" link next to each allotment record order to view allotments or log the return of unused consumables from assigned members or departments.

**Examples**

- A department returns 10 unused staplers from a previous allotment.

**Questions this answers**

- How do I record returned consumable assets?
- Can I log the return of unused supplies?
- Where can I process asset returns?
- What happens when a member returns consumables?

**Keywords:** return assets, return consumables, log return, unused consumables, asset return, inventory return, consumable asset, allotment section, asset management, asset admin, view or return link, returns

**Synonyms:** check-in consumables, retrieve assets

**Related:** allot-consumable-assets, view-consumable-allotments

**Tags:** consumable assets, return, inventory, asset management

---

## View Consumable Asset Allotments

<!-- id: view-consumable-allotments | category: Consumable Asset Management -->

**What it does**

Allows Asset Administrators to review existing records of consumable assets that have been allotted to members or departments.

**Why it matters**

Provides an overview of asset distribution, helps track who has which items, and supports auditing and reconciliation of consumable inventory.

**How to use**

1. Go to the "Consumable Asset" tab.
2. Click the "Allotment" section.
3. Click the "View or Return" link next to each allotment record order to view the details.

**Examples**

- Checking the allotment record for the 'Science Department' to see what lab supplies they currently have.

**Questions this answers**

- How do I see who has been allotted consumables?
- Where can I view existing asset allotments?
- Can I track distributed consumable items?
- How to check the status of an allotment?

**Keywords:** view allotments, check allotments, consumable asset allotments, review distribution, asset tracking, consumable asset, allotment section, asset management, asset admin, view or return link, allotments

**Synonyms:** check assigned assets, review distribution records

**Related:** allot-consumable-assets, return-consumable-assets

**Tags:** consumable assets, allotment, view, tracking, asset management

---
