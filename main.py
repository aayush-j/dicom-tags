import pydicom

ttfm = pydicom.dcmread("ttfm.dcm")
bmode = pydicom.dcmread("bmode.dcm")
ttfm_tag_names = ttfm.dir()
bmode_tag_names = ttfm.dir()

with open("ttfm_tags.txt", "w") as file:
    for tag in ttfm_tag_names:
        tag_id = ttfm.data_element(tag).tag
        line = str(tag_id) + " " + str(tag) + "\n";
        file.write(line)
        
with open("bmode_tags.txt", "w") as file:
    for tag in bmode_tag_names:
        tag_id = bmode.data_element(tag).tag
        line = str(tag_id) + " " + str(tag) + "\n";
        file.write(line)