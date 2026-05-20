# Asset Management FAQ

**Module:** Asset Management  
**Tags:** Asset Management, Consumable Assets, Inventory Management, FAQ, Asset Administrator


## Overview

This document provides frequently asked questions and answers regarding the Asset Management module, focusing on the definition of asset schemas, management of consumable assets, purchase orders, allocation, expiry tracking, and inventory thresholds. It guides Asset Administrators through various processes for efficient asset control.

## Prerequisites

- **Asset Administrator Role** — User must have the Asset Administrator role assigned to perform these actions.

## Define Asset Schema

<!-- id: define-asset-schema | category: Asset Schema -->

**What it does**

Asset Administrators define the Asset Schema by adding appropriate Asset Categories and Asset Sub-Categories for consumable assets to be recorded in the Asset Management module.

**Why it matters**

This foundational step structures how all consumable assets are organized and tracked in the system, ensuring proper inventory management and data consistency.

**Questions this answers**

- How do I define the asset schema?
- What is an asset schema?
- How to set up asset categories?
- How to set up asset sub-categories?
- Who defines the asset schema?

**Keywords:** asset schema, define schema, create schema, asset categories, asset sub-categories, consumable assets, Asset Management (AM), asset administrator, organize assets, structure assets, inventory setup, asset classification, schema definition

**Synonyms:** asset structure, asset classification, schema definition

**Related:** add-asset-category-consumable, add-asset-sub-category-consumable

**Tags:** asset schema, setup, configuration, asset management

---

## Add Consumable Asset Category

<!-- id: add-asset-category-consumable | category: Asset Schema -->

**What it does**

Asset Administrators can add new categories specifically for consumable assets within the Asset Management (AM) module to organize inventory.

**Why it matters**

Categorizing assets helps in efficient tracking, reporting, and management of different types of consumable items, improving inventory control.

**How to use**

1. 1. Navigate to the Asset Management module.
2. 2. Under the Asset Schema section, click Add Category.
3. 3. Enter the Category Name.
4. 4. Select the Category Type as Consumable.
5. 5. Provide a Description if required.
6. 6. Click Save to create the new asset category for consumable assets.

**Questions this answers**

- How do I add a new asset category?
- Can I create a category for consumable items?
- Steps to add an asset category?
- What is a consumable asset category?
- How to categorize assets?

**Keywords:** add category, create category, asset category, consumable asset category, Asset Management (AM), asset schema, category name, category type, description, save category, inventory organization, asset administrator, new asset type, define category, asset categories

**Synonyms:** new asset type, create consumable group, define category

**Related:** define-asset-schema, add-asset-sub-category-consumable

**Tags:** asset schema, setup, configuration, consumable assets, category

---

## Add Consumable Asset Sub-Category

<!-- id: add-asset-sub-category-consumable | category: Asset Schema -->

**What it does**

Asset Administrators can create sub-categories under existing consumable asset categories to further refine asset organization within the Asset Management (AM) module.

**Why it matters**

Sub-categories allow for more granular classification and management of consumable assets, improving inventory detail, searchability, and reporting accuracy.

**How to use**

1. 1. Navigate to the Asset Management module.
2. 2. Under the Asset Schema section, click Add Sub-Category.
3. 3. Select the Parent Category under which the new sub-category should be created.
4. 4. Enter the Sub-Category Name and provide a Description if required.
5. 5. Click Save to create the new sub-category for the selected category of consumable assets.

**Questions this answers**

- How do I add a sub-category for assets?
- Can I create sub-categories for consumable items?
- Steps to add an asset sub-category?
- How to further classify assets?
- What is an asset sub-category?

**Keywords:** add sub-category, create sub-category, asset sub-category, consumable asset sub-category, Asset Management (AM), asset schema, parent category, sub-category name, description, save sub-category, inventory organization, asset administrator, new sub-type, define sub-category, asset sub-categories

**Synonyms:** new sub-type, create consumable subgroup, define sub-category

**Related:** define-asset-schema, add-asset-category-consumable

**Tags:** asset schema, setup, configuration, consumable assets, sub-category

---

## Custom Fields for Consumable Asset Sub-Category

<!-- id: custom-fields-consumable-sub-category | category: Asset Schema -->

**What it does**

