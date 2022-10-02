import os
import json
import requests

#fhir server endpoint
FHIR_URL = "http://localhost:8080/fhir/"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

print("Start program.")
print(os.getcwd() + "/src/codesamples/fhir-data/synthea_sample_data_fhir_r4_sep2019/fhir")
print("Starting loop.")
for filename in os.listdir(os.getcwd() + "/src/codesamples/fhir-data/synthea_sample_data_fhir_r4_sep2019/fhir"):
    if filename.endswith(".json"):
        dir = os.getcwd() + "/src/codesamples/fhir-data/synthea_sample_data_fhir_r4_sep2019/fhir/"
        print(filename)
        with open(dir + filename, "r", encoding="utf8") as bundle_file:
            data = bundle_file.read()
        r = requests.post(url = FHIR_URL, data = data.encode('utf-8'), headers = headers)