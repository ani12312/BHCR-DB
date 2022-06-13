from flask import Flask,render_template,request,flash,url_for
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename
#from flask_restful import Resource, Api , reqparse , abort , fields , marshal_with
#from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'Uploads'
uploads_dir= os.path.join(APP_ROOT, UPLOAD_FOLD)
os.makedirs(uploads_dir,exist_ok=True)

@app.route('/',methods=['GET','POST'])

def home():
    prediction=0
    if request.method == 'POST':
        
        file = request.files['file']
        
        
        filename = secure_filename(file.filename)
        path=os.path.join('Uploads', filename)
        file.save(path)
        model = load_model("bhcr_model_3004_batch200_epo20_-6.h5")
        #user_input=request.form.get('myFile')
        #user_input.save(os.path.join(uploads_dir,))

        test_img = image.load_img(path, target_size = (224,224))
        test_img_arr = image.img_to_array(test_img)
        test_img_arr = np.expand_dims(test_img_arr, axis = 0)
        prediction = model.predict(test_img_arr)
        result = np.argmax(prediction, axis = 1)
        print(result)
        
        prediction=determine_character(result)
    
    return render_template('BHCR.html',prediction=prediction)
def determine_character(res):
    if res == 0:
        return("prediction : অ")
    elif res == 11:
        return("prediction : আ")
    elif res == 22:
        return("prediction : ই")
    elif res == 33:
        return("prediction : ঈ")
    elif res == 44:
        return("prediction : উ")
    elif res == 46 :
        return("prediction : ঊ")
    elif res == 47:
        return("prediction : ঋ")
    elif res == 48:
        return("prediction : এ")
    elif res == 49:
        return("prediction : ঐ")
    elif res == 1:
        return("prediction : ও")
    elif res == 2:
        return("prediction : ঔ")
    elif res == 3:
        return("prediction : ক")
    elif res == 4:
        return("prediction : খ")
    elif res == 5:
        return("prediction : গ")
    elif res == 6:
        return("prediction : ঘ")
    elif res == 7:
        return("prediction : ঙ")
    elif res == 8:
        return("prediction : চ")
    elif res == 9:
        return("prediction : ছ")
    elif res == 10:
        return("prediction : জ")
    elif res == 12:
        return("prediction : ঝ")
    elif res == 13:
        return("prediction : ঞ")
    elif res == 14:
        return("prediction : ট")
    elif res == 15:
        return("prediction : ঠ")
    elif res == 16:
        return("prediction : ড")
    elif res == 17:
        return("prediction : ঢ")
    elif res == 18:
        return("prediction : ণ")
    elif res == 19:
        return("prediction : ত")
    elif res == 20:
        return("prediction : থ")
    elif res == 21:
        return("prediction : দ")
    elif res == 23:
        return("prediction : ধ")
    elif res == 24:
        return("prediction : ন")
    elif res == 25:
        return("prediction : প")
    elif res == 26:
        return("prediction : ফ")
    elif res == 27:
        return("prediction : ব")
    elif res == 28:
        return("prediction : ভ")
    elif res == 29:
        return("prediction : ম")
    elif res == 30:
        return("prediction : য")
    elif res == 31:
        return("prediction : র")
    elif res == 32:
        return("prediction : ল")
    elif res == 34:
        return("prediction : শ")
    elif res == 35:
        return("prediction : ষ")
    elif res == 36:
        return("prediction : স")
    elif res == 37:
        return("prediction : হ")
    elif res == 38:
        return("prediction : ড়")
    elif res == 39:
        return("prediction : ঢ়")
    elif res == 40:
        return("prediction : য়")
    elif res == 41:
        return("prediction : ৎ")
    elif res == 42:
        return("prediction : ং")
    elif res == 43:
        return("prediction : ঃ")
    elif res == 45:
        return("prediction : ঁ")
if __name__ == '__main__':
    app.run(debug=True)