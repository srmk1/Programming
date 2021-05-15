import os
import sys
import yaml

############### SG RAPID UT ENV SETUP ##############################
global is_sr_pkg_test, is_standby_sup_present, yaml_list, build_user_id, build_tag

def jenkins_sg_rapid_ut_env_setup():
    # Read Yaml and figure out which tests to run
    yaml_file = os.getenv('SR_RP_UT_YAML')
    with open(os.path.normpath(yaml_file), 'r') as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    # Read os environment variables sent from AUTOMATION-TOOL
    is_sr_pkg_test = os.getenv('Package_Testing')
    if is_sr_pkg_test == 'Yes':
        cco_image = os.getenv('CCO_IMAGE')
        cco_image = cco_image.rstrip(',')
        sel_pkg = os.getenv('Select_Package')
        sel_pkg = sel_pkg.rstrip(',')
        yaml_list['testbed']['custom']['IS_SR_PKG_TEST'] = 1
        yaml_list['testbed']['custom']['SELECT_PKG_NAMES'] = []
        yaml_list['testbed']['custom']['CCO_IMAGE'] = []
        yaml_list['testbed']['custom']['BRANCH'] = os.getenv('BRANCH')
        yaml_list['testbed']['custom']['SELECT_PKG_NAMES'].append(sel_pkg)
        yaml_list['testbed']['custom']['CCO_IMAGE'] = cco_image
    else:
        image_name = os.getenv('IMAGE_PATH')
        image_name = image_name.rstrip(',')
        yaml_list['testbed']['custom']['IS_SR_PKG_TEST'] = 0
        yaml_list['testbed']['custom']['IMAGE_NAME'] = image_name

    # From jenkins below enviornment variables are set in bash
    build_user_id = os.getenv('BUILD_USER_ID')
    build_tag = os.getenv('BUILD_TAG')
    TC_NAME = os.getenv('TC_NAME')
    yaml_file_name = '%s-%s-%s.yaml'%(TC_NAME, build_user_id, build_tag)
    yaml_dir='/usr/srk/yaml'
    yaml_file=os.path.join(yaml_dir,yaml_file_name)
    with open(yaml_file, 'w') as file:
        yaml.dump(yaml_list, file, default_flow_style=False)

def jenkins_sg_rapid_ut_env_cleanup():
    cmd = 'rm /usr/srk/yaml/yaml-file-name  -%s-%s.yaml'%(build_user_id, build_tag)
    os.system(cmd)
############### SG RAPID UT ENV SETUP ##############################

jenkins_sg_rapid_ut_env_setup(
