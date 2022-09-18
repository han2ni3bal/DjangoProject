Before submit the code:
1. pip install isort
2. isort .
3. pip install yapf==0.28.0
4. yapf --in-place --recursive --style="{indent_width:2,column_limit:120,continuation_indent_width:2,
   allow_split_before_dict_value=False,indent_dictionary_value=True}" --exclude "manage.py" .

Run the server:
1. Make sure you have the correct mysql server open and all tables are all good
2. Make sure all requirement packages are installed
