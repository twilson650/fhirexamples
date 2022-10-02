from fhirclient import client
import fhirclient.models.patient as p

settings = {
    'app_id': 'local_docker_fhir',
    'api_base': 'http://localhost:8080/fhir'
}
smart = client.FHIRClient(settings=settings)


try:
    print("Hi there")
    patient = p.Patient.read('1', smart.server)
    print(patient.birthDate.isostring)
except Exception as e:
    print("FHIR Operation error: {0}".format(e))

