# Automation of Exchange Rates

## Purpose
The aim of this project is to automate the update of an Excel file on your local PC, which should contain the daily exchange rates from various currency. The exchange rate are taken from the [Banca d'Italia API](https://www.bancaditalia.it/compiti/operazioni-cambi/cambi/index.html).
 <br />  <br />
 Currency from: 
- USD
- JPY
- AUD
- RUB

Currency to:
- EUR

## Installation
You can find [here](https://github.com/Brosssh/ExchangeRates/releases) the last version of the .exe file you should download, named AutoupdateRates.exe. When you try to download this, your antivirus/browser will (most likely) flag this EXE as a virus. It doesn't has any malicious intenction, but unless I pay for a certicate it will always be flagged like this.

## How it works
After installing the .exe file, simply double click it. You will get prompted to choose a file from your file explorer. Here you have to choose your destination Excel file, which should be a file with xlsx extension and with (at least) 4 columns header like below: 
Date | From | To | Rate
--- | --- | --- | --- 

After choosing a valid file, the exchange rates will start to get automatically loaded. If the Date column is empty, the process will start from the date January 1, 2022. If the Date column was not empty, the process will look for the bigger date and start from the day after that. The process will end when the last loaded date is the one from the current day. 

## General notes
- Saturday and Sunday never have rates. The Banca d'Italia site do not provide them.
- The sheet where you want to load the rates into should be the first sheet of the Excel file.
- The process can be terminated in any time with the key combination CTRL + C.
- If you want to modify the Excel file, make sure the Date columns is of type Date in Excel.
- If you want to select another Excel file, make sure the process do not find the old file (rename it, move it to another location). You will get asked again to choose the destionation Excel.
