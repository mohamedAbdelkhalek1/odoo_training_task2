# odoo_training_task2
HMS Odoo addon

# Task Statements:
1- Create new module called “hms”.
2- Create a model for patient called “hms.patient”.
3 Create needed menus to view/create patients' data.
4 The model contains the following data:
  ➢ First name
  ➢ Last name
  ➢ Birth date
  ➢ History (html)
  ➢ CR Ratio (float)
  ➢ Blood type (drop down)
  ➢ PCR (checkbox)
  ➢ Image (upload image)
  ➢ Address (text)
  ➢ Age
5- Create a model for departments called “hms.department” contains the following:
  ➢ Name
  ➢ Capacity (integer)
  ➢ Is_opened (boolean)
  ➢ Patients
6- Create a model for doctors called “hms.doctors” contains the following:
  ➢ First Name
  ➢ Last Name
  ➢ Image
7- The patient model should be linked to department and doctors and the selected department capacity should be shown from the patient view too.
8- Add new log history for the patient, and the log record shows the following date:
  ➢ Created by
  ➢ Date
  ➢ description
9- The patient should have a states (Undetermined, Good, Fair, Serious), and With each change of the state a new log record is being created with a description of (State changed to NEW_STATE).
10- The patient can’t choose a closed department.
11- The Doctors field is a many2many tags and should be readonly until the department is being selected.
12- The first name and last name are required.
13- If The pcr field is checked, the CR ratio field should be mandatory.
14- The history field should be hidden if the age is less than 50.
15- The PCR field should be automatically checked if the age is lower than 30 and show a warning message that it has been checked.
16- Add email field to patients' model and make sure that it is a valid and unique email address.
17- Link patient model with customers model from CRM module by adding a new field in customers model called “related_patient_id” and show this field inside Misc group within sales and purchase tab.
18- Convert the patient’s age field to be auto calculated based on birth date.
19- Add a constraint on CRM customer model which prevents linking customer with email which already exists in patient model.
20- Prevent users to delete any customer linked to a patient.
21- Show website field in the list view for customers.
22- Make the Tax ID field mandatory for CRM Customers.
23- Create two new user groups (user , manager).
24- The user group has the following access rights:
  ➢ Can create/read/update his own patients records
  ➢ Can read only departments
  ➢ Can read only doctors
  ➢ Can’t view doctor fields in patients’ form view
  ➢ Can’t view doctors’ menu item
25- The Manager group has the following access rights:
  ➢ Can create/read/update/delete all patients records
  ➢ Can create/read/update/delete departments
  ➢ Can create/read/update/delete doctors
  ➢ Can view doctor fields in patients form view
  ➢ Can view doctors menu item
26- Create a patients report like the following design.
