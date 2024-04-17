from flask import Blueprint, render_template
from .permissions import role_required

main = Blueprint('main', __name__)


@main.route('/')
def index_View():
    return render_template("main_page_ds.html")


# hospital views

@main.route('/dashboard-h')
@role_required('hospital')
def hospital_dashboard_View():
    return render_template("dashboardH.html")

@main.route('/appointment-h')
@role_required('hospital')
def hospital_appointment_View():
    return render_template("appointmentsH.html")

@main.route('/records-h')
@role_required('hospital')
def hospital_records_View():
    return render_template("recordsH.html")

@main.route('/lens-h')
@role_required('hospital')
def hospital_lens_View():
    return render_template("lensH.html")


# patient views

@main.route('/dashboard-p')
@role_required('patient')
def patient_dashboard_View():
    return render_template("dashboardP.html")


@main.route('/appointment-p')
@role_required('patient')
def patient_appointment_View():
    return render_template("appointmentsP.html")

@main.route('/profile-p')
@role_required('patient')
def patient_profile_View():
    return render_template("profileP.html")