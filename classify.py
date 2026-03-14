# Import necessary libraries
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Dense, Dropout,
    GlobalAveragePooling2D, BatchNormalization
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os




# Dataset Paths
train_dir = 'train'  
test_dir = 'test'   


#  Data Preprocessing

# Training data generator with augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split = 0.2,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

# Test data generator (only rescaling)
test_datagen = ImageDataGenerator(rescale=1./255)

# Load datasets from directories
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=64,
    class_mode='binary',
    subset = "training"
)

val_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=64,
    class_mode='binary',
    subset='validation'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=64,
    class_mode='binary',
    shuffle=False
)

print("Class indices:", train_generator.class_indices)



#CNN Model

# model = Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
#     MaxPooling2D(2,2),
#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(2,2),
#     Conv2D(128, (3,3), activation='relu'),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dropout(0.5),
#     Dense(1, activation='sigmoid')  # Binary classification
# ])

model = Sequential([

    Conv2D(32, (3,3), activation='relu', padding='same',
           input_shape=(128,128,3)),
    BatchNormalization(),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu', padding='same'),
    BatchNormalization(),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu', padding='same'),
    BatchNormalization(),
    MaxPooling2D(2,2),

    GlobalAveragePooling2D(),

    Dense(128, activation='relu'),
    Dropout(0.5),

    Dense(1, activation='sigmoid')  # Binary output
])



model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.save('current_model_mid_training.h5')

checkpoint = ModelCheckpoint(
    'best_model.h5',       # filename to save best weights
    monitor='val_accuracy',    # metric to monitor
    save_best_only=True,   # save only if improved
    verbose=1
)

model.summary()


early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)


history = model.fit(
    train_generator,
    epochs=5,
    validation_data=test_generator,
    callbacks=[checkpoint,early_stop]
)

loss, accuracy = model.evaluate(test_generator)
print(f'Test Accuracy: {accuracy*100:.2f}%')


print("Dataset loaded and CNN model built successfully.")



# use multiple methodologies as discussed in the project ; CNN, deeplearnig, snapshot
# trying different datasets for different results
# option in interface to choose what model fot prediction
#  compare to existing models or porjects 
#  compare results and give reasons for variances and deviations
# Gradio for interface 
# database to store results and images