Consumable asset categories and sub-categories do not support the addition of custom fields.

**Why it matters**

This clarifies a system limitation, preventing users from attempting to add unsupported data fields to consumable asset types and managing expectations.

**Questions this answers**

- Can I add custom fields to consumable asset sub-categories?
- Are custom fields supported for consumable assets?
- How to add extra fields to asset sub-categories?
- Why can't I add custom fields to consumable assets?

**Keywords:** custom fields, consumable assets, asset sub-category, asset category, add custom fields, unsupported feature, limitation, Asset Management (AM), asset administrator, custom attributes, extra fields, additional data

**Synonyms:** custom attributes, extra fields, additional data

**Tags:** asset schema, limitation, customization, consumable assets

---

## Add Consumable Asset Product

<!-- id: add-asset-product | category: Consumable Asset Management -->

**What it does**

Asset Administrators can add new consumable products to the inventory, specifying details like category, sub-category, product code, unit of measurement, store location, reorder threshold, and expiry handling.

**Why it matters**

Adding products is essential for tracking specific items, managing stock levels, and ensuring that consumable units can be properly recorded and allocated within the system.

**How to use**

1. 1. Navigate to the Asset Management module and click on the Consumable Asset Section.
2. 2. Click on the Manage Products tab.
3. 3. Click Add Product, then select the appropriate Category and Sub-Category for the product.
4. 4. Enter the Product Name, Product Code, and Unit of Measurement.
5. 5. Specify the Store Location, set the Reorder Threshold, and indicate whether to Handle Expiry for the product.
6. 6. Optionally, provide a Description and upload a Product Image.
7. 7. Once all details are entered, click Save to add the new product to the inventory.

**Questions this answers**

- How do I add a new product to asset management?
- Steps to add a consumable product?
- What information is needed to add an asset product?
- How to set up reorder thresholds for products?
- Can I upload a product image?

**Keywords:** add product, create product, asset product, consumable product, product name, product code, unit of measurement, store location, reorder threshold, handle expiry, product image, description, manage products, Asset Management (AM), asset administrator, inventory management, new item, add stock item, create inventory item

**Synonyms:** new item, add stock item, create inventory item

**Related:** mandatory-add-product, manage-product-expiry, track-inventory-thresholds

**Tags:** consumable assets, product management, inventory, setup

---

## Mandatory Product Addition

<!-- id: mandatory-add-product | category: Consumable Asset Management -->

**What it does**

Yes, adding a Product is mandatory in the Asset Management (AM) module. The Product is a crucial part of the asset hierarchy, and consumable units can only be added under a specific product.

**Why it matters**

This ensures that all consumable items are properly categorized and linked to a defined product, maintaining data integrity and enabling accurate inventory tracking and reporting.

**Questions this answers**

- Do I have to add a product in asset management?
- Is adding products compulsory?
- Why is a product mandatory for assets?
- Can I add consumable units without a product?

**Keywords:** mandatory product, required product, Asset Management (AM), consumable units, asset hierarchy, product requirement, add product, inventory management, data integrity, product necessity, essential product, must add product

**Synonyms:** product necessity, essential product, must add product

**Related:** add-asset-product, record-consumable-assets

**Tags:** consumable assets, product management, requirement, inventory

---

## Create Consumable Asset Purchase Order

<!-- id: create-purchase-order | category: Purchase Management -->

**What it does**

Asset Administrators can create new purchase orders for consumable assets by selecting a vendor, entering purchase details, and specifying the products, costs, quantities, and expiry dates.

**Why it matters**

Creating purchase orders is vital for formally documenting asset acquisitions, tracking expenses, and ensuring that new stock is properly recorded and integrated into inventory.

**How to use**

1. 1. Go to the Purchase Management tab in the Consumable Asset section of the Asset Management module.
2. 2. Click on Create New Purchase, select the Vendor, and enter the Purchase Order ID, Date of Purchase, Invoice Number, Date of Invoice, Receipt Number and Date of Receipt.
3. 3. Then, select the product being procured, cost per unit, batch quantity and Expiry Date.
4. 4. Click on Submit to create the purchase order.

**Questions this answers**

- How do I create a purchase order for consumable assets?
- Steps to make a new purchase order?
- What details are needed for a purchase order?
- Can I record product expiry in a purchase order?
- How to procure consumable items?

