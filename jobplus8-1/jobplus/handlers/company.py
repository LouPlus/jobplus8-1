from flask import Blueprint ,render_template,redirect,url_for,flash,request, current_app
from flask_login import login_user,login_required,current_user
from jobplus.models import db,Company,User,Job,Delivery
from jobplus.forms import CompanyProfileForm,Add_Job_Form
from jobplus.decorators import company_required

company = Blueprint('company',__name__,url_prefix='/company')


@company.route('/')
def company_index():
    page = request.args.get('page', default=1, type=int)
    pagination = Company.query.paginate(
        page=page,
        per_page = current_app.config['COMPANY_PER_PAGE'],
        error_out = False
    )
    return render_template('company/index.html', pagination=pagination)

@company.route('/<int:id>')
def company_detail(id):
    company = Company.query.get_or_404(id)
    return render_template('company/company_detail.html', company=company, panel = 'about')

@company.route('/<int:id>/jobs')
def company_jobs(id):
    company = Company.query.get_or_404(id)
    return render_template('company/company_detail.html', company=company, panel = 'job')

@company.route('/profile',methods=['GET','POST'])
@company_required
def profile():
    user = User.query.filter_by(id=current_user.id).first()
    form = CompanyProfileForm(obj=current_user.company,
                              username=current_user.username,
                              email=current_user.email,
                              id=current_user.id)
    if form.validate_on_submit():
        form.Company_update(user)
        flash('公司资料修改成功！','success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html',form=form)

@company.route('/<int:id>/admin')
@company_required
def manage(id):
    return render_template('company/manage.html')


@company.route('/<int:id>/admin/jobs')
@company_required
def manage_jobs(id):
    page = request.args.get('page', default=1, type=int)
    job_id = request.args.get('job_id', default=None ,type=int)
    action = request.args.get('action', default=None )
    delete = request.args.get('delete', default=False)
    if delete:
        job = Job.query.filter_by(id = job_id).first()
        db.session.delete(job)
        db.session.commit()

    if job_id and not delete:
        job = Job.query.filter_by(id = job_id).first()
        if action == 'open':
            job.is_open = True
        else:
            job.is_open = False
        db.session.add(job)
        db.session.commit()
        job = Job.query.filter_by(id = job_id).first()

    company_id = User.query.filter_by(id = id).first().companys.id
    pagination = Job.query.filter_by(company_id = company_id).paginate(
        page=page,
        per_page = current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('company/manage_jobs.html', pagination = pagination)

@company.route('/<int:id>/admin/edit_job/<int:job_id>', methods = ['GET','POST'])
@company_required
def edit_job(id,job_id):
    job = Job.query.get_or_404(job_id)
    form = Add_Job_Form(obj = job)
    if form.validate_on_submit():
        form.update_job(job)
        return redirect(url_for('.manage_jobs', id=id))
    return render_template('company/edit_job.html', form = form )

@company.route('/<int:id>/admin/add_job', methods = ['GET','POST'])
@company_required
def add_job(id):
    form = Add_Job_Form()
    if form.validate_on_submit():
        form.create_job(id)
        return redirect(url_for('.manage_jobs',id = id))
    return render_template('company/add_job.html', form=form)

@company.route('/<int:id>/admin/manage_resumes', methods = ['GET','POST'])
@company_required
def manage_resumes(id):
    page = request.args.get('page',default=1,type=int)
    response = request.args.get('response', default=None)
    if response:
        del_id = request.args.get('del_id', default=None, type=int)
        delivery = Delivery.query.get_or_404(del_id)
        delivery.response = response
        db.session.add(delivery)
        db.session.commit()

    company_id = User.query.filter_by(id = id).first().companys.id
    pagination = Delivery.query.filter_by(company_id  = company_id).paginate(
        page = page,
        per_page = current_app.config['ADMIN_PER_PAGE'],
        error_out = False
    )
    return render_template('company/manage_resumes.html',pagination = pagination)

