from audit.utils import log_activity

def log_payslip_activity(user, action, payslip):
    log_activity(user, action, module="Payslip", instance=payslip, changes={
        "basic": payslip.basic,
        "allowance": payslip.allowance,
        "deduction": payslip.deduction,
        "net_salary": payslip.net_salary,
    })
