from flask.ext.mail import Message
from flask import render_template
from app import mail
from config import ADMINS
from decorators import async
from flask.ext.babel import gettext

@async
def send_async_email(msg):
	mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	#thr = Thread(target=send_async_email, args = [msg])
	#thr.start()

def follower_notifications(followed, follower):
	send_email(gettext("[microblog] %s is now following you!" % follower.nickname, 
		ADMINS[0],
		[followed.email],
		render_template("follower_email.txt",
			user = followed, follower = follower),
		render_template("follower_email.html",
			user = followed, follower = follower)))