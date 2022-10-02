from fhirclient import client
import fhirclient.models.patient as p

settings = {
    'app_id': 'e55e8eec6-9df3-4c3a-a410-7720bc5a96ed',
    'app_secret': '',
    'api_base': 'https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4/'
}
smart = client.FHIRClient(settings=settings)


try:
    print("Hi there")
    patient = p.Patient.read('erXuFYUfucBZaryVksYEcMg3', smart.server)
    print(patient.birthDate.isostring)
except Exception as e:
    print("FHIR Operation error: {0}".format(e))