**Keywords:** create purchase order, new purchase, purchase management, consumable asset, Asset Management (AM), vendor, purchase order ID, date of purchase, invoice number, date of invoice, receipt number, date of receipt, product, cost per unit, batch quantity, expiry date, submit purchase, asset administrator, procurement, generate PO, record purchase, buy assets

**Synonyms:** generate PO, record purchase, buy assets

**Related:** record-consumable-assets

**Tags:** purchase management, consumable assets, procurement, inventory

---

## Recording Consumable Assets

<!-- id: record-consumable-assets | category: Consumable Asset Management -->

**What it does**

Consumable assets are recorded by first creating the Asset Schema (Category and Sub-Category), then adding a Product, and finally entering its Purchase Details. The platform automatically creates consumable units upon purchase, making them available for allocation.

**Why it matters**

This structured recording process ensures that all consumable assets are accurately tracked from acquisition to allocation, providing a clear audit trail and facilitating inventory control.

**How to use**

1. 1. Create the Asset Schema by adding a Category and a Sub-Category.
2. 2. Add a Product.
3. 3. Enter its Purchase Details.
4. 4. The platform automatically creates consumable units based on the quantity purchased.
5. 5. These units are then available for allocation by asset administrators to specific departments or members as per institutional requirements.

**Questions this answers**

- How are consumable assets recorded?
- What is the process for recording assets?
- When are consumable units created?
- How do I get assets ready for allocation?
- What steps are involved in asset recording?

**Keywords:** record assets, consumable assets, asset schema, category, sub-category, product, purchase details, consumable units, automatic creation, allocation, asset administrator, inventory tracking, Asset Management (AM), asset entry, logging assets, asset registration, inventory recording

**Synonyms:** asset entry, logging assets, asset registration, inventory recording

**Related:** define-asset-schema, add-asset-category-consumable, add-asset-sub-category-consumable, add-asset-product, create-purchase-order, allocate-consumable-assets

**Tags:** consumable assets, inventory, workflow, asset management

---

## Allocate Consumable Assets

<!-- id: allocate-consumable-assets | category: Consumable Asset Management -->

**What it does**

Asset Administrators can allocate consumable assets to specific departments or individual members by selecting the category, sub-category, product, quantity, recipient, date, location, and purpose of the allotment.

**Why it matters**

Asset allocation ensures that consumable items are distributed efficiently and tracked to their respective users or departments, maintaining accountability and accurate inventory levels.

**How to use**

1. 1. Go to the Allotment Tab in the Consumable Asset section of Asset Management module.
2. 2. Click Create New Allotment.
3. 3. Select the Category, Sub-Category, Product, and Quantity.
4. 4. Choose the Allotted To field (Department or Member), select the Date of Allotment, Location, and Purpose.
5. 5. Click Save to finalize the allotment.

**Questions this answers**

- How do I allocate consumable assets?
- Can I assign assets to a department?
- How to allot items to a staff member?
- What details are needed for asset allocation?
- Steps to distribute consumable inventory?

**Keywords:** allocate assets, allot assets, distribute assets, consumable assets, department allocation, member allocation, allotment tab, create new allotment, category, sub-category, product, quantity, allotted to, date of allotment, location, purpose, save allotment, asset administrator, inventory distribution, assign assets, issue assets, hand out consumables

**Synonyms:** assign assets, issue assets, hand out consumables

**Related:** record-consumable-assets, return-allotted-quantity

**Tags:** consumable assets, allocation, inventory, asset management

---

## Manage Consumable Product Expiry

<!-- id: manage-product-expiry | category: Consumable Asset Management -->

**What it does**

Asset Administrators can manage product expiry by enabling the 'Handle Expiry' toggle when creating a product, which makes the expiry date field available for tracking products with a limited shelf life.

**Why it matters**

Tracking expiry dates is crucial for managing perishable or time-sensitive consumable assets, reducing waste, and ensuring that only valid items are allocated to users.

**How to use**

1. 1. Enable the Handle Expiry toggle when creating a product in the Consumable Asset section of Asset Management module.
2. 2. When this option is enabled, the expiry date field will appear in the product details, allowing asset administrators to track and manage products with a limited shelf life.

**Questions this answers**

