from flask import Flask,request,render_template,redirect
import WanKeYunApi

app = Flask(__name__)
#绑定访问地址127.0.0.1:5000/user
@app.route("/",methods=['GET','POST'])
def login():
    if request.method =='POST':
        
        pin = request.form['pin']
        if pin != '9612':
            message = "incorrect pin!"
            return render_template('login.html',message=message)
        magnet = request.form['magnet']

        onething = WanKeYunApi.WanKeYunApi()
        bok = onething.LoginEx(user='17092619612',passwd='liming1996')
        if bok is False:
            return
        bok = onething.GetUSBInfo()
        if bok is False:
            return
        bok = onething.RemoteDlLogin()
        if bok is False:
            return
        bok = onething.GetRemoteDlInfo()
        if bok is False:
            return

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
