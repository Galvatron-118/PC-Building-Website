from import_export import resources 
from .models import *

class cpuResource(resources.ModelResource):
     class Meta:
         model = cpu

class cpucoolerResource(resources.ModelResource):
     class Meta:
         model = cpucooler

class motherboardResource(resources.ModelResource):
     class Meta:
         model = motherboard

class memoryResource(resources.ModelResource):
     class Meta:
         model = memory

class storageResource(resources.ModelResource):
     class Meta:
         model = storage

class videocardResource(resources.ModelResource):
     class Meta:
         model = videocard


class caseResource(resources.ModelResource):
     class Meta:
         model = case


class powersupplyResource(resources.ModelResource):
     class Meta:
         model = powersupply