import os
import json
import requests

#fhir server endpoint
FHIR_URL = "http://localhost:8080/fhir/"

PATIENT_DATA_DIR = os.getcwd() + "/data/fhirpatients"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

print("Start program.")
print(PATIENT_DATA_DIR)
print("Starting loop.")
for filename in os.listdir(PATIENT_DATA_DIR"):
    if filename.endswith(".json"):
        print(filename)
        with open(PATIENT_DATA_DIR + filename, "r", encoding="utf8") as bundle_file:
            data = bundle_file.read()
        r = requests.post(url = FHIR_URL, data = data.encode('utf-8'), headers = headers)