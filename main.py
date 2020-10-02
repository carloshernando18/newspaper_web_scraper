import datetime
import pathlib
import subprocess

root_path = pathlib.Path(__file__).parent.absolute()
now = datetime.datetime.now().strftime('%Y_%m_%d')
news_sites_uids = ['vanguardia']


def main():
    _extract()
    _transform()
    _load()


def _extract():
    global root_path
    global now

    for new_site in news_sites_uids:
        filename = '{0}_{1}_articles.csv'.format(new_site, now)
        final_destination = r'{0}\{1}\ '.format(root_path, 'transform')
        origin = r'{0}\{1}\{2} '.format(root_path, 'extract', filename)

        subprocess.run(['python', 'extract.py', new_site], cwd='.\extract')
        _copy_file(origin, final_destination)


def _copy_file(origin, final_destination):
    subprocess.call('copy {0} {1}'.format(
        origin, final_destination), shell=True)
    subprocess.call('del {0}'.format(origin), shell=True)


def _transform():
    global root_path
    global now

    for new_site in news_sites_uids:
        extract_data_file = '{0}_{1}_articles.csv'.format(new_site, now)
        transform_data_file = '{0}_{1}_articles_transform.csv'.format(
            new_site, now)
        final_destination = r'{0}\{1}\ '.format(root_path, 'load')
        origin = r'{0}\{1}\{2} '.format(
            root_path, 'transform', transform_data_file)

        subprocess.run(['python', 'transform.py',
                        extract_data_file], cwd='./transform')
        _copy_file(origin, final_destination)


def _load():
    global now

    for new_site in news_sites_uids:
        transform_data_file = '{0}_{1}_articles_transform.csv'.format(
            new_site, now)
        subprocess.run(
            ['python', 'load.py', transform_data_file], cwd='./load')


main()
