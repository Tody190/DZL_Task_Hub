# -*- coding: utf-8 -*-
__author__ = "yangtao"




def version_name(project, link, pipline, ver):
    ver = "%02d"%ver
    link=link.replace(" ", "")
    return "{project}_{link}_{pipline}_v{ver}".format(project=project,
                                                         link=link,
                                                         pipline=pipline,
                                                         ver=ver)