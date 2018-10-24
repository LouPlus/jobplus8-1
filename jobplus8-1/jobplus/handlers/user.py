
from flask import Blueprint ,render_template,redirect,url_for,flash
from flask_login import login_user,login_required,current_user
from jobplus.models import db,User
from jobplus.forms import LoginForm,RegisterForm,UserProfileForm
from werkzeug import secure_filename
import os

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/')
def user_index():
    return render_template('user/index.html')


@user.route('/profile',methods=['GET','POST'])
@login_required
def user_profile():
    user = User.query.filter_by(id=current_user.id).first()
    form = UserProfileForm(obj=user,id=user.id)
    if form.validate_on_submit():
        file = form.upload_resume_file.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('jobplus/resume', filename))
            user.upload_resume_jobname = filename
            db.session.add(user)
            db.session.commit()
            print(filename)
        form.Profile_update(user)
        flash('您的个人资料修改成功！','success')
        return redirect(url_for('front.index'))
    return render_template('user/profile.html',form=form,user=user)
