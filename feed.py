import yaml
import xml.etree.cElementTree as xml_tree
with open('feed.yaml','r') as file:
    ymal_data =yaml.safe_load(file)

    rss_ele=xml_tree.Element('rss',{
        'version':'2.0',
         'xmlns:googleplay':'http://www.google.com/schemas/play-podcasts/1.0',
         'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
         'xmlns:atom':'http://www.w3.org/2005/Atom',
         'xmlns:rawvoice':'http://www.rawvoice.com/rawvoiceRssModule/',
         'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    })
    channel_element = xml_tree.SubElement(rss_ele,'channel')
    xml_tree.SubElement(channel_element,'title').text=ymal_data['title']
    xml_tree.SubElement(channel_element,'format').text=ymal_data['format']
    xml_tree.SubElement(channel_element,'subtitle').text=ymal_data['subtitle']
    xml_tree.SubElement(channel_element,'itunes:author').text=ymal_data['author']
    xml_tree.SubElement(channel_element,'description').text=ymal_data['description']
    xml_tree.SubElement(channel_element,'language').text=ymal_data['language']
    xml_tree.SubElement(channel_element,'itunes:image',{'href': ymal_data['link']+ymal_data['image']})
    xml_tree.SubElement(channel_element,'link').text=ymal_data['link']
    xml_tree.SubElement(channel_element,'itunes:category',{'text':ymal_data['link']})
    
    
    
    for item in ymal_data['item']:
        item_element=xml_tree.SubElement(channel_element,'item')
        xml_tree.SubElement(item_element,'title').text=item['title']
        xml_tree.SubElement(item_element,'itunes:author').text=ymal_data['author']
        xml_tree.SubElement(item_element,'description').text=item['description']
        xml_tree.SubElement(item_element,'published').text=item['published']
        xml_tree.SubElement(item_element,'itunes:duration').text=item['duration']
        xml_tree.SubElement(item_element,'enclosure',{'length':item['length']
,'type':'audio/x-m4a','url':ymal_data['link']+item['file']})
    output_tree=xml_tree.ElementTree(rss_ele)
    output_tree.write('podcast.xml',encoding='UTF-8',xml_declaration=True)