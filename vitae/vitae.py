from docx import Document
import helpers

def get_resume_obj(filepath: str):
    doc = Document(filepath)

    # Loop through paragraphs and separate them into section objects
    resume_obj = {}
    section_list = []
    # Number of sections found - initially, none
    i = -1
    for paragraph in doc.paragraphs:
        # Skip empty paragraphs completely
        if paragraph.text == '':
            continue

        # Create new resume section entry for each new section
        # Append section name to section list
        if (helpers.is_section(paragraph.text)):
            section_list.append(paragraph.text)
            resume_obj[paragraph.text] = []
            i += 1
            continue

        # Skip personal information so we don't violate brazilian LGPD
        # To-do: should we process personal information? 
        if i < 0:
            continue

        if section_list[i]:
            resume_obj[section_list[i]].append(paragraph.text)

    return resume_obj