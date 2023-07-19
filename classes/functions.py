from classes.private import atCredentials,apiCredentials,atCredentials_rompeflix,atCredentials_materials,atCredentials_sct
from classes.Airtable import Airtable
from classes.Rompetechos import RompetechosAPI

# Connect to Airtable > Componentización Playground
token,baseId = atCredentials()
at = Airtable(token,baseId)

# Connect to Airtable > Tech Business Suport
token_staff,baseId_staff = atCredentials_rompeflix()
at_staff = Airtable(token_staff,baseId_staff)

# Connect to Airtable > Maestro materiales & Partidas
token_material,baseId_material = atCredentials_materials()
at_materials = Airtable(token_material,baseId_material)

# Connect to Airtable > 011h Sistema Constructivo
token_sct,baseId_sct = atCredentials_sct()
at_sct = Airtable(token_sct,baseId_sct)

# Connect to Rompetechos > API
api_key,api_token = apiCredentials()
rt = RompetechosAPI(api_key,api_token)
#rt.regenToken()



# ----- EVOLUTION ----- #
def coloreEU(EU):
    text = EU.split('_')
    output = []
    for eu in text:
        site = eu[1:4]
        eu_name = eu[5:]
        if site == 'ono':
            eu_output = '<span class="eu-ono">'+eu_name+'</span>'
        elif site == 'onm':
            eu_output = '<span class="eu-onm">'+eu_name+'</span>'
        elif site == 'ofm':
            eu_output = '<span class="eu-ofm">'+eu_name+'</span>'
        elif site == 'ofo':
            eu_output = '<span class="eu-ofo">'+eu_name+'</span>'
        else:
            eu_output = '<span>'+eu_name+'</span>'
        output.append(eu_output)
        output_string = '_'.join(output)
    return output_string

def filter_projects(projects):
    info = {'2116. Casernes J': 'bg-yellow', '2201. Distrito Z': 'bg-green', '2301. Calonge': 'bg-orange'}
    output = {project: info[project] for project in projects if project in info}
    return output

def extract_cases_of_study(data):
    cases_of_study = list(data.keys())
    return cases_of_study

def extract_projects(data):
    info = {'2116. Casernes J': 'bg-yellow', '2201. Distrito Z': 'bg-green', '2301. Calonge': 'bg-orange'}
    projects = {}
    for case in data.keys():
        for project in data[case].keys():
            if project in info:
                projects[project] = info[project]
    return projects

def get_unique_components(data):
    output = {}
    for case, projects in data.items():
        unique_components = []
        for project, components in projects.items():
            for component in components:
                if component.code not in [comp.code for comp in unique_components]:
                    unique_components.append(component)
        output[case] = unique_components
    return output

def setCurrency(value):
    if value:
        output = '{:,.2f}'.format(float(value))
    else:
        output = '0,00'
    return output

def getStatus():
    list = rt.get()
    status = {item["code"]: item["status"] for item in list}
    return status
    
def componentStatus(component,allStatus):
    if component in allStatus:
        status = allStatus[component]
    else:
        status = '...'
    return status

class Header():
    def __init__(self,case,code,name,feature,blind_cost,status):
        self.case = case
        self.code = code
        self.name = name
        self.feature = feature
        self.blind_cost = blind_cost
        self.status = status
        
class Component:
    def __init__(self,case,project,code,name,feature,blind_cost,case_cost,rat_cost,img,status='Development'):
        self.case = case
        self.project = project
        self.code = code
        self.name = coloreEU(name)
        self.feature = feature
        self.blind_cost = setCurrency(blind_cost)
        self.case_cost = setCurrency(case_cost)
        self.rat_cost = setCurrency(rat_cost)
        self.img = img
        self.status = status

def getProperty(element,property,list=False):
    if property in element:
        if list:
            output = element[property][0]
        else:
            output = element[property]
    else:
        output = ''
    return output
    
