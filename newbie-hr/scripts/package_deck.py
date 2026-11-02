"""Rebuild the offline teaching bundle without dependencies or QA artifacts."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
ROOT=Path(__file__).resolve().parent.parent
names=['index.html','README.md','outline.md','content-plan.md','sources.md','MEDIA_CREDITS.md','slides.json','scripts','assets','workshop','examples','package.json','package-lock.json']
with ZipFile(ROOT/'claude-code-workshop.zip','w',ZIP_DEFLATED) as archive:
    for name in names:
        path=ROOT/name
        files=path.rglob('*') if path.is_dir() else [path]
        for file in sorted(files):
            if file.is_file() and '__pycache__' not in file.parts and file.name!='.DS_Store':
                archive.write(file,file.relative_to(ROOT))
    archive.writestr('workshop/output/','')
print('Created claude-code-workshop.zip')
