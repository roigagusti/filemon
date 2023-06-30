from classes.private import atCredentials, devCredentials, atCredentials_rompeflix
from classes.Airtable import Airtable
from classes.Rompetechos import RompetechosDEV


token,base_id = atCredentials_rompeflix()
at = Airtable(token,base_id)
rt = RompetechosDEV(devCredentials())


ids = rt.list('rompeflix_media',['atid'])
media = at.list('demodays',view='public_(no tocar)')

def getProperty(element,property):
    #check if property exists
    if property in element['fields']:
        output = element['fields'][property]
    else:
        output = ''
    return output

actualitzats = 0
inserits = 0

for element in media['records']:
    id = element['id']
    if id in ids:
        actualitzats += 1
    else:
        inserits += 1
    title = getProperty(element,'title')
    status = getProperty(element,'status')
    cover_image_color = getProperty(element,'cover_image_color')
    cover_image = getProperty(element,'cover_image')
    video = getProperty(element,'video')
    created = getProperty(element,'created')
    modified = getProperty(element,'modified')
    description1 = getProperty(element,'description1')
    description2 = getProperty(element,'description2')
    description3 = getProperty(element,'description3')
    staff = getProperty(element,'name (from staff)')
    release_date = getProperty(element,'release_date')
    owner = getProperty(element,'owner')
    ppt_link = getProperty(element,'ppt_link')
    main_image = getProperty(element,'main_image')
    main_image_position = getProperty(element,'main_image_position')
    slider_main = getProperty(element,'slider_main')
    category = getProperty(element,'category')
    area = getProperty(element,'area')
    categoryArea = getProperty(element,'categoryArea')
    video_source = getProperty(element,'video_source')
    
print('Actualitzats: ' + str(actualitzats))
print('Inserits: ' + str(inserits))


    