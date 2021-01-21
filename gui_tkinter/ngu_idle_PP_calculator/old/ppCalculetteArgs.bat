@echo off

set path2File=script_with_args
set nbPoint=126098
set time=2.5
set goalPP=100

python %path2File%/pp_calculator_with_args.py %nbPoint% %time% %goalPP%
