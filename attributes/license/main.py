from core import tokenize
from utilities import url_to_json


def run(project_id, repo_path, cursor, **options):
    query = 'SELECT url FROM projects WHERE id = ' + str(project_id)
    cursor.execute(query)
    record = cursor.fetchone()

    full_url = tokenize(record[0].rstrip())
    json_response = url_to_json(full_url, headers={
            'Accept': 'application/vnd.github.drax-preview+json'
        }
    )

    result = 'license' in json_response
    return result, int(result)

if __name__ == '__main__':
    print('Attribute plugins are not meant to be executed directly.')
