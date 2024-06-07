from django.contrib import admin
from .models import  cpu,cpucooler, memory, storage, motherboard, case, videocard, powersupply
from import_export.admin import ImportExportModelAdmin  
from product.resources import  cpuResource,cpucoolerResource, memoryResource, storageResource, motherboardResource, caseResource, videocardResource, powersupplyResource

# Register your models here.
class cpuAdmin(ImportExportModelAdmin):
    resource_class = cpuResource
admin.site.register(cpu, cpuAdmin)

class coolerAdmin(ImportExportModelAdmin):
    resource_class = cpucoolerResource
admin.site.register(cpucooler, coolerAdmin)

class memoryAdmin(ImportExportModelAdmin):
    resource_class = memoryResource
admin.site.register(memory, memoryAdmin)

class storageAdmin(ImportExportModelAdmin):
    resource_class = storageResource
admin.site.register(storage, storageAdmin)

class motherboardAdmin(ImportExportModelAdmin):
    resource_class = motherboardResource
admin.site.register(motherboard, motherboardAdmin)

class caseAdmin(ImportExportModelAdmin):
    resource_class = caseResource
admin.site.register(case, caseAdmin)

class videocardAdmin(ImportExportModelAdmin):
    resource_class = videocardResource
admin.site.register(videocard, videocardAdmin)

class powersupplyAdmin(ImportExportModelAdmin):
    resource_class = powersupplyResource
admin.site.register(powersupply, powersupplyAdmin)

