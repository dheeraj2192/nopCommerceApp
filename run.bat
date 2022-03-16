pytest -v -s -m "sanity" --html=Reports\batchreports.html --capture=tee-sys testCases\
rem pytest -v -s -m "sanity or regression" --html=Reports\reports.html --capture=tee-sys testCases\ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=Reports\reports.html --capture=tee-sys testCases\ --browser chrome
rem pytest -v -s -m "regression" --html=Reports\reports.html --capture=tee-sys testCases\ --browser chrome