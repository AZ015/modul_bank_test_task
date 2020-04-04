In order to run test project Module Bank, following steps should be done:
- _Python 3 installed(I have Python 3.8)_
- _Installed pip package manager_
- _Further steps are:_ 
  - _go to project folder (\modul_bank)_
  - _run pip install -r requirments.txt(**you would better do it in virtual env**)_

To run tests run from the command line pytest with arguments
  1. **_--browser="chrome"_** or -B chrome
     - available browsers: [firefox, chrome, safari] 
     - also you need same version browser's driver as installed on your PC
  2. **_--url=https://....._** or -U https://...
  3. _**--path_to_browser_driver=...**_ or -P 

**_Example command_** pytest -B chrome -U https://rc.dev.avanpos.com -P C:\Users\Downloads\chromedriver_win32\chromedriver 