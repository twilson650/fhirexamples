from pprint import pprint

from fhirclient import client
import fhirclient.models.capabilitystatement as metadata



resourcesOfInterest = [
    'AdverseEvent',
    'AllergyIntolerance',
    'Bundle',
    'CarePlan',
    'CareTeam'
]

otherResourcees = [
    'AdverseEvent',
    'AllergyIntolerance',
    'Bundle',
    'CarePlan',
    'CareTeam',
    'ChargeItem',
    'ChargeItemDefinition',
    'Claim',
    'ClaimResponse',
    'ClinicalImpression',
    'CodeSystem',
    'Communication',
    'CommunicationRequest',
    'Condition',
    'Encounter',
    'EpisodeOfCare',
    'Goal',
    'ImagingStudy',
    'Immunization',
    'InsurancePlan',
    'Medication',
    'MedicationAdministration',
    'MedicationDispense',
    'MedicationRequest',
    'Observation',
    'Patient',
    'Practitioner',
    'PractitionerRole',
    'Procedure',
    'RelatedPerson',
    'RiskAssessment',
    'ValueSet'
]


settings = {
    'app_id': 'local_docker_fhir',
    'api_base': 'http://localhost:8080/fhir'
}

smart = client.FHIRClient(settings=settings)

meta = smart.server.capabilityStatement
# "meta" is the capability statement. First let's 
# get some basic information about this FHIR server
softwareName = meta.software.name
fhirVersion = meta.fhirVersion
formats = meta.format


#rest operations 
rest = meta.rest[0]
#pprint(rest)
for restResource in rest.resource:
    #pprint(restResource)
    if (restResource.type in resourcesOfInterest):
        pprint('RESOURCE ' + restResource.type)
        interactionList = restResource.interaction
        operationList = restResource.operation
        searchParameters = restResource.searchParam
        supportedProfile = restResource.supportedProfile
        #pprint('INTERACTIONS')
        #for interaction in interactionList:
        #    pprint(interaction.code)
        #pprint('OPERATIONS')
        #for operation in operationList:
        #    pprint(operation.name)
        pprint('SEARCH PARAMS')
        for searchParam in searchParameters:
            pprint(searchParam.name)





