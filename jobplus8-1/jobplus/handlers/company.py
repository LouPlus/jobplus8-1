from flask import Blueprint ,render_template,redirect,url_for,flash,request, current_app
from flask_login import login_user,login_required,current_user
from jobplus.models import db,Company,User
from jobplus.forms import CompanyProfileForm
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



@company.route('/profile',methods=['GET','POST'])
@company_required
def profile():
    form = CompanyProfileForm(obj=current_user.company,
                              username=current_user.username,
                              email=current_user.email,
                              id=current_user.id)
    if form.validate_on_submit():
        form.Company_update(user)
        flash('公司资料修改成功！','success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html',form=form)
