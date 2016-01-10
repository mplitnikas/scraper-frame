from flask import render_template
from app import app

import subprocess


@app.route('/')
@app.route('/index')
def index():
	title = "Home"
	return render_template('index.html', title=title)

@app.route('/restart')		# todo - should this be accessible as such?
def restart():
	cmd = 'sudo shutdown -r 10'.split()
	subprocess.Popen(cmd)
	return "Restarting in 10 seconds..."

@app.route('/shutdown')
def shutdown():
	cmd = 'sudo shutdown -h 10'.split()
	subprocess.Popen(cmd)
	return "Shutting down in 10 seconds..."

@app.route('/restart_slideshow')
def restart_slideshow():
	cmd = 'bash ./bash/restart_slides.sh' # todo - make this not hardcoded
	cmd = cmd.split()
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
							stderr = subprocess.PIPE,
							stdin = subprocess.PIPE)
	out, err = p.communicate()
	return "Did it!" # todo - redirect back to home

