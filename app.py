import pickle
import numpy as np

import os
path = r"C:\Users\kesha\Desktop\New folder\diabetes.pkl"
assert os.path.isfile(path)
os.makedirs(os.path.dirname(path), exist_ok = True)
model = pickle.load(open(path, 'rb'))

print("Enter values for the following:\nTotal Pregnancies: \nGlucose levels: \nBlood Pressure: \nSkin Thickness: \nInsulin: \nBMI: \nDiabetes Pedigree Function: \nAge: ")

preg = float(input())
glucose = float(input())
bp = float(input())
st = float(input())
insulin = float(input())
bmi = float(input())
dpf = float(input())
age = float(input())

def predict(preg, glucose, bp, st, insulin, bmi, dpf, age):
		
		l = [preg, glucose, bp, st, insulin, bmi, dpf, age]
		l = np.asarray(l)
		l = np.reshape(l, (1,8))
		pred = model.predict(l)
		return pred[0]

	
value = predict(preg, glucose, bp, st, insulin, bmi, dpf, age)
if value == 1:
	print("Our evaluation system has discovered that you most likely have diabetes. We suggest you visit a doctor.")
else:
	print("Congratulations! You don't have diabetes.")

