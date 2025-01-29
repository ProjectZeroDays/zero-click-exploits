import os
import sys
from archive.archive_parser import parse_sources

def analyze_sources():
    sources = parse_sources()
    # Perform analysis on sources
    print(sources)