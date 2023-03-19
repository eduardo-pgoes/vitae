# Example file for using vitae
import vitae

# filepath is a 'magic string' because the 'real' resume can't be commited;
# it contains truckloads of sensitive data.
resume_obj = vitae.get_resume_obj('../assets/resume.docx')

print(resume_obj)