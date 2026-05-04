<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# 📁 dataset path
DATASET_PATH = "dataset"

IMG_SIZE = (100, 100)
BATCH_SIZE = 32

# 🔄 data augmentation
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

# 📚 TRAIN DATA
train_data = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

# 📚 VALIDATION DATA
val_data = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

print("CLASS MAP:", train_data.class_indices)

# 🧠 MODEL
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(100,100,3)),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),

    layers.Dense(train_data.num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# 🚀 TRAIN
model.fit(
    train_data,
    validation_data=val_data,
    epochs=15
)

# 💾 SAVE MODEL
model.save("crop_model.h5")

=======
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# 📁 dataset path
DATASET_PATH = "dataset"

IMG_SIZE = (100, 100)
BATCH_SIZE = 32

# 🔄 data augmentation
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

# 📚 TRAIN DATA
train_data = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

# 📚 VALIDATION DATA
val_data = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

print("CLASS MAP:", train_data.class_indices)

# 🧠 MODEL
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(100,100,3)),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),

    layers.Dense(train_data.num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# 🚀 TRAIN
model.fit(
    train_data,
    validation_data=val_data,
    epochs=15
)

# 💾 SAVE MODEL
model.save("crop_model.h5")

>>>>>>> 0f1587fa1ba90820e521794a20efcdc7f93b8da8
print("✅ Model trained and saved as crop_model.h5")