import os
url_mk = 'https://app.mokahr.com/recommendation-apply/tuya/3237?containerType=workwechat&goto=recommendations#/'
url_bs = 'https://www.zhipin.com/web/boss/index'
url_bs_login = 'https://login.zhipin.com/?ka=header-login'


current_dir = os.path.abspath(__file__)
project_dir = os.path.split(os.path.split(current_dir)[0])[0]
resume_unpush = os.path.join(project_dir, "resume_unpush")
resume_push_readfail = os.path.join(project_dir, "resume_push_readfail")
resume_push_success = os.path.join(project_dir, "resume_push_success")
resume_push_toolate = os.path.join(project_dir, "resume_push_toolate")