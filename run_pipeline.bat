@echo off
echo Starting Preprocessing...
python scripts\preprocess.py > logs\preprocess.log
if errorlevel 1 goto error

echo Training Model...
python scripts\train_model.py > logs\train.log
if errorlevel 1 goto error

echo Evaluating Model...
python scripts\evaluate.py > logs\evaluation.log
if errorlevel 1 goto error

echo Pipeline execution completed!
echo Check the 'logs' and 'visuals' folder for details.
pause
exit 

:error
echo An error occured. Check the logs for more information.
pause
