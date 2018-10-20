from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField,IntegerField
from wtforms import FileField
from wtforms.validators import Length,Email,EqualTo,DataRequired,ValidationError
from jobplus.models import User,Job,db,Company
from flask import flash

class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(3,24,message='用户名长度必须大于3小于24位数')])
    email = StringField('电子邮箱',validators=[DataRequired(),Email(message='email格式错误')])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24,message='密码长度必须大于6位小于24位')])
    repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo('password',message='重复密码必须与上一个密码相同')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return user


class LoginForm(FlaskForm):
    email = StringField('电子邮箱',validators=[DataRequired(),Email(message='Email格式错误')])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24,message='密码长度需大于6位小于24位')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('用户名未注册')

    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')



class UserProfileForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(3,24,message='用户名长度必须大于3小于24位数')])
    email = StringField('电子邮箱',validators=[DataRequired(),Email(message='email格式错误')])
    password = PasswordField('密码')
    phonenumber = StringField('手机号',validators=[Length(11,12,message='请输入11位长度手机号码')])
    work_experience = IntegerField('工作年限')
    upload_resume_url = StringField('个人简历URL地址')
     
    submit = SubmitField('提交')

    def __init__(self,id,**kw):
        super(UserProfileForm,self).__init__(**kw)
        self.id=id

    def validate_username(self,field):
        if User.query.filter(User.username == field.data,User.id != self.id).first():
            raise ValidationError('您修改的用户名称已存在')
    def validate_email(self,field):
        if User.query.filter(User.email == field.data,User.id != self.id).first():
            raise ValidationError('您修改的邮箱已注册')
    def validate_password(self,field):
        if field.data != ''and (len(str(field.data)) < 3 or len(str(field.data)) >24) :
            raise ValidationError('您修改的密码长度必须在3到23位之间')


    def Profile_update(self,user):
        if self.password.data == '':
            self.password.data = user.password
        self.populate_obj(user)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash('数据提交失败','success')
        return user

class CompanyProfileForm(FlaskForm):
    username = StringField('公司名称',validators=[DataRequired(),Length(2,54,message='公司名称长度必须大于2小于54位数')])
    email = StringField('电子邮箱',validators=[DataRequired(),Email(message='email格式错误')])
    password = PasswordField('密码')
    phonenumber = StringField('手机号',validators=[Length(11,12,message='请输入11位长度手机号码')])
    work_experience = IntegerField('工作年限')
    upload_resume_url = StringField('个人简历URL地址')
     
    submit = SubmitField('提交')

    def __init__(self,id,**kw):
        super(UserProfileForm,self).__init__(**kw)
        self.id=id

    def validate_username(self,field):
        if User.query.filter(User.username == field.data,User.id != self.id).first():
            raise ValidationError('您修改的用户名称已存在')
    def validate_email(self,field):
        if User.query.filter(User.email == field.data,User.id != self.id).first():
            raise ValidationError('您修改的邮箱已注册')
    def validate_password(self,field):
        if field.data != ''and (len(str(field.data)) < 3 or len(str(field.data)) >24) :
            raise ValidationError('您修改的密码长度必须在3到23位之间')


    def Profile_update(self,user):
        if self.password.data == '':
            self.password.data = user.password
        self.populate_obj(user)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash('数据提交失败','success')
        return user
