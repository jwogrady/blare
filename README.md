# blare

Blare is a client interface for Blesta. 

## Blesta Module API Structure
Blesta model's API can be grouped in to Modular and Functional categories.

### Modular Categories
Modular categories corresond to different aspects of the system (e.g., Accounts, Clients, Invoices, Services, Users, etc.).

1. **User and Staff Management**
   - [Users](https://source-docs.blesta.com/class-Users.html)
   - [Staff](https://source-docs.blesta.com/class-Staff.html)
   - [StaffGroups](https://source-docs.blesta.com/class-StaffGroups.html)

2. **Client Management**
   - [Clients]()
   - [ClientGroups]()
   - [Contacts]()

3. **Service Management**
   - Services
   - ServiceChanges

4. **Package and Product Management**
   - Packages
   - PackageGroups
   - PackageOptions
   - PackageOptionGroups

5. **Invoicing and Payments**
   - Invoices
   - Payments
   - Transactions
   - ServiceInvoices

6. **Reporting and Analytics**
   - Reports
   - ReportManager
   - Logs

7. **System and Settings**
   - Settings
   - SystemEvents
   - Backup

### Functional Categories
Functional categies cover domain within the system such as client management, invoicing, payments, system settings, etc.
1. **API and Integration**
   - ApiKeys
   - GatewayManager
   - ModuleManager
   - PluginManager

2. **Communication and Messaging**
   - Emails
   - EmailGroups
   - Messages
   - MessageGroups
   - EmailVerifications
   - MessengerManager

3. **Financial and Tax Management**
   - Taxes
   - Currencies
   - Pricings

4. **Security and Compliance**
   - Permissions
   - Encryption
   - Actions

5. **Localization and Customization**
   - Languages
   - Countries
   - States
   - Themes

6. **Event and Schedule Management**
   - CalendarEvents
   - CronTasks

7. **Marketing and Promotions**
   - Coupons
   - CouponTerms
   - Marketplace


# Blesta Resources

[Blesta API Documentation](https://docs.blesta.com/display/dev/API) provides comprehensive information on how to configure, connect, and interact with the API.

[Blesta API Documentation](https://docs.blesta.com/display/dev/API) provides comprehensive information on how to configure, connect, and interact with the API

[Blesta PHP SDK on GitHub](https://github.com/blesta/sdk-php)
