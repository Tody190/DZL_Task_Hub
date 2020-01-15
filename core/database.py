# -*- coding: utf-8 -*-
__author__ = "yangtao"

import shotgun_api3




class SGDB:
    def __init__(self):
        self.sg = None
        self.supper_sg = None
        self.current_user = None

    def login(self, sgurl, login, password, current_user):
        self.sg = shotgun_api3.Shotgun(sgurl,
                                       login=login,
                                       password=password)
        if not current_user:
            return self.sg
        else:
            self.current_user = self.get_user(current_user)
            if self.current_user:
                return self.sg

    def get_user(self, login_name):
        try:
            return self.sg.find_one("HumanUser", [["login", "is", login_name]], ["name"])
        except Exception as e:
            print(e)
            return None

    def get_proejcts(self):
        fields = ["name"]
        filters = [["sg_status", "is", "Active"],
                   ["users", "is", self.current_user]]
        return self.sg.find("Project", filters, fields)

    def get_task_display_status(self, project_entity):
        status_schema = self.sg.schema_field_read("Task",
                                         field_name="sg_status_list",
                                         project_entity=project_entity)
        display_values = []
        for value in status_schema["sg_status_list"]["properties"]["display_values"]["value"].values():
            display_values.append(value)
        return display_values

    def get_status_short_code(self, name):
        fields = ["code"]
        filters = [["name", "is", name]]
        status_entity = self.sg.find_one("Status", filters, fields)
        if status_entity:
            return status_entity["code"]

    def get_task(self, project_name, task_status=None, limit=0):
        fields = ["content", "entity", "sg_status_list",
                  "start_date", "due_date"]
        filters = [["project", "name_is", project_name],
                   ["task_assignees", "in", self.current_user]]
        if task_status:
            status_short_code = self.get_status_short_code(task_status)
            filters.append(["sg_status_list", "is", status_short_code])

        return self.sg.find("Task", filters, fields, limit=limit)

    def get_task_info(self, task_id):
        fields = ["project", "step", "content", "entity",
                  "sg_status_list", "sg_description",
                  "start_date", "due_date", "time_logs_sum"]
        filters = [["id", "is", int(task_id)]]
        return self.sg.find_one("Task", filters, fields)

    def get_task_versions(self, task_id):
        fields = ["code", "sg_status_list", "created_at", "description"]
        filters = [["sg_task", "is",{"type": "Task", "id": int(task_id)}]]
        return self.sg.find("Version", filters, fields)

    def create_version(self, task_id, version_name, uploaded, description, logged_time):
        # 创建
        task_entity = self.get_task_info(task_id)
        if task_entity:
            project_entity = task_entity["project"]
            entity_entity = task_entity["entity"]

        version_data = {"sg_task": task_entity,
                        "user": self.current_user,
                        "project": project_entity,
                        "entity": entity_entity,
                        "code": version_name,
                        "description": description}
        # 创建版本
        version_entity = self.sg.create("Version", version_data)
        if not version_entity:
            return
        try:
            #上传文件
            self.sg.upload(version_entity["type"],
                           version_entity["id"],
                           uploaded,
                           field_name="sg_uploaded_movie",
                           display_name=version_name)
        except Exception as e:
            print(e)

        # 检查
        version_id = version_entity["id"]
        try:
            sg_uploaded_movie = self.get_version_info(version_id)
            if not sg_uploaded_movie:
                raise Exception("sg_uploaded_movie is empty")
        except Exception as e:
            print(e)
            self.sg.delete("Version", version_id)
            return

        # 添加任务 timelogged
        timelog_data = {"project": project_entity,
                        "user": self.current_user,
                        "entity": task_entity,
                        "duration": logged_time*600,
                        "description": version_name}
        self.sg.create("TimeLog", timelog_data)

        return version_entity

    def get_version_info(self, version_id):
        fields = ["sg_uploaded_movie"]
        filters = [["id", "is", int(version_id)]]
        return self.sg.find_one("Version", filters, fields)




if __name__ == "__main__":
    project_name = "HAS"
    task_status = "In Progress"
    last_month_num = 2

    sgurl = "https://dezerlin.shotgunstudio.com"
    # login = "yangtao"
    # password = "SG#yt@10"
    login = "art"
    password = "dezerlin_111"
    current_user = "sunxl"

    sgdb = SGDB()
    sgdb.login(sgurl, login, password, current_user)
    print(sgdb.get_task_info(30478))