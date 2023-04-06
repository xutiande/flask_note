# 问答
from flask import Blueprint, request, render_template, g, redirect, url_for

from models import ArticlesModels
from exts import db
from ducorators import login_required  # 引用装饰器
from .forms import ArticlesForm
import datetime
bp = Blueprint('qa', __name__, url_prefix="/")



# 文章首页
@bp.route("/")
def index():
    return render_template('index.html')

#笔记
@bp.route("/add/note")
def add_note():
    articles=ArticlesModels.query.order_by(ArticlesModels.create_date.desc())#根据用户发布的时间，降序排序
    return render_template('add_note.html',article=articles)

# 添加笔记
@bp.route("/qa/note", methods=['GET', 'POST'])
@login_required  # 使用装饰器
def note_content():
    if request.method == 'GET':
        return render_template('note.html')
    else:
        form = ArticlesForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = ArticlesModels(title=title, content=content, author=g.user.username)  # 登录用户名绑定在g上
            db.session.add(question)
            db.session.commit()
            # todo:跳转到首页
            return redirect(url_for('qa.add_note'))
        else:
            print(form.errors)
            return redirect(url_for("qa.note_content"))

#删除笔记
@bp.route("/qa/del/<qa_id>")
def del_note(qa_id):
    articles=ArticlesModels.query.get(qa_id)
    db.session.delete(articles)
    db.session.commit()

    return redirect(url_for('qa.add_note'))


#修改笔记

@bp.route("/qa/revise/<qa_id>", methods=['GET', 'POST'])
@login_required  # 使用装饰器
def revise_note(qa_id):
    articles = ArticlesModels.query.get(qa_id)
    form = ArticlesForm(request.form)
    if form.validate():
        articles.title = form.title.data
        articles.content = form.content.data
        articles.create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        articles.question = ArticlesModels(title=articles.title, content=articles.content, author=g.user.username,create_date=articles.create_date)  # 登录用户名绑定在g上
        db.session.add(articles)
        db.session.commit()
        return redirect(url_for('qa.add_note'))
    return render_template('revise_note.html')


# 笔记详情页
@bp.route('/qa/detail/<qa_id>')
def qa_detail(qa_id):
    question = ArticlesModels.query.get(qa_id)
    # print(question.author.username)         author是QuestionModel中绑定Usermodel的变量
    return render_template('detail.html', question=question)




# 关于
@bp.route('/qa/about')
def about_note():
    return render_template('about.html')