GLORIA: This would be our drop message box, so we dont mess up the pull request, you can comment on the pull request for me to check this readme for the explanation or modification i did and the steps involved

The python script isn't hardcoded, that means you can use it for an existing .md file or a new md like we discussed

Instead of just using the previous method, this python script, when you run it from the terminal:

```json

python3.12 generate_rows_column_with_content.py README.md 3 5

```
For example so i have asked the python script to generate a table with 3 number of rows and 5 number of coulumns, i also added a usage where if you did not type the number of input argument, it shows you that you haven't input all the input for the argument.

1. It will ask if you want to insert content into the table like your ingredient flour, the instruction of how to bake the bread, the instruction on the measurement, if no, you just want to generate an empty table, then it will prompt you to give the headings of the table instead of the default name like column1, 2, 3 e.t.c...You name the heading of your table according the number of column you request, once it is done, it exists and let you know it has generated the table without content into the .md file

2. Then if you want to insert content and don't want to generate an empty table but also inset content in it, same procedure but will prompt further for content intake.

3. I have created two test file one without content and one with content to see sample, i also generated a table without and with content to you readme.md to see also you can generate to a .md file with even an existing content in it.

If there is any changes or instruction that is confusing drop it in this read me and i will do another pull request to add or the remove. Any number of rows and column can be generated