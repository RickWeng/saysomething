from flask import flash, url_for, redirect, render_template
from saysomething import app, db
from saysomething.forms import SayForm
from saysomething.models import Message

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SayForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('You have said something.')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', messages=messages,form=form)


