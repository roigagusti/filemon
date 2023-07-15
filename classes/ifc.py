import ifcopenshell
import ifcopenshell.util.element
import pandas as pd
import openpyxl


class PartialSegment:
    def __init__(self, guid: str, element: dict):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_TypeID = getIFCinfo(element, "EI_Elements Identification", "EI_TypeID")
        self.EI_TypeName = getIFCinfo(element, "EI_Elements Identification", "EI_TypeName")
        self.EI_Description = getIFCinfo(element, "EI_Elements Identification", "EI_Description")
        self.EI_InstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_InstanceID")

class Component:
    def __init__(self, guid, element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_TypeID = getIFCinfo(element, "EI_Elements Identification", "EI_TypeID")
        self.EI_TypeName = getIFCinfo(element, "EI_Elements Identification", "EI_TypeName")
        self.EI_Description = getIFCinfo(element, "EI_Elements Identification", "EI_Description")
        self.EI_InstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_InstanceID")
        self.EI_LocalisationCodeFloor = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeFloor")
        self.EI_ShortID = getIFCinfo(element, "EI_Elements Identification", "EI_ShortID")
        self.QU_Height_m = getIFCinfo(element, "QU_Quantity", "QU_Height_m")
        self.QU_Length_m = getIFCinfo(element, "QU_Quantity", "QU_Length_m")
        self.QU_Thickness_m = getIFCinfo(element, "QU_Quantity", "QU_Thickness_m")
        self.QU_Volume_m3 = getIFCinfo(element, "QU_Quantity", "QU_Volume_m3")
        self.ST_LowerElasticBand = getIFCinfo(element, "ST_Structure Specification", "ST_LowerElasticBand")
        self.ST_StructuralLG_SKU = getIFCinfo(element, "ST_Structure Specification", "ST_StructuralLG_SKU")
        self.ST_StructuralLG_Width_m = getIFCinfo(element, "ST_Structure Specification", "ST_StructuralLG_Width_m")
        self.ST_TopElasticBand = getIFCinfo(element, "ST_Structure Specification", "ST_TopElasticBand")
        
class ExecutionUnit:
    def __init__(self, guid, element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_TypeID = getIFCinfo(element, "EI_Elements Identification", "EI_TypeID")
        self.EI_TypeName = getIFCinfo(element, "EI_Elements Identification", "EI_TypeName")
        self.EI_Description = getIFCinfo(element, "EI_Elements Identification", "EI_Description")
        self.EI_InstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_InstanceID")
        self.EI_LocalisationCodeFloor = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeFloor")
        self.EI_ShortID = getIFCinfo(element, "EI_Elements Identification", "EI_ShortID")
        self.EI_011hClassCode = getIFCinfo(element, "EI_Elements Identification", "EI_011hClassCode")
        self.EI_HostComponentInstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentInstanceID")
        self.EI_HostComponentType = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentType")
        self.QU_Height_m = getIFCinfo(element, "QU_Quantity", "QU_Height_m")
        self.QU_Length_m = getIFCinfo(element, "QU_Quantity", "QU_Length_m")
        self.QU_Thickness_m = getIFCinfo(element, "QU_Quantity", "QU_Thickness_m")
        self.QU_Volume_m3 = getIFCinfo(element, "QU_Quantity", "QU_Volume_m3")
        self.QU_Area_m2 = getIFCinfo(element, "QU_Quantity", "QU_Area_m2")
        self.QU_GrossArea_m2 = getIFCinfo(element, "QU_Quantity", "QU_GrossArea_m2")
        
class LayerGroup:
    def __init__(self, guid, element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_TypeID = getIFCinfo(element, "EI_Elements Identification", "EI_TypeID")
        self.EI_TypeName = getIFCinfo(element, "EI_Elements Identification", "EI_TypeName")
        self.EI_Description = getIFCinfo(element, "EI_Elements Identification", "EI_Description")
        self.EI_InstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_InstanceID")
        self.EI_HostComponentInstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentInstanceID")
        self.EI_HostComponentType = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentType")
        self.EI_HostEUInstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_HostEUInstanceID")
        self.EI_HostEUType = getIFCinfo(element, "EI_Elements Identification", "EI_HostEUType")
        self.EI_LocalisationCodeFloor = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeFloor")
        self.EI_ShortID = getIFCinfo(element, "EI_Elements Identification", "EI_ShortID")
        self.MS_ApplicationParameter = getIFCinfo(element, "MS_Manufacturing Specification", "MS_ApplicationParameter")
        self.QU_Area_m2 = getIFCinfo(element, "QU_Quantity", "QU_Area_m2")
        self.QU_GrossArea_m2 = getIFCinfo(element, "QU_Quantity", "QU_GrossArea_m2")
        self.QU_Height_m = getIFCinfo(element, "QU_Quantity", "QU_Height_m")
        self.QU_Length_m = getIFCinfo(element, "QU_Quantity", "QU_Length_m")
        self.QU_Thickness_m = getIFCinfo(element, "QU_Quantity", "QU_Thickness_m")
        self.QU_Volume_m3 = getIFCinfo(element, "QU_Quantity", "QU_Volume_m3")

class Box:
    def __init__(self, guid, element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.JS_JointTypeID = getIFCinfo(element, "JS_Joint Specification", "JS_JointTypeID")
        self.JS_ParentJointInstanceID = getIFCinfo(element, "JS_Joint Specification", "JS_ParentJointInstanceID")
        self.QU_Length_m = getIFCinfo(element, "QU_Quantity", "QU_Length_m")

class Joint:
    def __init__(self, typeID, parentID, length):
        self.EI_Type = "Joint"
        self.JS_JointTypeID = typeID
        self.JS_ParentJointInstanceID = parentID
        if isinstance(length, (int, float)):
            self.QU_Length_m = length
        else:
            self.QU_Length_m = 0
         
class Connection:
    def __init__(self,guid,element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_Description = getIFCinfo(element, "EI_Elements Identification", "EI_Description")
        self.EI_LocalisationCodeFloor = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeFloor")
        self.JS_ConnectionTypeID = getIFCinfo(element, "JS_Joint Specification", "JS_ConnectionTypeID")
        self.JS_ParentJointInstanceID = getIFCinfo(element, "JS_Joint Specification", "JS_ParentJointInstanceID")
        
class RelatedMaterial:
    def __init__(self,rmgroup,sku,position,description,performance,calculationFormula,isOnsite,phase=None,units=None):
        self.rmgroup = rmgroup
        self.sku = sku
        self.position = position
        self.description = description
        self.performance = performance
        self.calculationFormula = calculationFormula
        self.isOnsite = isOnsite
        self.phase = phase
        self.units = units
                 
class JointRelatedMaterial(RelatedMaterial):
    def __init__(self,jointType,parentJoint,length,rmgroup,sku,position,description,performance,calculationFormula,isOnsite,phase=None,quantity=None,units=None):
        super().__init__(rmgroup,sku,position,description,performance,calculationFormula,isOnsite,phase,units)
        self.jointType = jointType
        self.parentJoint = parentJoint
        self.length = length
        self.quantity = quantity        
        
class ConnectionRelatedMaterial(RelatedMaterial):
    def __init__(self,connectionType,parentJoint,rmgroup,sku,position,description,performance,calculationFormula,isOnsite,phase=None,units=None):
        super().__init__(rmgroup,sku,position,description,performance,calculationFormula,isOnsite,phase,units)
        self.connectionType = connectionType
        self.parentJoint = parentJoint

class Opening:
    def __init__(self, guid, element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_LocalisationCodeArea = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeArea")
        self.EI_LocalistaionCodeRoom = getIFCinfo(element, "EI_Elements Identification", "EI_LocalistaionCodeRoom")
        self.EI_LocalisationCodeFloor = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeFloor")
        self.EI_OpeningType = getIFCinfo(element, "EI_Elements Identification", "EI_OpeningType")
        self.EI_SKUNumber = getIFCinfo(element, "EI_Elements Identification", "EI_SKUNumber")
        self.EI_011hClassCode = getIFCinfo(element, "EI_Elements Identification", "EI_011hClassCode")
        self.EI_HostComponentInstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentInstanceID")
        self.EI_HostComponentType = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentType")
        self.MS_ApplicationParameter = getIFCinfo(element, "MS_Manufacturing Specification", "MS_ApplicationParameter")
        self.QU_Height_m = getIFCinfo(element, "QU_Quantity", "QU_Height_m")
        self.QU_CostCode011h = getIFCinfo(element, "QU_Quantity", "QU_CostCode011h")
        self.QU_Thickness_m = getIFCinfo(element, "QU_Quantity", "QU_Thickness_m")
        self.QU_PassArea_m2 = getIFCinfo(element, "QU_Quantity", "QU_PassArea_m2")
        self.QU_PassHeight_m = getIFCinfo(element, "QU_Quantity", "QU_PassHeight_m")
        self.QU_PassWidth_m = getIFCinfo(element, "QU_Quantity", "QU_PassWidth_m")
        self.QU_Area_m2 = getIFCinfo(element, "QU_Quantity", "QU_Area_m2")
        self.QU_Weight_kg = getIFCinfo(element, "QU_Quantity", "QU_Weight_kg")
        self.QU_Width_m = getIFCinfo(element, "QU_Quantity", "QU_Width_m")
        
class MEPBox:
    def __init__(self, guid, element):
        self.Guid = guid
        self.EI_Type = getIFCinfo(element, "EI_Elements Identification", "EI_Type")
        self.EI_LocalisationCodeArea = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeArea")
        self.EI_LocalistaionCodeRoom = getIFCinfo(element, "EI_Elements Identification", "EI_LocalistaionCodeRoom")
        self.EI_LocalisationCodeFloor = getIFCinfo(element, "EI_Elements Identification", "EI_LocalisationCodeFloor")
        self.EI_OpeningType = getIFCinfo(element, "EI_Elements Identification", "EI_OpeningType")
        self.EI_SKUNumber = getIFCinfo(element, "EI_Elements Identification", "EI_SKUNumber")
        self.EI_011hClassCode = getIFCinfo(element, "EI_Elements Identification", "EI_011hClassCode")
        self.EI_HostComponentInstanceID = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentInstanceID")
        self.EI_HostComponentType = getIFCinfo(element, "EI_Elements Identification", "EI_HostComponentType")
        self.MS_ApplicationParameter = getIFCinfo(element, "MS_Manufacturing Specification", "MS_ApplicationParameter")
        self.QU_Height_m = getIFCinfo(element, "QU_Quantity", "QU_Height_m")
        self.QU_Area_m2 = getIFCinfo(element, "QU_Quantity", "QU_Area_m2")
        self.QU_Weight_kg = getIFCinfo(element, "QU_Quantity", "QU_Weight_kg")
        self.QU_Width_m = getIFCinfo(element, "QU_Quantity", "QU_Width_m")
        self.QU_Thickness_m = getIFCinfo(element, "QU_Quantity", "QU_Thickness_m")

def getIFGguid(element: dict):
    return element.get_info().get('GlobalId', '')

def getIFCinfo(psets: dict, group: str, param: str):
    if group in psets and param in psets[group]:
        output = psets[group][param]
    else:
        output = ""
    return output

def getType(psets):
    try:
        type = psets["EI_Elements Identification"]["EI_Type"]
    except:
        type = ""
    return type
    
def getElements(ifc_file,EI_Type,dataframe=False):
    elementTypes = {
        "Component": 'IfcColumn',
        "component": 'IfcColumn',
        "ExecutionUnit": 'IfcWall',
        "LayerGroup": 'IfcWall',
        "Opening": 'IfcWindow',
        "MEPBox": 'IfcBuildingElementProxy',
        "ComponentJoint": 'IfcBuildingElementProxy',
        "Joint": 'IfcBuildingElementProxy',
        "Connection": 'IfcBuildingElementProxy',
        "PartialSegment": 'IfcWall'
    }
    headers = {
        "Component": ['Guid', 'EI_Type', 'EI_TypeID', 'EI_TypeName', 'EI_Description', 'EI_InstanceID', 'EI_LocalisationCodeFloor', 'EI_ShortID', 'QU_Height_m', 'QU_Length_m', 'QU_Thickness_m', 'QU_Volume_m3', 'ST_LowerElasticBand', 'ST_StructuralLG_SKU', 'ST_StructuralLG_Width_m', 'ST_TopElasticBand'],
        "component": ['Guid', 'EI_Type', 'EI_TypeID', 'EI_TypeName', 'EI_Description', 'EI_InstanceID', 'EI_LocalisationCodeFloor', 'EI_ShortID', 'QU_Height_m', 'QU_Length_m', 'QU_Thickness_m', 'QU_Volume_m3', 'ST_LowerElasticBand', 'ST_StructuralLG_SKU', 'ST_StructuralLG_Width_m', 'ST_TopElasticBand'],
        "ExecutionUnit": ['Guid', 'EI_Type', 'EI_TypeID', 'EI_TypeName', 'EI_Description', 'EI_InstanceID', 'EI_LocalisationCodeFloor', 'EI_ShortID', 'EI_011hClassCode', 'EI_HostComponentInstanceID', 'EI_HostComponentType', 'QU_Height_m', 'QU_Length_m', 'QU_Thickness_m', 'QU_Volume_m3', 'QU_Area_m2', 'QU_GrossArea_m2'],
        "LayerGroup": ['Guid','EI_Type','EI_TypeID','EI_TypeName','EI_Description','EI_InstanceID','EI_HostComponentInstanceID','EI_HostComponentType','EI_HostEUInstanceID','EI_HostEUType','EI_LocalisationCodeFloor','EI_ShortID','MS_ApplicationParameter','QU_Area_m2','QU_GrossArea_m2','QU_Height_m','QU_Length_m','QU_Thickness_m','QU_Volume_m3'],
        "Opening": ['Guid', 'EI_Type', 'EI_LocalisationCodeArea', 'EI_LocalistaionCodeRoom', 'EI_LocalisationCodeFloor', 'EI_OpeningType', 'EI_SKUNumber', 'EI_011hClassCode', 'EI_HostComponentInstanceID', 'EI_HostComponentType', 'MS_ApplicationParameter', 'QU_Height_m', 'QU_CostCode011h', 'QU_Thickness_m', 'QU_PassArea_m2', 'QU_PassHeight_m', 'QU_PassWidth_m', 'QU_Area_m2', 'QU_Weight_kg', 'QU_Width_m'],
        "MEPBox": ['Guid', 'EI_Type', 'EI_LocalisationCodeArea', 'EI_LocalistaionCodeRoom', 'EI_LocalisationCodeFloor', 'EI_OpeningType', 'EI_SKUNumber', 'EI_011hClassCode', 'EI_HostComponentInstanceID', 'EI_HostComponentType', 'MS_ApplicationParameter', 'QU_Height_m', 'QU_Area_m2', 'QU_Weight_kg', 'QU_Width_m', 'QU_Thickness_m'],
        "ComponentJoint": ['Guid','EI_Type','JS_JointTypeID','JS_ParentJointInstanceID','QU_Length_m'],
        "Joint": ['Guid','EI_Type','JS_JointTypeID','JS_ParentJointInstanceID','QU_Length_m'],
        "Connection": ['Guid','EI_Type','EI_Description','EI_LocalisationCodeFloor','JS_ConnectionTypeID','JS_ParentJointInstanceID'],
        "PartialSegment": ['Guid','EI_Type','EI_TypeID','EI_TypeName','EI_Description','EI_InstanceID']
    }
    entityGroup = []
    elements = ifc_file.by_type(elementTypes[EI_Type])
    for element in elements:
        guid = getIFGguid(element)
        psets = ifcopenshell.util.element.get_psets(element)
        type = getType(psets)
        if type == "Component" == EI_Type:
            elementClass = Component(guid,psets)
            entityGroup.append(elementClass)
        if type == "component" == EI_Type:
            elementClass = Component(guid,psets)
            entityGroup.append(elementClass)
        if type == "ExecutionUnit" == EI_Type:
            elementClass = ExecutionUnit(guid,psets)
            entityGroup.append(elementClass)
        if type == "LayerGroup" == EI_Type:
            elementClass = LayerGroup(guid,psets)
            entityGroup.append(elementClass)
        if type == "Opening" == EI_Type:
            elementClass = Opening(guid,psets)
            entityGroup.append(elementClass)
        if type == "MEPBox" == EI_Type:
            elementClass = MEPBox(guid,psets)
            entityGroup.append(elementClass)
        if type == "ComponentJoint" == EI_Type:
            elementClass = Box(guid,psets)
            entityGroup.append(elementClass)
        if type == "Joint" == EI_Type:
            elementClass = Box(guid,psets)
            entityGroup.append(elementClass)
        if type == "Connection" == EI_Type:
            elementClass = Connection(guid,psets)
            entityGroup.append(elementClass)
        if type == "PartialSegment" == EI_Type:
            elementClass = PartialSegment(guid,psets)
            entityGroup.append(elementClass)
    if dataframe:
        export = create_dataframe_from_objects(entityGroup, headers[EI_Type])
    else:
        export = entityGroup
    return export

def create_dataframe_from_objects(objects, columns):
    data = {column: [getattr(obj, column) for obj in objects] for column in columns}
    return pd.DataFrame(data)
    
def exportToExcel(df, fileName, sheetName):
    writer = pd.ExcelWriter(fileName, engine='openpyxl')
    if isinstance(df, list):            
        for i in range(len(df)):
            data = df[i]
            if isinstance(sheetName, list):
                sheet = sheetName[i]
            else:
                sheet = sheetName+str(i)
            data.to_excel(writer, sheet_name=sheet)
    else:
        df.to_excel(writer, sheet_name=sheetName)
    writer.save()
    
def getIFCInfo(file_path,entities):
    ifc_file = ifcopenshell.open(file_path)
    #entities = [c,eu,lg,op,mep,box,h,ps]
    definition = [
        {'name':'Components','EI_type':'Component'},
        {'name':'Execution Units','EI_type':'ExecutionUnit'},
        {'name':'Layer Groups','EI_type':'LayerGroup'},
        {'name':'Openings','EI_type':'Opening'},
        {'name':'MEP boxes','EI_type':'MEPBox'},
        {'name':'Joint boxes','EI_type':'Joint'},
        {'name':'Connections','EI_type':'Connection'},
        {'name':'Partial segments','EI_type':'PartialSegment'}        
    ]
    
    # if info_type == 'partialSegments':
    #     entity = getElements(ifc_file,"PartialSegment",True)
    # if info_type == 'layerGroups':
    #     entity = getElements(ifc_file,"LayerGroup",True)
    # if info_type == 'boxes':
    #     entity = getElements(ifc_file,"ComponentJoint",True)
    # if info_type == 'connections':
    #     entity = getElements(ifc_file,"Connection",True)
    
    # excel = exportToExcel(entity,'static/export/export.xlsx',info_type)
    dfs = []
    sheets = []
    
    for i, definition in enumerate(definition):
        if entities[i] == 1:
            entity_type = definition['EI_type']
            df = getElements(ifc_file, entity_type, True)
            dfs.append(df)
            sheets.append(definition['name'])
    
    excel = exportToExcel(dfs, 'static/export/export.xlsx', sheets)
    return excel