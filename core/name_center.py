# -*- coding: utf-8 -*-
__author__ = "yangtao"




# def version_name(project, link, pipline, ver):
#     ver = "%02d"%ver
#     link=link.replace(" ", "")
#     return "{project}_{link}_{pipline}_v{ver}".format(project=project,
#                                                          link=link,
#                                                          pipline=pipline,
#                                                          ver=ver)


class Version_Name():
    def __init__(self):
        self.project = ""
        self.link = ""
        self.pipline = ""
        self.description = ""
        self.ver = 1

    def get_name(self):
        link = self.link.replace(" ", "")
        version_name_list = [self.project, link, self.pipline]
        if self.description:
            version_name_list.append(self.description)
        version_name_list.append("v%02d" % self.ver)
        return "_".join(version_name_list)


if __name__ == "__main__":
    version_name = Version_Name()
    print(version_name.get_name())
