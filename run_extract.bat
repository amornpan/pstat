@echo off
cd /d C:\Users\Asus\pstat
call conda activate pstat13
python extract_notebooks.py > notebook_contents.txt 2>&1
echo Done! Check notebook_contents.txt
