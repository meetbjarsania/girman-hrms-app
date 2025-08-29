# Copyright (c) 2025, Meet and contributors
# For license information, please see license.txt


import frappe

def execute(filters=None):
    columns = [
        {"label":"Source","fieldname":"source","fieldtype":"Data","width":200},
        {"label":"Applicants","fieldname":"count","fieldtype":"Int","width":120},
    ]
    data = frappe.db.sql("""
        SELECT COALESCE(custom_source_of_application, 'Not Set') as source,
               COUNT(*) as count
        FROM `tabJob Applicant`
        GROUP BY custom_source_of_application
        ORDER BY count DESC
    """, as_dict=True)
    chart = {
        "data": {
            "labels": [d["source"] for d in data],
            "datasets": [{"values": [d["count"] for d in data]}]
        },
        "type": "bar"
    }
    return columns, data, None, chart
