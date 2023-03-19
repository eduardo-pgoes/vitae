"""
    File for storing helper functions.
"""
import inspect
import constants

def is_section(paragraph: str) -> bool:
    """
        Figures out if an paragraph is a section or not.
        
        Params
        ----------
        paragraph : str
            Paragraph we want to discover if is a section divider or not.

        Returns
        ----------
            bool: Is the paragraph a section divider?
    """
    sections = [s.value for s in constants.Constants().Sections]
    return paragraph in sections