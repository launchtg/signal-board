#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_PATH = ROOT / 'projects.json'
TEMPLATE_PATH = ROOT / 'PROJECT_TEMPLATE.json'


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-')


def main():
    parser = argparse.ArgumentParser(description='Create a new Signal Board project record')
    parser.add_argument('--name', required=True, help='Project display name')
    parser.add_argument('--domain', required=True, help='Preferred domain, e.g. example.com')
    parser.add_argument('--stage', default='ideas', choices=['ideas', 'design', 'validation', 'build', 'live'])
    parser.add_argument('--id', dest='project_id', help='Optional explicit project id')
    parser.add_argument('--folder', help='Optional asset folder name')
    parser.add_argument('--with-folder', action='store_true', help='Create the project folder scaffold')
    args = parser.parse_args()

    data = json.loads(PROJECTS_PATH.read_text())
    template = json.loads(TEMPLATE_PATH.read_text())

    project_id = args.project_id or slugify(args.name)
    folder = args.folder or project_id

    if any(p.get('id') == project_id for p in data['projects']):
        print(f'ERROR: project id already exists: {project_id}')
        sys.exit(1)

    project = template
    project['id'] = project_id
    project['name'] = args.name
    project['domain'] = args.domain
    project['stage'] = args.stage
    project['assets']['folder'] = folder
    project['assets']['logo'] = f'{folder}/logo.png'
    project['assets']['uiMockup'] = f'{folder}/ui-mockup.png'
    project['assets']['prd'] = f'{folder}/PRD.md'
    project['assets']['metaPrompt'] = f'{folder}/meta-prompt.md'

    if args.stage == 'ideas':
        project.pop('assets', None)
        project.pop('validation', None)
    elif args.stage == 'design':
        pass

    data['projects'].append(project)
    data['meta']['lastUpdated'] = str(date.today())
    PROJECTS_PATH.write_text(json.dumps(data, indent=2) + '\n')

    if args.with_folder or args.stage != 'ideas':
        folder_path = ROOT / folder
        folder_path.mkdir(exist_ok=True)
        prd = folder_path / 'PRD.md'
        meta_prompt = folder_path / 'meta-prompt.md'
        if not prd.exists():
            prd.write_text(f'# {args.name} PRD\n\nTBD\n')
        if not meta_prompt.exists():
            meta_prompt.write_text(f'# {args.name} Meta Prompt\n\nTBD\n')

    print(f'Created project `{project_id}` in projects.json')
    if args.with_folder or args.stage != 'ideas':
        print(f'Folder ready: {folder}')
    print('Next step: run tools/validate_projects.py')


if __name__ == '__main__':
    main()
