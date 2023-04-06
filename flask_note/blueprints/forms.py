from wtforms.validators import Email, Length, EqualTo, InputRequired
import wtforms
from models import UserModel,ArticlesModels


# Email依赖于email_validator包


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
    username = wtforms.StringField(validators=[Length(min=6, max=20, message="用户名错误!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="密码要保持一致！")])

    # 自定义验证
    # 1，验证邮箱是否已经被注册

    def validate_email(self, filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册!")

# 登录表单

class loginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=6,max=20,message='用户名格式错误!')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误!")])



# 文章验证
class ArticlesForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题格式错误!")])
    content = wtforms.StringField(validators=[Length(min=3, message="内容格式错误!")])