- How do I track expiry dates for consumable products?
- Can I manage product expiration in asset management?
- How to enable expiry tracking for assets?
- What happens when 'Handle Expiry' is enabled?
- How to prevent using expired items?

**Keywords:** manage expiry, product expiry, handle expiry, expiry date, consumable assets, Asset Management (AM), product creation, toggle, shelf life, track expiry, asset administrator, inventory control, expiry management, expiration tracking, perishable goods

**Synonyms:** expiry management, expiration tracking, perishable goods

**Related:** add-asset-product

**Tags:** consumable assets, inventory, expiry management, product management

---

## Track Consumable Inventory Thresholds

<!-- id: track-inventory-thresholds | category: Consumable Asset Management -->

**What it does**

Asset Administrators can track inventory thresholds by setting a 'Reorder Threshold' value during product creation, which triggers a notification when stock levels fall below this minimum.

**Why it matters**

Setting reorder thresholds helps prevent stockouts, ensures timely replenishment of consumable assets, and optimizes inventory levels to avoid disruptions.

**How to use**

1. 1. Enter the value in the Reorder Threshold field when creating or a product in the Consumable Asset section of Asset Management module to set a minimum stock level.
2. 2. When stock falls below this threshold, the platform will notify the asset administrator to reorder the product.

**Questions this answers**

- How do I set a reorder threshold for assets?
- Can I get notified when stock is low?
- How to track minimum inventory levels?
- What is a reorder threshold?
- How to manage stock levels for consumables?

**Keywords:** track inventory thresholds, reorder threshold, minimum stock level, stock notification, consumable assets, Asset Management (AM), product creation, inventory control, stock management, asset administrator, replenishment, low stock alert, reorder point, minimum inventory, stock level tracking

**Synonyms:** low stock alert, reorder point, minimum inventory, stock level tracking

**Related:** add-asset-product

**Tags:** consumable assets, inventory, stock management, notifications

---

## Record Consumable Asset Return

<!-- id: record-allotted-quantity-return | category: Consumable Asset Management -->

**What it does**

Asset Administrators can record the return of an allotted quantity of consumable assets by accessing the specific allotment record, entering the return quantity, and processing the return to update inventory levels.

**Why it matters**

Recording returns accurately updates inventory, ensures accountability for allocated items, and provides a clear record of asset movements for auditing purposes.

**How to use**

1. 1. Go to the Allotment Tab in the Consumable Assets module.
2. 2. Click on the View or Return Link against the specific allotment record.
3. 3. Once the allotment details are displayed, click on the Return Items Button.
4. 4. Enter the Quantity to Return and click Process Return to complete the return process.
5. 5. This will update the allotment records and adjust inventory levels accordingly.

**Questions this answers**

- How do I record a return of an allocated asset?
- Can I return consumable items?
- Steps to process an asset return?
- How does returning assets affect inventory?
- Where do I record asset returns?

**Keywords:** record return, return allotted quantity, return assets, consumable assets, allotment tab, view return link, return items button, quantity to return, process return, update inventory, adjust inventory, asset administrator, Asset Management (AM), asset check-in, return stock, de-allocate assets

**Synonyms:** asset check-in, return stock, de-allocate assets

**Related:** allocate-consumable-assets

**Tags:** consumable assets, allocation, returns, inventory

---

## Staff Notification for Asset Allocation

<!-- id: staff-asset-allocation-notification | category: Consumable Asset Management -->

**What it does**

The platform currently does not support automated notifications for asset allocations to staff members; Asset Administrators will need to manually communicate these allocations.

**Why it matters**

This clarifies a current system limitation regarding automated communication, managing user expectations and outlining the manual process required for informing staff.

**Questions this answers**

- Does the system notify staff about asset allocations?
- How are staff informed about allocated assets?
- Are there automatic notifications for asset assignments?
- Do I need to manually tell staff about asset allocations?

**Keywords:** staff notification, asset allocation notification, automated notification, manual communication, staff member, asset administrator, system limitation, consumable assets, Asset Management (AM), asset assignment alert, employee notification, automatic alerts

**Synonyms:** asset assignment alert, employee notification, automatic alerts

**Related:** allocate-consumable-assets

**Tags:** consumable assets, notifications, limitation, communication

---