def convert_json(json_data):
    statuses = getStatus() 
    records = json_data['records']
    result = {}

    for recordbase in records:
        record = recordbase['fields']
        case_type = getProperty(record,'Case_type_api')
        project = getProperty(record,'Project')
        code = getProperty(record,'Component_type_api')
        name = getProperty(record,'Component_name',True)
        feature = getProperty(record,'Main_feature',True)
        blind_cost = getProperty(record,'Blind_cost',True)
        case_cost = getProperty(record,'Case_cost')
        rat_cost = getProperty(record,'Rat_cost')
        img = getProperty(record,'Img')
        status = componentStatus(code,statuses) 

        component = Component(case_type,project,code,name,feature,blind_cost,case_cost,rat_cost,img,status)

        if case_type in result:
            if project in result[case_type]:
                result[case_type][project].append(component)
            else:
                result[case_type][project] = [component]
        else:
            result[case_type] = {project: [component]}

    return result

def sort_components(components):
    sorted_components = {}
    for case_type, projects in components.items():
        sorted_projects = {}
        for project, component_list in projects.items():
            sorted_components_list = sorted(component_list, key=lambda x: (x.case, x.project))
            sorted_projects[project] = sorted_components_list
        sorted_components[case_type] = sorted_projects
    return sorted_components

def getAT(filter=None):
    atlist = at.list('RL_Case-Component',filter=filter)
    return atlist

def evolution(filter):
    filtrat = "type='" + filter + "'"
    json_data = getAT(filtrat)
    components_notSorted = convert_json(json_data)
    components = sort_components(components_notSorted)

    cases = extract_cases_of_study(components)
    projects = extract_projects(components)
    headers = get_unique_components(components)
    
    return components,cases,projects,headers



# ----- SKU ----- #
def get011hTeam():
    list = at_staff.list('staff')
    names = []
    supply = []
    for element in list['records']:
        name = element['fields']['name']
        names.append(name)
        if element['fields']['team'] == 'Supply Chain':
            supply.append(name)
    return names,supply

def materialGroup():
    list = at_materials.list('Material-Group',view='Grid view')
    groups = []
    for element in list['records']:
        name = element['fields']['Group Long Name']
        groups.append(name)
    return groups

def insertSKUrequested(data):
    records = {
        "requested_by": data[0],
        "material_type": data[1],
        "material_project": data[2],
        "similar_to": data[3],
        "material_group": data[4],
        "material_description1": data[5],
        "material_unit": data[6],
        "main_material": data[7],
        "material_brand": data[8],
        "material_model": data[9],
        "material_information": data[10]
    }
    inserted = at_sct.insert('Supply SKU requests', records)
    if 'error' in inserted:
        output = 'error'
    else:
        output = inserted['fields']['SKU_temporal']
    return output        
    
def materialsList():
    list = at_sct.list('Supply SKU requests')
    if 'error' in list:
        output = 'error'
    elif 'records' not in list:
        output = []
    else:
        output = list['records']
    return output

def excelMaterials(json):
    output = []
    for element in json:
        record = element['fields']
        if record['status'] == 'Pending':
            sku = getProperty(record,'material_sku')
            sku_temporal = getProperty(record,'SKU_temporal')
            requested_by = getProperty(record,'requested_by')
            material_type = getProperty(record,'material_type')
            material_project = getProperty(record,'material_project')
            similar_to = getProperty(record,'similar_to')
            material_group = getProperty(record,'material_group')
            material_description1 = getProperty(record,'material_description1')
            material_unit = getProperty(record,'material_unit')
            main_material = getProperty(record,'main_material')
            material_brand = getProperty(record,'material_brand')
            material_model = getProperty(record,'material_model')
            material_information = getProperty(record,'material_information')
            output.append([sku,sku_temporal,requested_by,material_type,material_project,similar_to,material_group,material_description1,material_unit,main_material,material_brand,material_model,material_information])
    return output