from xml.etree import ElementTree

tree = ElementTree.parse("films.xml")
root = tree.getroot()
for movie in root.iter('movie'):
    print(movie.attrib['title'])
    for movie_child in movie.findall('*'):
        print(movie_child.text)
    #movie_children = movie.findall("*")
    #print(movie_children)
    #print(movie.items())
    #print(movie.attrib)
print(root)