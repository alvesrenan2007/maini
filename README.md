# Maini (毎日の家計簿)

## About

Maini (short of "mainichi no kakeibou", or "everyday's kakeibou") is planned to be a simple expense tracker application that focused on daily expenses to incentivize behavioural changes (to create good spending habits). The objective is to have an independent CLI application and a GUI application, with the former following Unix conventions to work as a standalone tool and the latter being a GTK4 interface that allows more visual functionalities, such as plotting graphs and drawing charts.

## Philosophy

- **Daily allowance:** After setting the amount of the user's income that is available for expense tracking, the application will set a daily limit, which represents how much can be spent on a single day.
- **Daily averages:** Everytime a transaction is registered, the daily average of the expenses will be updated, giving the user an idea of whether he is going to succeed in meeting the monthly spending goals. If the daily average is greater than the limit, that's an indication that it's wise to spend less on the next day. If the average is below the limit, that's an indication that it's safe to spend more in the next day.
- **Urgency to save:** By having feedback on a daily basis, a sense of urgency can be felt. This urgency prevents household finance related decisions to be postponed and ignored until the there is a unpleasant bank report. This makes awareness and response regarding the household finances a habit. 

## Architecture

- **Language:** Python (with the possibility of changing parts of the code to C or Rust).
- **Storage:** SQLite (relational structure that associates transactions with tags for querying).
- **Interface:** CLI written in Python with `click` and GUI also written in Python using `PyObjects` to build a GTK4 application.

## Kakeibou Technique

The application refrain from trying to apply traditional kakeibou techniques, such as defining 固定費 (fixed-value recurring expenses), 変動費 (varied-value recurring expenses) or やりくり費 (expenses that are not necessarily recurring), instead putting all of that responsibility on the user through the tags system. Each transaction can receive an arbitrary amount of tags (which are registered in a specific table), so consistency is expected to make future queries be useful.

## CLI command options

- **--tag, -t** -> treats the next spaced-separated words as tags
- **--direction, -dir** -> sets the transaction "direction" to either "income" or "outcome", with "outcome" being the default value
- **--date, -d** -> sets the date of the transaction following "YY-MM-DD" format, with today's date being the default
- **--currency, -c** -> sets the currency of the transaction, with the currency defined in the configuration file being the default
