from flask import Blueprint ,render_template, request, current_app
from ..models import Job
#from jobplus.forms import LoginForm,RegisterForm

job = Blueprint('job',__name__,url_prefix='/job')
@job.route('/')
def job_index():
    page = request.args.get('page', default=1, type=int)

    pagination = Job.query.paginate(
        page = page,
        per_page = current_app.config['ADMIN_PER_PAGE'],
        error_out = False
    )
    return render_template('job/index.html', pagination = pagination)

@job.route('/detail/<int:id>')
def job_detail(id):
    return render_template('job/job_detail.html')
