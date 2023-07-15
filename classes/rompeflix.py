from classes.private import atCredentials, devCredentials, atCredentials_rompeflix
from classes.Airtable import Airtable
from classes.Rompetechos import RompetechosDEV
from datetime import datetime


token,base_id = atCredentials_rompeflix()
at = Airtable(token,base_id)
rt = RompetechosDEV(devCredentials())



def convert_to_array(data):
    array = [item[0] for item in data]
    return array

def getProperty(element,property,type=0):
    #check if property exists
    if property in element['fields']:
        if type == 1: # simple array
            output = element['fields'][property][0]
        elif type == 2: # array with multiple elements
            all = ', '.join(element['fields'][property])
            output = all.replace("'"," ")
        elif type == 3: # datetime input
            input = datetime.strptime(element['fields'][property], '%Y-%m-%dT%H:%M:%S.%fZ')
            output = input.strftime('%Y-%m-%d %H:%M:%S')
        else:
            output = element['fields'][property].replace("'"," ")
    else:
        output = ''
    return output

def provaaa():
    a = 'holi'
    return a

def putMediaRT():
    ids = rt.list('rompeflix_media',['atid']) # ids from rompetechos (organitzat amb array de arrays)
    media = at.list('demodays',view='public_(no tocar)') # all content from airtable 
    ids = convert_to_array(ids) # ids from rompetechos (organitzat amb array)
    
    table = 'rompeflix_media'
    actualitzats = 0
    inserits = 0
    for element in media['records']:
        id = element['id']
        title = getProperty(element,'title',4)
        status = getProperty(element,'status')
        cover_image_color = getProperty(element,'cover_image_color')
        cover_image = getProperty(element,'cover_image')
        video = getProperty(element,'video')
        created = getProperty(element,'created',3)
        modified = getProperty(element,'modified',3)
        description1 = getProperty(element,'description1')
        description2 = getProperty(element,'description2')
        description3 = getProperty(element,'description3')
        staff = getProperty(element,'name (from staff)',2)
        release_date = getProperty(element,'release_date')
        owner = getProperty(element,'owner',1)
        ppt_link = getProperty(element,'ppt_link')
        main_image = getProperty(element,'main_image')
        main_image_position = getProperty(element,'main_image_position')
        slider_main = getProperty(element,'slider_main')
        category = getProperty(element,'category')
        area = getProperty(element,'area')
        categoryArea = getProperty(element,'categoryArea')
        video_source = getProperty(element,'video_source')
        
        columns = ['atid','title','estat','cover_image_color','cover_image','video','created','modified','description1','description2','description3','staff','release_date','owner','ppt_link','main_image','main_image_position','slider_main','category','area','categoryArea','video_source']
        extendValues = [id,title,status,cover_image_color,cover_image,video,created,modified,description1,description2,description3,staff,release_date,owner,ppt_link,main_image,main_image_position,slider_main,category,area,categoryArea,video_source]

        if id in ids:
            where = 'atid = "' + id + '"'
            #rt.update(table, columns, extendValues, where)
            actualitzats += 1
        else:
            #rt.insert(table, columns, extendValues)
            inserits += 1

    return actualitzats, inserits

    