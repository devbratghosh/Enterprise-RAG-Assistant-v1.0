"""
============================================================
File      : exceptions.py
Project   : Enterprise-RAG-Assistant
Purpose   : Custom exceptions used throughout the project.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""


class EnterpriseRAGError(Exception):
    """
    Base exception for the Enterprise RAG project.
    """

    pass


class FileOperationError(EnterpriseRAGError):
    """
    Raised when a filesystem operation fails.
    """

    pass


class DirectoryCreationError(FileOperationError):
    """
    Raised when a directory cannot be created.
    """

    pass


class FileReadError(FileOperationError):
    """
    Raised when a file cannot be read.
    """

    pass


class FileWriteError(FileOperationError):
    """
    Raised when a file cannot be written.
    """

    pass


class InvalidDataError(EnterpriseRAGError):
    """
    Raised when invalid data is supplied.
    """

    pass


class ValidationError(EnterpriseRAGError):
    """
    Raised when validation fails.
    """

    pass