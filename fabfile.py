from datetime import datetime

from fabric.api import local



def create_session(name):
    local('mkdir sessions/{0}'.format(name))
    local('mkdir sessions/{0}/data'.format(name))
    local('mkdir sessions/{0}/plots'.format(name))
    local('mkdir sessions/{0}/scripts'.format(name))

    name_parts = name.split('-',1)

    sess_id = name_parts[0]
    sess_title = name_parts[1].replace('-', ' ').title()

    index_title = 'Session {0}: {1}'.format(sess_id, sess_title)
    header_marks = len(index_title)*'='

    index_path = 'sessions/{0}/index.rst'.format(name)
    index_file = open(index_path, 'w')
    now = datetime.now()
    date_string = datetime.now().strftime('%d-%m-%Y %H:%M')
    index_file.write('{0}\n{1}\n{0}\n\nStart time:\n    {2}\n\nEnd time:\n    {2}\n\n'.format(
            header_marks, index_title, date_string))
    index_file.close()

cs = create_session


def docs():
    local('sphinx-build -c sphinx/ . web/')
d = docs
