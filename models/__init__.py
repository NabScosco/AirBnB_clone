#!/usr/bin/python3
"""
Calling reload on storage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
