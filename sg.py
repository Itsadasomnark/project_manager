import shotgun_api3

sg = shotgun_api3.Shotgun("https://silpakorn.shotgunstudio.com", "testAPI", "dzqjkanmogumluq_wXakcwd2c")

# CRUD
# C = Create
# R = Read
# U = Update
# D = Delete 


filters = []
fields = ['sg_type', 'name', 'Asset']
project_entity = sg.find_one('ProjectTaskTemplateConnection', filters)
asset_filters = [['project', 'is', project_entity], ['sg_asset_type', 'is', 'Character']]
asset_field = ['sg_asset_type', 'code']
assets_entity =sg.find('Asset', asset_filters, asset_field)
template_entity = {'type': 'TaskTemplate', 'id': 31}
data = {'code': 'Shot5', 'project': project_entity, 'sg_cut_in': 1100, 'sg_cut_out': 1140 ,'task_template': template_entity, 'sg_cut_duration': 40}

project = sg.find_one("Project", [["name","is","Himmapan"]], fields)
project_data = {'name': 'test', 'layout_project': project}
#result = sg.create('Project', project_data)

##for asset in assets_entity:
#	print (asset)

#data = {'sg_asset_type': 'Character'}
#sg.update('Asset', 1412, data)
#project = sg.find("Project", [["id","is",122]])
print (project)