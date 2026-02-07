import os

print("STEP 1: Fetching stock data")
os.system("python fetch_data.py")

print("STEP 2: Preprocessing data")
os.system("python preprocessing.py")

print("STEP 3: Training ML model")
os.system("python train_ML.py")

print("PIPELINE COMPLETED SUCCESSFULLY")

