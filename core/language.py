# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtCore




class Chinese():
    login_title = "登录到 shotgun"
    shotgun_url = "shotgun 地址"
    user_name = "用户名"
    password = "密码"
    current_user = "当前身份"
    current_user_placeholder_text = "身份同为登录账户时，此处为空"
    language = "语言"
    login_failed = "登陆失败"
    login_failed_info = "请检查账号密码后，重新登录\n如果多次登录失败请联系管理员"
    project = "项目"
    status = "状态"
    limit = "显示最近%s个"
    limit_all = "显示所有"
    load = "加载"
    details = "详情"
    versions = "版本"
    submit = "提交"
    search = "搜索"
    version_name = "版本名："
    name_description = "名称描述："
    upload = "上传："
    clear = "清空"
    description = "描述："
    time_logged = "用时（天）："
    submission_status = "提交状态"
    delete = "删除"
    select_task_submit = "请选中一个任务再提交"
    del_version = "正在删除版本 %s"
    failed_delete = "删除失败"
    sub_task = "任务 %s 提交中..."
    sub_successfully = "提交成功"
    incomplete_sub_retry = "信息不全，请补全后重新提交"
    failed_sub_retry = "提交失败,请重新提交"
    get_task_details = "任务 %s 获取任细节..."
    get_version_details = "任务 %s 获取版本信息..."
    complete = "完成"
    get_sg_data = "正在从 shotgun 拉取数据..."
    find_task = "找到 %s 个任务"
    get_projects = "获取项目..."
    get_status = "获取状态..."


class English():
    login_title = "Login to Shotgun"
    shotgun_url = "Shotgun Url"
    user_name = "User Name"
    password = "Password"
    current_user = "Current User"
    current_user_placeholder_text = "When the [Current User] is the same as the [User Name], leave it blank"
    language = "language"
    login_failed = "Login failed"
    login_failed_info = "Please check your account password and try it again\nIf you fail to log in multiple times, please contact the administrator"
    project = "Project"
    status = "Status"
    limit = "Show last %s"
    limit_all = "Show all"
    load = "Load"
    details = "Details"
    versions = "Versions"
    submit = "Submit"
    search = "Search"
    version_name = "Version Name: "
    name_description = "Name Description: "
    upload = "Upload: "
    clear = "Clear"
    description = "Description："
    time_logged = "Time logged (days): "
    submission_status = "Submission Status"
    delete = "Delete"
    select_task_submit = "Please select a task and submit again"
    del_version = "Deleting version %s"
    failed_delete = "failed to delete"
    sub_task = "Task %s is being submitted..."
    sub_successfully = "Submitted successfully"
    incomplete_sub_retry = "Incomplete submission information, please complete and resubmit it again"
    failed_sub_retry = "Submission failed, please resubmit"
    get_task_details = "Task %s: getting task details from shtogun..."
    get_version_details = "Task %s: getting version details from shtogun..."
    complete = "Complete"
    get_sg_data = "Getting data from shotgun ..."
    find_task = "%s tasks found"
    get_projects = "Get projects information form shotgun"
    get_status = "Get Status form shotgun"



class lan():
    def __init__(self):
        self.settings = QtCore.QSettings("dezerlin_soft", "submitter")
        self.language_list = ["Chinese", "English"]

    def get_language_name(self):
        return self.settings.value("language", "Chinese")

    def get_language(self):
        language_name = self.get_language_name()
        if language_name == "Chinese":
            lan = Chinese()
        if language_name == "English":
            lan = English()
        return lan