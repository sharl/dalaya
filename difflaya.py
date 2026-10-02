# -*- coding: utf-8 -*-
import io
import json
import sys
import time

import requests

questions = {
    'opt': {
        'type': 'noul',
        'instructions': 'この差分には最適化性が認められますか?',
    },
    'int': {
        'type': 'noul',
        'instructions': 'この差分には整合性が認められますか?',
    },
    'safe': {
        'type': 'noul',
        'instructions': 'この差分には安全性が認められますか?',
    },
}

if not sys.stdin.isatty():
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    text = sys.stdin.read().strip()
else:
    text = ' '.join(sys.argv)

begin = time.perf_counter()
with requests.post(
        'http://localhost:18000/v1/systemone',
        json={
            'state': text,
            'questions': questions
        },
        timeout=60,
) as r:
    print(json.dumps(r.json()['answers'], indent=2))
elapsed = time.perf_counter() - begin
print(f'{elapsed:.4f}')
