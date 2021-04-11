
from flask import Flask,request, url_for, redirect, render_template
#from werkzeug import secure_filename


app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

@app.route('/')
def main():
    return render_template("index.html")

#@app.route('/uploader', methods = ['GET', 'POST'])
#def upload_file():
#   if request.method == 'POST':
#      f = request.files['file']
#      f.save(secure_filename(f.filename))
#      return 'file uploaded successfully'

#@app.route('/predict',methods=['POST','GET'])
#def predict():
#    int_features=[int(x) for x in request.form.values()]
#    final=[np.array(int_features)]
#    print(int_features)
#    print(final)
#    prediction=model.predict_proba(final)
#    output='{0:.{1}f}'.format(prediction[0][1], 2)

#    if output>str(0.5):
#        return render_template('ff.html',pred='Your Forest is in Danger.\nPercentage of fire occuring is {}%'.format(float(output)*100),bhai="danger")
#    else:
#        return render_template('ff.html',pred='Your Forest is safe.\n Percentage of fire occuring is {}%'.format(float(output)*100),bhai="safe")

if __name__ == '__main__':
    app.run()