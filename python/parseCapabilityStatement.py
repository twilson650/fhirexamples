from fhirclient import client
import fhirclient.models.capabilitystatement as metadata

settings = {
    'app_id': 'local_docker_fhir',
    'api_base': 'http://localhost:8080/fhir'
}

smart = client.FHIRClient(settings=settings)

meta = smart.server.capabilityStatement
#softwareName = meta["software"]["name"]
print("Got capability statement")
print(type(meta))
rest = meta.rest
for restResource in rest:
    type(restResource)



