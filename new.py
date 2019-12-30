from flask import Flask, request, url_for, redirect, flash, render_template
import WanKeYunApi

app = Flask(__name__)

app.secret_key = '123456'

@app.route("/",methods=['GET','POST'])
def login():
    if request.method =='POST':
        
        pin = request.form['pin']
        if pin != '设置你的pin':
            flash('incorrect pin!')
            return redirect(url_for('login'))
        magnet = request.form['magnet']

        onething = WanKeYunApi.WanKeYunApi()
        bok = onething.LoginEx(user='你的用户名',passwd='你的密码')
        if bok is False:
            flash('login failed!')
            return redirect(url_for('login'))
        bok = onething.GetUSBInfo()
        if bok is False:
            flash('get usb error!')
            return redirect(url_for('login'))
        bok = onething.RemoteDlLogin()
        if bok is False:
            flash('dl login failed!')
            return redirect(url_for('login'))
        bok = onething.GetRemoteDlInfo()
        if bok is False:
            flash('get dl info failed!')
            return redirect(url_for('login'))

        JobList = []
        OneJob = {
            "filesize": 0,
            "name": ' ',
            "url" : magnet,
        }
        
        JobList.append(OneJob)

        onething.AddDownloadTasks(JobList)
        # --------------------------------------------------------------------------------
        message = "done!"
        return render_template('login.html',message=message)

    return render_template('login.html')
 
if __name__ == '__main__':
    app.run(debug=True)
