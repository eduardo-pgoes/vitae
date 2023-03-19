from enum import Enum
class Constants:
    """Stores all constants for the project."""
    __slots__ = ()

    class Sections(Enum):
        """Stores the constants for splitting up a default CV .docx file into sections."""
        qualifications: str = 'Resumo das Qualificações'
        academic: str = 'Formação Acadêmica'
        languages: str = 'Idiomas'
        extra_courses: str = 'Cursos e palestras'
        work_experience: str = 'Trajetória Profissional'
        previous_experience: str = 'Experiências anteriores'
        tech: str = 'Tecnologias e ferramentas'
