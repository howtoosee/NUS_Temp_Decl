# NUS Temp Declaration

## Introduction

A short Python script to automate temperature declaration.

## Setting Up

1. Install _chromedriver_
   - Windows: [Tutorial](https://youtu.be/dz59GsdvUF8)
   - MacOS: Open terminal, enter command `brew install chromedriver`
2. Install necessary libraries `pip install -r requirements.txt`
3. Add credentials
   - Rename file `.env.sample` to `.env`
   - Fill in UserID and Password
   - Example:

        ```env
        USERID=nusstu\e1234567
        PASSWORD=abcdef
        ```

   - Note: do NOT add spaces around the equal sign
4. Run the script `python3 AutomatedTempDec.py`
