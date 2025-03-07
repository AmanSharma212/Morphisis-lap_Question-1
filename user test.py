from flask import Flask  
import datetime  
import subprocess  

app = Flask(__name__)  

@app.route('/htop')  
def htop():  
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()  
    output = f"""  
    Name: Your Full Name  
    Username: {subprocess.check_output(['whoami']).decode().strip()}  
    Server Time (IST): {datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)}  
    TOP output:  
    <pre>{top_output}</pre>  
    """  
    return output  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)  
