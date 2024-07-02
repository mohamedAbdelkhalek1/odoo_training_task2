{
    'name': 'HMS',
    'summary': 'Hospital Management System',
    'description': 'Hospital Management System Lab',

    'author': 'Mohammed Abd Elkhalek',
    'website': 'github.com/mohamedAbdelkhalek1',

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'crm', 'sale', 'account'],

    'data': [
        'security/hms_security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/medicine_view.xml',
        'views/medicine_invoice_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'views/customers_view.xml',
        'views/log_history_view.xml',
        # 'reports/custom_external_layout.xml',
        'reports/hms_reports.xml',
        'reports/hms_report_templates.xml',
    ],
}
