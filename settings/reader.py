#!/usr/bin/python
# -*- coding: utf-8 -*-

import configparser

def read(filename, sections=(), create_file=True):
    return Reader(filename, sections, create_file)

class Reader(object):
    """
    A class to read filename.ini file.
        
    :param str filename:
        
    :param tuple sections: 
        - Tuple of required sections (str)
        - Tuple of 2-tuples containing the required section (str) and the default options (dict)

    :param boolean create_file:
    """
    
    def __init__(self, filename, sections=(), create_file=True):
        filename = filename + ".ini"
        self.config = configparser.ConfigParser()
        self.config.read("./" + filename)

        missingSections = []

        if len(sections) == 2 and isinstance(sections[0], str) and isinstance(sections[1], dict):
            sections = (sections, "GLOBAL")

        for section in sections:
            sectionName = None
            defaultOptions = {}
            try:
                if isinstance(section, tuple):
                    sectionName = section[0]
                    if len(section) > 1 and isinstance(section[1], dict):
                        defaultOptions = section[1]
                elif isinstance(section, str):
                    sectionName = section
                else:
                    continue
                self.config.sections().index(sectionName)
                if len(defaultOptions) > 0:
                    for option in defaultOptions:
                        if not self.config.has_option(sectionName, option):
                            value = defaultOptions[option]
                            if not isinstance(value, str):
                                value = str(value)
                            self.config.set(sectionName, option, value)
            except ValueError:
                if create_file is True:
                    missingSections.append(sectionName)
                #print e
                #print "Missing %s:%s" % (filename, sectionName)
                self.config[sectionName] = {}
                for option in defaultOptions.items():
                    self.config[sectionName][option[0]] = str(option[1])
        
        if len(missingSections) > 0:
            #print "Updating %s ..." % filename
            cfgfile = open("./" + filename,'w')
            self.config.write(cfgfile)
            cfgfile.close()

    def get_section_options(self, section):
        """
        Return a dictionary of options (dict) from a section.
        """
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                value = self.config.get(section, option, raw=True)
                dict1[option] = value
                #if dict1[option] == -1:
                #    pass
            except Exception as e:
                # print("exception on %s!" % option)
                print(e)
                dict1[option] = None
        return dict1
    
    def get_section(self, section):
        """
        Return a section.

        :param str section:
        """
        return self.config[section]