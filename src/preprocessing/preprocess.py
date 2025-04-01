import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1️⃣ Image Preprocessing for Crop Disease Detection
def preprocess_images():
    # Define directories for training and validation data
    raw_train_dir = '/Users/vishnu/Desktop/agri_project/datasets/raw/PlantVillage'  # Path to your training image folder
    raw_validation_dir = '/Users/vishnu/Desktop/agri_project/datasets/raw/PlantVillage'  # Path to your validation image folder

    # Image size and batch size
    img_size = (224, 224)
    batch_size = 32

    # Data Augmentation for training (for image data)
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    # Rescale validation images
    validation_datagen = ImageDataGenerator(rescale=1./255)

    # Prepare the training and validation data
    train_generator = train_datagen.flow_from_directory(
        raw_train_dir,  # Path to the training images
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical'  # Assuming multiple categories (diseases)
    )

    validation_generator = validation_datagen.flow_from_directory(
        raw_validation_dir,  # Path to the validation images
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical'
    )

    print("\nImage Preprocessing Done! Training and validation data ready.")
    return train_generator, validation_generator


# Main function to preprocess images
if __name__ == "__main__":
    # Preprocess image data for crop disease detection
    train_gen, val_gen = preprocess_images()