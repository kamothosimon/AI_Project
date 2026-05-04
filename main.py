<<<<<<< HEAD
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

# 🚀 INIT APP
app = FastAPI()

# 🌐 CORS (allow mobile app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🤖 LOAD MODEL
model = load_model("crop_model.h5")

# ⚠️ MUST MATCH TRAINING ORDER
class_labels = ["beans_fit", "kunde_fit"]

IMG_SIZE = (100, 100)


# 🧠 PREPROCESS IMAGE
def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image).astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# 🧠 MARKET LOGIC (NEW IMPROVEMENT)
def get_market_status(label, confidence):
    if confidence < 0.6:
        return "Uncertain - Retake Image"

    if "fit" in label:
        return "Fit for Market"
    else:
        return "Not Fit for Market"


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # 📥 Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # 🔄 preprocess
        processed = preprocess_image(image)

        # 🤖 prediction
        predictions = model.predict(processed)[0]

        index = int(np.argmax(predictions))
        confidence = float(predictions[index])
        label = class_labels[index]

        # 🚨 CONFIDENCE THRESHOLD (KEY FIX)
        THRESHOLD = 0.75

        if confidence < THRESHOLD:
            return {
                "label": "unknown",
                "display": "Product Not Recognized",
                "confidence": confidence,
                "market_status": "Try again with clearer image"
            }

        # 🎯 display mapping
        display_map = {
            "beans_fit": "Beans",
            "kunde_fit": "Kunde"
        }

        display = display_map.get(label, "Unknown")

        # 📊 market logic
        if label == "beans_fit" or label == "kunde_fit":
            market_status = "Fit for Market"
        else:
            market_status = "Not Fit for Market"

        return {
            "label": label,
            "display": display,
            "confidence": confidence,
            "market_status": market_status
        }

    except Exception as e:
        return {
            "error": str(e)
=======
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

# 🚀 INIT APP
app = FastAPI()

# 🌐 CORS (allow mobile app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🤖 LOAD MODEL
model = load_model("crop_model.h5")

# ⚠️ MUST MATCH TRAINING ORDER
class_labels = ["beans_fit", "kunde_fit"]

IMG_SIZE = (100, 100)


# 🧠 PREPROCESS IMAGE
def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image).astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# 🧠 MARKET LOGIC (NEW IMPROVEMENT)
def get_market_status(label, confidence):
    if confidence < 0.6:
        return "Uncertain - Retake Image"

    if "fit" in label:
        return "Fit for Market"
    else:
        return "Not Fit for Market"


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # 📥 Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # 🔄 preprocess
        processed = preprocess_image(image)

        # 🤖 prediction
        predictions = model.predict(processed)[0]

        index = int(np.argmax(predictions))
        confidence = float(predictions[index])
        label = class_labels[index]

        # 🚨 CONFIDENCE THRESHOLD (KEY FIX)
        THRESHOLD = 0.75

        if confidence < THRESHOLD:
            return {
                "label": "unknown",
                "display": "Product Not Recognized",
                "confidence": confidence,
                "market_status": "Try again with clearer image"
            }

        # 🎯 display mapping
        display_map = {
            "beans_fit": "Beans",
            "kunde_fit": "Kunde"
        }

        display = display_map.get(label, "Unknown")

        # 📊 market logic
        if label == "beans_fit" or label == "kunde_fit":
            market_status = "Fit for Market"
        else:
            market_status = "Not Fit for Market"

        return {
            "label": label,
            "display": display,
            "confidence": confidence,
            "market_status": market_status
        }

    except Exception as e:
        return {
            "error": str(e)
>>>>>>> 0f1587fa1ba90820e521794a20efcdc7f93b8da8
        }