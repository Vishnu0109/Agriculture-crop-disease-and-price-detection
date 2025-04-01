import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import os

# Define paths to your train and validation data
train_dir = "/Users/vishnu/Desktop/agri_project/datasets/raw/PlantVillage"  # Update this with actual path to the training images
val_dir = "/Users/vishnu/Desktop/agri_project/datasets/raw/PlantVillage"      # Update this with actual path to the validation images

# ImageDataGenerators for loading images
train_datagen = ImageDataGenerator(
    rescale=1./255, 
    horizontal_flip=True, 
    rotation_range=20,
    zoom_range=0.2
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Load pre-trained MobileNetV2 model (without the top layers)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model layers to avoid training them
base_model.trainable = False

# Build a custom classifier
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(16, activation='softmax')  # 16 classes (adjust if needed)
])

# Compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
history = model.fit(
    train_generator,
    epochs=20,
    validation_data=val_generator,
    callbacks=[early_stopping]
)

# Save the trained model
model_save_path = "/Users/vishnu/Desktop/agri_project/model/plant_disease_model.h5"  # Update this path to save the model
model.save(model_save_path)

print(f"Model Training Complete! Model saved at {model_save_path}")
