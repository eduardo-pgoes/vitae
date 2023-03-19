# vitae
a library for parsing resume .docx documents and transforming them into filled-out LinkedIn profiles. 

## backlog
- [X] develop section enums to figure out if a paragraph is a section or not
- [ ] parse sections into subobjects
- [ ] generate "work experience" object - separate company, timespan and activities
- [ ] generate "resume" object
```json
    "resume": {
        "personal-information": {...},
        "work-experience": [ {...} ],
    }
``` 
- [ ] Generate macros/use beautifulsoup4/... for filling out LinkedIn profile
