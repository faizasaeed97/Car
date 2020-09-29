# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class logsrdetDetails(models.TransientModel):
    _name = 'emplog.wage.details'
    _description = "Project Report Details"

    # start_date = fields.Date(string='Start Date', required=True)
    # end_date = fields.Date(string='End Date', required=True)
    # stage_id = fields.Many2one('project.task.type', string="Stage", required=True)

    def print_report(self):
        plist = []

        dept = self.env['hr.department'].search(
            [])

        for dpt in dept:
            dix = {}
            dix['data'] = 'd'
            dix['div'] = dpt.name
            plist.append(dix)

            emps = self.env['hr.employee'].search(
                [('contract_id.grade.department', '=', dpt.id)])
            for rec in emps:
                dix = {}

                dix['emp'] = rec.name
                dix['roll'] = rec.identification_id
                dix['wphone'] = rec.work_phone
                dix['div'] = rec.contract_id.grade.department.name
                dix['wage'] = rec.contract_id.wage
                dix['hallow'] = rec.contract_id.housing_allowance
                dix['tallow'] = rec.contract_id.travel_allowance
                dix['gosi_deduc'] = rec.contract_id.gosi_Salary_Deduction
                dix['data'] = 'nd'

                plist.append(dix)

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {

                'dta': plist

                # 'user_id': self.user_id.id,
                # 'start_date': self.start_date,
                # 'end_date':self.end_date,
                # 'stage_id':self.stage_id.id,
            },
        }
        return self.env.ref('design_creative_custom.action_report_salary_listing').report_action(self, data=data)


class emplogscxReport(models.AbstractModel):
    _name = 'report.design_creative_custom.salary_report_empx'
    _description = "Emp Wage Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        datax = data['form']['dta']

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],

            'dtax': datax,

            # 'end_date':end_date,
            # 'project_id':self.env['project.project'].browse(project_id),
            # 'stage_id':self.env['project.task.type'].browse(stage_id),
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
