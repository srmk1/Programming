import os
import sys 
import yaml

############### SG RAPID UT ENV SETUP ##############################
def jenkins_sg_rapid_ut_env_cleanup():
    build_user_id = os.getenv('BUILD_USER_ID')
    build_tag = os.getenv('BUILD_TAG')
    TC_NAME = os.getenv('TC_NAME')
    yaml_file_name = '/usr/srk/yamls/yaml-file-name-%s-%s.yaml'%(TC_NAME, build_user_id, build_tag)
    cmd = 'rm %s'%yaml_file_name
    os.system(cmd)
############### SG RAPID UT ENV SETUP ##############################

jenkins_sg_rapid_ut_env_cleanup()
