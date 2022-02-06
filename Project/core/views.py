from flask import render_template,url_for,Blueprint,redirect,request
from Project.core.forms import FeedbackForm
from Project.users.forms import ChangePassword
from Project.models import Feedback,admin
from Project import db

core = Blueprint('core',__name__)

@core.route('/')
def index():
    try: 
        feedback = Feedback.query.all()
        first_feedback = feedback[0]
    except:
        return render_template('index.html',feedback=False)
    feedback = feedback[1:]
    if(len(feedback) > 2):
        feedback = feedback[:2]
    return render_template('index.html',feedback=True,feedbacks=feedback,first=first_feedback)

# route for our products tab
@core.route('/products')
def products():
    return render_template('/core/products.html')


# route for pricing tab 
@core.route('/pricing')
def pricing():
    return render_template('/core/pricing.html')

# route for contactus tab 
@core.route('/contactus',methods=['GET','POST'])
def contactus():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(form.name.data,form.email.data,form.comment.data)
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for('core.contactus'))
    return render_template('/core/contactus.html',form=form)
