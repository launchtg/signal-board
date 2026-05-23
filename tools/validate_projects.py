#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_PATH = ROOT / 'projects.json'
INDEX_PATH = ROOT / 'index.html'

REQUIRED_TOP_LEVEL = [
    'id', 'name', 'domain', 'stage', 'pain', 'tags', 'score', 'scorePercent', 'mvpTime', 'pricing'
]
REQUIRED_DETAIL_TITLES = {
    'Current Manual Workflow',
    'Workflow Friction',
    'Evidence',
    'Relevant APIs',
    "Why They'd Pay",
    'Existing Bad Solutions',
}


def fail(errors):
    for error in errors:
        print(f'ERROR: {error}')
    sys.exit(1)


def warn(warnings):
    for item in warnings:
        print(f'WARN: {item}')


def main():
    errors = []
    warnings = []

    if not PROJECTS_PATH.exists():
        fail([f'Missing {PROJECTS_PATH.name}'])

    try:
        data = json.loads(PROJECTS_PATH.read_text())
    except Exception as e:
        fail([f'Invalid JSON in {PROJECTS_PATH.name}: {e}'])

    meta = data.get('meta')
    projects = data.get('projects')
    if not isinstance(meta, dict):
        errors.append('`meta` must be an object')
    if not isinstance(projects, list):
        errors.append('`projects` must be an array')
    if errors:
        fail(errors)

    stage_ids = [s.get('id') for s in meta.get('stages', []) if isinstance(s, dict)]
    allowed_stages = set(stage_ids)
    if not allowed_stages:
        errors.append('No stages found in meta.stages')

    last_updated = meta.get('lastUpdated')
    if not isinstance(last_updated, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', last_updated):
        errors.append('meta.lastUpdated must be YYYY-MM-DD')

    ids = set()
    domains = set()

    for idx, project in enumerate(projects, start=1):
        prefix = f'projects[{idx}]'
        if not isinstance(project, dict):
            errors.append(f'{prefix} must be an object')
            continue

        for key in REQUIRED_TOP_LEVEL:
            if key not in project:
                errors.append(f'{prefix} missing required field `{key}`')

        pid = project.get('id')
        if isinstance(pid, str):
            if not re.fullmatch(r'[a-z0-9-]+', pid):
                errors.append(f'{prefix}.id must be lowercase letters/numbers/hyphens only')
            if pid in ids:
                errors.append(f'Duplicate project id: {pid}')
            ids.add(pid)

        domain = project.get('domain')
        if isinstance(domain, str):
            if domain in domains:
                warnings.append(f'Duplicate domain detected: {domain}')
            domains.add(domain)

        stage = project.get('stage')
        if stage not in allowed_stages:
            errors.append(f'{prefix}.stage `{stage}` is not in meta.stages')

        tags = project.get('tags')
        if not isinstance(tags, list) or not tags:
            errors.append(f'{prefix}.tags must be a non-empty array')
        else:
            for tag in tags:
                if not isinstance(tag, dict) or 'text' not in tag:
                    errors.append(f'{prefix}.tags entries must be objects with `text`')

        score_percent = project.get('scorePercent')
        if not isinstance(score_percent, int) or not (0 <= score_percent <= 100):
            errors.append(f'{prefix}.scorePercent must be an integer between 0 and 100')

        if stage == 'ideas':
            details = project.get('details')
            if not isinstance(details, list) or not details:
                errors.append(f'{prefix}.details is required for Ideas-stage projects')
            else:
                titles = {d.get('title') for d in details if isinstance(d, dict)}
                missing = REQUIRED_DETAIL_TITLES - titles
                if missing:
                    warnings.append(f'{prefix} missing common detail titles: {sorted(missing)}')

        if stage in {'design', 'validation', 'build', 'live'}:
            if 'assets' not in project:
                errors.append(f'{prefix}.assets is required for {stage}-stage projects')
            if 'validation' not in project:
                errors.append(f'{prefix}.validation is required for {stage}-stage projects')

        assets = project.get('assets')
        if isinstance(assets, dict):
            for field in ['logo', 'uiMockup', 'prd', 'metaPrompt']:
                val = assets.get(field)
                if val:
                    if not isinstance(val, str):
                        errors.append(f'{prefix}.assets.{field} must be a string path')
                    elif not (ROOT / val).exists():
                        errors.append(f'{prefix}.assets.{field} path does not exist: {val}')
            folder = assets.get('folder')
            if folder:
                folder_path = ROOT / folder
                if not folder_path.exists() or not folder_path.is_dir():
                    errors.append(f'{prefix}.assets.folder does not exist as a directory: {folder}')

        validation = project.get('validation')
        if validation is not None and not isinstance(validation, dict):
            errors.append(f'{prefix}.validation must be an object when present')
        elif isinstance(validation, dict):
            for field in ['lpUrl', 'signups', 'qualified', 'conversion', 'trafficSource', 'lastCheck', 'status']:
                if field not in validation:
                    warnings.append(f'{prefix}.validation missing field `{field}`')

    if not INDEX_PATH.exists():
        errors.append('index.html is missing')

    if errors:
        fail(errors)

    warn(warnings)
    print(f'OK: {len(projects)} projects validated across {len(allowed_stages)} stages')


if __name__ == '__main__':
    main()
