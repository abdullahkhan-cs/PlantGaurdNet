import os
import numpy as np
from flask import Flask, render_template, request, redirect
from PIL import Image
import tensorflow.lite as tflite

app = Flask(__name__)

# Folders setup
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 38 Classes Labels
CLASSES = [
    'Apple Scab', 'Apple Black Rot', 'Apple Cedar Rust', 'Apple Healthy',
    'Blueberry Healthy', 'Cherry Powdery Mildew', 'Cherry Healthy',
    'Corn Gray Leaf Spot', 'Corn Common Rust', 'Corn Northern Leaf Blight', 'Corn Healthy',
    'Grape Black Rot', 'Grape Black Measles', 'Grape Leaf Blight', 'Grape Healthy',
    'Orange Huanglongbing (Citrus Greening)', 'Peach Bacterial Spot', 'Peach Healthy',
    'Pepper Bell Bacterial Spot', 'Pepper Bell Healthy', 'Potato Early Blight', 'Potato Late Blight', 'Potato Healthy',
    'Raspberry Healthy', 'Soybean Healthy', 'Squash Powdery Mildew', 'Strawberry Leaf Scorch', 'Strawberry Healthy',
    'Tomato Bacterial Spot', 'Tomato Early Blight', 'Tomato Late Blight', 'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot',
    'Tomato Spider Mites', 'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 'Tomato Mosaic Virus', 'Tomato Healthy'
]

# --- Path Fix ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Spelling "Guard" (u-a-r-d) as per your terminal output
MODEL_PATH = os.path.join(BASE_DIR, "PlantGuard_Mobile.tflite")

interpreter = None
try:
    if os.path.exists(MODEL_PATH):
        interpreter = tflite.Interpreter(model_path=MODEL_PATH)
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        print(f"✅ Success: Model Loaded from {MODEL_PATH}")
    else:
        # Agar file models folder ke andar hai
        MODEL_PATH_ALT = os.path.join(BASE_DIR, "models", "PlantGuard_Mobile.tflite")
        if os.path.exists(MODEL_PATH_ALT):
            interpreter = tflite.Interpreter(model_path=MODEL_PATH_ALT)
            interpreter.allocate_tensors()
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            print(f"✅ Success: Model Loaded from {MODEL_PATH_ALT}")
        else:
            print("❌ Error: PlantGuard_Mobile.tflite not found in main folder or models folder.")
except Exception as e:
    print(f"❌ Error during loading: {e}")
    interpreter = None

def predict_label(img_path):
    if interpreter is None:
        return "Model Error", 0
    
    img = Image.open(img_path).convert('RGB').resize((224, 224))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    prediction_index = np.argmax(output_data)
    confidence = float(output_data[prediction_index] * 100)
    
    # Show disease name even for low confidence (with warning flag)
    disease_name = CLASSES[prediction_index]
    is_low_confidence = confidence < 70
    
    return disease_name, round(confidence, 2), is_low_confidence

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle captured image from camera
        captured_data = request.form.get('captured_image')
        if captured_data:
            # Decode base64 image data
            import base64
            import io
            from PIL import Image
            
            header, encoded = captured_data.split(',', 1)
            data = base64.b64decode(encoded)
            img = Image.open(io.BytesIO(data))
            
            # Save to uploads folder
            filename = f"camera_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(file_path)
            
            label, score, is_low_confidence = predict_label(file_path)
            img_rel_path = f"static/uploads/{filename}"
            
            return render_template("result.html", 
                                 prediction=label, 
                                 confidence=score,
                                 low_confidence=is_low_confidence,
                                 img_path=img_rel_path)
        
        # Handle file upload
        if 'file' not in request.files: return redirect(request.url)
        file = request.files['file']
        if file.filename == '': return redirect(request.url)
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            label, score, is_low_confidence = predict_label(file_path)
            # Use correct static folder path
            img_rel_path = f"static/uploads/{filename}"
            
            return render_template("result.html", 
                                 prediction=label, 
                                 confidence=score,
                                 low_confidence=is_low_confidence,
                                 img_path=img_rel_path)
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)