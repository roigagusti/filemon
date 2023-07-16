#!/usr/bin/env python

import ifcopenshell
import ifcopenshell.util.element


# INFO TO CHECK
properties_AP_title = "AP_Assembly Planning"
properties_AP = ["AP_KeyUse"]
properties_EI_title = "EI_Elements Identification"
properties_EI = ["EI_SKUNumber","EI_HostComponentInstanceID","EI_HostComponentType","EI_HostEUInstanceID","EI_HostEUType","EI_LocalisationCodeArea","EI_LocalisationCodeFloor","EI_LocalisationCodeRoom","EI_Type"]
properties_MP_title = "MP_Manufacturing Planning"
properties_MP = ["MP_OperationNumber","MP_ProcessCode"]
properties_MS_title = "MS_Manufacturing Specification"
properties_MS = ["MS_ApplicationParameter"]
properties_ST_title = "ST_Structure Specification"
properties_ST = ["ST_GrainDirection","ST_LamellaBuildUp","ST_PanelType","ST_StrengthClass","ST_SurfaceQuality","ST_WoodSpecies"]

properties_title = [properties_AP_title,properties_EI_title,properties_MP_title,properties_MS_title,properties_ST_title]
properties = [properties_AP,properties_EI,properties_MP,properties_MS,properties_ST]


# FUNCTIONS
def checkProperties(element):
    global properties_title
    global properties
    
    guid = element.get_info()['GlobalId']
    name = element.get_info()['Name']
    psets = ifcopenshell.util.element.get_psets(element)
    i = 0
    errors = 0
    reponse = ""
    emptyProperties = []
    for title in properties_title:
        for property in properties[i]:
            try:
                psets[title][property]
            except:
                errors += 1
                emptyProperties.append(property)
        i += 1
    if len(emptyProperties) > 0:
        reponse1 = name + "(" + guid + ") elements not found:"
        reponse2 = str(emptyProperties)
    return element, reponse1, reponse2, errors

def unitaryTest450(path):
    ifc_file = ifcopenshell.open(path)
    elements = ifc_file.by_type('IfcBuildingElementProxy')

    output = []

    for element in elements:
        element, reponse1, reponse2, errors = checkProperties(element)
        if errors > 0:
            output = [reponse1 + " " + reponse2]
        else:
            output = ["Everything OK!"]
    return output